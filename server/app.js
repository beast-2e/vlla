#!/usr/bin/env node

var WebSocketServer = require('websocket').server;
var SerialPort = require('serialport');
var http = require('http');


// CONSTANTS

var WIDTH = 60;
var HEIGHT = 32;
var TOTAL_PIXELS = WIDTH * HEIGHT;
var TOTAL_BYTES = TOTAL_PIXELS * 3;

var reversed = 0; // Sometimes the order of the teensys get swapped.
// In that case, change this flag to 1
var brightness = 1;
var colorcorrect = [1, 0.63, 0.43];

var TRANSITION_FPS = 60;
var TRANSITION_DURATION = 2; // Seconds, how long the fade lasts
var TRANSITION_HOLD = 60; // Seconds, how long to stay on each shader

// TRANSPORT SETUP

var server = http.createServer(function(request, response) {
    console.log((new Date()) + ' Received request for ' + request.url);
    response.writeHead(404);
    response.end();
});

server.listen(8080, function() {
    console.log((new Date()) + ' Server is listening on port 8080');
});

wsServer = new WebSocketServer({
    httpServer: server,
    // You should not use autoAcceptConnections for production
    // applications, as it defeats all standard cross-origin protection
    // facilities built into the protocol and the browser.  You should
    // *always* verify the connection's origin and decide whether or not
    // to accept it.
    autoAcceptConnections: false
});

function originIsAllowed(origin) {
    // put error here to detect whether the specified origin is allowed.
    return true;
}


// SOCKET AND CLIENT MANAGEMENT

var connections = []; // A list of connected clients

wsServer.on('request', function(request) {
    if (!originIsAllowed(request.origin)) {
        // Make sure we only accept requests from an allowed origin
        request.reject();
        console.log((new Date()) + ' Connection from origin ' + request.origin + ' rejected.');
        return;
    }

    var connection = request.accept('vlla', request.origin);
    console.log((new Date()) + ' Connection accepted.');

    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            brightness = Math.min(Math.max(parseFloat(message.utf8Data) || 0, 0), 1);
            renderTransition();
        }
        else if (message.type === 'binary') {
            if(!connection.buffer){
                // Create a temporary frame buffer for every connection,
                // helps with transitions
                connection.buffer =
                    new Buffer(TOTAL_BYTES).fill(0);

                connections.push(connection);
                console.log("Streaming connections: " + connections.length);

                moveToNextConnection(connection);
            }

            message.binaryData.copy(connection.buffer);
            bufferHasUpdated(connection.buffer);
        }
    });
    connection.on('close', function(reasonCode, description) {
        console.log((new Date()) + ' Peer ' + connection.remoteAddress + ' disconnected.');
        var index = connections.indexOf(connection);
        if (index > -1) {
            connections.splice(index, 1);
            if(currentConnection === connection){
                moveToNextConnection();
            }
            console.log("Streaming connections: " + connections.length);
        }
    });
});


// TRANSITION CODE

var currentConnection = null;
var connectionLoopTimeout = -1;
var black = new Buffer(TOTAL_BYTES).fill(0);
function moveToNextConnection(gotoThisConnection){
    if(gotoThisConnection !== undefined){
        currentConnection = gotoThisConnection;
    }
    else{
        if (connections.length == 0){
            currentConnection = null;
        }
        else {
            currentConnection = connections[(connections.indexOf(currentConnection) + 1) % connections.length];
        }
    }
    beginTransitionTo(currentConnection && currentConnection.buffer || black,
            TRANSITION_DURATION,
            fadeEffect);
    clearTimeout(connectionLoopTimeout);
    connectionLoopTimeout = setTimeout(moveToNextConnection, 1000 * TRANSITION_HOLD);
}

function fadeEffect(before, after, mixing, factor){
    //factor = Math.pow(factor, 2);
    for(var i = 0; i < TOTAL_BYTES; i++){
        mixing[i] = before[i] * (1 - factor) + after[i] * factor;
    }
}

function wipeEffect(before, after, mixing, factor){
    //factor = Math.pow(factor, 2);
    for(var i = 0; i < WIDTH; i++){
        for(var j = 0; j < HEIGHT; j++){
            for(var k = 0; k < 3; k++){
                var index = 3*(i + WIDTH * j) + k;
                mixing[index] = factor < i/WIDTH ? before[index] : after[index];
            }
        }
    }
}

var bufferBefore = black;
var bufferAfter = black;
var mixingBuffer = new Buffer(TOTAL_BYTES).fill(0);
var mixAmount = 1; // 0 shows bufferBefore, 1 shows bufferAfter;

var transitionLoopTimeout = -1;
var currentTransitionDuration = 0;
var currentTransitionEffect = null;

function beginTransitionTo (buffer, duration, effect) {
    /* Starts transitioning to a buffer.
    */
    if(buffer == bufferAfter) return;

    currentTransitionDuration = duration || 1; // duration in seconds
    currentTransitionEffect = effect || fadeEffect;

    bufferBefore = bufferAfter;
    bufferAfter = buffer;
    mixAmount = 0;
    transitionLoop();
}

function transitionLoop(){
    /* Runs continuously to fade between transitions.
     * Initiated by beginTransitionTo.
     */
    clearTimeout(transitionLoopTimeout);
    if(mixAmount < 1){
        mixAmount = currentTransitionDuration <= 0 ? 1 :
            Math.min(mixAmount + currentTransitionDuration / TRANSITION_FPS, 1);
        renderTransition();
        transitionLoopTimeout = setTimeout(transitionLoop, 1000 / TRANSITION_FPS);
    }
}

function renderTransition() {
    if(mixAmount >= 1){
        writeToVlla(bufferAfter);
    }
    else{
        currentTransitionEffect(bufferBefore, bufferAfter, mixingBuffer, mixAmount);
        writeToVlla(mixingBuffer);
    }
}

function bufferHasUpdated (buffer) {
    if(mixAmount < 1 && buffer === bufferBefore || buffer === bufferAfter){
        renderTransition();
    }
}

// PHYSICAL DRIVER CODE

var teensy1 = new SerialPort('/dev/ttyACM' + (reversed), {baudRate: 4000000});
var teensy2 = new SerialPort('/dev/ttyACM' + (1 - reversed), {baudRate: 4000000});

var writeFrame1 = new Buffer(TOTAL_BYTES/2 + 1).fill(0);
var writeFrame2 = new Buffer(TOTAL_BYTES/2 + 1).fill(0);
function writeToVlla(buffer){
    // Make sure to add that framestart character
    writeFrame1[0] = 0xff;
    writeFrame2[0] = 0xff;

    for(var i = 0; i < TOTAL_BYTES; i++) {
        var value = Math.min(buffer[i] * brightness * colorcorrect[i % 3], 254);
        if (i < TOTAL_BYTES / 2) {
            writeFrame1[i + 1] = value;
        }
        else {
            writeFrame2[i + 1 - TOTAL_BYTES / 2] = value;
        }
    }
    // Also, using Math to make sure no values are frameStart

    teensy1.write(writeFrame1);
    teensy2.write(writeFrame2);
};
