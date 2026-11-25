#!/usr/bin/env python3
"""Composite classic top/bottom meme caption text onto the generated scene.
Text is drawn with PIL (DejaVu Sans Bold, white fill, black stroke) so it is
always crisp and readable, unlike text baked in by an image model."""
from PIL import Image, ImageDraw, ImageFont

BUILD = "/home/hatch/workspace/makefun/builds/meme-sprint-3-20261124"
SRC = BUILD + "/media-generation-base-scene-0-2ab4a761-63ae-4dfd-8ac4-430e3999fe8b.webp"
OUT = BUILD + "/meme.png"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.open(SRC).convert("RGB")
W, H = img.size
print("base size:", W, "x", H)

d = ImageDraw.Draw(img)


def fit_font(text, max_w, start):
    size = start
    while size > 10:
        f = ImageFont.truetype(FONT, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return ImageFont.truetype(FONT, 10)


TOP = 'ME: "JUST FIX THE TYPO"'
BOT = [
    "MY AI AGENT: REWROTE THE CODEBASE,",
    "DELETED THE DATABASE,",
    "AND ORDERED 400 PIZZAS",
]

# Top caption, one line, near the top edge.
f_top = fit_font(TOP, int(W * 0.92), int(H * 0.085))
tw = d.textlength(TOP, font=f_top)
d.text(((W - tw) / 2, int(H * 0.025)), TOP, font=f_top, fill="white",
       stroke_width=max(3, f_top.size // 10), stroke_fill="black")

# Bottom caption, three lines, near the bottom edge.
f_bot = fit_font(max(BOT, key=len), int(W * 0.92), int(H * 0.062))
line_h = int(f_bot.size * 1.18)
total = line_h * len(BOT)
y = H - total - int(H * 0.025)
for line in BOT:
    tw = d.textlength(line, font=f_bot)
    d.text(((W - tw) / 2, y), line, font=f_bot, fill="white",
           stroke_width=max(3, f_bot.size // 10), stroke_fill="black")
    y += line_h

img.save(OUT)
print("saved:", OUT)
import os
print("bytes:", os.path.getsize(OUT))
