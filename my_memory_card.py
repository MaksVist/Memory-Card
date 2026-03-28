from PyQt5.QtCore import Qt
from random import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_results():# Отображение формы с ответом
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button.setText('Следующий вопрос')

def show_questions():# Отображение формы вопроса
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        show_results()
    else:
        show_questions()

def ask(q: Question):#Функция для задания вопроса
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)
    text3.setText(q.right_answer)
    show_questions()

def check_answer():# Проверка ответа
    if answers[0].isChecked():
        text2.setText('Правильно')
        show_results()
        app_content.score += 1
    else:
        text2.setText('Неправильно')
        show_results()
    print_information()


def next_question():#Функция для вызова следующего вопроса
    app_content.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    question = questions_list[cur_question]
    ask(question)

def click_OK():#Обработчик клика по кнопке
    if button.text() == 'Ответить':
        check_answer()
    elif button.text() == 'Следующий вопрос':
        next_question()

def print_information():# Создание нового окна и печать на нём информации
    victory_winner = QMessageBox()
    victory_winner.setWindowTitle('Результат теста')
    victory_winner.setText(f'Статистика\n Всего вопросов: {app_content.total}\n Правильных ответов: {app_content.score}\n Рейтинг {round((app_content.score / app_content.total) * 100, 2)}')
    victory_winner.exec_()





app = QApplication([])# обьект приложение (ОБЪЯВЛЯТЬ ОБЯЗАТЕЛЬНО!!!)
app_content = QWidget()#окно приложения
app_content.total = 0
app_content.score = 0
app_content.setWindowTitle('Конкурс от Crazy People')#заголовок окна

app_content.move(900, 70)# точка появления виджета
app_content.resize(1000, 500)# размер окна приложения
text = QLabel('Какой национальности не существует?')
answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Чулымцы')
answer3 = QRadioButton('Смурфы')
answer4 = QRadioButton('Алеуты')
answers = [answer1, answer2, answer3, answer4]
button = QPushButton('Ответить')
vertical_line1 = QVBoxLayout()# по вертикали, размещена на горизонтале (horisontal_line1), размещение кнопок QRadioButton
vertical_line2 = QVBoxLayout()# по вертикале, размещена на горизонтале (horisontal_line!), размещение кнопок QRadioButton
vertical_line3 = QVBoxLayout()# главная вертикаль размещённая на окне, на ней будут находиться horizontal_line2, horizontal_line3, horizontal_line4
horizontal_line1 = QHBoxLayout()# по горизонтали, размещена на центральном виджете
horizontal_line2 = QHBoxLayout()# по горизонтали, на ней расположен вопрос "Какой национальности не существует?"
horizontal_line3 = QHBoxLayout()# по горизонтали, она расположена на группе "Варианты ответов"
horizontal_line4 = QHBoxLayout()# по горизонтали, на ней расположена кнопка "Ответить"
vertical_line1.addWidget(answer1, alignment = Qt.AlignCenter)
vertical_line1.addWidget(answer2, alignment = Qt.AlignCenter)
vertical_line2.addWidget(answer3, alignment = Qt.AlignCenter)
vertical_line2.addWidget(answer4, alignment = Qt.AlignCenter)
horizontal_line2.addWidget(text, alignment = Qt.AlignCenter)
horizontal_line1.addLayout(vertical_line1)
horizontal_line1.addLayout(vertical_line2)
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroupBox.setLayout(horizontal_line1)
#RadioGroupBox.hide()
AnswerGroupBox = QGroupBox('Результат теста')
text2 = QLabel('Правильно/Неправильно')#Информация о правильности ответа
text3 = QLabel('Правильный ответ')# Правильный ответ
vertical_line5 = QVBoxLayout()
vertical_line5.addWidget(text2)
vertical_line5.addWidget(text3, alignment = Qt.AlignCenter)
AnswerGroupBox.setLayout(vertical_line5)
horizontal_line3.addWidget(RadioGroupBox)
horizontal_line3.addWidget(AnswerGroupBox)
horizontal_line4.addWidget(button, alignment = Qt.AlignCenter)
vertical_line3.addLayout(horizontal_line2)
vertical_line3.addLayout(horizontal_line3)
vertical_line3.addLayout(horizontal_line4)
app_content.setLayout(vertical_line3)
AnswerGroupBox.hide()
button.clicked.connect(click_OK)# подписка на клик по кнопке
RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)
questions_list = []
questions_list.append(Question('Какое государство является наименьшим?', 'Ватикан', 'Микронезия', 'Беларусь', 'Испания'))
questions_list.append(Question('Самая протяжённая улица города Белгорода?', 'Проспект Богдана Хмельницкого', 'Попова', 'Октябрьская', 'Щорса'))
questions_list.append(Question('Дата основания города Белгорода?', '1596', '1625', '1256', '1693'))
questions_list.append(Question('Самый высокий водопад в мире?', 'Анхель', 'Виннуфосен', 'Зейгалан', 'Учар'))
questions_list.append(Question('Самый крупный в мире ледник?', 'ледник Ламберта', 'ледник Беринга', 'ледник Перито-Морено', 'ледник Джунё'))
questions_list.append(Question('Какая команда в Python используется для вывода текста на экран?', 'print', 'input', 'output', 'shift'))
questions_list.append(Question('Какая команда в Python используется для ввода информации пользователем с клавиатуры?', 'input', 'if', 'if', 'else'))
questions_list.append(Question('Самая большая в мире река?', 'Амазонка', 'Лена', 'Миссипи', 'Нил'))
questions_list.append(Question('Самое большое озеро по площади на планете Земля?', 'Каспийское', 'Титикака', 'Женевское', 'Виктория'))
next_question()





app_content.show()# отбражение окна (виджета)
app.exec_()# оставляет приложение открытым пока не произойдёт какое-либо событие которое позволяет закрыть окно или пока не будет нажата кнопка выхода из приложения'''

'''from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

def show_winner():
    victory_winner = QMessageBox()
    victory_winner.setText('Вы выиграли встречу с создателями канала!')
    victory_winner.exec_()

def show_loser():
    victory_winner = QMessageBox()
    victory_winner.setText('Повезёт в другой раз!')
    victory_winner.exec_()

app = QApplication([])# обьект приложение (ОБЪЯВЛЯТЬ ОБЯЗАТЕЛЬНО!!!)
app_content = QWidget()#окно приложения
app_content.setWindowTitle('Конкурс от Crazy People')#заголовок окна
app_content.move(900, 70)# точка появления виджета
app_content.resize(1000, 500)# размер окна приложения
text = QLabel('Как звали первого юютуб-блогера, набравшего 100000000 подписчиков?')#виджет надпись
answer_1 = QRadioButton('PewDiePie')
answer_2 = QRadioButton('Рэт и Линк')
answer_3 = QRadioButton('SlivkiShow')
answer_4 = QRadioButton('TheBrianMaps')#кнопка переключатель
answer_5 = QRadioButton('Mister Max')
answer_6 = QRadioButton('EeOneGuy')
v_line = QVBoxLayout()#по вертикали
h_line_1 = QHBoxLayout()#по горизонтали
h_line_2 = QHBoxLayout()#по горизонтали
h_line_3 = QHBoxLayout()#по горизонтали
h_line_4 = QHBoxLayout()#по горизонтали
h_line_1.addWidget(text, alignment = Qt.AlignCenter)#добавление виджета на макет (на направляющую линию)
h_line_2.addWidget(answer_1, alignment = Qt.AlignCenter)
h_line_2.addWidget(answer_2, alignment = Qt.AlignCenter)
h_line_3.addWidget(answer_3, alignment = Qt.AlignCenter)
h_line_3.addWidget(answer_4, alignment = Qt.AlignCenter)
h_line_4.addWidget(answer_5, alignment = Qt.AlignCenter)
h_line_4.addWidget(answer_6, alignment = Qt.AlignCenter)
v_line.addLayout(h_line_1)#добавление на один направляющий макет и на другой макет
v_line.addLayout(h_line_2)
v_line.addLayout(h_line_3)
v_line.addLayout(h_line_4)
app_content.setLayout(v_line)#разместить нааправляющий макет на окне или на другом виджете
answer_1.clicked.connect(show_winner)
answer_2.clicked.connect(show_loser)
answer_3.clicked.connect(show_loser)
answer_4.clicked.connect(show_loser)
answer_5.clicked.connect(show_loser)
answer_6.clicked.connect(show_loser)

app_content.show()# отбражение окна (виджета)
app.exec_()# оставляет приложение открытым пока не произойдёт какое-либо событие которое позволяет закрыть окно или пока не будет нажата кнопка выхода из приложения'''