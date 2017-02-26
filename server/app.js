#!/usr/bin/env node

var WebSocketServer = require('websocket').server;
var SerialPort = require('serialport');
var http = require('http');

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
            var to_write = new Buffer(message.utf8Data, 'base64');
	    write_to_vlla(to_write);
        }
        else if (message.type === 'binary') {
          write_to_vlla(message.binaryData);
        }
    });
    connection.on('close', function(reasonCode, description) {
        console.log((new Date()) + ' Peer ' + connection.remoteAddress + ' disconnected.');
    });
});

var teensy1 = new SerialPort('/dev/ttyACM0', {baudRate: 4000000});
var teensy2 = new SerialPort('/dev/ttyACM1', {baudRate: 4000000});
var teensyDivide = 960; // Half the pixels

var frameStart = new Buffer([0xff]);
function write_to_vlla(to_write){
    // Make sure no values are frameStart
    for(var i = 0; i < to_write.length; i++) {
	to_write[i] = to_write[i] >= 255 ? 251: to_write[i];
    }

    // Make sure to add that framestart character
    teensy1.write(Buffer.concat([frameStart, to_write.slice(0, teensyDivide)]));
    teensy2.write(Buffer.concat([frameStart, to_write.slice(teensyDivide)]));
};
