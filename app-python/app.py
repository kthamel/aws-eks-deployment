from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def function_flask():
    if(request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)

else:
    print(f"Something went wrong!!!")
