from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QSpinBox, QHBoxLayout, QFrame
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont


class MonitoringAppUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.update_interval = 1  # Интервал обновления в секундах
        self.recording = False
        self.start_time = None

        self.timer = QTimer()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Загруженность компьютера")
        self.setGeometry(300, 200, 400, 300)
        self.setStyleSheet("background-color: #f5f5f5;")

        self.cpu_label = QLabel("ЦП: 0%")
        self.ram_label = QLabel("ОЗУ: 0 MB свободно / 0 MB всего")
        self.disk_label = QLabel("ПЗУ: 0 GB свободно / 0 GB всего")

        for label in (self.cpu_label, self.ram_label, self.disk_label):
            label.setFont(QFont("Arial", 14))
            label.setStyleSheet("color: #333;")

        self.interval_label = QLabel("Время обновления (сек.):")
        self.interval_label.setFont(QFont("Arial", 12))
        self.interval_label.setStyleSheet("color: #555;")

        self.interval_spinbox = QSpinBox()
        self.interval_spinbox.setValue(1)
        self.interval_spinbox.setRange(1, 60)
        self.interval_spinbox.setStyleSheet(
            "background-color: #fff; border: 1px solid #ccc; border-radius: 5px; padding: 2px;"
        )

        self.start_button = QPushButton("Начать запись")
        self.start_button.setStyleSheet(
            "background-color: #28a745; color: white; font-size: 14px; border-radius: 5px; padding: 5px;"
        )

        self.stop_button = QPushButton("Остановить")
        self.stop_button.setStyleSheet(
            "background-color: #dc3545; color: white; font-size: 14px; border-radius: 5px; padding: 5px;"
        )
        self.stop_button.hide()

        self.timer_label = QLabel("Запись времени: 00:00:00")
        self.timer_label.setFont(QFont("Arial", 12))
        self.timer_label.setStyleSheet("color: #333;")
        self.timer_label.hide()

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #ccc;")

        layout = QVBoxLayout()
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.disk_label)
        layout.addWidget(separator)
        layout.addWidget(self.interval_label)

        interval_layout = QHBoxLayout()
        interval_layout.addWidget(self.interval_spinbox)
        layout.addLayout(interval_layout)

        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.timer_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
