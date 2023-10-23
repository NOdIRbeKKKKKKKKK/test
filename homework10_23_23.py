from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QLabel
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QRadioButton

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.h_main_lay=QHBoxLayout()
        self.setGeometry(200, 200, 500, 300)
        self.subject()
    def subject(self):
        self.yozuv=QLabel("belgilang",self)
        self.yozuv.move(10,50)
        self.setStyleSheet("font-size:25px")        
        self.btn1=QPushButton()
        self.btn1.setText("Tarix")
        self.btn2=QPushButton()
        self.btn2.setText("Ingliz tili")

        self.h_main_lay.addWidget(self.btn1)
        self.h_main_lay.addWidget(self.btn2)

        self.setLayout(self.h_main_lay)

        self.btn1.clicked.connect(self.tarix)
        self.btn2.clicked.connect(self.English)
    def tarix(self):
            self.yozuv.hide()
            self.btn1.hide()
            self.btn2.hide()

            self.question=QLabel(f"""1-savol\n1868-yilda tashkil etilgan Turkiston viloyati qaysi hudud tarkibiga kiritilgan edi?""",self)

            self.question.setGeometry(1,1,1000,50)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("A Turkiston general-gubernatorligi",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,30,1000,50)
            self.v1.show()

            self.v2=QRadioButton("B Sirdaryo viloyati",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,50,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("D Rossiya imperiyasi",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,70,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("C Orenburg general-gumenatorligi",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,90,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi)
            self.count=QLabel('',self)
            self.count.move(30,230)
            self.count.setStyleSheet("font-size:20px")

    def keyingi(self):
            if self.v4.isChecked():
              self.count.setText("1 True")    
              self.count.show() 
            else:
               self.count.setText("1 False") 
               self.count.show() 
            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""2-savol\n1922-yilda SSSR tarkibiga kirgan davlatlar:
                                  1)Rossiya; 2)O'zbekiston;3)Ukraina;
                                  4)Moladviya;5)Kavkazorti;6)Litva;7)Belorussiya""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("1,3,5,7",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("2,4,5,6",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("1,2,4,7",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("1,3,4,6",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi1)
    def keyingi1(self):
            if self.v1.isChecked():
                self.count.setText("2 True")  
                self.count.show()
            else:
                   self.count.setText("2 False")   
                   self.count.show()

            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""3-savol\nTurkiston Qaysi o'lkasida istiqlolchilik harakati avj olgan?""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("Xorazm viloyat",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("Farg'ona viloyati",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("Jizzax viloyati",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("Samarqand viloati",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi2)
    def keyingi2(self):
            if self.v2.isChecked():
              self.count.setText("3 True")
              self.count.show()

            else:
                  self.count.setText("3 False") 
                  self.count.show()

            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""4-savol\nO'zbekiston ikkinchi Jahon urushi qachon tugagan""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("1935",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("1940",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("1945",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("1955",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi3)
    def keyingi3(self):
            if self.v1.isChecked():
                self.count.setText("4 True")
                self.count.show()

            else:
                    self.count.setText("4 False")
                    self.count.show()
            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""5-savol\nGermaniyada Veymer Respublikasi boshqaruvi tugatilgan yilni belgilang""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("1939-yil",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("1923-yil",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("1934-yil",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("1945-yil",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Finish")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.natija)
    def natija(self):  
            if self.v2.isChecked():
                self.count.setText("5 True")  
                self.count.show()
            else:
                   self.count.setText("5 False")    
    def English(self):
            self.yozuv.hide()
            self.btn1.hide()
            self.btn2.hide()

            self.question=QLabel(f"""Question1. Hello what ... your name?""",self)

            self.question.setGeometry(1,1,1000,50)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("A) is",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,30,1000,50)
            self.v1.show()

            self.v2=QRadioButton("B) are",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,50,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("D) am",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,70,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("C) be",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,90,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi)
            self.count=QLabel('',self)
            self.count.move(30,230)
            self.count.setStyleSheet("font-size:20px")

    def keyingi(self):
            if self.v1.isChecked():
              self.count.setText("1 True")    
              self.count.show() 
            else:
               self.count.setText("1 False") 
               self.count.show() 
            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""Question 2 ______ name is John. And my ______ is Johnson""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton('A) Your / surname',self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("B) My / surname",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("C) I / surname",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("D) I / name",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi1)
    def keyingi1(self):
            if self.v2.isChecked():
                self.count.setText("2 True")  
                self.count.show()
            else:
                   self.count.setText("2 False")   
                   self.count.show()

            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""Question3. My name is Lisa. ______ Lisa Peterson.""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("A) My am",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("B) I is",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("C) I am",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("D) I",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi2)
    def keyingi2(self):
            if self.v3.isChecked():
              self.count.setText("3 True")
              self.count.show()

            else:
                  self.count.setText("3 False") 
                  self.count.show()

            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""Question4. ______ from Spain. I'm Rodriguez .""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("A) I'm",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("B) He's",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("C) You're",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("D) She's",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Next")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.keyingi3)
    def keyingi3(self):
            if self.v1.isChecked():
                self.count.setText("4 True")
                self.count.show()
            else:
                    self.count.setText("4 False")
                    self.count.show()
            self.question.hide()
            self.v1.hide()
            self.v2.hide()
            self.v3.hide()
            self.v4.hide()
            self.btn_next.hide()
            self.question=QLabel(f"""Question5. Pierre is a French boy. ______ from ______ .""",self)
            self.question.setGeometry(0,0,1000,80)
            self.question.setStyleSheet("font-size: 15px")
            self.question.show()
            self.v1=QRadioButton("A) He's / France",self)
            self.v1.setStyleSheet("font-size: 13px")
            self.v1.setGeometry(10,40,1000,50)
            self.question.show()
            self.v1.show()

            self.v2=QRadioButton("B) His's / French",self)
            self.v2.setStyleSheet("font-size: 13px")
            self.v2.setGeometry(10,60,1000,50)
            self.v2.show()

            
            self.v3=QRadioButton("C) His / France",self)
            self.v3.setStyleSheet("font-size: 13px")
            self.v3.setGeometry(10,80,1000,50)
            self.v3.show()

            
            self.v4=QRadioButton("D) He / France",self)
            self.v4.setStyleSheet("font-size: 13px")
            self.v4.setGeometry(10,100,1000,50)
            self.v4.show()

            self.btn_next=QPushButton("Finish")
            self.h_main_lay.addWidget(self.btn_next)
            self.setLayout(self.h_main_lay)
            self.btn_next.clicked.connect(self.natija)
    def natija(self):  
            if self.v1.isChecked():
                self.count.setText("5 True")  
                self.count.show()
            else:
                   self.count.setText("5 False")           


app=QApplication([])
win=Win()
win.show()
app.exec_()