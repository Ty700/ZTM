import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)

    write = PyPDF2.PdfFileWriter()
    write.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        write.write(new_file)
    