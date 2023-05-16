#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
window = QWidget([])
window.setWindowTitle('Memory Card')
btn_OK = QPushButton('Ответить')
ld_Question = QLAbel('Какой национальности не существует?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadionButton('Энцы')
rbtn_2 = QRadionButton('Смурф')
rbtn_3 = QRadionButton('Чулымцы')
rbtn_4 = QRadionButton('Алеуты')
layout_ans1 = QHBoxLayout
layout_ans2 = QVBoxLayout
layout_ans3 = QVBoxLayout

layout_ans2.addWidgets(rbtn_1)
layout_ans2.addWidgets(rbtn_2)
layout_ans3.addWidgets(rbtn_3)
layout_ans3.addWidgets(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidgets(lb_Question, alignment = (Qt.AlignHCentre | Qt.AlignHCentre))

layout_line3.addStretch(1)
layout_line3.addWidgets(btn_OK, strech = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.setSpacing(5)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_card = QVBoxLayout()
layout_card.setSpacing(5)

layout_card.addLayout(layout_line1, strech = 2)
layout_card.addLayout(layout_line2, strech = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, strech = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window.setLayout(layout_card)
window.show()
app.exec()


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    ld_Question.setText(question)
    ld_Correct.setText(right_answer)
    show_question()

def show_correct(res):
    ld_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def test():
    if 'ответить' == btn_OK():
        show_result()
    else:
        'Следущий вопрос'
        show_question()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

cur_question = randint(0, len(question_list) - 1)
q = question_list[cur_question]

def next_qestion():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list(window.cur_question)
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_qestion

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
ask('Государственный язык Бразилии', 'Португальсикй', 'Бразильсикй', 'Испанский', 'Итальянский')
btn_OK.clicked.coonect(check_answer)
window.cur_question -= 1
btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_qestion()
window.resize(400, 300)
window.show()
app.exec()