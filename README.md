# EDID overrides for Mac OS X

So we bought this new monitor from Dell (P2720DC) and connected it to our
MacBooks. Out of the box, it seemed quite blurry with both the USB-C and HDMI
cables, particularly with text rendering.

According to the internet, this has to do with the Macs sending the signal in
YCbCr colour format. If you suspect that you are affected by this issue, see if
you find a reference to YCbCr in the menu of the monitor settings. For the Dell,
it was in `> Menu > Color > Input Color Format`.

This being a somewhat common issue there are a few blog posts, discussion
threads and scripts for it:

* https://www.edmundofuentes.com/blog/2018/08/10/macos-external-display-antialiasing/
* https://gist.github.com/adaugherity/7435890

This repository is mostly for me to remember how to do this if I need it again
in the future. It has shown to work in the following configurations:

| Monitor         | Laptop               | Cable   | Result             |
| --------------- | -------------------- | ------- | ------------------ |
| Dell P2720DC    | MacBook Pro 13, 2015 | HDMI    | :heavy_check_mark: |
