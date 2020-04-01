from copy import copy

from PyPDF2.generic import RectangleObject
from PyPDF2 import PdfFileWriter, PdfFileReader



def main():
    output = PdfFileWriter()
    input1 = PdfFileReader(open("/Users/odin/Downloads/What-is-Life-By-Erwin-Schrodinger.pdf", "rb"))
    print("document1.pdf has %d pages." % input1.getNumPages())
    page1 = input1.getPage(0)
    page1_copy = copy(page1)

    print(f'size of pdf pages: {page1.mediaBox.getUpperRight_x()} by {page1.mediaBox.getUpperRight_y()}')
    print(f'raw size of pdf pages: {page1.mediaBox}')
    width_trim_1 = 75
    width_trim_2 = 3

    # first_half_split = RectangleObject([60,60,303, 740])

    first_half_split = RectangleObject([width_trim_1,60,306-width_trim_2, 740])

    second_half_split = RectangleObject([306+width_trim_2, 60, 612-width_trim_1, 740])
    page1.mediaBox = first_half_split
    page1_copy.mediaBox = second_half_split


    output.addPage(page1)
    output.addPage(page1_copy)

    output_stream = open("PyPDF2-output.pdf", "wb")
    output.write(output_stream)
    output_stream.close()


if __name__ == '__main__':
    main()