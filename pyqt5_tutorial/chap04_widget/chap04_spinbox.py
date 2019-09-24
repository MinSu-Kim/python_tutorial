from PyQt5.QtCore import QDate, QTime
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QLabel, QSpinBox, QHBoxLayout, QDoubleSpinBox, QDateEdit, QTimeEdit


class MySpinBox(QGroupBox):

    def __init__(self):
        super().__init__()
        self.setTitle('QSpinBox')
        self.init_ui()

    def init_ui(self):
        layout_group1 = self.group_int_spinbox()
        layout_group2 = self.group_double_spinbox()
        layout_group3 = self.group_date_spinbox()


        group2 = QGroupBox('QTimeEdit')
        lbl = QLabel('QTimeEdit')
        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat('hh:mm:ss')
        timeedit.timeChanged.connect(self.time_value_change)
        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        # self.lbl4 = QLabel(QTime.toString(timeedit.dateTime, 'hh:mm:ss'))
        self.lbl4 = QLabel(timeedit.time().toString('hh:mm:ss'))

        layout_group4 = QHBoxLayout()
        layout_group4.addWidget(lbl)
        layout_group4.addWidget(timeedit)
        layout_group4.addWidget(self.lbl4)

        layout = QVBoxLayout()
        layout.addLayout(layout_group1)
        layout.addLayout(layout_group2)
        layout.addLayout(layout_group3)
        layout.addLayout(layout_group4)

        self.setLayout(layout)

    def group_date_spinbox(self):
        lbl = QLabel('QDateEdit')
        group2 = QGroupBox('QDateEdit')
        self.dateedit = QDateEdit(self)
        self.dateedit.setDate(QDate.currentDate())
        self.dateedit.setMinimumDate(QDate(1900, 1, 1))
        self.dateedit.setMaximumDate(QDate(2100, 12, 31))
        self.dateedit.setDisplayFormat('yyyy-MM-dd')
        self.dateedit.dateChanged.connect(self.date_value_change)
        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))
        self.lbl3 = QLabel(QDate.toString(self.dateedit.date(), 'yyyy-MM-dd'))
        layout_group3 = QHBoxLayout()
        layout_group3.addWidget(lbl)
        layout_group3.addWidget(self.dateedit)
        layout_group3.addWidget(self.lbl3)
        return layout_group3

    def group_double_spinbox(self):
        group2 = QGroupBox('Double QSpinbox')
        lbl = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        self.lbl2 = QLabel('$ 0.0')
        self.dspinbox.valueChanged.connect(self.double_value_changed)
        layout_group2 = QHBoxLayout()
        layout_group2.addWidget(lbl)
        layout_group2.addWidget(self.dspinbox)
        layout_group2.addWidget(self.lbl2)
        return layout_group2

    def group_int_spinbox(self):
        group1 = QGroupBox('Integer QSpinBox')
        lbl = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        # self.spinbox.setRange(-10, 30)
        self.spinbox.setSingleStep(2)
        self.lbl1 = QLabel(str(self.spinbox.value()))
        self.spinbox.valueChanged.connect(self.int_value_changed)
        layout_group1 = QHBoxLayout()
        layout_group1.addWidget(lbl)
        layout_group1.addWidget(self.spinbox)
        layout_group1.addWidget(self.lbl1)
        return layout_group1

    def int_value_changed(self):
        self.lbl1.setText(str(self.spinbox.value()))

    def double_value_changed(self):
        self.lbl2.setText(str(self.dspinbox.value()))

    def date_value_change(self, t):
        self.lbl3.setText(QDate.toString(t, 'yyyy-MM-dd'))

    def time_value_change(self, t):
        self.lbl4.setText( t.toString('hh:mm:ss'))