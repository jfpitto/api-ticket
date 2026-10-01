from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI(
    title="API Soporte Aplicaciones",
    version="1.0.0"
)


class CasoSoporte(BaseModel):
    aplicacion: str
    responsable_soporte: str
    comentarios: str
    solicitud_hp: str
    titulo_solicitud: str
    estado_solicitud: str
    detalle_estado: str
    fecha_envio_usuario: str
    proveedor: str
    fecha_derivacion_proveedor: str
    fecha_ultima_novedad: str
    fecha_creacion_ticket: str
    naturaleza: str
    prioridad: str
    solicito_sn3: str
    app: str
    app_det: str
    fecha_llegada_bandeja: str
    fecha_primera_derivacion: str
    masivo: str
    afecto_cliente: str
    causo_indisponibilidad: str
    tiempo_indisponibilidad: str
    tiempo_trabajado_sn2: str


def crear_bd():
    conn = sqlite3.connect("soporte.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS casos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        aplicacion TEXT,
        responsable_soporte TEXT,
        comentarios TEXT,
        solicitud_hp TEXT,
        titulo_solicitud TEXT,
        estado_solicitud TEXT,
        detalle_estado TEXT,
        fecha_envio_usuario TEXT,
        proveedor TEXT,
        fecha_derivacion_proveedor TEXT,
        fecha_ultima_novedad TEXT,
        fecha_creacion_ticket TEXT,
        naturaleza TEXT,
        prioridad TEXT,
        solicito_sn3 TEXT,
        app TEXT,
        app_det TEXT,
        fecha_llegada_bandeja TEXT,
        fecha_primera_derivacion TEXT,
        masivo TEXT,
        afecto_cliente TEXT,
        causo_indisponibilidad TEXT,
        tiempo_indisponibilidad TEXT,
        tiempo_trabajado_sn2 TEXT
    )
    """)

    conn.commit()
    conn.close()


crear_bd()


@app.get("/")
def root():
    return {
        "estado": "OK",
        "mensaje": "API Soporte Activa"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/casos")
def crear_caso(caso: CasoSoporte):

    conn = sqlite3.connect("soporte.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO casos(
            aplicacion,
            responsable_soporte,
            comentarios,
            solicitud_hp,
            titulo_solicitud,
            estado_solicitud,
            detalle_estado,
            fecha_envio_usuario,
            proveedor,
            fecha_derivacion_proveedor,
            fecha_ultima_novedad,
            fecha_creacion_ticket,
            naturaleza,
            prioridad,
            solicito_sn3,
            app,
            app_det,
            fecha_llegada_bandeja,
            fecha_primera_derivacion,
            masivo,
            afecto_cliente,
            causo_indisponibilidad,
            tiempo_indisponibilidad,
            tiempo_trabajado_sn2
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?,?,?,?,?,?,?,
            ?,?,?,?
        )
    """,
    (
        caso.aplicacion,
        caso.responsable_soporte,
        caso.comentarios,
        caso.solicitud_hp,
        caso.titulo_solicitud,
        caso.estado_solicitud,
        caso.detalle_estado,
        caso.fecha_envio_usuario,
        caso.proveedor,
        caso.fecha_derivacion_proveedor,
        caso.fecha_ultima_novedad,
        caso.fecha_creacion_ticket,
        caso.naturaleza,
        caso.prioridad,
        caso.solicito_sn3,
        caso.app,
        caso.app_det,
        caso.fecha_llegada_bandeja,
        caso.fecha_primera_derivacion,
        caso.masivo,
        caso.afecto_cliente,
        caso.causo_indisponibilidad,
        caso.tiempo_indisponibilidad,
        caso.tiempo_trabajado_sn2
    ))

    conn.commit()
    conn.close()

    return {
        "resultado": "OK",
        "mensaje": "Caso registrado correctamente"
    }


@app.get("/casos")
def obtener_casos():

    conn = sqlite3.connect("soporte.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM casos")

    datos = cursor.fetchall()

    conn.close()

    return datos


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
