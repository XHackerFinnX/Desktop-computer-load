import psutil
import time
from PyQt5.QtCore import QTime


class Monitoring:
    @staticmethod
    def get_stats():
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        return cpu, ram, disk

    @staticmethod
    def format_time(start_time):
        elapsed_time = QTime(0, 0, 0).addSecs(int(time.time() - start_time))
        return elapsed_time.toString("hh:mm:ss")
