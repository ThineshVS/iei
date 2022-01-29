import numpy
import serial
import requests
import json
import gspread
from datetime import date
import sys
import os
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
from matplotlib.pyplot import cm


def doc_g(list):
    # os.chdir(sys.path[0])
    sys.path[0]
    doc = DocxTemplate('template.docx')
    if list[-2] == "yellow":
        placeholder_1 = InlineImage(
            doc, 'Placeholders/yellow.png', Cm(1))
    elif list[-2] == "red":
        placeholder_1 = InlineImage(
            doc, 'Placeholders/red.png', Cm(1))
    elif list[-2] == "green":

        placeholder_1 = InlineImage(
            doc, 'Placeholders/green.png', Cm(1))
    # placeholder_2 = InlineImage(doc, 'Placeholders/Placeholder_1.png', Cm(1))

    context = {'placeholder_1':  placeholder_1,
               'id': list[0],
               'date': list[1],
               'question1': list[2],
               'question2': list[3],
               'question3': list[4],
               'question4': list[5],
               'question5': list[6],
               'question6': list[7],
               'question7': list[8],
               'question8': list[9],
               'code': list[-2],
               'temp': list[-1],
               }
    doc.render(context)
    doc_name = str(list[0]) + ".docx"
    doc.save(doc_name)


def id_increment(idstr):
    # here pass the I'd as a string
    new_id = int(idstr, 36) + 1
    return (str(numpy.base_repr(new_id, 36)))


def main(ref):

    loc_client_sec_json = r'F:/projects/xiona/xiona-339619-31dd05f6148a.json'
    gc = gspread.service_account(filename=loc_client_sec_json)
    sheet_name = "book"
    sh = gc.open(sheet_name)
    worksheet = sh.sheet1

  # First we have to make the ans suitable to upload
  # we have to get a ID for it
  # we will get ID from the last row and increment it
    while True:

      # getting the last row value
        values = worksheet.get_all_values()
   # print(values[0])
        for i in range(len(values)):
            if values[i][0] == str(ref):
                print(values[i])
                doc_g(values[i])
        # noofrows = len(values)
                return values[i]


# last_id = str(values[noofrows - 1][0])
# last_id = id_increment(last_id)
# print(last_id)
######
