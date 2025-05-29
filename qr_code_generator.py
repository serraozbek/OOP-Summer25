import qrcode

url = "https://preview--serra-warsaw-web.lovable.app/"

qr = qrcode.make(url)

qr.save("site_qr_kode.png")