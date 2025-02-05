import sys
import random
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QComboBox,
    QHBoxLayout,  # Added for button layout
)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
import gc

class LivePlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, plot_type="line", dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

        self.x_data = []
        self.y_data = []
        self.plot_type = plot_type  # Default to line plot

        self.line, = self.axes.plot([], [], 'r-')
        self.scatter = self.axes.scatter([], [])  # For scatter plot
        self.ani = None

    def update_plot(self, data):
        self.x_data.append(len(self.x_data))
        self.y_data.append(data)

        if self.plot_type == 'line':
            self.line.set_data(self.x_data, self.y_data)
            self.axes.set_xlim(0, len(self.x_data))
            self.axes.set_ylim(-15, 15)
        elif self.plot_type == 'scatter':
            self.scatter.remove()  # Remove the old scatter plot
            self.scatter = self.axes.scatter(self.x_data, self.y_data, c='b')
            self.axes.set_xlim(0, len(self.x_data))
            self.axes.set_ylim(-15, 15)
        self.draw()  # Explicitly call draw to update the plot


    def stop_animation(self):
        if self.ani:
            self.ani.event_source.stop()  # Stop the animation
            self.ani = None  # Dereference to allow garbage collection



class Live(QMainWindow):
    def __init__(self, plot_type,live):
        super().__init__()
        self.setWindowTitle("Live Plotting with Matplotlib")
        self.setWindowFlags(Qt.Window)  # Make the window closable

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.live = live
        self.is_active = False
        

        # Layout
        layout = QVBoxLayout(self.central_widget)

        # Plot Canvas
        width = 5
        height = 4
        self.plot_canvas = LivePlotCanvas(self, width, height, plot_type)
        layout.addWidget(self.plot_canvas)

        # Close button and signal connection
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.closeEvent)  # Connect to close function
        layout.addWidget(self.close_button, alignment=Qt.AlignRight)  # Align right

    def show(self):
        super().show()
        self.is_active = True

    def closeEvent(self, event):  # Override close event for proper handling
        self.live = 0  # Set live to 0 when window closes
        self.is_active = False
        self.plot_canvas.stop_animation()  # Stop the animation
        self.plot_canvas = None  # Dereference the canvas to allow garbage collection
        self.central_widget = None 
        gc.collect()
        event.accept()




