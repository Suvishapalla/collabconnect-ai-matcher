from fastapi import FastAPI
from match_engine import find_matches
import uvicorn

app = FastAPI()

@app.get("/match/{username}")
def match_user(username: str):
    matches = find_matches(username)
    return {"matches": matches}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
