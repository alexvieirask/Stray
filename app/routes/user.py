''' Importações das configurações '''
from services.config import *

''' Importações dos formulários '''
from forms.register import RegisterForm
from forms.login import LoginForm

''' Rota: [ user_register_route ]
    descrição: 
'''
@app.route("/user/register", methods = ["GET","POST"])
def user_register_route():
    form_register = RegisterForm(request.form)

    if request.method == 'POST' and form_register.validate():
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        User.register_form(
            name = name,
            username = username,
            email = email,
            password = password
        )
        
        return redirect(url_for('home_route'))

    return render_template('pages/register.html', form= form_register , title = 'User Register')

''' Rota: [ user_login_route ]
    descrição: 
'''
@app.route("/user/login", methods = ['GET', 'POST'])
def user_login_route():
    form_login = LoginForm(request.form)
    
    if request.method == 'POST' and form_login.validate():
        username = request.form['username']
        password = request.form['password']
        hash_password = generate_password_hash(password)
        
        user = User.query.filter_by(username = username, password = hash_password).first()

        if user != None:
            access_token = create_access_token(identity=username)
            return redirect(url_for('home_route'))
        else:
            return redirect('https://http.cat/401')
    
    return render_template('pages/login.html',form=form_login, title = 'User Login' )