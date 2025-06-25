import bcrypt

senha = b"minhaSenhaSegura"
hashed = bcrypt.hashpw(senha, bcrypt.gensalt())

if bcrypt.checkpw(senha, hashed):
    print("Senha correta")
else:
    print("Senha incorreta")
