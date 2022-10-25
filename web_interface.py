from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY'] ='6LeBCfIZAAAAAO39_L4Gd7f6uCM0PfP_N3XjHxkW'
app.config['RECAPTCHA_PRIVATE_KEY'] ='6LeBCfIZAAAAAJTjq0Xz_ndAW9LByCo1nJJKy'
app.config['RECAPTCHA_OPTIONS'] = {'theme':'black'}


@app.route('/')
def signup():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def signup_post():
    print(111)
    ip = request.files['ip']
    proxy = request.files['proxy']
    octet = request.form.get('octet_count')
    speed_check = request.form.getlist('speed')
    ipv_6_check = request.form.getlist('ipv6')
    proxy = str(proxy.read())[2:-1].split(r'\n')
    if proxy[-1] == '':
        proxy = proxy[:-1]
    ip = str(ip.read())[2:-1].split(r'\n')
    if ip[:-1] == '':
        ip = ip[:-1]
    if speed_check==[]:
        speed_check = False
    else:
        speed_check = True
        
    if ipv_6_check==[]:
        ipv_6_check = False
    else:
        ipv_6_check = True
    print(octet, speed_check, ipv_6_check)
        
    return redirect(url_for('signup'))


app.secret_key = 'some_secret_key'
if __name__ == "__main__":
    app.run(debug=True)
