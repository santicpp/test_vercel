from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Datos extraídos de tu CSV para testear
RIDER_DATABASE = {
    "827258": "Untrusted",
    "529582": "Trusted",
    "398264": "Trusted",
    "1167037": "Untrusted",
    "1431677": "Trusted"
}

@app.get("/")
def home():
    return {"status": "API Funcionando"}

# Este es el endpoint que conectará con tu código YAML
@app.get("/exec")
def get_rider_segment(riderId: str):
    # Buscamos el rider en nuestra "base de datos"
    segmento = RIDER_DATABASE.get(riderId, "Not Found")
    
    # Retornamos el formato exacto que espera tu YAML: $infoRider.response.body.segment
    return {
        "riderId": riderId,
        "segment": segmento
    }
