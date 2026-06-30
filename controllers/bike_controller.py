from database import SessionLocal
from models import Bicicleta

def registrar_bicicleta(marca, modelo, color, tipo, precio_hora):
    db = SessionLocal()

    try:
        nueva_bicicleta = Bicicleta(
            marca=marca,
            modelo=modelo,
            color=color,
            tipo=tipo,
            precio_hora=precio_hora,
            estado="Disponible"
        )
        db.add(nueva_bicicleta)
        db.commit()
        db.refresh(nueva_bicicleta)

        return {
            "success": True,
            "message": "Bicicleta registrada correctamente",
            "data": {
                "id": nueva_bicicleta.id,
                "marca": nueva_bicicleta.marca,
                "modelo": nueva_bicicleta.modelo,
                "color": nueva_bicicleta.color,
            }
        }
    except Exception as e:
        db.rollback()

        return {
            "success": False,
            "message": f"Error al registrar bicicleta: {str(e)}",
            "data": None
        }
    finally:
        db.close()