import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    # Run the FastAPI app with Uvicorn server
    uvicorn.run(app)
