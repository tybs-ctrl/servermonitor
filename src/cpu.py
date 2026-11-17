import psutil
import cpuinfo

class CPU:
    def __init__(self):
        self.update()
    def update(self):
        self.name = cpuinfo.get_cpu_info().get("brand_raw")
        self.cores = psutil.cpu_count()
        self.frequency = psutil.cpu_freq()[0]
        self.max_frequency = psutil.cpu_freq().max
        self.load = psutil.cpu_percent(interval=1)
        return self
    def __str__(self):
        return f"CPU Name: {self.name}, CPU Cores: {self.cores}, Frequency: {self.frequency} ({self.max_frequency}) MHz, Load: {self.load}%"

