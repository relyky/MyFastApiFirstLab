from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world. 哈囉世界。"}

@app.get('/book/{book_id}')
def get_book_by_id(book_id: int):
    return {
        'book_id': book_id
    }
