import qrcode
file_path="C:\\python learn\\QrCodes\\yt.png"
x=input("Enter url to generate qrcode: ").strip()
qrcode=qrcode.QRCode()
qrcode.add_data(x)
img=qrcode.make_image()
img.save(file_path)
print("Qr code generated successfully")

