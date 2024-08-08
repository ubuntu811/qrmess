#!/usr/bin/python3

import qrcode
import random
from pprint import pprint
from fpdf import FPDF

filename="./stuff.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

random.shuffle(lines)

pdf = FPDF()
pdf.add_page(orientation="Landscape", format="A4")

nr=row=col=0
max_cols = 4
col_width=40
row_height=40

for line in lines:
  nr+=1
  col += 1
  if col > max_cols:
    col = 1
    row += 1

  img = qrcode.make(line)

  img.save(f"img/{nr}.png")
  pdf.image(f"img/{nr}.png", 10 + (col * col_width), 10 + (row * row_height), 30, 30)

pdf.output("doc.pdf")
