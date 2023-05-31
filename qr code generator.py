import qrcode 
import image
qr = qrcode.QRCode(
    version = 15, # this number signif how complicated image will be and its type
    box_size = 10, # this number signify size of box 
    border = 5 # this number signify the white and black lines dimension in qr code  
)

data = "https://youtu.be/HF4-Ib-c-Zg"
# give the link and a qr code automaticaly will be generated soon
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black",back_colour = "white")
img.save("test.png")