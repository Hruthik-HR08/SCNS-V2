import qrcode

url = "https://scns-projectprototype.oneapp.dev/"

img = qrcode.make(url)
img.save("C:\\Users\\lenovo\\OneDrive\\Desktop\\scns_projectprototype_qr.png.jpg")

print("QR saved as scns_projectprototype_qr.png.jpg")

print("QR Code generation complete.")