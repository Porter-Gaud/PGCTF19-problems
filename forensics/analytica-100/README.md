# Phish Food
50 pts
---
## Problem
```
Link to index.html
```

## Hint (only give this out if people are struggling)
What's with all of the icing on top of this Google Form?

## Internal Notes
### Flag
pgctf{data_l3akage_n3ver_stops}

### Problem Notes
The goal of this problem is to get to "https://docs.google.com/forms/d/e/1FAIpQLSc5kBjZz_pW4fgFggOpR9hGYLwZUTLkqAqpXXVXyvizYjFDBg/viewanalytics".  This page lets any user view all of the form's responses, which lo-and-behold, has the flag in it.  The easiest way to get to this page is the nice little link on the form submission page.  When I initially thought of this problem, I did not realize that the link was there (which would have made this a more interesting problem).  I still wanted to do this problem after I realized this, so I embedded the Google Form in a page and wrote Javascript to redirect the user to a custom success page after hitting submit.

One idea that I had but couldn't figure out how to implement was how to redirect the user before Google "caught" the submission, which would have made it easier to find the flag after exploiting (sifting through "junk" responses isn't intended to be the pedagogical takeaway of this problem).

