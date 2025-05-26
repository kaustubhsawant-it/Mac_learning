import fitz 
import docx
import re
import pandas as pd


keywords = ['python','machine learning','power bi','sql']

def extract_text_from_pdf(file_path):
    doc=fitz.open(file_path)
    text=""
    for page in doc:
        text+= page.get_text()
    return text.lower()

def extract_text_from_docx(file_path):
    doc=docx.Document(file_path)
    text=""
    for para in doc.paragraphs:
        text+= para.text() + "\n"
    return text.lower()

def keyword_scan(text, keywords):
    found = {}
    for keyword in keywords:
        match = re.search(r'\b' + re.escape(keyword)+ r'\b',text)
        found[keyword]=bool(match)
    return found

def scan_resume(file_path, file_type = 'pdf'):
    if file_type == 'pdf':
        text = extract_text_from_pdf(file_path)
    
    elif file_type == 'docx':
        text=extract_text_from_docx(file_path)
    
    else:
        raise ValueError("Unsupported file type")
    
    results = keyword_scan(text,keywords)
    return pd.DataFrame([results])


file_path = '/Users/kaustubhsawant/Library/CloudStorage/OneDrive-Personal/Documents/Python_Advanced_Projects/resumes_for_try/simple-hipster-cv.pdf'
df = scan_resume(file_path,file_type='pdf')
print(df)