import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def balance():
    return {"content":"Ваш баланс 100 рублей"}

if __name__ == "__main__":
    uvicorn.run("core:app", host="127.0.0.1", port=8000, reload=True)