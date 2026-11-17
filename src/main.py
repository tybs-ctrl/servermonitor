from fastapi import FastAPI

from cpu import CPU

import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    cpu = CPU()
    print(cpu.update())
    return {
        "cpu_name": cpu.name,
        "cpu_cores": cpu.cores,
        "cpu_frequency": round(cpu.frequency, 2),
        "max_frequency": round(cpu.max_frequency,2),
        "cpu_load": cpu.load
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    
