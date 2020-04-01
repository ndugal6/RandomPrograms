from copy import copy

from PyPDF2.generic import RectangleObject
from PyPDF2 import PdfFileWriter, PdfFileReader



def main():
    output = PdfFileWriter()
    input1 = PdfFileReader(open("/Users/odin/Downloads/What-is-Life-By-Erwin-Schrodinger.pdf", "rb"))
    print("document1.pdf has %d pages." % input1.getNumPages())
    page1 = input1.getPage(0)
    print(f'raw size of pdf pages: {page1.mediaBox}')

    width_trim_1 = 75
    width_trim_2 = 3
    top_trim = 52
    bottom_trim = 60
    first_half_split = RectangleObject([width_trim_1, bottom_trim, 306 - width_trim_2, 792 - top_trim])
    second_half_split = RectangleObject([306 + width_trim_2, bottom_trim, 612 - width_trim_1, 792 - top_trim])

    for page_num in range(0,input1.getNumPages()):
        p = input1.getPage(page_num)
        p_copy = copy(p)
        p.mediaBox = first_half_split
        p_copy.mediaBox = second_half_split
        output.addPage(p)
        output.addPage(p_copy)

    output_stream = open("pdf_to_text_output.pdf", "wb")
    output.write(output_stream)
    output_stream.close()

if __name__ == '__main__':
    main()