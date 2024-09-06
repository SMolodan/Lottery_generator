#підключення модулів
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication , QWidget , QPushButton , QLabel , QVBoxLayout
from random import randint
app = QApplication([])
#головне вікно
my_win = QWidget()
my_win.setWindowTitle('Лотерея')
my_win.move(1100,400)
my_win.resize(400,400)

#віджети вікна: кнопка і напис
button = QPushButton("Випробувати удачу")
text = QLabel("Натисни,щоб взяти участь")
win = QLabel('?')
lose = QLabel("?")
result = QLabel('')
#розташування віджетів
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(win, alignment=Qt.AlignCenter)
line.addWidget(lose, alignment=Qt.AlignCenter)
line.addWidget(result, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
my_win.setLayout(line)
#функція яка генерує і показує число
def show_winner():
    number1 = randint(0,9)
    number2 = randint(0,9)
    win.setText(str(number1))
    lose.setText(str(number2))
    if number1 == number2:
        result.setText("Ви виграли! Зіграйте знову")
    else:
        result.setText("Ви програли! Зіграйте знову")
#обробка натискання на кнопку

button.clicked.connect(show_winner)
my_win.show()
app.exec_()

#my code(:
