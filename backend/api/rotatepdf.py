
import PyPDF2
from flask.wrappers import Request
from flask import request , session
from api.reply import Response
from flask_restful import reqparse, Resource
import time
import hashlib
import json
import time
from datetime import datetime
import time
from flask import session, request
import os
from pathlib import Path
# from flask.config import Config
# from api.transfertos3 import img_to_url
m=hashlib.sha256()


#parsing the request data coming from the client side
login_post_arguments = reqparse.RequestParser()
login_post_arguments.add_argument('path', type=str, help='password is not there', required=False)
login_post_arguments.add_argument('page_list', type=dict, help='password is not there', required=False)

class Rotate_PDF(Resource):
    def post(self) :
        req_data = login_post_arguments.parse_args()
        list_data = req_data['page_list']
        path = req_data['path']
        print(list_data)
        final_file_path = rotate_pdf(path , list_data)
        return Response(body={'final_pdf_path' : final_file_path} , message="Fine" , status="sucds").json() , 200





def rotate_pdf(path , page_list) :

    pdf_in = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        if str(pagenum) in page_list.keys() : 
            page.rotateClockwise(page_list[str(pagenum)])
        pdf_writer.addPage(page)
    print(pdf_in.name)
    in_name = Path(pdf_in.name).stem
    name = pdf_in.name
    while name[len(name)-1] !='/' : 
        name = name[:-1]
        
    pdf_out = open('c:/Users/Abhishek/OneDrive/Desktop/image upload project/backend/api/'+'pdfs/'+in_name+'rotated3.pdf', 'wb')
    pdf_writer.write(pdf_out)
    final_file_path = os.path.realpath(pdf_out.name)
    pdf_out.close()
    pdf_in.close()
    return final_file_path