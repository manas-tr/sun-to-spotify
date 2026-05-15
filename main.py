from fastapi import FastAPI

app = FastAPI(
    title="SUN-flower",
    description="Your daily SUN-rise, delivered before your commute.",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "message": "SUN-flower has bloomed 🌻"
    }