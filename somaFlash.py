from flask import Flask,request, jsonify

app = Flask(__name__)

@app.get("/somar")

def somar():
    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))
    return jsonify({"resultado": a + b})

@app.get("/subtrair")
def subtrair():
    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))
    return jsonify({"resultado": a - b})    

if __name__ ==  "__main__":
    app.run(port=5000)