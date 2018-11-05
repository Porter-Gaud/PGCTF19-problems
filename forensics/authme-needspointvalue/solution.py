from otpauth import OtpAuth
import qrcode

auth = OtpAuth('ASDFKLJ')  # a secret string
# Generate QR code

uri = auth.to_uri('totp', 'PGCTF:tgalloway18@portergaud.edu', 'PGCTF')
print "Generaing QR code with encdoded uri: " + uri
img = qrcode.make(uri)
img.save("generated-qr.png")


# Solve
print auth.totp(timestamp=1529139600)


