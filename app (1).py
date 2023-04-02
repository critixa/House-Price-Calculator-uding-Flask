from flask import Flask, request, render_template
import mysql.connector
app = Flask(__name__)
l=[]
from content import pickle
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def main():
    return render_template("login.html")


@app.route("/login",methods=['post'])
def login():
    nam=request.form["username"]
    pas=request.form["pswrd"]

    conn=mysql.connector.connect(user="root",host="localhost",password="Sriksrik1*@",database="pythonlogin")
    cursor=conn.cursor()
    if conn.is_connected():
           print("Connected")

    cursor.execute('SELECT * FROM users WHERE name=%s and password=%s',(nam,pas))
    print("Done")
    rows=cursor.fetchone()
    if rows:
     return render_template("index.html")
    else:
        error="Invalid Username or Password"
        return render_template("login.html",error=error)

@app.route("/predict",methods=["post"])
def predict():
    LotArea=request.form["LotArea"]
    Overallcondition=request.form["Overall condition"]
    Yearbuilt=request.form["Year built"]
    Yearremodified=request.form["Year remodified"]
    
    try:
        features = [float(i) for i in (request.form.values())]
        pred = model.predict([features])
        print(pred)
        return render_template("success.html",
                           users=1)
        l=model.recommend(features)
        print(l)
        return render_template("pred.html",users=l)
    except:
        return render_template("index.html",err="Check the spelling or try another book")


if __name__=='__main__':
    app.run(host='localhost',port=5000, debug=True)
    
    
    
    
    
    
    
    