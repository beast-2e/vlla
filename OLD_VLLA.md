Bvlla-new
========

Here's an overview of the project from the point of view of folders.

# Existing codebase

GLSL <--> vlla-shader <--> libvlla <--> Teensy <--> OctoWS2811 <--> LEDs

## ~/vlla
The existing vlla serial communication library, which I'll be referring
to as libvlla. Helps to write an array of pixels over serial to the
Teensys on the vlla.
[Github](https://github.com/jmptable/libvlla)

## ~/vlla-shader
The existing vlla GLSL shader toy. Runs shaders and displays the
result onto the vlla using libvlla.
[Github](https://github.com/jmptable/vlla-shader)

### ./OctoWS2811
This library helps the Teensy communicate with the LEDs. Just flash
`OctoWS2811/examples/VideoDisplay/VideoDisplay.ino` onto both Teensy's
and it'll work without a hitch with vlla-shader and libvlla.
[Github](https://github.com/PaulStoffregen/OctoWS2811)


# Development environment

### ./Teensy
Teensy uploader. Helps upload code to the Teensy.
You'll need too `ssh -X` and run it outside `screen`.
[Teensy](https://www.pjrc.com/teensy/loader_linux.html)

### ./arduino-...
Installation of Arduino IDE with TeensyDuino. An easy way to write and
run code for the Teensy. Be sure that the Teensy uploader is also
running to be able to upload code!
Also, note that you'll need to `ssh -X` and run it outside `screen`.
[Arduino](https://www.arduino.cc/en/Main/Software)
[TeensyDuino](https://www.pjrc.com/teensy/td_download.html)

# It begins!

Spent a while trying to figure out why strips of LEDs on both sides
of the vlla don't work. It isn't a Teensy/software problem, because
interchanging the Teensy's in the sockets don't seem to change anything.
Might return to this later.

Anyways, I began by trying to understand the data format that
`VideoDisplay.ino` accepts. After some fooling around, I've assembled
this diagram, where numbers represent the index of *bits* that need to
be sent:

```
                   STRIP 1    STRIP 2    STRIP 3    STRIP 4    STRIP 5    STRIP 6    STRIP 7    STRIP 8
                --
            msb |    0          1          2          3          4          5          6          7
                |    8          9          10         11         12         13         14         15
                |    16         17         18         19         20         21         22         23
    [   GREEN   |    24         25         26         27         28         29         30         31
    [   byte    |    32         33         34         35         36         37         38         39
    [           |    40         41         42         43         44         45         46         47
    [           |    48         49         50         51         52         53         54         55
    [       lsb |    56         57         58         59         60         61         62         63
    [           --
    [       msb |    64         65         66         67         68         69         70         71
    [           |    72         73         74         75         76         77         78         79
    [           |    80         81         82         83         84         85         86         87
LED [   RED     |    88         89         90         91         92         93         94         95
#1  [   byte    |    96         97         98         99         100        101        102        103
    [           |    104        105        106        107        108        109        110        111
    [           |    112        113        114        115        116        117        118        119
    [       lsb |    120        121        122        123        124        125        126        127
    [           --
    [       msb |    128        129        130        131        132        133        134        135
    [           |    136        137        138        139        140        141        142        143
    [           |    144        145        146        147        148        149        150        151
    [   BLUE    |    152        153        154        155        156        157        158        159
    [   byte    |    160        161        162        163        164        165        166        167
                |    168        169        170        171        172        173        174        175
                |    176        177        178        179        180        181        182        183
            lsb |    184        185        186        187        188        189        190        191
                --
                --
            msb |    192        193        194        195        196        197        198        199
                |    200        201        202        203        204        205        206        207
                |    208        209        210        211        212        213        214        215
    [   GREEN   |    216        217        218        219        220        221        222        223
LED [   byte    |    224        225        226        227        228        229        230        231
#2  v           v    ...        ...        ...        ...        ...        ...        ...        ...
```


Note that a single "STRIP" above refers to *TWO* physical LED strips:
when a strip connected to the Teensy reaches the end of the VLLA, it's
actually connected to another strip running the opposite
direction!

Overall, the current spec is quite non-straightforward. I created a new
version of `VideoDisplay.ino`, called `VideoDisplay_8bit.ino` that
accepts 1 byte per LED (960 bytes total, 60 wide by 16 px high),
sent in reading order (across left-to-right, then top-to-bottom).
Each byte should be in the 256 color format: RRRGGGBB.
However, more has changed:

- No more Master/Slave system. A little bit of screen tear never hurt
  anyone. Just send the desired data to both Teensys.

- Before sending the data, you must send ascii byte 255.
  This helps the Teensy know when a frame starts.
  Make sure that in your color data, you aren't sending 255.

After upping the baud rate to 4000000 (can you believe it? Linux
actually supports that!) I've created a series of tests in
`tests_for_8bit`: an image loader example, and a high-frame-rate
example that goes up to 240hz!

However, at this point, we're working with individual Teensys, each
controlling half of the vlla. I tried working on `SerialSplitter`,
which would redirect standard in to both teensys, but I couldn't get
it to work.

Instead, Willie and I threw together `vlla-socket`, a
websocket interface that you can write a full RRRGGGBB frame to,
(60 x 32, 1960 total bytes) without worrying about sending the
frame start signal - vlla-socket takes care of that for you.
It comes with a companion p5.js sketch that controls the vlla
in real time from your browser. How cool is that?

To start the server, cd into `vlla-new/vlla-socket` and run
`npm run start`