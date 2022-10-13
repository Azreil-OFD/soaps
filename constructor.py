import requests
import xmltodict, json

class Base:
    group_id = "ИС 2.20"
    date = "20.11.2022"
    
    def _validation(self):
        pass
    
    def _converter(self):
        pass
    
    def _cromatter(self):
        pass
    
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
        """.format(self.group_id , self.date).encode()
        headers = {
            "Authorization":"Basic V1NOUEs6V1NOUEs="
        }
        
        res = requests.post('http://m.neftpk.ru/college/ws/Schedule.1cws' , data=xml , headers=headers)
        print(res.text)
        return res.text
        
        
    



class Day:
    
    def __init__(self , data) -> None:
        self.group_id = data['group_id']
        self.date = data['date']
    
    def getData(self):
        return json.dumps( xmltodict.parse(ass.RequestWS()) , indent=50 , separators=(". ", " = ") , ensure_ascii=False)
    
    
    

class Week(Base):
    
    def __init__(self , data) -> None:
        self.group_id = data['group_id']
        self.date = data['date']
    
    def getData(self):
        return  xmltodict.parse(ass.RequestWS() , encoding='utf-8' )


ass = Week({'group_id':"ИС 1.20" ,'date':"13.10.2022"})
ass.RequestWS()