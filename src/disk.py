import psutil

class DISK:
    def __init__(self):
        self.update()
    def update(self):
            
        self.total = 0
        self.used = 0
        seen = set()

        for part in psutil.disk_partitions(all=False):
            key = (part.device, part.fstype)
            if key in seen:
                continue
            seen.add(key)

            try:
                usage = psutil.disk_usage(part.mountpoint)
            except PermissionError:
                continue

            self.total += usage.total
            self.used += usage.used
        self.total = self.total / (1024.0 ** 3)
        self.used = self.used / (1024.0 ** 3)
        return self
    def __str__(self):
        return f"Disk: {self.used} ({self.total})"