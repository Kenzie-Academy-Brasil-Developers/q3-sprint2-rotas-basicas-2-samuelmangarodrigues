from flask import Flask
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

@app.get("/")
def home():
    return {'data':'Hello Flask!'}


@app.get('/current_datetime')
def date():

    message=''
    date=datetime.now()

    date_complete=date.strftime('%d/%m/%Y %I:%M:%S %p')
    date_hour=int(date.strftime('%H'))


    if date_hour < 12:
        message='Bom dia!'
    elif date_hour< 18: 
        message='Boa tarde!'
    else:
        message='Boa noite!'  

    return {'current_datetime':f'{date_complete}',
            'message':message
            }