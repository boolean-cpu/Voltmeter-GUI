

import os
import sys
import time
import threading
from PySide6.QtWidgets import QMainWindow, QApplication,QMessageBox
from PySide6.QtGui import QFontDatabase
from PySide6.QtCore import Signal, QObject
from Voltage import Voltage
import subprocess
from LivePlotCanvas import Live
from Perf import Perf
from validate_email_address import validate_email
from pythonping import ping
from password_strength import PasswordPolicy
from ui_interface import *
import gc

from cpu import CPU
import psutil
import contextlib
import urllib.request
from Database import Database

cpu_initial = psutil.cpu_percent()

global precision
precision=100
global filename
filename = "putty.log"
global web
web=0
global folder
folder=""
global log 
log=''
global logy
logy =0
global type_g
type_g="line"
global live
live=0
global P 
P = Perf()
C = CPU()
window=''

class Worker(QObject):
    update_label_signal = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        track = 1
        global filename
        global log
        global web
        global live
        v = Voltage()


        while True:
            
            try:
                window.Checking()
            except:
                pass
            start_time = time.time()
            output = v.Read(track,filename)
            if output == 1000:
                continue
            else:
                
                track += 2
                self.update_label_signal.emit(str(output))
                if web ==1:
                    with open('web_log.log', 'w') as f:
                        f.write(str(output) + '\n')
                if logy ==1:
                    with open(log, 'a') as t:
                        t.write(str(output) +" "+str(time.strftime("%H:%M:%S"))+ '\n')
                if track%60 ==0:
                    gc.collect()
                execution =f"Thread Overall Time Logging-{logy},Live-{live},Sharing-{web}:{time.time() - start_time}:seconds"
                P.Log(execution)
                C.Log(str(psutil.cpu_percent()-cpu_initial))
                time.sleep(100/10000)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.show()


        self.ui.widget.enableBarGraph = True

        self.ui.widget.valueNeedleSnapzone = 1


        self.ui.widget.units = "cV"


        self.ui.widget.minValue = -1600

        self.ui.widget.maxValue = 1600


        self.ui.widget.scalaCount = 10
        self.putty_process = ''
        self.process = ''
        self.user = {'email':"", 'password':""}
        self.user_data = {'email':"", 'filename':"", 'data':[]}
        self.Data = Database()


        self.ui.widget.updateValue(int(self.ui.widget.maxValue - self.ui.widget.minValue)/2)

        
        self.ui.widget.valueChanged.connect( lambda:  self.updateSliderValue())
        

        self.ui.MinValueSlider.valueChanged.connect( lambda:  self.updateMinVal())

        self.ui.MaxValueSlider.valueChanged.connect( lambda:  self.updateMaxVal())

        self.ui.MainGridSlider.valueChanged.connect( lambda:  self.updateScalaCount())

        

        
        self.ui.widget.setCustomGaugeTheme(
            color1 = "#002523",
            color2= "#990008",
            color3 = "#00F6E9"
        )



        self.ui.widget.setBigScaleColor("#005275")
        self.ui.widget.setFineScaleColor("#005275")


        self.ui.prec_comboBox.addItem("centivolts")
        self.ui.prec_comboBox.addItem("millivolts")
        



        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), 'fonts/ds_digital/DS-DIGIB.TTF') )


       
        self.ui.prec_comboBox.currentTextChanged.connect(lambda: self.changePrecision())
        self.ui.btn1.clicked.connect(self.LogPath)
        self.ui.btn2.clicked.connect(self.Server)
        self.ui.btn5.clicked.connect(self.Fpath)
        self.ui.btn3.clicked.connect(self.Logging)
        self.ui.btn4.clicked.connect(self.StopLogging)
        self.ui.btn7.clicked.connect(self.Plotting)
        self.ui.btn6.clicked.connect(self.FToPlot)
        self.ui.create.clicked.connect(self.Create1)
        self.ui.Login.clicked.connect(self.Login1)
        self.ui.refresh.clicked.connect(self.Refresh)
        
        self.w=''
        

        self.updateGaugeValue()    
        self.Putty()   
        self.startWorkerThread() 
    def Refresh(self):
        if self.user['email'] == "":
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Log In first")
            msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()
        else:
            if self.is_connected():

                check_1 = self.Data.db.child('users').child('files')
            
                for checking in check_1.get():
                    print(checking.val()['email'])
                    if checking.val()['email'] == self.user['email']:
                        item = QListWidgetItem(checking.val()['filename'])
                        item.setFlags(item.flags() | Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        self.ui.file_list.addItem(item)    
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Error")
                msg_box.setText("Please check your internet connection")
                msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec()                   
            
    def is_connected(self):
        try:
            urllib.request.urlopen('https://www.google.com', timeout=5)  
            return True
        except urllib.error.URLError:
            return False       
    def Login1(self):
     
        if (self.ui.email.toPlainText().strip() =="") or (self.ui.password.text().strip() ==""):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Enter your email and password ")
            msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()

        else:
            if self.is_connected():
                check_1 = self.Data.db.child('users').child('users').get()
                flag = 0
                for checking in check_1:
                    if checking.val()['email'] == self.ui.email.toPlainText():
                        flag = 1
 
                if flag ==1:                                     
                    try:
                        self.Data.Login(self.ui.email.toPlainText(),self.ui.password.text())
                        self.user['email']=self.ui.email.toPlainText()
                        
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setWindowTitle("Successfull")
                        msg_box.setText("Login successfull")
                        msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                        msg_box.setDefaultButton(QMessageBox.Ok)
                        msg_box.exec()
                    except:
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setWindowTitle("Error")
                        msg_box.setText("An error occured while creating an account please try again or Check your Internet Connection")
                        msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                        msg_box.setDefaultButton(QMessageBox.Ok)
                        msg_box.exec() 
                else:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("Error")
                    msg_box.setText("No account with specified email exists")
                    msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                    msg_box.setDefaultButton(QMessageBox.Ok)
                    msg_box.exec()                    
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Error")
                msg_box.setText("Check your Internet connection")
                msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec() 
    def Create1(self):
       
        policy = PasswordPolicy.from_names(
            length=8,  # min length: 8
            uppercase=2,  # need min. 2 uppercase letters
            numbers=2,  # need min. 2 digits
            special=2,  # need min. 2 special characters
            nonletters=2,  # need min. 2 non-letter characters (digits, specials, anything)
        )   
        res = policy.test(self.ui.password.text())
        if (self.ui.email.toPlainText().strip() =="") or (self.ui.password.text().strip() ==""):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Enter your email and password ")
            msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()
        elif validate_email(self.ui.email.toPlainText(), verify=True) == False:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Please Enter a valid email address or Check your internet connection")
            msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec() 
        elif len(res) != 0:
            res2 = str(res)
            print(res2)
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Your Password must have atleast 8 characters with atleast 2 Uppercase letters, 2 Number, 2 Special characters")
            msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec() 
        else:
            if self.is_connected():
                check_1 = self.Data.db.child('users').child('users').get()
                flag = 0
                for checking in check_1:
                    if checking.val()['email'] == self.ui.email.toPlainText():
                        flag = 1
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setWindowTitle("Error")
                        msg_box.setText("The Email is already in use")
                        msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                        msg_box.setDefaultButton(QMessageBox.Ok)
                        msg_box.exec()  
                if flag ==0:
                    
                    try:
                        self.Data.Create(self.ui.email.toPlainText(),self.ui.password.text())
                        print("Where is the error")
                        self.user['email']=self.ui.email.toPlainText()
                        self.user['password'] = self.ui.password.text()
                        print(self.user)
                        self.Data.db.child('users').child("users").push(self.user)
                        
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setWindowTitle("Successfull")
                        msg_box.setText("Account successfully created")
                        msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                        msg_box.setDefaultButton(QMessageBox.Ok)
                        msg_box.exec()
                    except Exception as e:
                        print(e)
                        msg_box = QMessageBox()
                        msg_box.setIcon(QMessageBox.Information)
                        msg_box.setWindowTitle("Error")
                        msg_box.setText("An error occured while creating an account please try again or Check your Internet Connection")
                        msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                        msg_box.setDefaultButton(QMessageBox.Ok)
                        msg_box.exec() 
            else:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Error")
                msg_box.setText("Check your Internet connection")
                msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec() 
                    
                                                      

            
             
                      

    def Checking(self):
        return_code = self.putty_process.poll()
       
        if return_code is None:
            pass
        else:
            self.Putty()

    def Putty(self):    
        self.putty_process = subprocess.Popen(["C:/Program Files/PuTTY/putty.exe", "-load", "session 1"])

    def FToPlot(self):
        global P
        start_time = time.time()
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("*.log")
        dialog.setViewMode(QFileDialog.Detail)
        execution =f"File To Plot:{time.time() - start_time}:seconds"
        P.Log(execution)
        if dialog.exec_():
            self.ui.path3.setPlainText(str(dialog.selectedFiles()[0]))

        start_time =None
        execution=None
        gc.collect()
       

    def Plotting(self):
        global type_g
        global P
        global live
        start_time = time.time()

          
        if self.ui.graphdata_comboBox.currentText() == "Live":
            type_g=self.ui.graph_comboBox.currentText()
            live=1
            self.w = Live(type_g,live)
            self.w.show()
            execution =f"Live Plotting:{time.time() - start_time}:seconds"
            P.Log(execution)
            start_time = None
            execution = None
            
        elif self.ui.graphdata_comboBox.currentText() == "Already Exists":
            if self.ui.path3.toPlainText().strip() =="":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Error")
                msg_box.setText("Select File Path With Data To Plot")
                msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec()
                start_time=None
            else:
                type_g=self.ui.graph_comboBox.currentText()
                self.w = Live(type_g,0)
                self.w.show()
                with open(self.ui.path3.toPlainText(), 'r') as f:
                    arr = f.readlines()
                    for i in arr:
                        beta = i.split(" ")
                        self.w.plot_canvas.update_plot(float(beta[0]))
                        beta = None
                    arr = None
                execution =f"Plotting Existing Data:{time.time() - start_time}:seconds"
                P.Log(execution)
                start_time=None
                execution = None

        elif self.ui.graphdata_comboBox.currentText() == "Database":
            if self.user['email'] == "":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Error")
                msg_box.setText("Please Log In first")
                msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec()
            elif self.ui.file_list.currentItem().text() =="":
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setWindowTitle("Error")
                msg_box.setText("Select a File on the Database List  With Data To Plot")
                msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec()
                start_time=None
            else:
                type_g=self.ui.graph_comboBox.currentText()
                self.w = Live(type_g,0)
                self.w.show()
                arr=[]
                try:
                    check_1 = self.Data.db.child('users').child('files')           
                    for checking in check_1.get():
                        if checking.val()['filename'] == self.ui.file_list.currentItem().text() :
                            arr = checking.val()['data']
                except:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setWindowTitle("Error")
                    msg_box.setText("Check your intrnet connection")
                    msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
                    msg_box.setDefaultButton(QMessageBox.Ok)
                    msg_box.exec()                   
                        
                for i in arr:
                    beta = i.split(" ")
                    self.w.plot_canvas.update_plot(float(beta[0]))
                    beta = None
                arr = None
                execution =f"Plotting Existing Data:{time.time() - start_time}:seconds"
                P.Log(execution)
                start_time=None
                execution = None              
                
            
    def StopLogging(self):
        if (self.ui.path2.toPlainText().strip() =="") and (self.ui.filename2.toPlainText().strip() !="") and self.ui.online.isChecked():
            d=[]
            with open("temporal.log", "r") as file1:
                d = file1.readlines()
            self.user_data['email'] = self.user['email']
            self.user_data['filename'] = self.ui.filename2.toPlainText()
            self.user_data['data'] = d
            self.Data.db.child('users').child('files').push(self.user_data)          
                
        global logy
        logy=0
        self.ui.status.setText("Status:Not Logging")
        gc.collect()
        
    def Logging(self):
        global log
        global logy
        global P
        if (self.ui.path2.toPlainText().strip() =="") and (self.ui.filename2.toPlainText().strip() !="") and self.ui.online.isChecked():
           
            
            
            start_time = time.time()
            log ="temporal.log"
            with open(log, 'w+') as f:
                pass
            logy=1
            self.ui.status.setText("Status:Logging")
            execution =f"Creating File:{time.time() - start_time}:seconds"
            P.Log(execution)
            start_time = None
            execution = None            
        elif (self.ui.path2.toPlainText().strip() =="") or (self.ui.filename2.toPlainText().strip() ==""):
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle("Error")
            msg_box.setText("Enter Filename And Select Path To Save The File")
            msg_box.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec()
        else:
            

            start_time = time.time()
            log =self.ui.path2.toPlainText()+"/"+ self.ui.filename2.toPlainText()
            with open(log, 'w+') as f:
                pass
            logy=1
            self.ui.status.setText("Status:Logging")
            execution =f"Creating File:{time.time() - start_time}:seconds"
            P.Log(execution)
            start_time = None
            execution = None
            
            
    def Fpath(self):
        global folder
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.ui.path2.setPlainText(str(folder_path))
        folder = str(folder_path)
        folder_path = None
        gc.collect()
    
        
    def Server(self):
        global web
        global P
        start_time = time.time()
        if self.ui.access_comboBox.currentText() == "Local Network":
            self.process = subprocess.Popen(["python", "web_interface.py"])
            web=1
            self.ui.local_status.setText("Access: Local Network, Visit http://192.168.8.101:80 On Any Device Connected To The Network")
            execution =f"Starting Subprocess:{time.time() - start_time}:seconds"
            P.Log(execution)
            start_time= None
            execution = None
        else:
            try:
                self.process.kill()
            except:
                pass
            web=0
            self.ui.local_status.setText("Access: Only Me")
            execution =f"Killing Subprocess:{time.time() - start_time}:seconds"
            P.Log(execution)
            start_time = None
            execution = None
            gc.collect()
           
            
    def LogPath(self):
        global filename
        global P
        start_time = time.time()
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("*.log")
        dialog.setViewMode(QFileDialog.Detail)
        execution =f"Main Log File:{time.time() - start_time}:seconds"
        P.Log(execution)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            self.ui.pathbox.setPlainText(str(fileNames[0]))
            filename = str(fileNames[0])

        start_time =None
        execution = None
        gc.collect()
        

    def changePrecision(self):
        global precision
        global P
        start_time = time.time()
        print(self.ui.prec_comboBox.currentText())
        if self.ui.prec_comboBox.currentText() == "centivolts":
            precision=100
            self.ui.widget.units="cV"
        elif self.ui.prec_comboBox.currentText() == "millivolts":
            precision = 1000
            self.ui.widget.units = "mV"
        self.ui.widget.minValue = -16*precision
        self.ui.widget.maxValue =  16*precision
        self.ui.MinValueSlider.setMinimum(-16*precision)
        self.ui.MaxValueSlider.setMaximum(16*precision)
        execution =f"Precission Change:{time.time() - start_time}:seconds"
        P.Log(execution)
        start_time = None
        execution = None
        gc.collect()
        
        
        


    def updateScalaCount(self):
        self.ui.widget.setScalaCount(self.ui.MainGridSlider.value())
        self.ui.lcdScalaCount.display(int(self.ui.MainGridSlider.value()))    

    def updateMaxVal(self):
        self.ui.widget.setMaxValue(self.ui.MaxValueSlider.value())
        self.ui.lcdMaxVal.display(int(self.ui.MaxValueSlider.value()))     

    def updateMinVal(self):
        self.ui.widget.setMinValue(self.ui.MinValueSlider.value())
        self.ui.lcdMinVal.display(int(self.ui.MinValueSlider.value()))  



    def updateSliderValue(self):
        if self.ui.prec_comboBox.currentText() == "Volts":         
            self.ui.ActualValue.setText("{:.2f}".format(float(self.ui.widget.value/precision)))
        else:                      
            self.ui.ActualValue.setText(str(int(self.ui.widget.value)))       

    def updateGaugeValue(self):
        if self.ui.prec_comboBox.currentText() == "Volts":       
            self.ui.ActualValue.setText("{:.2f}".format(float(self.ui.widget.value/precision)))
        else : 
            self.ui.ActualValue.setText("{:.2f}".format(float(self.ui.widget.value)))
   


   

        
    def startWorkerThread(self):
        global P
        start_time = time.time()
        self.worker = Worker()
        self.worker.update_label_signal.connect(self.RupdateGaugeValue)

        self.thread = threading.Thread(target=self.worker.run)
        self.thread.daemon = True
        self.thread.start()
        execution =f"Starting Thread:{time.time() - start_time}:seconds"
        P.Log(execution)
    def RupdateGaugeValue(self,xu):
        global P
        start_time = time.time()
        xu= float(xu)
        global live
        if live==1:
            try:          
                self.w.plot_canvas.update_plot(xu)
                execution =f"Update Graph:{time.time() - start_time}:seconds"
                P.Log(execution)
            except:
                live = 0
        start_time = time.time()
        if self.ui.prec_comboBox.currentText() == "Volts":
            self.ui.widget.updateValue(int(xu*precision))
           
            self.ui.ActualValue.setText("{:.2f}".format(float(xu)))
        elif self.ui.prec_comboBox.currentText() == "centivolts":
            self.ui.widget.updateValue(int(xu*precision))
       
            self.ui.ActualValue.setText("{:.2f}".format(float(xu*precision)))
        elif self.ui.prec_comboBox.currentText() == "millivolts":
            self.ui.widget.updateValue(int(xu*precision))
          
            self.ui.ActualValue.setText("{:.2f}".format(float(xu*precision)))
        execution =f"Update Values:{time.time() - start_time}:seconds"
        P.Log(execution)
        start_time = None
        execution = None
       

def reset_log():
    try:
        window.w.closeEvent()
    except:
        pass
    try:
        window.process.kill()
    except:
        pass
    try:
        window.putty_process.kill()
    except:
        pass

    
    with open("putty.log", "w") as fi:
        fi.write("")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.aboutToQuit.connect(reset_log)
    sys.exit(app.exec_())

 