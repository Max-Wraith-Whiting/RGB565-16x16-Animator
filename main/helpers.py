"""
Helper functions.
"""

def rgb_to_hex(r, g, b):
    """Takes RGB, returns tuple of RGB565 hex and RGB888 hex."""

    hex = "{0:x}".format((r << 16) + (g << 8) + b)
    while (len(hex) < 6):
        hex = "0" + hex
                
    rgb565 = "{0:x}".format(((r & 248) << 8) + ((g & 252) << 3) + ((b & 248) >> 3))
    while (len(rgb565) < 4):
        rgb565 = "0" + rgb565

    return('0x' + rgb565, hex)