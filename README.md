# Day 01
Bart Massey

Got GitHub Copilot Chat up and running. It immediately
solved Part 1 in Python, which appears to be its preferred
language for solving these.

Part 2 was a harder slog. I got several versions out of
Copilot that did not work for various reasons:

* First solution assumed word boundaries (whitespace) for
  everything.
  
* Second solution still assumed word boundaries, even though
  asked not to.
  
* Third solution did not assume word boundaries, but did
  assume that solution words would not overlap: they do overlap
  in the input, and are supposed to be treated as overlapping
  digits. For example "fiveightwo" is supposed to be treated
  as 582 with an intervening coincidental "igh".
  
In my opinion this is a very reasonable assumption: "the
digits were substituted with words" together with "random
other characters are present" doesn't seem to be an adequate
explanation for these overlaps. Ah well, I didn't write the
problem. Ironically the Part 1 solution, which used string
reversal to find the first digit on each end, would have
worked if modified appropriately: that would have been a
pain, though.

I give Copilot 4 of 5 on this. Have to deduct a point for
assuming word boundaries when the example didn't have them.
