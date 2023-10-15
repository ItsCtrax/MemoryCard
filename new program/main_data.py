from PyQt5.QtCore import QAbstractListModel, QModelIndex , Qt
from random import randint, shuffle

class Question():
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True
        self.attemps = 0
        self.correct= 0

    def got_right(self):
        self.attemps += 1
        self.correct += 1

    def got_wrong(self):
        self.attemps +=1


class QuestionView():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def change(self, frm_model):
        self.frm_model = frm_model

    def show(self):
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1(self.frm_model.wrong_answer1)
        self.wrong_answer2(self.frm_model.wrong_answer2)
        self.wrong_answer3(self.frm_model.wrong_answer3)

class QuestionEdit(QuestionView):
    def save_question(self):
        self.frm_model.question = self.question.text()

    def save_answer(self):
        self.frm_model.answer = self.question.text()

    def save_wrong(self):
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()

    def set_connects(self):
        self.question.editingFinished.connect(self.save_question())
        self.answer.editingFinished.connect(self.save_answer())
        self.wrong_answer1.editingFinished.connect(self.save_wrong())
        self.wrong_answer2.editingFinished.connect(self.save_wrong())
        self.wrong_answer3.editingFinished.connect(self.save_wrong())

    def __int__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        QuestionView.__init__(self, frm_model=frm_model, question=question, answer=answer, wrong_answer1=wrong_answer1, wrong_answer2=wrong_answer2, wrong_answer3=wrong_answer3)

        self.set_connects()


text_correct = "Вірно"
text_wrong = "Невірно"


class AnswerCheck(QuestionView):
    def __int__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, showed_answer, result):
        QuestionView.__init__(self, frm_model=frm_model, question=question, answer=answer, wrong_answer1=wrong_answer1,
                              wrong_answer2=wrong_answer2, wrong_answer3=wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):
        if self.answer.isChecked():
            self.result.settext(text_correct)
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_right()
        else:
            self.result.settext(text_wrong)
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_wrong()

class QuestionListModel(QAbstractListModel):
    def __int__(self, parent=None):
        QAbstractListModel.__init__(self,parent)
        self.form_list=[]

    def rowCount(self,index):
        return len(self.form_list)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            form = self.form_list[index_row()]
            return form.question

    def insertRows(self, parent=QModelIndex()):
        position = len(self.form_list)
        self.beginInsertRows(parent,position,position)
        self.form_list.append(position)
        self.endInsertRows()
        return True

    def removeRows(self, position, parent=QModelIndex()):
        self.beginInsertRows(parent,position,position)
        self.form_list.pop(position)
        self.endRemoveRows()
        return True

    def random_question(self):
        total = len(self.form_list)
        current = randint(0 , total-1)
        return self.form_list(current)

def random_AnswerCheck(list_model, w_question, widget_list, w_showed_answer, w_result):
    frm = list_model.random_question()
    shuffle(widget_list)
    frm_card=AnswerCheck(frm,w_question,widget_list[0],widget_list[1],widget_list[2],widget_list[3],widget_list[4], w_showed_answer, w_result)
    return frm_card




