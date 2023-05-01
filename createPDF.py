from fpdf import FPDF
from .dividers import dividers

pdf = FPDF(orientation='P', unit='mm', format='A4')

y = -1

scale = 1.04

width = 93 * scale
height = 68 * scale

card_separation = 4

offset_x = (210 - width * 2 - 1 / card_separation) / 2
offset_y = (297 - height * 4 - (1 / card_separation) * 3) / 2

for idx, image in enumerate(dividers):
    if not idx % 8:
        pdf.add_page()
        y = -1

    if not idx % 2:
        y += 1

    pos_x = idx % 2 * width + offset_x + idx % 2 / card_separation
    pos_y = y * (height + 1 / card_separation) + offset_y

    print(idx, image)
    pdf.image(image, x=pos_x, y=pos_y, w=width, h=height)


pdf.output('divider.pdf', 'F')
