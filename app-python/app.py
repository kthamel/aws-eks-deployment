from flask import Flask, jsonify, request
import psutil

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def function_flask():
    if(request.method == 'GET'):
        name = int(psutil.virtual_memory().used / (1024 ** 2))
        content = (f"Used Memory is {name} MB")
        return jsonify(content)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)

else:
    print(f"Something went wrong!!!")
