COMFORT_DICT = {
    "완벽주의자": "💧 너무 잘하려다 너무 지친 거야. 그냥 해도 충분히 괜찮아.",
    "게으름 대장": "🛋️ 누워 있는 것도 네 방식의 충전이야. 괜찮아, 일어날 타이밍은 올 거야.",
    "감성 폭발러": "🌧️ 감정이 많다는 건 네가 살아 있다는 증거야. 그건 약점이 아니라 재능이야.",
    "이성 만렙러": "📊 생각 많다고 다 나쁜 건 아냐. 천천히 해도 괜찮아, 결국 네 길로 갈 거야.",
    "자존감 낮은 타입": "🪞 넌 생각보다 훨씬 괜찮은 사람이야. 그걸 아는 사람부터 하나씩 생길 거야.",
    "자기애 최강자": "🦚 네 자신을 믿는 건 멋진 일이야. 세상도 곧 따라올 거야. 계속 나아가자.",
    "우유부단형": "🤹 고민한다고 망한 게 아니야. 오히려 신중한 사람일 뿐이야. 그건 장점이야.",
    "의욕 과잉형": "🔥 불붙는 것도 재능이야. 쉬어가는 중일 뿐이지 꺼진 건 아니야.",
    "현실 회피형": "☁️ 가끔은 도망도 전략이야. 너무 자책 말고, 다시 돌아올 타이밍만 잡자.",
    "타인 의존형": "🎈 남들 눈치 보느라 힘들었지. 이젠 너 눈치 좀 보자, 그게 더 중요해."
}
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
        self.best_type = max(self.scores, key=lambda k: self.scores[k])
        advice = ADVICE_DICT.get(self.best_type, '스스로를 더 잘 이해하려고 노력해봐.')

        # 팩폭 결과 QWidget 팝업
        self.result_popup = QWidget(self, flags=Qt.Window)
        self.result_popup.setWindowTitle('성격 분석 팩트 폭행 프로그램')
        self.result_popup.setFixedSize(520, 350)
        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(30)

        # 결과 텍스트 (QScrollArea로 감싸서 길어도 스크롤 가능)
        from PyQt5.QtWidgets import QScrollArea
        result_label = QLabel(f"<b>[분석 결과]</b><br>당신의 성격 유형: <b>{self.best_type}</b><br><br><b>[팩폭 멘트]</b><br>{advice.replace(chr(10), '<br>')}")
        result_label.setTextFormat(Qt.RichText)
        result_label.setFont(QFont('맑은 고딕', 13))
        result_label.setAlignment(Qt.AlignCenter)
        result_label.setWordWrap(True)
        result_label.setMinimumHeight(60)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.NoFrame)
        scroll.setWidget(result_label)
        layout.addWidget(scroll)

        # 휴지 버튼
        tissue_btn = QPushButton('😭 너무 아픈데요? 휴지 좀 주세요')
        tissue_btn.setFixedHeight(40)
        tissue_btn.setFont(QFont('맑은 고딕', 12, QFont.Bold))
        tissue_btn.setCursor(Qt.PointingHandCursor)
        tissue_btn.setStyleSheet('''
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
        ''')
        tissue_btn.clicked.connect(self.show_tissue_msg)
        layout.addWidget(tissue_btn)

        self.result_popup.setLayout(layout)
        self.result_popup.setStyleSheet('''
            QWidget {
                background: #f8fcff;
            }
        ''')
        self.result_popup.show()

    def show_tissue_msg(self):
        comfort = COMFORT_DICT.get(self.best_type, '💧 울지 마. 네가 못난 건 아니야. 그냥 좀 느린 거야.')
        tissue_box = QMessageBox(self)
        tissue_box.setWindowTitle('위로 한 스푼')
        tissue_box.setTextFormat(Qt.RichText)
        tissue_box.setText(comfort.replace('\n', '<br>'))
        tissue_box.setStyleSheet('''
            QMessageBox {
                background: #f8fcff;
            }
            QLabel {
                font-family: '맑은 고딕';
                font-size: 12pt;
                color: #222;
                padding: 10px 0 0 0;
                qproperty-alignment: AlignCenter;
            }
            QPushButton {
                background-color: #b3e5fc;
                color: #222;
                border-radius: 16px;
                border: none;
                min-width: 80px;
                min-height: 32px;
                font-size: 12pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4dd0e1;
                color: #fff;
            }
        ''')
        tissue_box.setFixedSize(520, 300)
        tissue_box.exec_()
        self.result_popup.close()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PersonalityTestApp()
    win.show()
    sys.exit(app.exec_())
