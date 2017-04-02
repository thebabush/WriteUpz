# Dakota State University and University of Nebraska-Kearny Reverse Engineering CTF

This CTF was fun :D

I managed to solve all the challenges but some guy named *Nick* managed to
finish before me so he got moar points.
To my defense, I was playing in a totally different timezone.

Most of the challenges involved obfuscated (pseudo-)malware so there's no much
point in explaining how I gradually deobfuscated them.
They were simple enough to not require complex automated tools.

## x86

### Challenge 3

The file was the dump of a MBR.
You can easily verify it using `file <name of the file>`.
Once set up to run inside bochs, it started showing random-looking text:

![x86 screenshot](images/x86_3.png)

The 16-bit assembly code in the MBR is printing some weird strings using the
BIOS's built-in functionalities.
Basically, it starts from an hard-coded array of 16-bit words and cyclically
XOR them with the same key.
This key is incremented every time the string is printed to the screen.

At this point, I was lost for a good amount of hours (too many, actually) since
I couldn't think of a way to turn this knowledge into a valid flag.
I reimplemented the ASM logic in python but I was totally lost.
In desperation, I did the simplest thing I could do: discard all the strings
which contained non-printable ASCII characters.
To my surprise, only one such string was outputted by my script and its XOR key
was 0x1337, so I knew I found the correct value.

The final script to get the flag is implemented in [x86_3.py](x86_3.py).

