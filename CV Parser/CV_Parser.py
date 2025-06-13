from pdfminer.high_level import extract_text
import re

def extract_text_from_pdf(file_path):
    text = extract_text(file_path)
    return text

extracted_data = extract_text_from_pdf('Mohamed.Ewees.pdf').lower()

#print(extracted_data)

pattern = r"(skills)[\s:\n\-]*([\s\S]{0,1000})"

matches = re.findall(pattern,extracted_data,re.IGNORECASE)
skills_row = matches[0][1]
print(skills_row)
