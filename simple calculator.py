from flask import Flask,request,jsonify

app = Flask(__name__)          #initial base class for flask,it is always on 2nd line

@app.route("/",methods=['GET'])                 #home page url
def home_page():
    return "home page"

@app.route("/math",methods=['POST'])
def math():
    if request.method=='POST':
        operation = request.json['operation']  #we will use []brackets as dictionary objects are not collable.
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])

        if operation=='add':
            r=num1+num2
            result="the sum is " +str(r)

        if operation=='subtraction':
            r=num1-num2
            result="the difference is " +str(r)

        if operation=='mul':
            r=num1*num2
            result="the multiplication is " +str(r)

        if operation=='divide':
            r=num1/num2
            result="the division is " +str(r)

    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)

