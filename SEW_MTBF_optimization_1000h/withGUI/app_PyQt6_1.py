import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTextEdit
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from main import genetic_algorithm, GENOME_LENGTH, POPULATION_SIZE, GENERATIONS, p_c_min, p_c_max, p_m_min, p_m_max
from main import calculate_info


class GeneticAlgorithmWorker(QThread):
    result_signal = pyqtSignal(object, float, object)
    error_signal = pyqtSignal(str)

    def __init__(self, C_s, C_d, m):
        super().__init__()
        self.C_s = C_s
        self.C_d = C_d
        self.m = m

    def run(self):
        try:
            best_individual, best_fitness = genetic_algorithm(GENOME_LENGTH, self.m, POPULATION_SIZE, GENERATIONS, p_c_min, p_c_max, p_m_min, p_m_max, self.C_s, self.C_d)
            maintenance_plan = calculate_info(best_individual)
            print(maintenance_plan)
            self.result_signal.emit(best_individual, best_fitness, maintenance_plan)
        except Exception as e:
            self.error_signal.emit(str(e))

class GeneticAlgorithmGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GUI")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.cs_label = QLabel("C_s (Setup Cost):")
        self.cs_entry = QLineEdit()
        layout.addWidget(self.cs_label)
        layout.addWidget(self.cs_entry)

        self.cd_label = QLabel("C_d (Downtime Cost Rate):")
        self.cd_entry = QLineEdit()
        layout.addWidget(self.cd_label)
        layout.addWidget(self.cd_entry)

        self.m_label = QLabel("m (Number of Repairmen):")
        self.m_entry = QLineEdit()
        layout.addWidget(self.m_label)
        layout.addWidget(self.m_entry)

        self.run_button = QPushButton("Run Algorithm")
        self.run_button.clicked.connect(self.run_genetic_algorithm)
        layout.addWidget(self.run_button)

        self.loading_label = QLabel("", alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loading_label)

        self.result_label = QLabel("", alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        self.maintenance_plan_box = QTextEdit()

        self.maintenance_plan_box.setReadOnly(True)

        self.maintenance_plan_box.setFixedHeight(500)

        layout.addWidget(self.maintenance_plan_box)

        self.setLayout(layout)

    def run_genetic_algorithm(self):
        try:
            C_s = float(self.cs_entry.text())
            C_d = float(self.cd_entry.text())
            m = int(self.m_entry.text())

            self.loading_label.setText("Running... Please wait")
            self.worker = GeneticAlgorithmWorker(C_s, C_d, m)
            self.worker.result_signal.connect(self.display_result)
            self.worker.error_signal.connect(self.display_error)
            self.worker.start()
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter valid numerical values for C_s, C_d, and m")

    def display_result(self, best_individual, best_fitness, maintenance_plan):
        self.loading_label.setText("")
        self.result_label.setText(f"Best Individual: {best_individual}\nBest Fitness: {best_fitness}")
        formatted_info = json.dumps(maintenance_plan, indent=10, ensure_ascii=False)
        self.maintenance_plan_box.setText(formatted_info)

    def display_error(self, error_message):
        self.loading_label.setText("")
        QMessageBox.critical(self, "Error", error_message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GeneticAlgorithmGUI()
    gui.show()
    sys.exit(app.exec())
