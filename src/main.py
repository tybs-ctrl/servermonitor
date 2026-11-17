from fastapi import FastAPI

from cpu import CPU
from ram import RAM

import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    cpu = CPU()
    ram = RAM();
    print(cpu.update())
    print(ram.update())

    return {
        "cpu_name": cpu.name,
        "cpu_cores": cpu.cores,
        "cpu_frequency": round(cpu.frequency, 2),
        "max_frequency": round(cpu.max_frequency,2),
        "cpu_load": cpu.load,
        "total_ram": round(ram.total_ram,2),
        "used_ram": round(ram.used_ram,2),
        "total_swap": round(ram.total_swap,2),
        "used_swap": round(ram.used_swap,2)        
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    
