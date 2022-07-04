from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def main():
    return "Yes, you did."