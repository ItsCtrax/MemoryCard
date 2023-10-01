from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QSpinBox, QApplication, QHBoxLayout,
                             QLineEdit, QPushButton, QLabel, QRadioButton, QButtonGroup,
                             QGroupBox, QVBoxLayout, QWidget,QApplication,QHBoxLayout,
                             QLineEdit,QPushButton,QLabel,QLineEdit)

app=QApplication([])
main_win = QWidget()
edit_layout = QVBoxLayout()

question_label = QLabel('Введіть запитання')
corect_answer_label = QLabel('Введіть правильну відповідь')
answer_1_label = QLabel('Введіть першу хибну відповідь')
answer_2_label = QLabel('Введіть другу хибну відповідь')
answer_3_label = QLabel('Введіть третю хибну відповідь')
button_1=QPushButton('Додати запитання')
button_2=QPushButton('Очистити')

question = QLineEdit()
corect_answer = QLineEdit()

answer1 = QLineEdit()
answer2 = QLineEdit()
answer3 = QLineEdit()

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()

line1.addWidget(question_label)
line1.addWidget(question)
line2.addWidget(corect_answer_label)
line2.addWidget(corect_answer)
line3.addWidget(answer_1_label)
line3.addWidget(answer1)
line4.addWidget(answer_2_label)
line4.addWidget(answer2)
line5.addWidget(answer_3_label)
line5.addWidget(answer3)
line6.addWidget(button_1)
line6.addWidget(button_2)

edit_layout.addLayout(line1)
edit_layout.addLayout(line2)
edit_layout.addLayout(line3)
edit_layout.addLayout(line4)
edit_layout.addLayout(line5)
edit_layout.addLayout(line6)

stat_title = QLabel('Статистика')
amount_atemp = QLabel('Разів відповіли')
amount_correct = QLabel('Вірних відповідей')
sucsessful = QLabel('Успішність')

stat_line = QVBoxLayout()
stat_line.addWidget(stat_title,alignment=Qt.AlignLeft)
stat_line.addWidget(amount_atemp,alignment=Qt.AlignLeft)
stat_line.addWidget(amount_correct,alignment=Qt.AlignLeft)
stat_line.addWidget(sucsessful,alignment=Qt.AlignLeft)

button_3=QPushButton('Назад')
line7 = QHBoxLayout()
line7.addWidget(button_3)

edit_layout.addLayout(stat_line)

edit_layout.addLayout(line7)

main_win.setLayout(edit_layout)
main_win.show()
app.exec_()