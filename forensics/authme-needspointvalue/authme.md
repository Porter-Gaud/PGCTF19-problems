# Authenticate Me!
?? pts
---
## Problem
```
[Image attachment]('generated-qr.png)
What will I be at t=1529139600?
```

## Hint
I'm deterministic.  What does that mean?

## Internal Notes
### Creator's Note
It is highly encouraged that the reader of these "internal notes" should attempt to *solve* the problem before reading the solution for the first time.  It truly is a fun problem to solve for CTF-lovers, if you haven't seen the "trick" before.

### Problem Notes
Solution: "537508"


**Solution:**
TOTP, or time-based one-time passwords, is the [RFC standardized](https://tools.ietf.org/html/rfc6238#section-4.1) protocol to generates 2FA keys that are displayed to the user.  This occurs in SMS-based 2FA, of predictable importantce to CTF competitors, apps like Google Authenticator and Authy.  These apps can actually read the QR code, as its in the de facto [standardized URI format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format)!  After scanning the QR code, the user will see "otpauth://totp/PGCTF:tgalloway18@portergaud.edu?secret=IFJUIRSLJRFA&issuer=PGCTF" and will then realize that the protocol is this TOTP.  TOTP uses a secret key to *deterministically* (the hint!) generate a six digit sequence that acts as a 2FA code.  Generally, these keys are assigned by user.  Think about what the implications would be if that secret key got leaked!
So, after looking at the TOTP documentation and googling around, we now have a little bit of understanding of what this URI tells us:
Label: PGCTF
Account name: tgalloway18@portergaud.edu
Secret (encoded): IFJUIRSLJRFA
Issuer: PGCTF
Back to the problem description.  The really cool thing about this problem is that now that we have the secret key and the associated account name, we can generate a six digit 2FA key for *any* arbitrary time!  So lets take [epoch time](https://en.wikipedia.org/wiki/Unix_time) t=1529139600, which is June 19th 2019 at 9:00:00AM GMT (importantly, the RFC standard for TOTP specifies the use of GMT timestamps).  You can use [this totp Python library](https://pythonhosted.org/otpauth/) to generate a TOTP token for a specific time. If you're ignorantly avoiding having to program, you may be able to also get the right one with some clever changing of your system clock and [this](https://totp.danhersam.com/) website.  Check out the solution.py file to see the rest.