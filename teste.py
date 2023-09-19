import docx

arquivo = "Magic Form"
doc = docx.Document(f"documents/{arquivo}.docx")
reslt = [p.text for p in doc.paragraphs]

print(reslt)