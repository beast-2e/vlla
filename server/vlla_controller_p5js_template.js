// noprotect

function setup() {
    pixelDensity(1); // Work across screen densities

    var canvas = createCanvas(60, 32); // vlla is 60 x 32

    canvas.elt.style.width = "100%"; // Let's style our
    canvas.elt.style.height = "auto"; // preview appropriately
    canvas.elt.style.imageRendering = "pixelated";

    frameRate(60); // Can go up to 120 or down to 30
}

function draw() {

    /////////////
    // YOUR CODE GOES HERE
    background(0);
    ellipse(mouseX, mouseY, 20, 20);
    //
    /////////////

    updateVlla(); // You'll need this!
}

var wsopen = false, ws = new WebSocket('ws://evil.mit.edu:8080', 'vlla');
ws.onopen = function() { wsopen = true; }

function updateVlla() {
    loadPixels();
    if (wsopen) {
	ws.send(btoa(encodeVlla(pixels)));
    }
}

function encodeVlla(pixels) {
    var frame = "";
    for (var i = 0; i < pixels.length; i += 4) {
	frame += String.fromCharCode(
	    (floor(pixels[i] / 32) << 5) + // Red - 3 bits
      
	    (floor(pixels[i + 1] / 32) << 2) + // Green - 3 bits
	    (floor(pixels[i + 2] / 64)) // Blue - 2 bits
	);
    }
    return frame;
}
