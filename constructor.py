import datetime
import requests
import xmltodict
import json


class Base:
    group_id = "ИС 2.20"
    date = "20.11.2022"
    weekdays = {
        0:'Понедельник',
        1:'Вторник',
        2:'Среда',
        3:'Четверг',
        4:'Пятница',
        5:'Суббота',
        6:'Воскресенье'
    }


    def RequestWS(self):
        xml = """
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:sch="http://www.neftpk.ru/Schedule">
            <soap:Header/>
            <soap:Body>
                <sch:Operation>
                    <sch:ID_GROUP>{0}</sch:ID_GROUP>
                    <sch:Date>{1}</sch:Date>
                </sch:Operation>
            </soap:Body>
        </soap:Envelope>
        """.format(self.group_id, self.date).encode()
        headers = {
            "Authorization": "Basic V1NOUEs6V1NOUEs="
        }

        res = requests.post(
            'http://m.neftpk.ru/college/ws/Schedule.1cws', data=xml, headers=headers)
        return res.text


class Day(Base):
    

    def __init__(self, data : set) -> None:
        self.group_id   = data['group_id']
        self.date       = data['date']


    def _formatter(self , day):
        date = datetime.datetime.strptime(self.date, '%d.%m.%Y')
        
        return {
            'weekday': f"{self.weekdays[date.weekday()]}",
            'data' : day,
            'request': {
                'group_id':self.group_id,
                'date':self.date
                }
        }

    def getData(self):
        day = []
        
        data = xmltodict.parse(self.RequestWS(), encoding='utf-8') ['soap:Envelope']['soap:Body']['m:OperationResponse']['m:return']['m:Tab']
        for i in data:
            if i['m:UF_DATE'] == self.date + ' 0:00:00':
                day.append(i)
        return self._formatter(day)


class Week(Base):

    def __init__(self, data) -> None:
        self.group_id = data['group_id']
        self.date = data['date']


    def getData(self):
        return xmltodict.parse(self.RequestWS(), encoding='utf-8')


