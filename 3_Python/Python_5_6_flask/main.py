from flask import Flask, url_for

app = Flask(__name__)

# decoratore Statico
@app.route('/') # avere solo il percorso e basta restituisce un get
def home() -> str:
    return "<h3>Hello, world!</h3>"

# decoratore Dinamico
@app.route('/user/<string:username>')
def show_user_profile(username:str) -> str:
    return f"Profilo di : {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id:int) -> str:
    return f"Post : {post_id}"

@app.route('/user2/<string:username>/age/<int:age>')
def show_user_profile_2(username:str, age:int) -> str:
    return f"Profilo di : {username} di anni : {age}"

@app.route('/urls/')
def show_urls() -> str:
    return f"<h3>url: {url_for('show_user_profile', username='Lorenzo_Anzivino')} </h3>"


with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='Lorenzo_Anzivino'))
    print(url_for('show_post', post_id=42))
    print(url_for('show_user_profile_2', username='Marco_Anzivino', age=35))


# Sempre a fine codice
app.run(debug=True, host='127.0.0.1', port=5000)
# in production, set debug to false

# Tipi da inserire come argomento della funzione <argomento>
    # string
    # int
    # float
    # path
    # uuid

# url_for('nome della funzione') - evita di scrivere tutto il path
# importare url_for sull'import