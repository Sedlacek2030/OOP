import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt
import folium

class MissionMap:
    def __init__(self):
        self.map = folium.Map(location=[49.7433, 15.1000], zoom_start=8)
        self.data_file = "missions.json"
        self.load_data()

    def save_map(self, filename="map.html"):
        self.map.save(filename)

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump([], file)  # Placeholder for future data storage

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                pass  # Placeholder for loading data in the future
        except FileNotFoundError:
            self.save_data()


class CommandCenterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mission Briefing System")

        self.map_handler = MissionMap()
        self.map_handler.save_map()

        # Get screen resolution and set the window size to fit the screen
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Set the window to be as large as the screen, but adjust for multiple monitors
        self.setGeometry(screen_geometry)  # Adjust to available geometry
        self.setWindowState(Qt.WindowState.WindowMaximized)  # Start maximized

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.map_view = QWebEngineView()
        self.map_view.setHtml(open("map.html").read())
        self.layout.addWidget(self.map_view)

        self.refresh_button = QPushButton("Refresh Map")
        self.refresh_button.clicked.connect(self.refresh_map)
        self.layout.addWidget(self.refresh_button)

    def refresh_map(self):
        self.map_handler.save_map()
        self.map_view.setHtml(open("map.html").read())

class POI():
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CommandCenterGUI()
    window.show()
    sys.exit(app.exec())
