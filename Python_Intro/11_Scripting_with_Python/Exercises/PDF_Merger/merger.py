#############################################################
# Usage:                                                    #
#   Adds a watermark to every page in a pdf                 #
#                                                           #
# How to use:                                               #
#   Argument 1: Folder path containing the pdf to watermark #
#   Argument 2: Folder path containing watermark pdf        #
#   Argument 3: Folder path and name of output file         #
#       Note: Relative paths                                #
#                                                           #
#   Example:                                                #
#       python3 merger.py super.pdf wtr.pdf output/file.pdf #
#                                                           #
#############################################################
import PyPDF2
import sys
import os

def main(base_pdf_path, stamp_pdf_path, output_name):
    base_pdf = PyPDF2.PdfFileReader(open(base_pdf_path, 'rb'))
    stamp_pdf = PyPDF2.PdfFileReader(open(stamp_pdf_path, 'rb'))
    output_pdf = PyPDF2.PdfFileWriter()

    for index in range(base_pdf.getNumPages()):
        page = base_pdf.getPage(index)
        page.mergePage(stamp_pdf.getPage(0))
        output_pdf.addPage(page)

    with open(output_name, 'wb') as outfile:
        output_pdf.write(outfile)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage Error: python3 merger.py <path/to/pdf>.pdf <path/to/watermark/pdf>.pdf <output_name>.pdf")
    else:
        base_pdf_path, stamp_pdf_path, output_name, *others = sys.argv[1:]

        pdf_list = [base_pdf_path, stamp_pdf_path, output_name]

        # Standardizes files and paths
        for index, pdf in enumerate(pdf_list):
            if not pdf.startswith('./'):
                pdf_list[index] = './' + pdf_list[index]
            
            if not pdf.endswith('.pdf'):
                pdf_list[index] = pdf_list[index] + '.pdf'

        if not os.path.isfile(pdf_list[0]):
            print(f'Path Error: {pdf_list[0]} is not a file')
        elif not os.path.isfile(pdf_list[1]):
            print(f'Path Error: {pdf_list[1]} is not a file')
        else:
            # Builds file path to place output file if not there already
            path_len = output_name.rfind('/')
            output_path = output_name[:path_len]

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            main(pdf_list[0], pdf_list[1], pdf_list[2])

