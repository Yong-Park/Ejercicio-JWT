import jwt

# Generar un JWT firmado
clave = "yongbumpark_20117"  # Deberías mantener esta clave segura
payload = {"info": "Hola soy yong y este es mi mensaje"}  # Puedes poner aquí la información que quieras transmitir

token = jwt.encode(payload, clave, algorithm='HS256')
print(f"JWT Firmado: {token}")

# Verificar el JWT
try:
    data = jwt.decode(token, clave, algorithms=['HS256'])
    print(f"Información del Payload: {data["info"]}")
except jwt.InvalidTokenError:
    print("El token es inválido o ha sido modificado.")
