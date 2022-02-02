import uvicorn
from app.main import app

# async def read_items(commons: CommonQueryParams = Depends()):

if __name__ == "__main__":
    uvicorn.run("start:app", host="0.0.0.0", port=8000, reload=True)