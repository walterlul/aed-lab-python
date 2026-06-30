import bcrypt
from database import SessionLocal
from models import Usuario




def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password.decode("utf-8")


def verify_password(password, hashed_password):
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)


def obtener_usuario(username):
    db = SessionLocal()

    usuario = (
        db.query(Usuario)
        .filter(Usuario.usuario == username)
        .first()
    )
    db.close()
    return usuario


def obtener_email(email):
    db = SessionLocal()

    usuario = (
        db.query(Usuario)
        .filter(Usuario.email == email)
        .first()
    )
    db.close()
    return usuario


def registrar_usuario(nombre: str, apellido: str, username: str, email: str, password: str):
    db = SessionLocal()

    try:
        # 1. Validar si el usuario ya existe
        usuario_existente = obtener_usuario(username)
        if usuario_existente:
            return {
                "success": False,
                "message": "El nombre de usuario ya está en uso",
                "data": None
            }

        # 2. Validar si el email ya existe
        email_existente = obtener_email(email)
        if email_existente:
            return {
                "success": False,
                "message": "El email ya está registrado",
                "data": None
            }

        # 3. Hashear contraseña
        password_hash = hash_password(password)

        # 4. Crear usuario
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            usuario=username,
            email=email,
            password=password_hash,
            rol="cliente"
        )

        # 5. Guardar en base de datos
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

        return {
            "success": True,
            "message": "Usuario creado correctamente",
            "data": {
                "id": nuevo_usuario.id,
                "usuario": nuevo_usuario.usuario,
                "email": nuevo_usuario.email
            }
        }

    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "message": f"Error al crear usuario: {str(e)}",
            "data": None
        }

    finally:
        db.close()


def iniciar_sesion(username:str, password:str):
    db = SessionLocal()
    try:
        #Buscar usuario x username
        usuario = obtener_usuario(username)

        if not usuario:
            return {
                "success": False,
                "message": "Usuario o contraseña incorrecto",
                "data": None
            }
        if not verify_password(password, usuario.password):
            return {
                "success": False,
                "message": "Usuario o contraseña incorrecto",
                "data": None
            }
        return {
            "success": True,
            "message": "Inicio de sesión exitoso",
            "data": {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "apellido": usuario.apellido,
                "email": usuario.email,
                "rol": usuario.rol
            }
        }
    except Exception as e:
        return{
            "success": False,
            "message": f"Error al iniciar sesion: {str(e)}",
            "data": None
        }
    finally:
        db.close()