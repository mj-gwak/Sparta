from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_review():
    # title_receive로 클라이언트가 준 000 가져오기
    ordername_receive = request.form['ordername_give']
    orderquantity_receive = request.form['orderquantity_give']
    orderduration_receive = request.form['orderduration_give']
    ordercategory_receive = request.form['ordercategory_give']
    orderphoneno_receive = request.form['orderphoneno_give']

    # DB에 삽입할 order 만들기
    order = {
        'order_name' : ordername_receive,
        'order_quantity' : orderquantity_receive,
        'order_duration' : orderduration_receive,
        'order_category' : ordercategory_receive,
        'order_phoneno' : orderphoneno_receive
    }

    # review에 review 저장하기
    db.orders.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result':'success', 'msg': '예약이 성공적으로 작성되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

