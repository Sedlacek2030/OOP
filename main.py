import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget #UI
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt
import folium #mapa

class MMap:
    def __init__(self):
        self.map = folium.Map(location=[49.7433, 15.1000], zoom_start=8) #skoro střed ČR
        self.data_file = "missions.json"
        self.load_data()

    def save_map(self, filename="map.html"):
        self.map.save(filename)

    def save_data(self): #TBF
        with open(self.data_file, "w") as file:
            json.dump([], file)  # Placeholder pro ukládání

    def load_data(self): #TBF
        try:
            with open(self.data_file, "r") as file:
                pass  # Placeholder pro načítání
        except FileNotFoundError:
            self.save_data()


class CCGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MBS")

        self.map_handler = MMap()
        self.map_handler.save_map()

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

    def refresh_map(self): #useless here?
        self.map_handler.save_map()
        self.map_view.setHtml(open("map.html").read())

class POI():
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CCGUI()
    window.show()
    sys.exit(app.exec())
