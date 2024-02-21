I recently acquired a Samsung Odyssey G95SC, a 49-inch ultrawide desktop monitor with impressive specifications:

- OLED panel
- 5120x1440 resolution
- 240Hz refresh rate (G-Sync Compatible)
- DisplayHDR True Black 400

The only issue I encountered was that the highest HiDPI resolution available on macOS is 2560x720, as macOS seems to only provide 2x integer scaling for third-party monitors. However, after some trial and error, I figured out a way to enable more scaled resolutions. All you need to do is download SwitchResX and set its scaled resolution base to 5120x1440.

After a reboot, you should see several new scaled resolutions, which could provide more vertical space.

For example, when you are using a 3840x1080 HiDPI scaled mode, macOS would render at 7680x2160, then scale it down to display on the monitor's physical resolution of 5120x1440.