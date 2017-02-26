var VLLA_WIDTH = 60;
var VLLA_HEIGHT = 32;

var WebSocketClient = require('websocket').client
  , Canvas = require('canvas')
  , canvas = new Canvas(VLLA_WIDTH, VLLA_HEIGHT)
  , context = canvas.getContext('2d');

module.exports = {
  encode: function(pixels) {
      var frame = "";
      for (var i = 0; i < pixels.length; i += 4) {
    frame += String.fromCharCode(
        (Math.floor(pixels[i + 1] / 32) << 5) + // Red - 3 bits

        (Math.floor(pixels[i + 2] / 32) << 2) + // Green - 3 bits
        (Math.floor(pixels[i + 3] / 64)) // Blue - 2 bits
    );
      }
      return frame;
  },
  width: VLLA_WIDTH,
  height: VLLA_HEIGHT,
  requestCanvas: function() {
    return canvas;
  },
  requestContext: function() {
    return context;
  },
  render: function() {
    var buffer = canvas.toBuffer('raw');
    var encoded = vlla.encode(buffer);
  },
};
