from pypdf import PdfReader 
import re 
file = PdfReader("Standard A 01.lcd.pdf")
page = file.pages[0]
text = page.extract_text()
text=text.split("\n")
for i,line in enumerate(text) : 
    line=line.lower()
    if re.match("^name",line):
        print(f"Name : {text[i+1].strip()}")
    if line.__contains__("area"):
        print(f"Area : {text[i+1].strip()}")
    if line.__contains__("ret. time"):
        print(f"Retention time : {text[i+1].strip()}")
    