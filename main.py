from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # IMPORTANTE

app = FastAPI()

# Configuración de seguridad para que cualquier sitio pueda consultar tu API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

RIDER_DATABASE = {
    "827258": "Untrusted",
    "529582": "Trusted",
    "398264": "Trusted",
    "1167037": "Untrusted",
    "1431677": "Trusted"
}

@app.get("/exec")
def get_rider_segment(riderId: str = None):
    # Aseguramos que riderId sea un string y quitamos espacios
    rid_clean = str(riderId).strip() if riderId else ""
    
    segmento = RIDER_DATABASE.get(rid_clean, "Not Found")
    
    return {
        "riderId": rid_clean,
        "segment": segmento
    }
