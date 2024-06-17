from flask import Flask, render_template, request
from main import main
from api import get_categories

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    access_token = "616MeuZTOLGUUfhh4S7PB39h7T0L3iRLZAYiL1pu"  # Token real aqui
    category_id = request.args.get('category_id')  # Pega o category_id do formulário
    projection, categories = main(category_id, access_token)
    return render_template('dashboard.html', projection=projection, categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
