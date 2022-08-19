import sys
from datetime import date
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QSizePolicy, QStyledItemDelegate, \
    QAction, qApp, QMenu, QSystemTrayIcon, QStyle
from GUI import ADD, INFO
import base
from GUI.TAB import Ui_MainWindow


class FirstAid(QMainWindow):

    check_box = None
    tray_icon = None

    def __init__(self):
        super(FirstAid, self).__init__()

        self.dialog_add = class_ADD()
        self.dialog_info = info_for_user()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog_add.window_closed.connect(
            lambda: self.table_activate(2))  # сигнал перестал друблироваться в теле класса
        self.dialog_info.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.dialog_add.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.dialog_info.window_info.connect(self.info_close)
        self.ui.lineEdit.returnPressed.connect(self.serch_med)
        QFontDatabase.addApplicationFont("font/static/Rubik-Regular.ttf")
        self.ui.tableWidget.setItemDelegate(ColorDelegate())
        self.ui.pushButton.clicked.connect(self.open_ADD)
        self.ui.pushButton_2.clicked.connect(self.serch_med)
        self.ui.pushButton_3.clicked.connect(self.info_userOpen)
        self.ui.pushButton_4.clicked.connect(self.returned)
        self.table_activate(2)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_MessageBoxQuestion))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/main_ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        show_action = QAction("Показать окно", self)
        quit_action = QAction("Закрыть программу", self)
        hide_action = QAction("Свернуть", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def returned(self):
        self.ui.pushButton_4.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        self.table_activate(2)

    def info_userOpen(self):
        self.dialog_info.show()

    def info_close(self):
        """Остановка передачи сигналов"""

    def open_ADD(self):
        self.dialog_add.show()


    def serch_med(self):
        index_Policy = self.ui.lineEdit.sizePolicy()
        text_serch = self.ui.lineEdit.text()
        if index_Policy.horizontalPolicy() == 13:
            self.ui.lineEdit.setEnabled(True)
            self.ui.lineEdit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

            print('Пусто1')

        else:
            self.ui.lineEdit.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
            self.ui.lineEdit.setEnabled(False)
            if text_serch == '':
                print('Пусто')
            else:
                self.table_activate(1)


    def table_activate(self, table_type):

        if table_type == 1:
            serch_object = self.ui.lineEdit.text().upper()
            select = base.Search_Objects_inBase(serch_object)

            if not select:
                select = base.ListWidget_Object_in_Base('med')
                QMessageBox.information(self, "Внимание ", serch_object + " не найден!", QMessageBox.Ok)
            else:
                self.ui.pushButton_4.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        else:
            select = base.ListWidget_Object_in_Base('med')

        self.ui.lineEdit.clear()
        self.ui.tableWidget.clearContents()
        certainTable = self.ui.tableWidget
        certainTable.setRowCount(len(select))
        tablerow = 0


        for date_cut in select:
            Y = int(date_cut[4][:4])
            M = int(date_cut[4][5:7])
            D = int(date_cut[4][8:10])
            delta = date(Y, M, D) - date.today()
            if str(delta.days) > '0':
                go_table = str(delta.days)
            else:
                go_table = 'ПРОСРОЧЕНО'

            certainTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(date_cut[1])))
            certainTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(date_cut[2])))
            certainTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(date_cut[3])))
            certainTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(date_cut[4])))
            certainTable.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(go_table))
            certainTable.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(date_cut[5])))

            if int(delta.days) < 0:
                self.setColortoRow(tablerow, QColor(144, 144, 144))
                btm_del = QtWidgets.QPushButton('ПРОСРОЧЕНО')
                btm_del.setStyleSheet("background-color : yellow")
                btm_del.clicked.connect(lambda: self.del_expired(self.ui.tableWidget.currentRow()))
                self.ui.tableWidget.setCellWidget(tablerow, 4, btm_del)
            elif 0 < int(delta.days) < 11:
                self.setColortoRow(tablerow, QColor(255, 81, 36))
            elif 10 < int(delta.days) < 21:
                self.setColortoRow(tablerow, QColor(255, 127, 36))
            elif 20 < int(delta.days) < 31:
                self.setColortoRow(tablerow, QColor(255, 183, 36))
            elif 30 < int(delta.days) < 101:
                self.setColortoRow(tablerow, QColor(212, 255, 36))

            tablerow += 1

        nornal_med = 0
        expired_med = 0

        if self.ui.tableWidget.rowCount() == 0:
            value = 0
        else:
            for i in range(self.ui.tableWidget.rowCount()):

                if self.ui.tableWidget.item(i, 4).text() == "ПРОСРОЧЕНО":
                    expired_med += 1
                else:
                    nornal_med += 1

            value = 100 - ((nornal_med * 100) / (self.ui.tableWidget.rowCount()))

        self.ui.progressBar.setValue(int(value))

    def setColortoRow(self, rowIndex, color):
        for j in range(self.ui.tableWidget.columnCount()):
            self.ui.tableWidget.item(rowIndex, j).setBackground(color)


    def del_expired(self, row):
        print(self.ui.tableWidget.item(row, 0).text())
        reply = QMessageBox.question(
            self, 'Вопрос', 'Удалить "' + self.ui.tableWidget.item(row, 0).text() + '" безвозвратно?',
            QMessageBox.Yes, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            base.Del_Object_in_Base(self.ui.tableWidget.item(row, 0).text())
            self.ui.tableWidget.clearContents()
            self.table_activate(2)
        elif reply == QMessageBox.No:
            self.table_activate(2)


class ColorDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        if index.data() == "ПРОСРОЧЕНО":
            option.palette.setColor(QPalette.Text, QColor("red"))
        QStyledItemDelegate.paint(self, painter, option, index)


class class_ADD(QDialog):
    window_closed = pyqtSignal()  # сигнал используется для передачи состояния закрытого окна

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ADD.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Add)
        self.ui.pushButton_2.clicked.connect(self.Del)
        self.ui.pushButton_3.clicked.connect(self.close)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/main_ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.block_del()

    def block_del(self):
        self.window_closed.emit()
        self.ui.comboBox_2.clear()
        select = base.ListWidget_Object_in_Base('med')
        nameContaner = []
        for date_cut in select:
            nameContaner.append(date_cut[1])
        self.ui.comboBox_2.addItems(nameContaner)

    def Add(self):
        if self.ui.lineEdit.text() == '':
            QMessageBox.critical(self, "Ошибка ", "Необходимо добавить название препарата", QMessageBox.Ok)
        else:
            l1 = self.ui.lineEdit.text().upper()

            if self.ui.comboBox.currentIndex() < 0:
                QMessageBox.critical(self, "Ошибка ", "Необходимо выбрать лекарственную форму", QMessageBox.Ok)
            else:
                if self.ui.comboBox.currentIndex() == 0:
                    l2 = "Жидкое"
                elif self.ui.comboBox.currentIndex() == 1:
                    l2 = "Твердое"
                elif self.ui.comboBox.currentIndex() == 2:
                    l2 = "Мягкое"
                elif self.ui.comboBox.currentIndex() == 3:
                    l2 = "Аэрозоль"
                else:
                    l2 = 'Нет'

                if self.ui.textEdit.toPlainText() == '':
                    l3 = 'Нет'
                else:
                    l3 = self.ui.textEdit.toPlainText()

                Y = self.ui.calendarWidget.yearShown()
                M = self.ui.calendarWidget.monthShown()
                D = self.ui.calendarWidget.selectedDate().toString("dd")
                todayDate = date.today().strftime('%Y-%m-%d')

                if self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd") == todayDate:
                    QMessageBox.warning(self, "Внимание ", "Выбранная дата срока годности " + todayDate +
                                        " совпадает с сегодняшним днем!", QMessageBox.Ok)

                elif self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd") < todayDate:
                    delta = date.today() - date(Y, M, int(D))  # Вычисление кол-во дней просрочки
                    QMessageBox.warning(self, "Внимание ", "У препарата вышел срок годности "
                                        + str(delta.days) + " дня(й) назад!", QMessageBox.Ok)
                else:
                    l4 = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")

                    userLink = self.ui.lineEdit_2.text()

                    if userLink.lower().find("http") != -1 or userLink.lower().find("www") != -1:
                        l5 = userLink.lower()

                    elif userLink == '':
                        l5 = 'Нет'

                    else:
                        QMessageBox.information(self, "Внимание ", " Ссылка имеет не верный формат, "
                                                                   "отсутствуют эллементы http или www. "
                                                                   "Если ссылки на препарат нет, "
                                                                   "оставьте строку пустой.", QMessageBox.Ok)
                        l5 = 'Нет'

                    name_dublicate = base.Search_Dublicate_inBase(l1)

                    if not name_dublicate:
                        pass
                    else:
                        tablerow = 1

                        while True:
                            name_dublicates = base.Search_Dublicate_inBase(l1 + "(" +
                                                                           (str(name_dublicate[1] + tablerow)) + ")")

                            if not name_dublicates:
                                print("ДУбли кончились")
                                l1 = l1 + "(" + (str(name_dublicate[1] + tablerow)) + ")"
                                QMessageBox.information(self, "Внимание ", 'Препарат уже существует в списке, '
                                                                           'программа автоматически присваивает '
                                                                           'новое название копии "' + l1 + '"',
                                                        QMessageBox.Ok)
                                break

                            else:
                                i = str(name_dublicate[0])
                                name_dublicate = base.Search_Dublicate_inBase(i)
                                print('ЕЩЕ ЕСТЬ')
                                print(name_dublicate[0])
                                l1 = name_dublicate[0]

                            tablerow += 1

                    base.addObject_in_Base('med', l1, l2, l3, l4, l5)  # "med" по задумке адресует в нужную базу SQL
                    QMessageBox.information(self, "Внимание ", l1 + " успешно добавлен в базу!", QMessageBox.Ok)
                    self.block_del()

    def Del(self):
        reply = QMessageBox.question(
            self, 'Вопрос', 'Удалить безвозвратно??',
            QMessageBox.Yes, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            name_pills = self.ui.comboBox_2.currentText()
            base.Del_Object_in_Base(name_pills)
            self.block_del()
        else:
            print('NO')

    def closeEvent(self, event):
        self.window_closed.emit()  # передает слот по Эвенту
        event.accept()


class info_for_user(QDialog):
    window_info = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = INFO.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/main_ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

    def info_call(self):
        self.window_info.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirstAid()
    window.show()
    sys.exit(app.exec())
