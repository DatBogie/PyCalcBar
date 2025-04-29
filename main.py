import sys, os, pyclip
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLineEdit, QLabel
from PyQt6.QtCore import Qt
import math, random

WSTYLE = "Fusion"
STYLESHEET = """WIDGETS=Fusion
QWidget {
    background: transparent;
    border: none;
    color: white;
}
QLineEdit {
    background-color: rgba(36, 39, 58,.5);
    border: 2px solid rgb(183, 189, 248);
    border-radius: 5px;
}
"""

VALID_OUTPUT_TYPES = ["int","float","str","list","dict"]
for i,t in enumerate(VALID_OUTPUT_TYPES):
    VALID_OUTPUT_TYPES[i] = f"<class '{t}'>"

def invalid():
    print("No matching pattern of options found: " + " ".join(sys.argv[1:]) + "\nUse pycalcbar --help for more information.")
    sys.exit(-1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 50)
        self.setWindowTitle("PyCalcBar")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        layout = QHBoxLayout()
        
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter expression here")
        self.input.textEdited.connect(self.input_changed)
        
        self.output = QLineEdit()
        self.output.setPlaceholderText("Result")
        self.output.setReadOnly(True)

        layout.addWidget(self.input)
        layout.addWidget(QLabel("="))
        layout.addWidget(self.output)

        central = QWidget()
        central.setLayout(layout)

        self.setCentralWidget(central)
    def setup(self):
        self.setGeometry(self.x(),50,self.width(),self.height())
    def input_changed(self):
        try:
            result = eval(self.input.text())
            if not str(type(result)) in VALID_OUTPUT_TYPES: return
            self.output.setText(str(result))
        except Exception as e:pass
    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_Escape:
            self.close()
        elif a0.key() == Qt.Key.Key_Return or a0.key() == Qt.Key.Key_Enter:
            pyclip.copy(self.output.text())
        super().keyPressEvent(a0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        _1 = sys.argv[1]
        if _1 == "--help" or _1 == "-h":
            print("""
PyCalcBar - A simple popup calculator bar written in Python.
Usage:
    pycalcbar [option]
Options:
    --help,     -h               Show this help message
    --style,    -s <path>        Load a custom stylesheet from the specified css file
    --calc,     -c <expression>  Print the result of the given expression
    --defstyle, -d               Print the default stylesheet
Guide:
    Type a math expression into the input (left) box.
    As you type, the last valid result will be displayed in the output (right) box.
    Press Return/Enter to copy the result (Linux : requires wl-clipboard/xclip).
    Press Escape to close.

""")
            sys.exit(0)
        elif _1 == "--defstyle" or _1 == "-d":
            print(STYLESHEET)
            sys.exit(0)
        if len(sys.argv) < 3:
            invalid()
        _2 = sys.argv[2]
        if _1.startswith("--style") or _1.startswith("-s"):
            try:
                path = os.path.expanduser(_2.strip())
                if os.path.exists(path):
                    with open(path, "r") as f:
                        STYLESHEET = f.read()
                        print(f"Loaded stylesheet from {path}")
                else:
                    print(f"File {path} not found.")
            except Exception as e:
                print(f"Error loading stylesheet: {e}")
        elif _1.startswith("--calc") or _1.startswith("-c"):
            expression = _2.strip()
            try:
                print(eval(expression))
            except Exception as e:
                print(f"Error: {e}")
            sys.exit(-1)
        else:
            invalid()
                
    
    app = QApplication(sys.argv)
    if STYLESHEET.startswith("WIDGETS="):
        WSTYLE = STYLESHEET[STYLESHEET.find("=")+1:STYLESHEET.find("\n")]
        STYLESHEET = STYLESHEET[STYLESHEET.find("\n")+1:]
    app.setStyle("Fusion")
    app.setStyleSheet(STYLESHEET)
    window = MainWindow()
    window.show()
    window.setup()
    sys.exit(app.exec())