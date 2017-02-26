var vlla = require('../libvlla.js');

var canvas = vlla.requestCanvas();
var context = vlla.requestContext();

// fill background
context.fillStyle = 'rgb(0, 0, 0)';
context.fillRect(0, 0, vlla.width, vlla.height);

context.fillStyle = 'rgb(255, 255, 0)';
context.font = '20px Impact';
context.fillText("hello", 0, 29);

var te = context.measureText('Awesome!');
context.strokeStyle = 'rgba(255,0,0,0.5)';
context.beginPath();
context.lineTo(0, 29);
context.lineTo(0 + te.width, 29);
context.stroke();

var buffer = canvas.toBuffer('raw');
console.log(vlla.encode(buffer));
