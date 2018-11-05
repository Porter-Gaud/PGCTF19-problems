from otpauth import OtpAuth
import qrcode

auth = OtpAuth('P98WQ4RAOSIDF')  # a secret string
# Generate QR code

uri = auth.to_uri('totp', 'PGCTF:dbergman@portergaud.edu', 'PGCTF')
img = qrcode.make(uri)
img.save("generated-qr.png")


# Solve
print auth.totp(timestamp=1529139600)


