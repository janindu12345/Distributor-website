from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jjsbandara@gmail.com'  # 🔁 Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'mjjs whfi cefy lxpl'  # 🔁 Replace with your Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'jjsbandara@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    shop = request.form['shop']
    location = request.form['location']
    phone = request.form['phone']
    instructions = request.form.get('instructions', '')

    # Fetch product names and quantities from the array inputs
    product_names = request.form.getlist('product_name[]')
    product_qtys = request.form.getlist('product_qty[]')

    # Build a formatted product list string
    product_lines = [
        f"{p_name} - {qty} pcs" 
        for p_name, qty in zip(product_names, product_qtys)
    ]
    products = "\n".join(product_lines)

    msg_body = f"""
    🧾 New Order Received

    Full Name: {name}
    Shop Name: {shop}
    Location: {location}
    Mobile Number: {phone}
    
  
    Products Needed:
    {instructions}
    """

    msg = Message(
        subject='🛒 New Order from Janindu Distributor Website',
        recipients=['jjsbandara@gmail.com'],  # 🔁 Replace with your destination email
        body=msg_body
    )

    mail.send(msg)
    return '✅ Order submitted successfully!'

if __name__ == '__main__':

    app.run(debug=False,host='0.0.0.0')
