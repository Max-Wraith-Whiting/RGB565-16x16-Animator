"""
Helper functions.
"""

def rgb_to_hex888(r, g, b):
    """Takes RGB, returns RGB888 hex."""
    hex = "{0:x}".format((r << 16) + (g << 8) + b)
    while (len(hex) < 6):
        hex = "0" + hex

    return(hex)

def rgb_to_hex565(r, g, b):
    """Takes RGB, returns RGB565 hex."""
    rgb565 = "{0:x}".format(((r & 248) << 8) + ((g & 252) << 3) + ((b & 248) >> 3))
    while (len(rgb565) < 4):
        rgb565 = "0" + rgb565

    return('0x' + rgb565)

def hex888_to_rgb(colour):
    """Takes hex888, returns RGB888."""
    hex = colour[1:]
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))