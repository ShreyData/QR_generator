import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    SquareModuleDrawer, CircleModuleDrawer, RoundedModuleDrawer, GappedSquareModuleDrawer
)
from qrcode.image.styles.colormasks import SolidFillColorMask
import io
import base64
from PIL import Image, ImageColor

def generate_qr_advanced(data, version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, 
                         box_size=10, border=4, fit=True, 
                         fill_color="black", back_color="white", 
                         module_drawer='square', logo_base64=None):
    """
    Generates an advanced QR code with custom styles, colors, and an optional logo.
    Returns the image as a base64 encoded string.
    """
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=fit)

    # Map module drawer string to actual drawer object
    drawers = {
        'square': SquareModuleDrawer(),
        'circle': CircleModuleDrawer(),
        'rounded': RoundedModuleDrawer(),
        'gapped': GappedSquareModuleDrawer()
    }
    drawer = drawers.get(module_drawer, SquareModuleDrawer())

    # Handle Colors using PIL's ImageColor for robust conversion
    try:
        f_rgb = ImageColor.getrgb(fill_color)
        b_rgb = ImageColor.getrgb(back_color)
    except Exception as e:
        print(f"Color conversion error: {e}")
        f_rgb = (0, 0, 0)
        b_rgb = (255, 255, 255)

    # Generate the image with styles
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        color_mask=SolidFillColorMask(back_color=b_rgb, front_color=f_rgb),
    )

    # Handle Logo
    if logo_base64:
        try:
            # Clean base64 string
            if ',' in logo_base64:
                logo_base64 = logo_base64.split(',')[-1]
            
            logo_data = base64.b64decode(logo_base64)
            logo = Image.open(io.BytesIO(logo_data)).convert("RGBA")
            
            # Calculate logo size (max 20% of QR size)
            qr_width, qr_height = img.size
            logo_size = int(qr_width * 0.2)
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Paste logo in the middle
            pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            
            # Create a white background for the logo to ensure visibility
            white_bg = Image.new("RGBA", (logo_size, logo_size), b_rgb + (255,))
            white_bg.paste(logo, (0, 0), logo)
            
            img.paste(white_bg, pos)
        except Exception as e:
            print(f"Error embedding logo: {e}")

    # Convert to base64 string
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return f"data:image/png;base64,{img_str}"
