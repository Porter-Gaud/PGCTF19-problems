# Wireshark 4: IRC 4
30 pts
---
## Problem
What version IRC is our AOL server running? (Flag EX: charlesirc-43.7.5)

## Hint
You may need to look deeper in the TCP/IRC stream...

## Internal Notes
* Solution * 2.8/hybrid-6.3.1

Same way as IRC_3 (since realistically, I want people to do it the other way than I did), you can see in the TCP stream:

```
:irc5.aol.com 002 rgdiuggac :Your host is irc5.aol.com[irc5.aol.com/6667], running version 2.8/hybrid-6.3.1
```
