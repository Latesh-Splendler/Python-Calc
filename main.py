from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont


app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")

main_window.resize(400, 450)


text_box = QLineEdit()
grid = QGridLayout()

button = ["7","8","9","/",
          "4","5","6","*",
          "1","2","3","-",
          "0",".","=","+"]

clear = QPushButton("Clear")
delete = QPushButton("Delete")
clear.setStyleSheet("QPushButton { font: 17pt Comic Sans MS; padding: 10px }")
delete.setStyleSheet("QPushButton { font: 17pt Comic Sans MS; padding: 10px }")


def button_click():
  button = app.sender()
  text = button.text()

  if text =="=":
    symbol = text_box.text()
    try:
      res = eval(symbol)
      text_box.setText(str(res))

    except Exception as e:
      print("Error:", e)

  elif text =="Clear":
    text_box.clear()

  elif text == "Delete":
    current_value = text_box.text()
    text_box.setText(current_value[:-1])

  else:
    current_value = text_box.text()
    text_box.setText(current_value + text)



row = 0
col = 0

for text in button:
  button = QPushButton(text)
  button.clicked.connect(button_click)
  button.setStyleSheet("QPushButton { font: 17pt Comic Sans MS; padding: 10px }")
  grid.addWidget(button, row, col)
  col += 1

  if col > 3:
    col = 0
    row += 1


#design
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)



button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)
master_layout.setContentsMargins(22,22,22,22)


master_layout.addLayout(button_row)
main_window.setLayout(master_layout)

clear.clicked.connect(button_click)
delete.clicked.connect(button_click)

main_window.setStyleSheet("QWidget {background-color: #f0f772; }")
main_window.show()
app.exec_()