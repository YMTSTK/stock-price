from flask import Flask,request,jsonify
import numpy as np
import pickle
from sklearn import preprocessing

model = pickle.load(open('stock.pkl','rb'))

app = Flask(__name__)


@app.route('/stock',methods=['POST'])
def stock_price():

    open=request.form.get('open')
    high=request.form.get('high')
    low=request.form.get('low')
    volume=request.form.get('volume')
    stock=request.form.get('stock')

    list=[open,high,low,volume,stock]

    result = model.predict([list])[0]

    return jsonify({'error':'false','result': str(result),'message':'Success'})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
