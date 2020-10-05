from flask import Flask,render_template,request,redirect,jsonify
import json
import requests
app = Flask(__name__)
s=""
j = {"data":""}
@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "GET":

        return render_template("index.html")
    else:
        
        x=request.form.get("creditscore")
        s=str(x)
        x=request.form.get("geography")
        s=s+","+str(x)
        x=request.form.get("gender")
        s=s+","+str(x)
        x=request.form.get("age")
        s=s+","+str(x)
        x=request.form.get("tenure")
        s=s+","+str(x)
        x=request.form.get("balance")
        s=s+","+str(x)
        x=request.form.get("noofpro")
        s=s+","+str(x)
        x=request.form.get("hascredit")
        s=s+","+str(x)
        x=request.form.get("activemember")
        s=s+","+str(x)
        x=request.form.get("salary")
        s=s+","+str(x)
        
        print(s)
        j={"data":s}
        print(type(j))
        print(j)
        
        
        j = json.dumps(j, indent = 4)
        r = requests.post(
            'https://fuhejtpfta.execute-api.us-east-1.amazonaws.com/finalstage/churn',
            data=j)
        if r.text == '1':
            res = "Yes"
        else:
            res = "No"
        print(r.text)
        return render_template("result.html",res=res)
        


if __name__ == '__main__':
    app.run(debug=True)