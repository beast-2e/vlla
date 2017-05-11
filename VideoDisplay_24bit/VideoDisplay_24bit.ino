/*  OctoWS2811 VideoDisplay.ino - Video on LEDs, from a PC, Mac, Raspberry Pi
    http://www.pjrc.com/teensy/td_libs_OctoWS2811.html
    Copyright (c) 2013 Paul Stoffregen, PJRC.COM, LLC

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.

Update: The movie2serial program which transmit data has moved to "extras"
https://github.com/PaulStoffregen/OctoWS2811/tree/master/extras
 
  Required Connections
  --------------------
    pin 2:  LED Strip #1    OctoWS2811 drives 8 LED Strips.
    pin 14: LED strip #2    All 8 are the same length.
    pin 7:  LED strip #3
    pin 8:  LED strip #4    A 100 to 220 ohm resistor should used
    pin 6:  LED strip #5    between each Teensy pin and the
    pin 20: LED strip #6    wire to the LED strip, to minimize
    pin 21: LED strip #7    high frequency ringining & noise.
    pin 5:  LED strip #8
    pin 15 & 16 - Connect together, but do not use
    pin 4:  Do not use
    pin 3:  Do not use as PWM.  Normal use is ok.
    pin 12: Frame Sync

    When using more than 1 Teensy to display a video image, connect
    the Frame Sync signal between every board.  All boards will
    synchronize their WS2811 update using this signal.

    Beware of image distortion from long LED strip lengths.  During
    the WS2811 update, the LEDs update in sequence, not all at the
    same instant!  The first pixel updates after 30 microseconds,
    the second pixel after 60 us, and so on.  A strip of 120 LEDs
    updates in 3.6 ms, which is 10.8% of a 30 Hz video frame time.
    Doubling the strip length to 240 LEDs increases the lag to 21.6%
    of a video frame.  For best results, use shorter length strips.
    Multiple boards linked by the frame sync signal provides superior
    video timing accuracy.

    A Multi-TT USB hub should be used if 2 or more Teensy boards
    are connected.  The Multi-TT feature allows proper USB bandwidth
    allocation.  Single-TT hubs, or direct connection to multiple
    ports on the same motherboard, may give poor performance.
*/

#include "OctoWS2811_modified.h"

// The actual arrangement of the LEDs connected to this Teensy 3.0 board.
// LED_HEIGHT *must* be a multiple of 8.  When 16, 24, 32 are used, each
// strip spans 2, 3, 4 rows.

#define LED_WIDTH      60   // number of LEDs horizontally
#define LED_HEIGHT     16   // number of LEDs vertically (must be multiple of 8)

const int totalLeds = LED_WIDTH * LED_HEIGHT;
const int ledsPerStrip = 2 * LED_WIDTH;

DMAMEM int displayMemory[3*totalLeds/4]; // 3 bytes per led, 4 bytes per int
int drawingMemory[3*totalLeds/4]; // 3 bytes per led, 4 bytes per int
char drawingMemory_24bit[3*totalLeds]; // 3 bytes per led, 4 bytes per int
elapsedMicros elapsedUsecSinceLastFrameSync = 0;

const int config = WS2811_800kHz; // color config is on the PC side

OctoWS2811 leds(ledsPerStrip, displayMemory, drawingMemory, config);

void setup() {
  //Serial.begin(250000);
  Serial.begin(4000000); // Gotta get that high data rate
  Serial.setTimeout(50);
  leds.begin();
  leds.show();
}

int i = 0;

bool get_bit(int num, int index){
  return (num >> index) & 1;
}

// Remaps colors if r = 0, g = 1, b = 2.
int grb_to_rgb(int index) {
  return index == 0 ? 1 :
         index == 1 ? 0 : index;
}
// Draw values to the drawingMemory
void draw(char* drawingMemory_24bit) {

  // Do the interleaving thing with the bits and bytes...
  // See the diagram in README.md

  // Sneaky bit hack
  char* drawingMemoryAsChar = (char *)drawingMemory;

  // Interleaving is pretty much matrix transpose, right?
  for(int column = 0; column < ledsPerStrip; column++) {
    // Take care of how each LED strip "zig-zags" across the vlla
    int flippedColumn = column >= LED_WIDTH ? ledsPerStrip - (column - LED_WIDTH) - 1: column;

    // Keep 24 bit RGB chunks together
    for(int color_24bit = 0; color_24bit < 24; color_24bit++) {
      char interleaved = 0;
      // Each byte consists of one bit from LEDs across each strip
      for(int strip = 0; strip < totalLeds / ledsPerStrip; strip++) {
        interleaved |= get_bit(drawingMemory_24bit[(flippedColumn + strip * ledsPerStrip) * 3 + grb_to_rgb(color_24bit/8)], 7 - color_24bit%8) << strip;
      }
      drawingMemoryAsChar[column * 24 + color_24bit] = interleaved;
    }
  }
}

void loop() {

  // Wait for frame start
  while(Serial.read() != 255);

  // Get that image
  Serial.readBytes(drawingMemory_24bit, sizeof(drawingMemory_24bit));

  // Decode 8 bit color values and copy into drawingMemory
  draw(drawingMemory_24bit);

  // Update LEDS
  leds.show();

}

