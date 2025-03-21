import random
from werkzeug.security import generate_password_hash  # Librería para aplicar hash

minus = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "@$"

base = minus + numeros + simbolos  # Combinación para la contraseña
longitud = 6  # Tamaño de la contraseña

for n in range(20):
    muestra = random.sample(base, longitud)  # Crea una contraseña
    password = "".join(muestra)  # Unión de cada carácter
    password_encriptado = generate_password_hash(password)  # Encriptación hash de contraseña

    print(f"Contraseña {n+1}: {password} -> {password_encriptado}")  # Imprime contraseña generada y su hash
