

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QScrollArea, QSizePolicy, QSlider,
    QTabWidget, QVBoxLayout, QWidget, QFileDialog, QPushButton, QPlainTextEdit, QListWidget, QListWidgetItem)

from Custom_Widgets.AnalogGaugeWidget import AnalogGaugeWidget
from PySide6.QtCore import QDir
import random




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(823, 431)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gauge_container = QWidget(self.centralwidget)
        self.gauge_container.setObjectName(u"gauge_container")
        self.gridLayout_4 = QGridLayout(self.gauge_container)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_5 = QWidget(self.gauge_container)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout = QVBoxLayout(self.widget_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.widget = AnalogGaugeWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(300, 300))
        self.widget.setMaximumSize(QSize(600, 600))
        self.widget.setBaseSize(QSize(300, 300))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.widget)


        self.gridLayout_4.addWidget(self.widget_5, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.gauge_container)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_6 = QVBoxLayout(self.widget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.widget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_28.setFont(font)

        self.verticalLayout_7.addWidget(self.label_28)


        self.verticalLayout_6.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.widget_15 = QWidget(self.widget1)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_8 = QVBoxLayout(self.widget_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Parameter = QTabWidget(self.widget_15)
        self.Parameter.setObjectName(u"Parameter")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_16 = QGridLayout(self.tab_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.scrollArea = QScrollArea(self.tab_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 350, 367))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")




       








        

       


       

        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])


        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(QFont("./fonts/ds_digital/DS-DIGIB.TTF",12))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)


 
        self.btn1 = QPushButton("Open")
        self.btn1.setFont(QFont("./fonts/ds_digital/DS-DIGIB.TTF",12))
        self.pathbox = QPlainTextEdit(self.widget_2)
        self.pathbox.setFixedSize(360,30)
        self.pathbox.setPlainText("putty.log")
        self.pathbox.setDisabled(True)
        self.gridLayout.addWidget(self.pathbox, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.btn1, 2, 1, 1, 1)

        self.empty = QWidget()
        self.empty.setFixedHeight(10)
        self.gridLayout.addWidget(self.empty, 3, 1, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(QFont("./fonts/ds_digital/DS-DIGIB.TTF",15))

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)



        font_id2 = QFontDatabase.addApplicationFont("./fonts/digital-7.ttf")
        font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.ActualValue = QLabel(self.scrollAreaWidgetContents)
        self.ActualValue.setObjectName(u"ActualValue")
        self.ActualValue.setFrameShape(QFrame.NoFrame)
        self.ActualValue.setFrameShadow(QFrame.Sunken)
        self.ActualValue.setFont(QFont(font_family2, 30))
        

        
        self.prec_comboBox = QComboBox(self.widget_2)
        self.prec_comboBox.addItem("Volts")
        self.prec_comboBox.setObjectName(u"prec_comboBox")
        self.prec_comboBox.setFont(QFont('./fonts/ds_digital/DS-DIGIB.TTF',15))
        
        


        self.gridLayout.addWidget(self.ActualValue,5,0,1,1)
        self.gridLayout.addWidget(self.prec_comboBox,5,1,1,1)


        self.label_r= QLabel(self.widget_2)
        self.label_r.setObjectName(u"label_r")
        self.label_r.setFont(QFont("./fonts/ds_digital/DS-DIGIB.TTF",15))

        self.gridLayout.addWidget(self.label_r, 6, 0, 1, 1)

        self.access_comboBox = QComboBox(self.widget_2)
        self.access_comboBox.addItem("Only Me")
        self.access_comboBox.addItem("Local Network")
        self.access_comboBox.setObjectName(u"access_comboBox")
        self.access_comboBox.setFont(QFont('',13))
        self.gridLayout.addWidget(self.access_comboBox, 7, 0, 1, 1)
        self.btn2 = QPushButton("Apply")
        self.btn2.setFont(QFont('./fonts/ds_digital/DS-DIGIB.TTF',12))
        self.gridLayout.addWidget(self.btn2, 7, 1, 1, 1)

        self.local_status= QLabel(self.widget_2)
        self.local_status.setObjectName(u"local_status")
        self.local_status.setFont(QFont("./fonts/ds_digital/DS-DIGIB.TTF",7))
        self.gridLayout.addWidget(self.local_status, 8, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.widget_2, 0, Qt.AlignTop)

        


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_16.addWidget(self.scrollArea, 3, 0, 1, 1)
        
        self.Parameter.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        # Create a grid layout for the new tab
        self.gridLayout_15 = QGridLayout(self.tab)
        self.gridLayout_15.setObjectName("gridLayout_15")

        # Create a scroll area within the new tab
        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)

        # Create the widget that will contain the scrollable content
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        # Remove setGeometry to allow layout to manage size dynamically

        # Create a vertical layout for the scroll area contents
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Create widget_10 and its vertical layout
        self.widget_10 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_2 = QVBoxLayout(self.widget_10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_4.setAlignment(Qt.AlignTop)
        
        # Create widget_4 and its grid layout
        self.widget_4 = QWidget(self.widget_10)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName("gridLayout_3")


        # Create widget_9 and its grid layout
        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_2 = QGridLayout(self.widget_9)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # Add label_9 to gridLayout_2
        self.label_9 = QLabel(self.widget_9)
        self.label_9.setObjectName("label_9")
        self.label_9.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',15))
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        # Add status to gridLayout_2
        self.status = QLabel(self.widget_9)
        self.status.setObjectName("status")
        self.status.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
        self.gridLayout_2.addWidget(self.status, 0, 1, 1, 1)
        # Add label_10 to gridLayout_2
        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        # Add filename QPlainTextEdit to gridLayout_2
        self.filename2 = QPlainTextEdit(self.widget_9)
        self.filename2.setFixedSize(300,30)
        self.gridLayout_2.addWidget(self.filename2, 2, 0, 1, 1)

        # Add label_11 to gridLayout_2
        self.label_11 = QLabel(self.widget_9)
        self.label_11.setObjectName("label_11")
        self.label_11.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        # Add path2 QPlainTextEdit to gridLayout_2
        self.path2 = QPlainTextEdit(self.widget_9)
        self.path2.setFixedSize(300,30)
        self.path2.setDisabled(True)
        self.gridLayout_2.addWidget(self.path2, 4, 0, 1, 1)
        self.btn5 = QPushButton("Open")
        self.btn5.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))  
        self.gridLayout_2.addWidget(self.btn5, 4, 1, 1, 1)
         
        self.btn3 = QPushButton("Start Logging")
        self.btn3.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
        self.btn4 = QPushButton("Stop Logging")
        self.btn4.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))
        self.gridLayout_2.addWidget(self.btn3, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.btn4, 5, 1, 1, 1)
        
        
        
        # Add label_11 to gridLayout_2
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName("label_11")
        self.label_2.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',15))
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        
        self.graph_type = QLabel(self.widget_9)
        self.graph_type.setObjectName("graph_type")
        self.graph_type.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',11))
        self.gridLayout_2.addWidget(self.graph_type, 7, 0, 1, 1)
        
        self.graph_comboBox = QComboBox(self.widget_9)
        self.graph_comboBox.addItem("line")
        self.graph_comboBox.addItem("scatter")
        self.graph_comboBox.setObjectName(u"graph_comboBox")
        self.graph_comboBox.setFont(QFont('./fonts/ds_digital/DS-DIGIB.TTF',11))
        self.gridLayout_2.addWidget(self.graph_comboBox, 7, 1, 1, 1)
        

        self.graph_data = QLabel(self.widget_9)
        self.graph_data.setObjectName("graph_data")
        self.graph_data.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',11))
        self.gridLayout_2.addWidget(self.graph_data, 8, 0, 1, 1)
        
        self.graphdata_comboBox = QComboBox(self.widget_9)
        self.graphdata_comboBox.addItem("Live")
        self.graphdata_comboBox.addItem("Already Exists")
        self.graphdata_comboBox.addItem("Database")
        self.graphdata_comboBox.setObjectName(u"graphdata_comboBox")
        self.graphdata_comboBox.setFont(QFont('./fonts/ds_digital/DS-DIGIB.TTF',11))
        self.gridLayout_2.addWidget(self.graphdata_comboBox, 8, 1, 1, 1)
        
        self.label_loc = QLabel(self.widget_9)
        self.label_loc.setObjectName("label_loc")
        self.label_loc.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))  
        self.gridLayout_2.addWidget(self.label_loc, 9, 0, 1, 1)      
        
        self.path3 = QPlainTextEdit(self.widget_9)
        self.path3.setFixedSize(300,30)
        self.path3.setDisabled(True)
        self.gridLayout_2.addWidget(self.path3, 10, 0, 1, 1)
        self.btn6 = QPushButton("Open")
        self.btn6.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))  
        self.gridLayout_2.addWidget(self.btn6, 10, 1, 1, 1) 
        
        self.widget_90 = QWidget(self.widget_9)
        self.plotlayout = QHBoxLayout(self.widget_90)

        self.btn7 = QPushButton("Plot")
        self.btn7.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',14))  
        self.plotlayout.addWidget(self.btn7)       


        

        # Add widget_9 to gridLayout_3
        self.gridLayout_3.addWidget(self.widget_9, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_90, 2, 0, 1, 1)
        

        # Add widget_4 to verticalLayout_2
        self.verticalLayout_2.addWidget(self.widget_4)

        # Add widget_10 to verticalLayout_4
        self.verticalLayout_4.addWidget(self.widget_10)

        # Set the scroll area widget
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        # Add the scroll area to gridLayout_15
        self.gridLayout_15.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        # Add the new tab to the QTabWidget with a label
       
  

        self.Parameter.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea_3 = QScrollArea(self.tab_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 350, 245))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_14 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_7 = QGridLayout(self.widget_14)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_12 = QLabel(self.widget_14)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_7.addWidget(self.label_12, 1, 0, 1, 1)

        self.lcdMinVal = QLCDNumber(self.widget_14)
        self.lcdMinVal.setObjectName(u"lcdMinVal")
        self.lcdMinVal.setFont(font1)
        self.lcdMinVal.setFrameShape(QFrame.NoFrame)
        self.lcdMinVal.setFrameShadow(QFrame.Plain)
        self.lcdMinVal.setLineWidth(0)
        self.lcdMinVal.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdMinVal, 0, 2, 1, 1)

        self.MaxValueSlider = QSlider(self.widget_14)
        self.MaxValueSlider.setObjectName(u"MaxValueSlider")
        self.MaxValueSlider.setMaximum(1600)
        self.MaxValueSlider.setSingleStep(10)
        self.MaxValueSlider.setValue(1600)
        self.MaxValueSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MaxValueSlider, 1, 1, 1, 1)



        self.lcdMaxVal = QLCDNumber(self.widget_14)
        self.lcdMaxVal.setObjectName(u"lcdMaxVal")
        self.lcdMaxVal.setFont(font1)
        self.lcdMaxVal.setFrameShape(QFrame.NoFrame)
        self.lcdMaxVal.setFrameShadow(QFrame.Plain)
        self.lcdMaxVal.setLineWidth(0)
        self.lcdMaxVal.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_7.addWidget(self.lcdMaxVal, 1, 2, 1, 1)

        self.lcdScalaCount = QLCDNumber(self.widget_14)
        self.lcdScalaCount.setObjectName(u"lcdScalaCount")
        self.lcdScalaCount.setFont(font1)
        self.lcdScalaCount.setFrameShape(QFrame.NoFrame)
        self.lcdScalaCount.setFrameShadow(QFrame.Plain)
        self.lcdScalaCount.setLineWidth(0)
        self.lcdScalaCount.setSegmentStyle(QLCDNumber.Flat)
        self.lcdScalaCount.setProperty("intValue", 10)

        self.gridLayout_7.addWidget(self.lcdScalaCount, 2, 2, 1, 1)

        self.label_14 = QLabel(self.widget_14)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 2, 0, 1, 1)

        self.MainGridSlider = QSlider(self.widget_14)
        self.MainGridSlider.setObjectName(u"MainGridSlider")
        self.MainGridSlider.setMinimum(1)
        self.MainGridSlider.setMaximum(20)
        self.MainGridSlider.setValue(10)
        self.MainGridSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MainGridSlider, 2, 1, 1, 1)

        

        self.label_15 = QLabel(self.widget_14)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)

        self.MinValueSlider = QSlider(self.widget_14)
        self.MinValueSlider.setObjectName(u"MinValueSlider")
        self.MinValueSlider.setMaximum(100)
        self.MinValueSlider.setValue(0)
        self.MinValueSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_7.addWidget(self.MinValueSlider, 0, 1, 1, 1)
        
        self.label_account = QLabel(self.widget_14)
        self.label_account.setObjectName("label_account")
        self.label_account.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))  
        self.gridLayout_7.addWidget(self.label_account, 3, 0, 1, 1)

        self.label_email = QLabel(self.widget_14)
        self.label_email.setObjectName("label_email")
        self.label_email.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',9))  
        self.gridLayout_7.addWidget(self.label_email, 4, 0, 1, 1)    
        
        self.email = QPlainTextEdit(self.widget_14)
        self.email.setFixedSize(250,30)
        self.gridLayout_7.addWidget(self.email,5, 0, 1, 1)
        
        self.label_pass = QLabel(self.widget_14)
        self.label_pass.setObjectName("label_pass")
        self.label_pass.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',9))  
        self.gridLayout_7.addWidget(self.label_pass, 6, 0, 1, 1)      
        
        self.password = QLineEdit(self.widget_14)
        self.password.setFixedSize(250,30)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.gridLayout_7.addWidget(self.password,7, 0, 1, 1)
        
        self.Login = QPushButton("Login")
        self.Login.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))  
        self.gridLayout_7.addWidget(self.Login, 8, 0, 1, 1)         
        
        self.create = QPushButton("Create Account")
        self.create.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))  
        self.gridLayout_7.addWidget(self.create, 8, 1, 1, 1) 

        self.online = QCheckBox("Select to Log data into the database")
        self.gridLayout_7.addWidget(self.online, 9, 0, 1, 1)
        
        self.label_base = QLabel(self.widget_14)
        self.label_base.setObjectName("label_base")
        self.label_base.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',9))  
        self.gridLayout_7.addWidget(self.label_base, 10, 0, 1, 1)
        
        self.file_list = QListWidget(self.widget_14)
        self.gridLayout_7.addWidget(self.file_list, 11, 0, 1, 1)

        self.refresh = QPushButton("Refresh List")
        self.refresh.setFont(QFont('./fonts/ds_digital/DS-DIGI.TTF',12))  
        self.gridLayout_7.addWidget(self.refresh, 12, 0, 1, 1)         

        self.verticalLayout_5.addWidget(self.widget_14, 0, Qt.AlignTop)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_8.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.Parameter.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.Parameter)


        self.verticalLayout_6.addWidget(self.widget_15)


        self.horizontalLayout_2.addWidget(self.widget1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Parameter.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VOLTMETER", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"VOLTMETER", None))    
        self.label_r.setText(QCoreApplication.translate("MainWindow", u"Voltage Readings Access:", None))
        self.local_status.setText(QCoreApplication.translate("MainWindow", u"Access: Only Me", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Select Log File Location:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Voltage Reading:", None))    
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Setup", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data Visualization:", None))
        
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Data Logging:", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Status:Not Logging", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Filename:", None))
        self.graph_type.setText(QCoreApplication.translate("MainWindow", u"Select Graph Type:", None))
        self.graph_data.setText(QCoreApplication.translate("MainWindow", u"Data To Be Plotted:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Select The Path To save File:", None))
        self.label_loc.setText(QCoreApplication.translate("MainWindow", u"Select The File With Data To Plot:", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Data Logging and Visualization", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Max Value", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"EMAIL:", None))
        self.label_pass.setText(QCoreApplication.translate("MainWindow", u"PASSWORD:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Grid Divider", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Min Value", None))
        self.label_base.setText(QCoreApplication.translate("MainWindow", u"Files from the DataBase", None))
        self.label_account.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
        self.Parameter.setTabText(self.Parameter.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

