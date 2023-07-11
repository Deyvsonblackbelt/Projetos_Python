import PyPDF2
from googletrans import Translator

def translate_pdf(input_path, output_path):
    # Extrai o texto do arquivo PDF
    text = extract_text_from_pdf(input_path)
    
    # Realiza a tradução
    translated_text = translate_text(text)
    
    # Salva o texto traduzido em um novo arquivo PDF
    save_text_as_pdf(translated_text, output_path)

def extract_text_from_pdf(path):
    with open(path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

def translate_text(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='pt')
    return translation.text

def save_text_as_pdf(text, path):
    with open(path, 'wb') as file:
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page()
        pdf_writer.pages[0].rotate = 90  # Rotaciona a página (opcional)
        pdf_writer.pages[0].set_text(text)
        pdf_writer.write(file)

# Exemplo de uso
input_file = 'input.pdf'
output_file = 'output.pdf'

translate_pdf(input_file, output_file)
print(f'A tradução foi salva no arquivo "{output_file}".')

'''Certifique-se de substituir 'input.pdf' pelo caminho do arquivo PDF que deseja traduzir e 'output.pdf' pelo caminho onde deseja salvar o arquivo traduzido. O texto traduzido será salvo em um novo arquivo PDF.

Tenha em mente que a tradução será feita usando a API do Google Translate, que tem limitações de uso. Portanto, se você precisar traduzir muitos arquivos ou um texto muito longo, talvez seja necessário considerar outras opções, como usar uma chave de API paga ou outras soluções de tradução.'''







