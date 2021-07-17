from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
QuestionsList = []
q1 = Question("Who was revealed to be the 8th dlc character for Smash Ultimate?", "Sephiroth", "Crash", "Geno", "Dante")
QuestionsList.append(q1)
q2 = Question("What is the most annoying part of sephiroth's moveset?", "Shadow Flare", "up air", "flare/megaflare/gigaflare", "Octaslash")
QuestionsList.append(q2)
q3 = Question("How much damage does K rool armour tank before breaking?", "36%", "28%", "14.4%", "36.02%")
QuestionsList.append(q3)


def showresult():
    RGB.hide()
    RGB2.show()
    btn.setText("Next")

def showquestion():
    RGB.show()
    RGB2.hide()
    btn.setText("Answer")
    BG.setExclusive(False)
    btn_answer.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    BG.setExclusive(True)

def test():
    if btn.text() == "Answer":
        showresult()
    else:
        showquestion()

app = QApplication([])
window = QWidget()
window.setWindowTitle("meh")
window.resize(420,420)
i = QLabel(".")
btn = QPushButton("You picked yet?")
RGB = QGroupBox("Pick one")
btn_answer = QRadioButton(".")
btn_answer2 = QRadioButton(".")
btn_answer3 = QRadioButton(".")
btn_answer4 = QRadioButton(".")
BG = QButtonGroup()
BG.addButton(btn_answer)
BG.addButton(btn_answer2)
BG.addButton(btn_answer3)
BG.addButton(btn_answer4)

layout_ans = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_answer)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
layout_ans.addLayout(layout_ans2)
layout_ans.addLayout(layout_ans3)



RGB.setLayout(layout_ans)
layout_main = QVBoxLayout()



layout_main.addWidget(i)
layout_main.addWidget(RGB)

RGB2 = QGroupBox(".")
A = QLabel(".")
B = QLabel(".")
v1 = QVBoxLayout()
v1.addWidget(A)
v1.addWidget(B)
RGB2.setLayout(v1)
layout_main.addWidget(RGB2)

layout_main.addWidget(btn)
window.setLayout(layout_main)

answers = [btn_answer,btn_answer2,btn_answer3,btn_answer4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    i.setText(q.question)
    B.setText(q.right_ans)
    showquestion()

def check_answer():
    if answer[0].isChecked():
        A.setText("U right")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            A.setText("Ha, nope")

q = 'E'

window.cur_question = -1
def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(QuestionsList):
        window.cur_question = 0
    q=QuestionsList[window.cur_question]
    ask(q)

def click_OK():
    if btn.text == 'answer':
        check_answer()
    else:
        next_question()




btn.clicked.connect(click_OK)
next_question()
window.show()
app.exec_()