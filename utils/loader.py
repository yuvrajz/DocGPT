from docx import Document
from bs4 import BeautifulSoup
import requests

def load_txt(file):
    return file.read().decode("utf-8")

def load_docx(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def load_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return "\n".join([p.text for p in soup.find_all("p")])
