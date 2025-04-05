#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QGroupBox, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
from random import randint, shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

#создание окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,200)



#кнопки-переключатели и вопрос
vopros = QLabel('Какой национальности не существует?')
answer1 = QRadioButton('Энцы')
answer2= QRadioButton('Смурфы')
answer3= QRadioButton('Чулымцы')
answer4= QRadioButton('Алеуты')

MainGroup = QGroupBox('Варианты ответов') #коробка с ответами

main_HLine1 = QHBoxLayout()
#лейауты коробки
HGroupLine1 = QHBoxLayout()
VGroupLine1 = QVBoxLayout()
VGroupLine2 = QVBoxLayout()
#добавление кнопок-переключателей к коробке
VGroupLine1.addWidget(answer1, alignment = Qt.AlignVCenter)
VGroupLine1.addWidget(answer2, alignment = Qt.AlignVCenter)
VGroupLine2.addWidget(answer3, alignment = Qt.AlignVCenter)
VGroupLine2.addWidget(answer4, alignment = Qt.AlignVCenter)
HGroupLine1.addLayout(VGroupLine1)
HGroupLine1.addLayout(VGroupLine2)

MainGroup.setLayout(HGroupLine1)
#распределение всего я хз как назвать
main_HLine2 = QHBoxLayout()
main_HLine2.addStretch(3)
main_HLine1.addWidget(vopros, alignment = Qt.AlignCenter)
main_VLine1 = QVBoxLayout()
main_VLine1.addLayout(main_HLine1)
main_VLine1.addWidget(MainGroup, alignment= Qt.AlignCenter)

#коробка правильно/неправильно
AccuracyCheckBox = QGroupBox('Результат теста')
Accuracy = QLabel('Правильно/Неправильно')
Otvet = QLabel('Правильный ответ')
VLineAccuracy = QVBoxLayout()
HLineAccuracy = QHBoxLayout()
VLineAccuracy.addWidget(Accuracy)
VLineAccuracy.addStretch(1)
HLineAccuracy.addLayout(VLineAccuracy)
HLineAccuracy.addWidget(Otvet)
AccuracyCheckBox.setLayout(HLineAccuracy)

AccuracyCheckBox.hide()

main_VLine1.addWidget(AccuracyCheckBox, alignment = Qt.AlignCenter) #добавление коробки

main_VLine1.addLayout(main_HLine2)

confirm = QPushButton('Ответить')
main_HLine2.addWidget(confirm, stretch=5)
main_HLine2.addStretch(3)

main_win.setLayout(main_VLine1)

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

main_win.score = 0
main_win.total = 0




#спрятать коробку с ответами показать коробку с результатом
def show_result():
    MainGroup.hide()
    AccuracyCheckBox.show()
    confirm.setText('Следующий вопрос')
#спрятать коробку с результатом показать коробку с ответами
def show_question():
    AccuracyCheckBox.hide()
    MainGroup.show()
    confirm.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)
#тык тык кнопка ыыыыы




answers = [answer1, answer2, answer3, answer4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    vopros.setText(q.question)
    Otvet.setText(q.right_answer)
    show_question()



def show_correct(res):
    Accuracy.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
    print('правильных:', main_win.score)
    scor = main_win.score/main_win.total*100
    print('всего рейтинг:', scor)
main_win.cur = []
main_win.cur2 = 0
'''
def start_test():
    if 'Ответить' == confirm.text():
        check_answer()
    else:
        show_question()
'''

def next_q():
    rand = randint(0,len(Question_list)-1)
    if1 = rand in main_win.cur
    if2 = rand not in main_win.cur
    if main_win.cur2 < len(Question_list):
        if if2:
            main_win.total += 1
            print('всего вопросов задано', main_win.total)
            main_win.cur.append(rand)
            ask(Question_list[rand])
            main_win.cur2+=1
        else:
            next_q()
    else:
        Accuracy.setText('конец теста')
        Otvet.setText('ваш результат: '+str(main_win.score/main_win.total*100))
        confirm.hide()

def click_ok():
    if 'Ответить' == confirm.text():
        check_answer()
    else:
        next_q()
        

Question_list = []
Question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
Question_list.append(Question('e^{i\pi }= ???', '1', "-1", "0", "3,14"))
Question_list.append(Question('1 + 1', '10', "1101", "1010", "2"))
Question_list.append(Question('АБВГ...', "Д", "E", "D", "W"))
next_q()

confirm.clicked.connect(click_ok)





main_win.show()
app.exec_()