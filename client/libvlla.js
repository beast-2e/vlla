var VLLA_WIDTH = 60;
var VLLA_HEIGHT = 32;

var WebSocketClient = require('websocket').client
  , Canvas = require('canvas')
  , canvas = new Canvas(VLLA_WIDTH, VLLA_HEIGHT)
  , context = canvas.getContext('2d');
  //, buffer = Buffer.allocUnsafe(VLLA_WIDTH * VLLA_HEIGHT);

var connected = false;

var client = new WebSocketClient();
var connection;

client.on('connectFailed', function(error) {
  console.log('Connect Error: ' + error.toString());
  process.exit(1);
});

client.on('connect', function(conn) {
  connected = true;
  connection = conn;

  console.log('WebSocket client connected');

  conn.on('error', function(error) {
    console.log("Connection Error: " + error.toString());
  });

  conn.on('close', function() {
    console.log('echo-protocol Connection Closed');
  });

  conn.on('message', function(message) {
    if (message.type === 'utf8') {
      console.log("Received: '" + message.utf8Data + "'");
    }
  });
});

client.connect('ws://localhost:8080/', 'vlla');

function encode(pixels) {
  this.buffer = this.buffer || new Buffer(VLLA_WIDTH * VLLA_HEIGHT);

  for (var i = 0; i < pixels.length; i += 4) {
    this.buffer[i / 4] = (Math.floor(pixels[i + 2] / 32) << 5) + // Red - 3 bits
      (Math.floor(pixels[i + 1] / 32) << 2) + // Green - 3 bits
      (Math.floor(pixels[i] / 64)); // Blue - 2 bits
  }

  return this.buffer;
}

module.exports = {

  width: VLLA_WIDTH,
  height: VLLA_HEIGHT,

  requestCanvas: function() {
    return canvas;
  },

  requestContext: function() {
    return context;
  },

  render: function() {
    if (connected) {
      var buffer = canvas.toBuffer('raw');
      connection.send(encode(buffer));
    }
  },
};
