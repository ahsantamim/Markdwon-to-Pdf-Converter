from PyQt6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit,
    QFileDialog, QLabel, QFrame, QScrollArea
)
from PyQt6.QtGui import QTextDocument
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtCore import Qt
import markdown2
import sys

class MarkdownToPdfApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🌈 Markdown to PDF Converter 🎨")
        self.setFixedSize(900, 600)  # অ্যাপের ফিক্সড সাইজ

        # === মূল লেআউট ===
        main_layout = QVBoxLayout()  # ভর্তিকাল লেআউট, যাতে বাটন নিচে যায়
        self.setStyleSheet("background-color: #F8F9FA;")  # ব্যাকগ্রাউন্ড কালার

        # === Markdown & PDF Preview (Side by Side) ===
        viewer_layout = QHBoxLayout()  # দুইটা ভিউয়ার এক লাইনে বসানোর জন্য

        # --- Markdown Viewer ---
        self.text_edit = QTextEdit(self)
        self.text_edit.textChanged.connect(self.update_preview)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #FFF3CD;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
               
            }
        """)

        scroll_area_input = QScrollArea()
        scroll_area_input.setWidgetResizable(True)
        scroll_area_input.setWidget(self.text_edit)

        # --- PDF Preview ---
        self.preview_label = QLabel("Markdown Preview", self)
        self.preview_label.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        self.preview_label.setStyleSheet("""
            padding: 10px; 
            background-color: #E3F2FD; 
          
            border-radius: 10px;
            font-size: 14px;
        """)
        self.preview_label.setWordWrap(True)

        scroll_area_preview = QScrollArea()
        scroll_area_preview.setWidgetResizable(True)
        scroll_area_preview.setWidget(self.preview_label)

        # === দুইটা Viewer এক লাইনে রাখা ===
        viewer_layout.addWidget(scroll_area_input, 1)
        viewer_layout.addWidget(scroll_area_preview, 1)

        # === বোতাম লেআউট (নিচে, কেন্দ্রস্থলে) ===
        button_layout = QHBoxLayout()
        self.btn_open = QPushButton("📂 Open Markdown")
        self.btn_save = QPushButton("💾 Save as PDF")

        for btn in [self.btn_open, self.btn_save]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #0078D7;
                    color: white;
                    font-size: 16px;
                    padding: 10px;
                    border-radius: 8px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #005A9E;
                }
            """)
            btn.setFixedHeight(40)
            button_layout.addWidget(btn)

        button_layout.setAlignment(self.btn_open, Qt.AlignmentFlag.AlignCenter)

        self.btn_open.clicked.connect(self.open_file)
        self.btn_save.clicked.connect(self.save_pdf)

        # === লেআউট সাজানো ===
        main_layout.addLayout(viewer_layout, 1)  # Markdown & PDF Viewer
        main_layout.addLayout(button_layout)  # বোতাম নিচে রাখা

        self.setLayout(main_layout)

    def open_file(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "Open Markdown File", "", "Markdown Files (*.md)")
        if filepath:
            with open(filepath, "r", encoding="utf-8") as file:
                self.text_edit.setText(file.read())

    def update_preview(self):
        """Live Markdown to HTML Preview"""
        md_text = self.text_edit.toPlainText()
        html_text = markdown2.markdown(md_text)
        self.preview_label.setText(html_text)

    def save_pdf(self):
        pdf_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if pdf_path:
            doc = QTextDocument()
            doc.setHtml(markdown2.markdown(self.text_edit.toPlainText()))
            printer = QPrinter()
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(pdf_path)
            doc.print(printer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarkdownToPdfApp()
    window.show()
    sys.exit(app.exec())
