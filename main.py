import requests
from io import BytesIO
from zipfile import ZipFile
from document import changeXml
from flask import Flask
# Zip FILE (binary)
import urllib.request

app=Flask(__name__)
@app.route("/analyze/**")
def inFunc():
    url = 'https://opendart.fss.or.kr/api/document.xml'
    params = {
        'crtfc_key': 'ad6f9c22dce2659dc20fd6d1e4ebb28f03e6e8e9',
        'rcept_no': '20210429800649'
    }

    res = requests.get(url, params)

    with ZipFile(BytesIO(res.content)) as zipfile:
        return zipfile.extractall('document/')
#
# rcept_no=input()
# inFunc(rcept_no)
# changeXml.change()

if __name__=='__main__':
    app.run(debug=False,host="3.37.167.84",port=80)