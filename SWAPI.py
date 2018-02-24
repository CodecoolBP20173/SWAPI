from flask import Flask, render_template, url_for, redirect, request, session
import data_manager

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = data_manager.check_user(request.form['register_user_name'])
        if len(user) == 0:

            password = data_manager.hash_password(request.form['register_password'])

            login_name = request.form['register_user_name']
            print("registered")
            data_manager.register(login_name, password)

            return redirect(url_for('route_main', already_used=False))
        else:
            return redirect(url_for('register', already_used=True))
    return render_template('register.html', already_used=False)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']

        data = data_manager.login(user_name)
        if not data:
            return redirect(url_for('route_main',log=False))
        user_id = data_manager.get_id_by_user_name(user_name)['user_id']
        session['user_name'] = user_name
        session['user_id'] = user_id

        log = data_manager.verify_password(request.form.to_dict()['password'], data[0]['user_password'])
        if log:

            return redirect(url_for('route_main'))
        else:
            session.pop('user_name', None)
            session.pop('user_id', None)
            log = False
            return redirect(url_for('route_main', log=False))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_name',None)
    return redirect(url_for('route_main'))

if __name__ == '__main__':
    app.run()

