# gui_main.py
# PyQt5 기반 성격 분석 팩트 폭행 프로그램 GUI

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from data import QUESTIONS, PERSONALITY_TYPES, ADVICE_DICT

class PersonalityTestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('성격 분석 팩트 폭행 프로그램')
        self.setFixedSize(420, 300)
        self.question_idx = 0
        self.scores = {ptype: 0 for ptype in PERSONALITY_TYPES}
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30, 30, 30, 30)
        self.layout.setSpacing(30)

        # 질문 라벨
        self.label = QLabel(self.get_question_text())
        self.label.setFont(QFont('맑은 고딕', 15, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        # 버튼 레이아웃
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(20)

        self.btn_yes = QPushButton('예')
        self.btn_no = QPushButton('아니오')
        for btn in (self.btn_yes, self.btn_no):
            btn.setFixedHeight(40)
            btn.setFont(QFont('맑은 고딕', 12, QFont.Bold))
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #b3e5fc;
                    color: #222;
                    border-radius: 20px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #4dd0e1;
                    color: #fff;
                }
            """)
        self.btn_yes.clicked.connect(lambda: self.answer('네'))
        self.btn_no.clicked.connect(lambda: self.answer('아니오'))
        btn_layout.addWidget(self.btn_yes)
        btn_layout.addWidget(self.btn_no)

        self.layout.addLayout(btn_layout)
        self.setLayout(self.layout)
        self.setStyleSheet("""
            QWidget {
                background: #f8fcff;
            }
        """)

    def get_question_text(self):
        return f"Q{self.question_idx+1}. {QUESTIONS[self.question_idx]['text']}"

    def answer(self, user_answer):
        # 점수 누적
        if user_answer == '네':
            for ptype, weight in QUESTIONS[self.question_idx]['weights'].items():
                self.scores[ptype] += weight
        self.question_idx += 1
        if self.question_idx < len(QUESTIONS):
            self.label.setText(self.get_question_text())
        else:
            self.show_result()

    def show_result(self):
        best_type = max(self.scores, key=lambda k: self.scores[k])
        advice = ADVICE_DICT.get(best_type, '스스로를 더 잘 이해하려고 노력해봐.')
        msg = f"<b>[분석 결과]</b><br>당신의 성격 유형: <b>{best_type}</b><br><br><b>[팩폭 멘트]</b><br>{advice.replace(chr(10), '<br>')}"
        QMessageBox.information(self, '성격 분석 팩트 폭행 프로그램', msg)
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PersonalityTestApp()
    win.show()
    sys.exit(app.exec_())
