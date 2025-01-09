import sys
import time
from PyQt5.QtWidgets import QApplication
from ui import MonitoringAppUI
from database import DatabaseManager
from monitoring import Monitoring


class MonitoringApp(MonitoringAppUI):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()

        # Подключение сигналов
        self.timer.timeout.connect(self.update_stats)
        self.interval_spinbox.valueChanged.connect(self.set_update_interval)
        self.start_button.clicked.connect(self.start_recording)
        self.stop_button.clicked.connect(self.stop_recording)

        # Запуск таймера
        self.timer.start(self.update_interval * 1000)

    def update_stats(self):
        cpu, ram, disk = Monitoring.get_stats()

        self.cpu_label.setText(f"ЦП: {cpu}%")
        self.ram_label.setText(f"ОЗУ: {ram.available // (1024**2)} MB свободно / {ram.total // (1024**2)} MB всего")
        self.disk_label.setText(f"ПЗУ: {disk.free // (1024**3)} GB свободно / {disk.total // (1024**3)} GB всего")

        if self.recording:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            self.db.insert_record(timestamp, cpu, ram.percent, disk.percent)
            self.timer_label.setText(f"Запись времени: {Monitoring.format_time(self.start_time)}")

    def set_update_interval(self):
        self.update_interval = self.interval_spinbox.value()
        self.timer.setInterval(self.update_interval * 1000)

    def start_recording(self):
        self.recording = True
        self.start_time = time.time()
        self.start_button.hide()
        self.stop_button.show()
        self.timer_label.show()
        self.timer_label.setText("Запись времени: 00:00:00")

    def stop_recording(self):
        self.recording = False
        self.start_button.show()
        self.stop_button.hide()
        self.timer_label.hide()

    def closeEvent(self, event):
        self.db.close()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonitoringApp()
    window.show()
    sys.exit(app.exec_())
