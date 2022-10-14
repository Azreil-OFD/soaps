#!flask/bin/python

from urllib import response
import json
from flask import Flask, request

import constructor 

app = Flask(__name__)

@app.route('/schedule' , methods = ['GET'] )
def emptySchedule():
    return [{"hello":"world"}]

@app.route('/schedule/<string:group_id>/<string:data>/' , methods = ['GET'] )
def schedule(group_id,data):
    print(request.args.getlist('week'))
    if (request.args.getlist('day') == ['']):
        
        answer = constructor.Day({"group_id": group_id, "date":data})
        return answer.getData()['soap:Envelope']['soap:Body']['m:OperationResponse']['m:return']['m:Tab']
    
    elif (request.args.getlist('week') == ['']):
        answer = constructor.Week({"group_id": group_id, "date":data})
        return answer.getData()['soap:Envelope']['soap:Body']['m:OperationResponse']['m:return']['m:Tab']
    
    
    return {'error':'xz'}


@app.route('/schedule/<string:group_id>/<string:data>/week' , methods = ['GET'] )
def scheduleWeek(group_id,data): 
    answer = constructor.Week({"group_id": group_id, "date":data})
    return answer.getData()['soap:Envelope']['soap:Body']['m:OperationResponse']['m:return']['m:Tab']

@app.route('/schedule/<string:group_id>/<string:data>/day' , methods = ['GET'] )
def scheduleDay(group_id,data):
    answer = constructor.Day({"group_id": group_id, "date":data})
    return answer.getData()

if __name__ == '__main__':
    app.run(debug=True)