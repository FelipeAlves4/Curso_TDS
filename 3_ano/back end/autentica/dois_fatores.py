import pyotp

totp = pyotp.TOTP('base32secret3232')
print("Código atual:", totp.now())

codigo_digitado = input("Digite o código: ")
if totp.verify(codigo_digitado):
    print("Código correto")
else:
    print("Código incorreto")
