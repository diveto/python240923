# demo_form.py는 Business Logic
# demo_form.ui는 Design Form

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

# 디자인파일 로딩
form_class = uic.loadUiType('demo_form.ui')[0]

# 폼클래스 정의
class DemoForm(QDialog, form_class):
    # 초기화
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText('첫번째화면 출력')

# 진입점 체크
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()