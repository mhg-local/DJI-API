#!/usr/bin/env python3
import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#host_addr = os.environ["localhost"]
#username = os.environ["Hive"]
#password = os.environ["Admin"]

app = FastAPI()


@app.get("/login")
async def pilot_login():
    file_path = "./couldhtml/login.html"
    with open(file_path, 'r') as file:
        file_content = file.read()
    file_content.replace("hostnamehere", localhost)
    file_content.replace("userloginhere", Hive)
    file_content.replace("userpasswordhere", Admin)
    return HTMLResponse(file_content)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000)
