from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def tax():
    if request.method=="POST":    
        return redirect(url_for("result"))
    else:
        return render_template("tax.html")

@app.route("/result",methods=["POST","GET"])
def result():
    taxable_amt=int(request.form['taxable_amt'])

    if taxable_amt>0:
        tax_class=1
    if taxable_amt>250000:
        tax_class=2
    if taxable_amt>500000:
        tax_class=3
    if taxable_amt>1000000:
        tax_class=4
    
    if tax_class==1:
        tax=0
    elif tax_class==2:
        tax=5*(taxable_amt-250000)/100
    elif tax_class==3:
        tax=12500+20*(taxable_amt-500000)/100
    elif tax_class==4:
        tax=12500+100000+30*(taxable_amt-1000000)/100
    data={
        'taxable_amt':taxable_amt,
        'tax':tax
    }
    print(data)
    return render_template("result.html",data=data)     

if __name__=="__main__":
    app.run()