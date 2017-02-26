var vlla = require('../libvlla.js');

var canvas = vlla.requestCanvas();
var context = vlla.requestContext();

// fill background
context.fillStyle = 'rgb(0, 0, 0)';
context.fillRect(0, 0, vlla.width, vlla.height);

context.fillStyle = 'green';
context.font = '18px sans';
context.fillText("hello", 0, 27);

setInterval(vlla.render, 100);
