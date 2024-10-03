from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import UserError
from .database import SessionLocal
from .config import N

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/generate-exercise")
def generate_exercise(user_id: int, db: Session = Depends(get_db)):
    results = db.query(
        UserError.category,
        UserError.sub_category,
        UserError.frequency
    ).filter(
        UserError.user_id == user_id
    ).order_by(
        UserError.frequency.desc()
    ).limit(N).all()

    if not results:
        raise HTTPException(status_code=404, detail="No errors found for this user")

    response = [
        {
            "errorCategory": result.category,
            "errorSubCategory": result.sub_category,
            "errorFrequency": result.frequency
        }
        for result in results
    ]

    return {"top_errors": response}

