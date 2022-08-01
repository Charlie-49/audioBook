import PyPDF2

pdf_document = open("Book.pdf", "rb")
pdf_document_read = PyPDF2.PdfFileReader(pdf_document)
number_of_pages = pdf_document_read.numPages


for page in range(1, number_of_pages):
    one_page = pdf_document_read.getPage(page)
    raw_text = one_page.extractText()
    from googletrans import Translator

    translator = Translator()
    translated = translator.translate(raw_text, dest='uk')
    translated_2 = translated.text
    import gtts
    from playsound import playsound

    tts = gtts.gTTS(translated_2, lang="uk")
    tts.save("text.mp3")
    playsound("text.mp3")
