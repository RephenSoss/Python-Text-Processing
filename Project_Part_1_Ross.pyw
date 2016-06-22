# Stephen Ross
# Python Programming for Database Apps
# Project Part 1

# I worked with and got help from Keegan Shirel over 
# over the course of the semester. 

# Import Libraries

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


# count occurances funtion
def countoccur():
    import string
    file = open ("LiTestFile.txt", "r")
    text = file.read().lower()
    for c in string.punctuation:
        text = text.replace(c,"")
    wordlist = text.split()
    mydict = {}
    for word in wordlist:
        if word not in mydict:
            mydict[word] = 1
        else:
            mydict[word] += 1
    return mydict


# Define Form as a Class
class Form( QDialog):
    # Form Constructor for GUI
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.pbutton1 = QPushButton("&Character Count")
        self.lineedit1 = QLineEdit("Character Count")
        self.pbutton2 = QPushButton("&Word Count")
        self.lineedit2 = QLineEdit("Word Count")
        self.pbutton3 = QPushButton("&Line Count")
        self.lineedit3 = QLineEdit("Line Count")
        self.label1 = QLabel("Enter Word to be Counted")
        self.lineedit4 = QLineEdit()
        self.pbutton4 = QPushButton("Count Occurrences of Word")
        self.lineedit4.selectAll()
        self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout()
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.label1)
        layout.addWidget(self.lineedit4)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        self.lineedit1.setFocus()
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL("clicked()"),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL("clicked()"),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL("clicked()"),self.button4Pressed)
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        self.setWindowTitle("File Processor")

# Define buttons and associated funtions

    def button1Pressed(self):
        file = open('LiTestFile.txt')
        charcount = 0
        for line in file:
            line = line.replace("\n", "")
            line = line.strip()
            for character in line:
                charcount = charcount + 1
        self.lineedit1.setText ("There are "+(str(charcount))+" characters.")
    def button2Pressed(self):
        myfile = open('LiTestFile.txt', 'r')
        wordcount = 0
        line = myfile.readline()
        while line != "":
            linelist = line.split()
            for x in linelist:
                wordcount = wordcount + 1
            line = myfile.readline()
        self.lineedit2.setText("There are "+(str(wordcount))+"  words.")
    def button3Pressed(self):
        myfile = open('LiTestFile.txt', 'r')
        linecount = 0
        line = myfile.readline()
        while line != "":
            linecount = linecount + 1
            line = myfile.readline()
        self.lineedit3.setText("There are "+(str(linecount))+" lines.")
 
    def button4Pressed(self):
        word = unicode(self.lineedit4.text()).lower()
        word_dictionary = countoccur()
        if word in word_dictionary:
            self.lineedit4.setText("This word occurs "+(str(word_dictionary[word]))+" times.")
        else:
            self.lineedit4.setText("Word not found in text.")
            
    def buttonQuitPressed(self):
        quit()
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()                           # Create Instance of Form
form.show()                             # Show the Form
app.exec_()                             # Start Event Handler Loop

        

