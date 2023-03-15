from flask import Flask,render_template,request
from app.utils import prediction

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def start():
    return render_template("concrete.html")

@app.route("/strength",methods=["POST","GET"])
def strength():
    data=request.form
    pred_obj=prediction()
    predicted_cs=pred_obj.predict_strength(data)
    print(predicted_cs)

    return(predicted_cs)

if __name__=="__main__":
    app.run( host="0.0.0.0", port=8000, debug=False)
    

