import qrcode

# URL de la imagen
url_imagen = "https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"  # Cambia esto por la URL de tu imagen

# Generar el código QR
qr = qrcode.QRCode(
    version=1,  # Tamaño del QR, puedes ajustarlo si es necesario
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada cuadro del QR
    border=4,     # Ancho del borde
)
qr.add_data(url_imagen)
qr.make(fit=True)

# Crear la imagen del QR
qr_img = qr.make_image(fill="black", back_color="white")

# Guardar el QR en un archivo
qr_img.save("codigo_qr.png")
print("¡Código QR generado y guardado como 'codigo_qr.png'!")
  # en este codigo realiza que una imagen desde internet y usando su liga enlazada
 # podemos convertirla a un codigo QR
