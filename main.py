from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# IN TERMINAL (ctrl + `) TYPE THE FOLLOWING: 
# pip install flask
# pip install flask_sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shoppinglist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ShoppingItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  quantity = db.Column(db.Integer, default=1)

  def __repr__(self):
    return f'<ShoppingItem {self.name}>'


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    item_name = request.form['name']
    item_quantity = request.form.get('quantity', 1)
    new_item = ShoppingItem(name=item_name, quantity=item_quantity)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

  items = ShoppingItem.query.all()
  return render_template('index.html', items=items)


@app.route('/delete/<int:item_id>')
def delete_item(item_id):
  item = ShoppingItem.query.get(item_id)
  if item:
    db.session.delete(item)
    db.session.commit()
  return redirect(url_for('index'))


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(host='0.0.0.0', port=5421, debug=True)
