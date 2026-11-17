import psutil

class RAM:
    def __init__(self):
        self.update()
    def update(self):
        virtual_memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()
        self.total_ram = virtual_memory.total / (1024.0 ** 3)
        self.used_ram = virtual_memory.used / (1024.0 ** 3)
        self.total_swap = swap_memory.total / (1024.0 ** 3)
        self.used_swap = swap_memory.used / (1024.0 ** 3)
        return self
    def __str__(self):
        return f"Memory: {self.used_ram} ({self.total_ram}), Swap: {self.used_swap} ({self.total_swap}"

