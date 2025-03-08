from fastapi import FastAPI  
from pymongo import MongoClient

     
    
app = FastAPI()


def get_db_client():
    try:
        client = MongoClient("mongodb+srv://ali:PLztqH3DFAOWYsQy@cluster0.dogd0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print("Connected to the database")
        return client
    except Exception as e:
        print(f"Error connecting to the database: {e}")
    
        return None
client = get_db_client()
    
db = client["students_db"]
# collection = db["students"]

@app.get("/")
def read_root():
    return {
        "data": [],
        "error": None,
        "message": "Welcome to the students API",
        "status": "success"
            }

 
 
        
@app.get("/read_user/{reg_no}")
def read_user(reg_no: int):
    try:
        user = db.students.find_one({"reg_no": reg_no})
        if user is None:
            raise Exception("User not found")
        return {
            "data": {
                "name": user["name"],	
                "email": user["email"],
                "reg_no": user["reg_no"]
                
},
            "error": None,
            "message": "User read successfully",
            "status": "success"
        }
    except Exception as e:
        return {
            "data": [],
            "error": "Error reading user",
            "message": str(e),
            "status": "failed"
        }
