from fastapi import FastAPI
import pandas as pd
from db.postgrese import get_postgres_data
from db.mongo import get_mongo_data

app = FastAPI()

@app.get("/")
def home():
    print("Home endpoint accessed")
    print("Fetching data from MongoDB...")
    return {"message": "FastAPI Script Runner"}

@app.get("/run-script")
def run_script():

    mongo_data = get_mongo_data()

    postgres_data = get_postgres_data()

    combined = mongo_data + postgres_data

    df = pd.DataFrame(combined)

    file_path = "output/test_data.csv"

    df.to_csv(file_path, index=False)

    return {
        "status": "success",
        "rows": len(df),
        "file": file_path
    }


@app.get("/test")
def test():
    x = 5
    y = 10
    result = x + y   # 👉 Put breakpoint here
    return {"result": result}