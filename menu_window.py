from PyQt5.QtCore import Qt
<<<<<<< HEAD
from PyQt5.QtWidgets import (QWidget,QSpinBox, QApplication, QHBoxLayout,
                             QLineEdit, QPushButton, QLabel, QRadioButton, QButtonGroup,
                             QGroupBox, QVBoxLayout)


app=QApplication([])
=======
from PyQt5.QtWidgets import (QWidget,QApplication,QHBoxLayout,
                             QLineEdit,QPushButton,QLabel)


>>>>>>> origin/main
main_win=QWidget()
main_win.setWindowTitle('Тестування')
main_win.resize(400,400)

qtext=QLabel('День незалежонсті україни')
v_line=QVBoxLayout()
<<<<<<< HEAD
rbtn_1=QRadioButton('caterpillar')
rbtn_2=QRadioButton('application')
rbtn_3=QRadioButton('apple')
rbtn_4=QRadioButton('building')

RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup=QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

btn_Menu=QPushButton('Меню')
btn_Sleep=QPushButton("Відпочити")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
btn_Ok=QPushButton('Відповісти')

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_line4=QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)

layout_line2.addWidget(qtext,alignment=Qt.AlignHCenter | Qt.AlignVCenter)
layout_line3.addWidget(RadioGroupBox)
layout_line4.addWidget(btn_Ok,alignment=Qt.AlignCenter)

layout_card=QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
layout_card.addLayout(layout_line4)

main_win.setLayout(layout_card)
=======
v1=QRadioButton('1991')
v2=QRadioButton('1989')
v3=QRadioButton('1999')
v4=QRadioButton('1941')

layout1=QHBoxLayout()
layout2=QHBoxLayout()
layout3=QHBoxLayout()

layout1.addWidget(qtext, alignment=Qt.AlignCenter)
layout2.addWidget(v1, alignment=Qt.AlignCenter)
layout2.addWidget(v2, alignment=Qt.AlignCenter)
layout3.addWidget(v3, alignment=Qt.AlignCenter)
layout3.addWidget(v4, alignment=Qt.AlignCenter)
v_line.addLayout(layout1)
v_line.addLayout(layout2)
v_line.addLayout(layout3)

main_win.setLayout(v_line)
>>>>>>> origin/main

main_win.show()
app.exec_()
