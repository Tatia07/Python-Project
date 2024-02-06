import sys
import json
from PyQt5.QtWidgets import (QApplication, 
QWidget, 
QVBoxLayout, 
QHBoxLayout, 
QLineEdit, 
QPushButton, 
QListWidget, 
QCheckBox, 
QListWidgetItem, 
QLabel)
from PyQt5.QtCore import Qt

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.ui()

    def ui(self):
        self.setWindowTitle('Todo App')

        self.t_input = QLineEdit(self)
        self.add_button = QPushButton('Add Task', self)
        self.delete_button = QPushButton('Delete Selected', self)
        self.delete_all_button = QPushButton('Delete All', self)
        self.save_button = QPushButton('Save Tasks', self)
        self.dark_label = QLabel('Dark Mode:', self)
        self.dark_button = QPushButton('☀️', self) 
        self.task_list = QListWidget(self)

        self.setStyleSheet("""
            /* ძირითადი ნაწილი */
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            /* ღილაკები */
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            QPushButton:hover{
                background-color: #389B3C;
                transition: 0.7s;
            }
            /* სია */
            QListWidget {
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 15px;
                font-size: 20px;
            }
            /* CheckBox */
            QCheckBox {
                color: #333;
                font-size: 14px;
            }
            /* ტექსტი */
            QLabel {
                font-weight: bold;
                margin-top: 10px;
                font-size: 16px;
            }
            /* Input*/
            QLineEdit {
                padding: 10px;
                font-size: 20px;
            }
        """)

        main_layout = QVBoxLayout(self)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.t_input)
        input_layout.addWidget(self.add_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.delete_all_button)
        button_layout.addWidget(self.save_button)

        dark_layout = QHBoxLayout()
        dark_layout.addWidget(self.dark_label)
        dark_layout.addWidget(self.dark_button)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(dark_layout)

        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.del_selected_task)
        self.delete_all_button.clicked.connect(self.delete_all)
        self.save_button.clicked.connect(self.save_tasks)
        self.t_input.returnPressed.connect(self.add_task)
        self.dark_button.clicked.connect(self.dark_mode)

        self.show()

    def add_task(self):
        task_title = self.t_input.text().strip()
        if task_title:
            task_item = QListWidgetItem()
            task_checkbox = QCheckBox(task_title)
            self.task_list.addItem(task_item)
            self.task_list.setItemWidget(task_item, task_checkbox)
            self.t_input.clear()

    def del_selected_task(self):
        selected_items = self.task_list.selectedItems()
        for item in selected_items:
            row = self.task_list.row(item)
            self.task_list.takeItem(row)

    def delete_all(self):
        self.task_list.clear()

    def save_tasks(self):
        tasks_data = []
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            task_title = self.task_list.itemWidget(item).text()
            tasks_data.append({"title": task_title, "completed": item.isSelected()})

        with open('tasks.json', 'w') as f:
            json.dump(tasks_data, f, indent=2)

    def dark_mode(self):
        dark_mode_enabled = self.dark_button.text() == '🌙'
        if dark_mode_enabled:
            self.setStyleSheet("""
            /* ძირითადი ნაწილი */
            QWidget {
                background-color: #0D1F23;
                font-family: Arial, sans-serif;
            }
            /* ღილაკები */
            QPushButton {
                background-color: #2D4A53;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            QPushButton:hover{
                background-color: #132E35;
                transition: 0.7s;
            }
            /* სია */
            QListWidget {
                background-color: #2D4A53;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            /* CheckBox */
            QCheckBox {
                background-color: #69818D;
                color: #E3E5D8;
                font-size: 20px;
            }
            /* ტექსტი */
            QLabel {
                font-weight: bold;
                margin-top: 10px;
                font-size: 15px;
                color: white;
            }
            /* input ველი */
            QLineEdit {
                color: white;
                padding: 10px;
                font-size: 20px;
            }
            """)
            self.dark_button.setText('☀️')
        else:
            self.setStyleSheet("""
                /* მთავარი ნაწილი */
                QWidget {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                }
                /* ღილაკები */
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 16px;
                }
                QPushButton:hover{
                    background-color: #389B3C;
                    transition: 0.7s;
                }
                /* სია */
                QListWidget {
                    background-color: #fff;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                    padding: 10px;
                    font-size: 14px;
                }
                /* CheckBox */
                QCheckBox {
                    color: #333;
                    font-size: 14px;
                }
                /* ტექსტი */
                QLabel {
                    font-weight: bold;
                    margin-top: 10px;
                    font-size: 16px;
                }
                /* Input ველი */
                QLineEdit {
                    padding: 10px;
                    font-size: 14px;
                }
            """)
            self.dark_button.setText('🌙')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    sys.exit(app.exec_())