from flask import Flask, render_template, request, redirect
import datetime
import csv

app = Flask(__name__)

def write_to_csv(data):
    with open('database.csv', mode='a') as database:
        email = data['email']
        subject = data['subject']
        subject = data['message']
        time = (datetime.datetime.now().strftime('%d/%m/%Y'))

        csv_write = csv.writer(database, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_write.writerow([email,subject,subject,time])

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<page_name>')
def render_page(page_name='/index.html'):    
    return render_template(page_name)
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return f'Did not save to DB' 
    else:
        return 'Something went wrong'