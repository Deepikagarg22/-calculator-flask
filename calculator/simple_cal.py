from flask import Flask

app = Flask(__name__)        #initial base class for flask,it is always on 2nd line

@app.route("/",methods=['GET','POST'])  #home page url
def home_page():
    return "home page"

@app.route("/math",methods=['POST'])
def math():
    if (request.method=='POST'):
        operation=request.json["operation"]    #we will use []brackets as dictionary objects are not collable.
        num1=int(request.json["num1"])
        num2=int(request.json["num2"])

        if operation=='add':
            r=num1 + num2
            result = "the sum is " + str(r)
            return jsonify(result)

        if operation=='sub':
            r=num1 - num2
            result = "the difference is " + str(r)
            return jsonify(result)

        if operation=='mul':
            r=num1 * num2
            result = "the multiplication is " + str(r)
            return jsonify(result)

        if operation=='divide':
            r=num1 / num2
            result = "the division is " + str(r)
            return jsonify(result)

        return jsonify(result)

if __name__=='__main__':
    app.run(debug=True)



