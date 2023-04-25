from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QGridLayout, QWidget
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtCore import Qt
import fuels
import minions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minion Calculator")

        # Define minion rates
        self.hour = 3600
        self.day = 86400
        self.week = 604800

        # Create main widget and layout
        main_widget = QWidget(self)
        main_layout = QGridLayout(main_widget)

        # Create minion selection combo box
        self.minion_combo_box = QComboBox()
        self.minion_combo_box.addItems(minions.minions_list)

        model = QStandardItemModel()
        for i in range(self.minion_combo_box.count()):
            item = QStandardItem(self.minion_combo_box.itemText(i))
            if i == 0:
                item.setBackground(QColor(0, 0, 0))
            elif i < 11:
                # set color for the farming items
                item.setBackground(Qt.darkGreen)
            elif i < 16:
                # set color for the farming items
                item.setBackground(QColor(34,34,34))
            else:
                # set color for the combat items
                item.setBackground(Qt.darkRed)
            model.appendRow(item)
        self.minion_combo_box.setModel(model)

        # boosts
        self.boosts_combo_box = QComboBox()
        self.boosts_combo_box.addItems(fuels.fuels_list)

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
        self.boosts_combo_box.currentIndexChanged.connect(self.update_table)

        # Add widgets to main layout
        main_widget.setStyleSheet("background-color: #000000; color: #FFFFFF; QLabel{text-align: center}")
        main_layout.addWidget(QLabel("Minion:"), 0, 0)
        main_layout.addWidget(self.minion_combo_box, 0, 1)
        main_layout.addWidget(QLabel("Fuel:"), 0, 2)
        main_layout.addWidget(self.boosts_combo_box, 0, 3, 1, 2)
        main_layout.setSpacing(1)

        self.update_table()

        # Set main widget
        self.setCentralWidget(main_widget)


    def update_table(self):

        # Get selected minion
        minion = self.minion_combo_box.currentText()
        boost = self.boosts_combo_box.currentText()

        tiers = ['I', 'III', 'V', 'VII', 'IX', 'XI']

        # Get minion rate based on selected minion
        minion_rates = [minions.minions[minion][0], minions.minions[minion][1], minions.minions[minion][2], minions.minions[minion][3], minions.minions[minion][4], minions.minions[minion][5]]
        item_sell = minions.minions[minion][6]
        item_boost = fuels.boosts[boost][0]

        if boost == "Everburning_Flame":
            if minions[minion][-1] == 3:
                item_boost = fuels.boosts[boost][0]
            else:
                item_boost = fuels.boosts[boost][0] - 0.05

        if minion == '----Choose_Minion----' or minion == '----Mining----' or minion == '----Farming----' or minion == '----Combat----':
            # Update table with minion rates
            for row, (label_prefix, time_interval) in enumerate([("", 1), ("Hour:", self.hour), ("Day:", self.day), ("Week:", self.week)]):
                self.table_labels[row][0].setText(label_prefix)
                self.table_labels[row][0].setAlignment(Qt.AlignCenter)
                self.table_labels[row][0].setStyleSheet("background-color: #313131; color: #FFFFFF; QLabel{text-align: center}")
                # round(base+base*item_boost, 2)
                for col, rate in enumerate(minion_rates):
                    base = "-"
                    items = "-"
                    items2 = "-"
                    if row == 0:
                        self.table_labels[row][col+1].setText(f'Tier {tiers[col]}')
                        self.table_labels[row][col+1].setAlignment(Qt.AlignCenter)
                        self.table_labels[row][col+1].setStyleSheet("background-color: #313131; color: #FFFFFF; QLabel{text-align: center}")
                    else:
                        self.table_labels[row][col+1].setText('<span style="color: white">items: ' + str(items) + '</span><br><br><span style="color: #FFAA00">sell: ' + str(items2) + '</span>')
                        self.table_labels[row][col+1].setAlignment(Qt.AlignCenter)
                        self.table_labels[row][col+1].setStyleSheet("background-color: #222222; color: #FFFFFF; QLabel{text-align: center}")
        else:
            # Update table with minion rates
            for row, (label_prefix, time_interval) in enumerate([("", 1), ("Hour:", self.hour), ("Day:", self.day), ("Week:", self.week)]):
                self.table_labels[row][0].setText(label_prefix)
                self.table_labels[row][0].setAlignment(Qt.AlignCenter)
                self.table_labels[row][0].setStyleSheet("background-color: #313131; color: #FFFFFF; QLabel{text-align: center}")
                # round(base+base*item_boost, 2)
                for col, rate in enumerate(minion_rates):
                    base = round((int(time_interval) / int(rate)*(minions.minions[minion][7]*0.5)), 2)
                    items = round(base+base*item_boost, 2)
                    items2 = round(items*item_sell, 2)
                    if row == 0:
                        self.table_labels[row][col+1].setText(f'Tier {tiers[col]}')
                        self.table_labels[row][col+1].setAlignment(Qt.AlignCenter)
                        self.table_labels[row][col+1].setStyleSheet("background-color: #313131; color: #FFFFFF; QLabel{text-align: center}")
                    else:
                        self.table_labels[row][col+1].setText('<span style="color: white">items: ' + str(items) + '</span><br><br><span style="color: #FFAA00">sell: ' + str(items2) + '</span>')
                        self.table_labels[row][col+1].setAlignment(Qt.AlignCenter)
                        self.table_labels[row][col+1].setStyleSheet("background-color: #222222; color: #FFFFFF; QLabel{text-align: center}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()