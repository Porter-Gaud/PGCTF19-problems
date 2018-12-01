# Reverse Engineering 2
80 pts
---
## Problem
Here's my binary- I think there's something in there...

## Internal Notes
* Solution * pgctf{obufekpz}
This was a Swift program compiled into a binary. This means you should use Mach-O 64-bit tools. The disassembler I used for testing was Hopper v4.0- it's free (as a trial) and makes it easy to follow specific variables around. Once you find the flag variable, which is almost immediately noticeable once disassembled in Hopper, you can follow any references to it. Once you find it, the string is intentionally under the limit for the Swift compiler to categorize it as a string, so it stays in assembly-form around the place it sets the variable.

You'll find the hex data: 7d 7a 70 6b 65 66 75 62 6f 7b 66 74 63 67 70
which, since it's assembly, is reversed per segment. So you'll need to, for instance, put 70 at the front and 7d at the end.

This spells out pgctf{obufekpz} once you decode the hex.
