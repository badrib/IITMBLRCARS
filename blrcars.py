
# BLRCARS APP


print("BLRCARS APP")

# This is a sample fastapi implementation
# run as a webservice on default port 8000 exposing 2 GET /health & /ask 
# To run in windows in command prompt
# ensure that the pipl list shows fastapi and uvicorn
# use the command 
# pip install fastapi uvicorn
# go to the command and run this main.py as follows
# using default port 8000
#       uvicorn main.app => runs in default port 8000
# if you want to run in a different port (8001)
#       uvicorn main:app --host 0.0.0.0 --port 8001
# go to the browser you can access the server http://localhost:<port>/


# ==== How to run your code available via a public url using ngrok.
# Signup in ngrok => get the token
# Download the ngrok zip file 
# run the command 
#       ngrok config add-authtoken YOUR_TOKEN_HERE

# after the uvicorn main:app is running in a port(8000) then create a tunnel with ngrok
#       ngrok http 8000 

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Ask endpoint with optional query parameter
@app.get("/ask")
def ask(q: Optional[str] = None):
    if not q:
        return {"message": "Please provide a query using ?q=your_question"}
    
    # Simple mock response
    return {
        "question": q,
        "answer": f"You asked: '{q}'. This is a placeholder response."
    }
