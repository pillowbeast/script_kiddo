import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import ImageOps

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,   # more tolerant of styling
    box_size=20,   # size of each module in pixels
    border=2       # quiet-zone in *modules*
)
# qr.add_data("https://pillowbeast.github.io/")
qr.add_data("https://arxiv.org/abs/2503.23255")
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),                  # swap squares for circles
    color_mask=SolidFillColorMask(front_color=(0, 0, 0), back_color=(255, 255, 255)),
)

img = img.convert("RGB")
# add a fat rounded outline like the one in your screenshot
img = ImageOps.expand(img, border=60, fill="white")       # white cushion
img = ImageOps.expand(img, border=10, fill="black")       # outer black stroke
# img.save("blog_qr.png")
img.save("arxiv_qr.png")
