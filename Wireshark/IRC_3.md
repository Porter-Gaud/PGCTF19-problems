# Wireshark 3: IRC 3
25 pts
---
## Problem
What does our client try to set their IRC nickname to? (Flag EX: charlest)

## Hint
Look inside the packet.

## Internal Notes
* Solution * rgdiuggac

There are multiple ways to solve this problem, as there are with all the Wireshark problems. I used the filter "tcp.port == 6667" and chose to follow a TCP conversation that was around the middle of the IRC. This reveals the following data:

```
NOTICE AUTH :*** Found your hostname
NICK rgdiuggac
USER rgdiuggac localhost localhost :rgdiuggac
:irc5.aol.com 001 rgdiuggac :Welcome to the Internet Relay Network rgdiuggac
```

Ideally, new Wireshark users will go to each packet individually and manually follow the TCP stream after completing the last problem; this way, it inadvertently shows how TCP following works.
