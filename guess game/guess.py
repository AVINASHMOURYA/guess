from flask import Flask,render_template,request
import random as rd
i = 0
generate_n = 0
value1=0
value2=0
app = Flask(__name__)

# value1 = int(input("enter starting number"))
# value2 = int(input("enter ending number"))
# genrate_n = rd.randint(value1,value2)
@app.route('/')
def index():
    return render_template("index.html",start=False)
@app.route('/game',methods=['GET','POST'])
def guessing():
    global i,generate_n,value1,value2
    loop_val = 0
    if(request.method=="POST"):
        if(i==0):
            value1 = int(request.form.get("start"))
            value2 = int( request.form.get("end")) 
            generate_n = rd.randint(value1,value2)
            i+=1
        elif(request.form.get('Play again')=='Play again'):
            i=0
        if(request.form.get('Play guess')=='Play guess'):
            geuss_n = int(request.form.get("guess"))
        # over = request.form.get("guess")
            if(geuss_n==generate_n):
                # print("your geussed number is correct")
                loop_val = 1
            elif(geuss_n>generate_n):
                loop_val = 2
                # print("less than your geuss number")
            elif(geuss_n<generate_n):
                loop_val = 3
        # print("grater than your geuss number")
        return render_template("index.html",val1=value1,val2=value2,con=i,val=loop_val,start=True)
        # print((request.method=="POST")
    else:
        return render_template("index.html",start=True,con=i)
if __name__=="__main__":
    app.run(debug=True)
    


