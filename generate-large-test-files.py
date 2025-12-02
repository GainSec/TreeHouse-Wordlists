from fpdf import FPDF
import os

class PDFGenerator(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=False)

    def add_dummy_page(self, text):
        self.add_page()
        self.set_font("Arial", size=12)
        for _ in range(100):
            self.cell(0, 10, text, ln=1)

pdf = PDFGenerator()
target_size = 1 * 1024 * 1024 * 1024  # 1 GB
page_text = "This is a dummy line to fill the PDF and increase file size." * 10

while True:
    pdf.add_dummy_page(page_text)
    tmp_path = "./large_test.pdf"
    pdf.output(tmp_path)
    if os.path.getsize(tmp_path) >= target_size:
        break
