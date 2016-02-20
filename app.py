from flask import Flask,render_template,request,url_for,jsonify,json
import unirest
import math
import numpy
app = Flask(__name__)

@app.route('/<company>/<selected_date>',methods=['GET'])
def get_stock_by_date(company,selected_date):
    url='data/'+company+'.json'
    with open (url) as f:
        data = json.loads(f.read())
    dict={}
    dict['graph_plot']=plotgraph()
    for i in data:
        if i["Date"]==selected_date:
            dict["stock_details"]=i
            return jsonify(dict)
    return "date related data not found"

@app.route('/<company>/<float:opening_price>',methods=['GET'])
def predict(company,opening_price):
    estimate=predict_closing_price(company,opening_price)
    #estimate=json.dumps(estimate)
    return jsonify(estimate)

def predict_closing_price(company,opening_price):
    url='data/'+company+'.json'
    with open (url) as f:
        data = json.loads(f.read())
    n=[]
    for i in range(0,len(data)-1):
        p=math.log(float(data[i+1]['Open'])/float(data[i]['Open']))
        n.append(p)
    avg=numpy.mean(n)
    variance=numpy.var(n)
    delta=float(1.00000000000/(len(n)-1))
    volatility_sigma=math.sqrt(variance/delta)
    drift_mu=((avg+(variance/2))/delta)
    estimate=opening_price*(math.exp(drift_mu*delta))
    dict={}
    dict['closing_price']=estimate
    dict['percentage_error']=(((float(data[0]['Close'])-estimate)/float(data[0]['Close']))*100)
    return dict

#@app.route('/plotgraph',methods=['GET'])
def plotgraph():
    with open ('data/wipro.json') as f:
        data = json.loads(f.read())
    opening_prices=[]
    for i in range(0,220):
        dict={}
        dict["open_price"]=data[i]["Open"]
        dict["date"]=data[i]["Date"]
        opening_prices.append(dict)
    return opening_prices

@app.route('/plotgraph',methods=['GET'])
def plotgraph_():
    with open ('data/wipro.json') as f:
        data = json.loads(f.read())
    opening_prices=[]
    for i in range(0,220):
        dict={}
        dict["open_price"]=data[i]["Open"]
        dict["date"]=data[i]["Date"]
        opening_prices.append(dict)
    opening_prices=json.dumps(opening_prices)
    return opening_prices


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
