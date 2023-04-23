from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QGridLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minion Calculator")

        # Define minion rates
        self.hour = 3600
        self.day = 86400
        self.week = 604800

        self.slime_minion1 = 26
        self.slime_minion3 = 24
        self.slime_minion5 = 22
        self.slime_minion7 = 19
        self.slime_minion9 = 16
        self.slime_minion11 = 12

        self.Blaze_minion1 = 33
        self.Blaze_minion3 = 31
        self.Blaze_minion5 = 28.5
        self.Blaze_minion7 = 25
        self.Blaze_minion9 = 21
        self.Blaze_minion11 = 16.5

        self.slime_sell = 5

        # Create main widget and layout
        main_widget = QWidget(self)
        main_layout = QGridLayout(main_widget)

        # Create minion selection combo box
        self.minion_combo_box = QComboBox()
        self.minion_combo_box.addItem("Slime")
        self.minion_combo_box.addItem("Blaze")

        # Create table labels
        self.table_labels = []
        for row, label_text in enumerate(["", "Hour:", "Day:", "Week:"]):
            row_labels = []
            for col, _ in enumerate(["Type:", "Tier 1:", "Tier 3:", "Tier 5:", "Tier 7:", "Tier 9:", "Tier 11:"]):
                label = QLabel()
                if row == 0:
                    label.setText(label_text)
                main_layout.addWidget(label, row+1, col)
                row_labels.append(label)
            self.table_labels.append(row_labels)

        # Connect combo box to update table on change
        self.minion_combo_box.currentIndexChanged.connect(self.update_table)

        # Add widgets to main layout
        main_layout.addWidget(QLabel("Minion:"), 0, 0)
        main_layout.addWidget(self.minion_combo_box, 0, 1)
        main_layout.setSpacing(5)

        self.update_table()

        # Set main widget
        self.setCentralWidget(main_widget)

    def update_table(self):
        # Get selected minion
        minion = self.minion_combo_box.currentText()
        tiers = ['I', 'III', 'V', 'VII', 'IX', 'XI']

        # Get minion rate based on selected minion
        if minion == "Slime":
            minion_rates = [self.slime_minion1, self.slime_minion3, self.slime_minion5, self.slime_minion7, self.slime_minion9, self.slime_minion11]
        elif minion == "Blaze":
            minion_rates = [self.Blaze_minion1, self.Blaze_minion3, self.Blaze_minion5, self.Blaze_minion7, self.Blaze_minion9, self.Blaze_minion11]
        else:
            print("not implemented yet")
            exit()

        # Update table with minion rates
        for row, (label_prefix, time_interval) in enumerate([("", 1), ("Hour:", self.hour), ("Day:", self.day), ("Week:", self.week)]):
            self.table_labels[row][0].setText(label_prefix)
            self.table_labels[row][0].setAlignment(Qt.AlignCenter)
            self.table_labels[row][0].setFixedWidth(130)
            self.table_labels[row][0].setStyleSheet("background-color: #313131; color: #FFFFFF; QLabel{text-align: center}")
            for col, rate in enumerate(minion_rates):
                items = round(int(time_interval) / int(rate))
                items2 = round((int(time_interval) / int(rate))*5)
                if row == 0:
                    self.table_labels[row][col+1].setText(f'Tier {tiers[col]}')
                    self.table_labels[row][col+1].setAlignment(Qt.AlignCenter)
                    self.table_labels[row][col+1].setFixedWidth(130)
                    self.table_labels[row][col+1].setStyleSheet("background-color: #313131; color: #FFFFFF; QLabel{text-align: center}")
                else:
                    self.table_labels[row][col+1].setText('<span style="color: white">items: ' + str(items) + '</span><br><br><span style="color: #FFAA00">sell: ' + str(items2) + '</span>')
                    self.table_labels[row][col+1].setAlignment(Qt.AlignCenter)
                    self.table_labels[row][col+1].setFixedWidth(130)
                    self.table_labels[row][col+1].setStyleSheet("background-color: #222222; color: #FFFFFF; QLabel{text-align: center}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()