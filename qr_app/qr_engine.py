import qrcode
import os
from datetime import datetime

def generate_qr(data,export_folder="static/exports"):

    filename = datetime.now().strftime("%Y%m%d-%H%M%S")+".png"
    filepath = os.path.join(export_folder,filename)
    img = qrcode.make(data)
    img.save(filepath)
    return filename
