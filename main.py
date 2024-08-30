import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout,QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QColor, QMouseEvent
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        screen_size = QApplication.screens()[0].size()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(int(screen_size.width()/2), int(screen_size.height()/2), 350, 150)
        self.bg_widget = QWidget(self)
        self.palette = QPalette()
        self.palette.setColor(QPalette.Background, QColor(0, 255, 0))  
        self.bg_widget.setPalette(self.palette)
        self.bg_widget.setAutoFillBackground(True)
        self.setCentralWidget(self.bg_widget)
        
        self.h_layout = QHBoxLayout()
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.bg_widget.setLayout(self.h_layout)

        self.color_input = QLineEdit()
        self.color_input.textChanged.connect(self.change_color)
        self.color_input.setPlaceholderText("r g b ")

        self.size_input = QLineEdit()
        self.size_input.textChanged.connect(self.change_size)
        self.size_input.setPlaceholderText("w h")

        self.confirm_button = QPushButton('ok')
        self.confirm_button.clicked.connect(self.hide_all)
     
        self.color_label = QLabel("color:")
        self.size_label = QLabel("size:")

        self.h_layout.addWidget(self.color_label)
        self.h_layout.addWidget(self.color_input)
        self.h_layout.addWidget(self.size_label)
        self.h_layout.addWidget(self.size_input)
        self.h_layout.addWidget(self.confirm_button)

    def change_color(self, event):
        color_str = self.color_input.text()
        if self.valid_color(color_str):
            colors = color_str.split(' ')
            r = int(colors[0])
            g = int(colors[1])
            b = int(colors[2])
            self.palette.setColor(QPalette.Background, QColor(r, g, b))
            self.bg_widget.setPalette(self.palette)
    
    def change_size(self, event):
        size_str = self.size_input.text()
        if self.valid_size(size_str):
            sizes = size_str.split(' ')
            w = int(sizes[0])
            h = int(sizes[1])
            self.resize(w, h)
    
    def hide_all(self):
        self.color_input.setVisible(False)
        self.size_input.setVisible(False)
        self.confirm_button.setVisible(False)
        self.color_label.setVisible(False)
        self.size_label.setVisible(False)
        size_str = self.size_input.text()
        if self.valid_size(size_str):
            sizes = size_str.split(' ')
            w = int(sizes[0])
            h = int(sizes[1])
            self.resize(w, h)
        
    
    def valid_color(self, color_str):
        colors = color_str.split(' ')
        if len(colors) != 3:
            return False
        for c in colors:
            if not c.isdigit():
                return False
            if int(c) > 255 or 0 > int(c):
                return False
        return True
            
    
    def valid_size(self, size_str):
        sizes = size_str.split(' ')
        if len(sizes) != 2:
            return False
        for s in sizes:
            if not s.isdigit() or 0 > int(s):
                return False
        return True

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.close()
        
def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
