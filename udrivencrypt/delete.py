from PyQt5.QtWidgets import (QCheckBox, QGroupBox, QComboBox, QLineEdit)
from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout)

def Delete(self):
    """
    The function which enables groupbox for deleting an existing key.

    :return: None
    """
    self.Dcheck = QCheckBox('Delete Keys', self)
    self.Dcheck.stateChanged.connect(self.Dtoggle)
    self.layout.addWidget(self.Dcheck)
    self.DgroupBox = QGroupBox("")
    self.DcomboBox = QComboBox()
    self.DcomboBox.addItem('Select your drive')
    self.DcomboBox.setMinimumWidth(300)
    device_list = self.listEncryptedDevices()
    for ele in device_list:
        self.DcomboBox.addItem(ele)

    label = QLabel()
    label.setText("Enter password to be deleted")
    self.Dtextbox = QLineEdit()
    #self.Dtextbox.setEnabled(False)
    self.Dtextbox.setEchoMode(QLineEdit.Password)
    self.Dtextbox.setMaxLength(10)
    #label1 = QLabel()
    #label1.setText("Enter your new password")
    #self.Dtextbox1 = QLineEdit()
    #self.Dtextbox1.setEchoMode(QLineEdit.Password)
    #self.Dtextbox1.setEnabled(False)
    #self.Dtextbox1.setMaxLength(10)
    self.Dbtn1 = QPushButton("Finish", self)
    self.Dbtn1.clicked.connect(self.check)
    vbox = QVBoxLayout()
    vbox.addWidget(self.DcomboBox)
    vbox.addWidget(label)
    vbox.addWidget(self.Dtextbox)
    #vbox.addWidget(label1)
    #vbox.addWidget(self.Dtextbox1)
    vbox.addWidget(self.Dbtn1)
    vbox.addStretch(1)
    self.DgroupBox.setLayout(vbox)
    self.layout.addWidget(self.DgroupBox)
