import pandas as pd

from docx import Document
from fpdf import FPDF
from fpdf.enums import TableCellFillMode

WIDTH = 210
HEIGHT = 297


class PDF(FPDF):
    def header(self):
        # Logo
        self.image("Ebw Invest.png", 0, 0, WIDTH)
        self.ln(50)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font("Arial", "I", 8)
        # Page number
        self.cell(0, 10, "Page " + str(self.page_no()) + "/{nb}", 0, 0, "C")


def Do_pdf(Destino):
    # Instantiation of inherited class
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font("Arial", "B", 24)
    pdf.write(10, f"As Melhores Ações \nCom Melhor Custo/Benefício")
    pdf.ln(40)
    pdf.set_font("Times", "", 12)

    TABLE_DATA = pd.read_csv("magicForm.csv")
    TABLE_DATA = TABLE_DATA.applymap(str)
    columns = [list(TABLE_DATA)]
    rows = TABLE_DATA.values.tolist()
    data = columns + rows

    with pdf.table(
        borders_layout="MINIMAL",
        cell_fill_color=200,
        cell_fill_mode="ROWS",
        line_height=pdf.font_size * 2.5,
        text_align="CENTER",
    ) as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    """Ultima página"""
    pdf.add_page()
    pdf.set_margin(40)
    pdf.set_font("Arial", "B", 24)
    pdf.write(10, f"DISCLAIMER")
    pdf.ln(15)
    pdf.set_margin(20)
    pdf.set_font("Times", "", 12)
    documento = Document("Disclaimer.docx")
    for paragrafo in documento.paragraphs:
        pdf.write(5, paragrafo.text)
        pdf.ln(10)

    pdf.output(Destino + "/Carteira.pdf", "F")
