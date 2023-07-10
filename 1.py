import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.system("cls")
class calculate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(290,500)
        self.setMaximumSize(290,500)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("c:\\Users\\Acer\\Desktop\\Foundation\\Iphone.ico"))
        self.setStyleSheet("background-color: rgb(28,28,28)")
        self.res=""
        self.action=False
        self.temp_bt=list()
        self.son=""
        self.point=False
        self.tmp=""
        #Button 1
        bc1=self.print_button_number("1")
        bc1.setGeometry(10,360,60,60)
        #Button 2
        bc2=self.print_button_number("2")
        bc2.setGeometry(80,360,60,60)
        #Button 3
        bc3=self.print_button_number("3")
        bc3.setGeometry(150,360,60,60)
        #Button 4
        bc4=self.print_button_number("4")
        bc4.setGeometry(10,290,60,60)
        #Button 5
        bc5=self.print_button_number("5")
        bc5.setGeometry(80,290,60,60)
        #Button 6
        bc6=self.print_button_number("6")
        bc6.setGeometry(150,290,60,60)
        #Button 7
        bc7=self.print_button_number("7")
        bc7.setGeometry(10,220,60,60)
        #Button 8
        bc8=self.print_button_number("8")
        bc8.setGeometry(80,220,60,60)
        #Button 9
        bc9=self.print_button_number("9")
        bc9.setGeometry(150,220,60,60)
        #Button 0
        bc0=self.print_button_number("0")
        bc0.setGeometry(10,430,130,60)
        #Button .
        bcv=self.print_button_number(".")
        bcv.setGeometry(150,430,60,60)
        #Button ÷
        bcb=self.print_button_action("÷")
        bcb.setGeometry(220,150,60,60)
        #Button ×
        bck=self.print_button_action("×")
        bck.setGeometry(220,220,60,60)
        #Button -
        bca=self.print_button_action("-")
        bca.setGeometry(220,290,60,60)
        #Button +
        bcq=self.print_button_action("+")
        bcq.setGeometry(220,360,60,60)
        #Button =
        bct=self.print_button_action("=")
        bct.setGeometry(220,430,60,60)
        #Button AC
        self.bcc=QPushButton("AC",self)
        self.bcc.setGeometry(10,150,60,60)
        self.bcc.setStyleSheet("background-color: rgb(212,212,210);color:rgb(28,28,28);border-radius:30px")
        self.bcc.setFont(QFont("Arial",18))
        self.bcc.clicked.connect(lambda: self.calcul(bcc))
        #+/-
        bci=self.print_button("+/-")
        bci.setGeometry(80,150,60,60)
        #%
        bcf=self.print_button("%")
        bcf.setGeometry(150,150,60,60)
        #QLineEdit
        self.ld=QLineEdit(self)
        self.ld.setGeometry(10,80,270,60)
        self.ld.setStyleSheet("color: rgb(212,212,210);border-style: solid;border-color: rgb(28,28,28);")
        self.ld.setFont(QFont("Arial",18))
        self.ld.setAlignment(Qt.AlignRight)

    def print_button_number(self,n):
        if n=="0":
            bc=QPushButton(n+"        ",self)
        else:
            bc=QPushButton(n,self)
        bc.setStyleSheet("background-color: rgb(85,85,85);color: rgb(212,212,210);border-radius: 30px")
        bc.setFont(QFont("Arial",18))
        bc.clicked.connect(lambda: self.calcul(bc))
        return bc
    
    def print_button(self,n):
        bc=QPushButton(n,self)
        bc.setFont(QFont("Arial",18))
        bc.setStyleSheet("background-color: rgb(212,212,210);color:rgb(28,28,28);border-radius:30px")
        bc.clicked.connect(lambda: self.calcul(bc))
        return bc

    def print_button_action(self,n):
        bc=QPushButton(n,self)
        bc.setFont(QFont("Microsoft Sans Senif",18))
        bc.setStyleSheet("background-color: rgb(255,149,0);color: rgb(212,212,210);border-radius:30px")
        bc.clicked.connect(lambda: self.calcul(bc))
        return bc
      
    def calcul(self,bt):
        n=bt.text()
        dc={"+":"+","-":"-","×":"*","÷":"//"}
        try:
            for x in self.temp_bt:
                x.setStyleSheet("background-color: rgb(255,149,0);color: rgb(212,212,210);border-radius:30px")
            if n=="=" and self.point==False:
                s=str(eval(self.res))
                if s[-1]=="0" and s[-2]==".":
                    s=s[:-2]
                self.ld.setText(s)
                self.action=False
                self.son=""
            elif n!="AC":
                self.bcc=QPushButton("AC",self)
            elif n=="C":
                self.ld.clear()
                self.action=False
                self.res=""
                self.son=""
                self.point=False
            elif n.isdigit():
                if len(self.res)>0 and self.res[-1] in ["+","-","*","//"]:
                    self.son=""
                self.son+=n
                self.ld.setText(self.son)
                self.res+=n
                self.action=False
                self.point=False
            elif n=="." and self.point==False:
                self.res+=n
                self.son+=n
                self.ld.setText(self.son)
                self.point=True
            else:
                if self.action and self.res[-1]=="/":
                    self.res=self.res[:-2]
                elif self.action:
                    self.res=self.res[:-1]
                self.action=True
                if n in ["×","÷"]:
                    self.tmp+=self.son
                    self.ld.setText(str(eval(self.tmp)))
                    self.tmp+=dc[n]
                else:
                    self.ld.setText(str(eval(self.res)))
                    self.tmp=""
                self.res+=dc[n]
                if n!="=":
                    bt.setStyleSheet("background-color: rgb(212,212,210);color: rgb(255,149,0);border-radius:30px")
                    self.temp_bt.append(bt)
        except:
            self.ld.setText("Error")
        
app=QApplication(sys.argv)
cal=calculate()
cal.show()
sys.exit(app.exec_())