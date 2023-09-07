#Collect text and conver the text into a QR code



import qrcode


def generate_qrcode():
    qr = qrcode.Qrcode(
        version =1,
        error_correction = qrcode.constants.ERROR_CORRECTION_L,
        box_size =10,
        border=4
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save("qrinmg001.png")
    
    
url = input("Input your url: ")
generate_qrcode(url)