#!/usr/bin/env node

// Sometimes the order of the teensys get swapped.
// In that case, change this flag to 1
const SWAP_TEENSY_ORDER = 0;

// Make false to test without teensys
const DEBUG_USE_TEENSY = true;

// Web socket port can be set from the command line as the second argument.
// Port 8080 is default. 80 is preferred but requires the use of sudo.
const PORT = process.env.PORT || parseInt(process.argv[2]) || 8080;

const express = require("express");
const WebSocket = require('ws');
const SerialPort = require('serialport');

// CONSTANTS

const WIDTH = 60;
const HEIGHT = 32;
const TOTAL_PIXELS = WIDTH * HEIGHT;
const TOTAL_BYTES = TOTAL_PIXELS * 3;

let brightness = 1;
let nightshift = 0;
let colorcorrect = [1, 0.63, 0.43];

// TRANSPORT SETUP

const app = express();
app.use(express.static("."));

const server = require('http').createServer(app);
const wss = new WebSocket.Server({server});

// Websocket code

// Polyfill
wss.broadcast = function broadcast(data) {
  wss.clients.forEach(function each(client) {
    if (client.readyState === WebSocket.OPEN) {
      client.send(data);
    }
  });
};

wss.on("connection", function(ws){
  console.log("Client connected!")
  ws.on("message", function(data){
    if(data instanceof Buffer){
      writeToVlla(data);
    }
    else{
      console.log("message",data)
      let message = JSON.parse(data);
      if("brightness" in message){
        brightness = Math.min(Math.max(parseFloat(message.brightness)||0,0),1);
      }
      writeToVlla();
    }
  })
})

// Color correction and mapping

function transformColor(colorToDisplay, i){
  // TODO: Use index for spatial dithering?
  return Math.round(colorToDisplay * brightness * colorcorrect[i % 3] * (i==0? 1 : 1-nightshift));
}


// PHYSICAL DRIVER CODE

let teensy1, teensy2;

if(DEBUG_USE_TEENSY){
  teensy1 = new SerialPort('/dev/ttyACM' + (SWAP_TEENSY_ORDER), {baudRate: 4000000});
  teensy2 = new SerialPort('/dev/ttyACM' + (1 - SWAP_TEENSY_ORDER), {baudRate: 4000000});
}

let writeFrame1 = new Buffer(TOTAL_BYTES/2 + 1).fill(0);
let writeFrame2 = new Buffer(TOTAL_BYTES/2 + 1).fill(0);

let lastBuffer = null;

function writeToVlla(buffer){
  if(!buffer){
    // Re-render previous buffer if buffer is not provided
    if(!lastBuffer){
      return;
    }
    buffer = lastBuffer;
  } else {
    lastBuffer = buffer;
  }

  // Make sure to add that framestart character
  writeFrame1[0] = 0xff;
  writeFrame2[0] = 0xff;

  // Also, using Math to make sure no values are frameStart
  for(let i = 0; i < TOTAL_BYTES; i++) {
    let value = Math.min(transformColor(buffer[i], i), 254);
    if (i < TOTAL_BYTES / 2) {
      writeFrame1[i + 1] = value;
    }
    else {
      writeFrame2[i + 1 - TOTAL_BYTES / 2] = value;
    }
  }
  
  if(DEBUG_USE_TEENSY){
    teensy1.write(writeFrame1);
    teensy2.write(writeFrame2);
  }
  else{
    // console.log(writeFrame1[1],writeFrame1[2],writeFrame1[3]);
    console.log("writing frames to teensy: ", writeFrame1, writeFrame2);
  }
};

server.listen(PORT, ()=>{
  console.log("Server has started on port",PORT);
})
