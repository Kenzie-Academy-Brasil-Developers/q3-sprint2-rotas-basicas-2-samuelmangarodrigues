from flask import Flask
from datetime import datetime
from os import getenv


app=Flask(__name__)

@app.get("/")
def home():
    return {'data':'Hello Flask'}


@app.get('/date')
def date():
    morning=getenv('morning')
    afternoon=getenv('afternoon')
    message=''
    date=datetime.now()
    date_complete=date.strftime('%d/%m/%Y %H:%M:%S')
    date_time=date.strftime('%p')
    if date_time=='PM':
        message=afternoon
    else:
        message=morning
        return message    
    return {'current_datetime':f'{date_complete} {date_time}',
            'message':message
            }