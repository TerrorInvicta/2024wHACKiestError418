from flask import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sa123"
)

app = Flask(__name__)
global clubname
clubname="ieee"

# Database connection function
def get_events(club):
    cursorObject = mydb.cursor(dictionary=True)
    cursorObject.execute("use clubs")
    cursorObject.execute(f"select * from {club} ")
    table=cursorObject.fetchall()
    j=table[::-1]
    
    return j

def put_event(c,n,d,t,l,o):
    cur=mydb.cursor()
    #For tables names there isnt really an easy way to use f-strings to replace them, cuz of the apostrophes :(
    if(c.lower()=="coderit"):
        cur.execute("insert into coderit (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()
    elif(c.lower()=="debsoc"):
        cur.execute("insert into debsoc (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()
    elif(c.lower()=="ieee"):
        cur.execute("insert into ieee (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()
    elif(c.lower()=="munsoc"):
        cur.execute("insert into munsoc (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()
    elif(c.lower()=="studiorit"):
        cur.execute("insert into studiorit (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()
    elif(c.lower()=="tedxmsrit"):
        cur.execute("insert into tedxmsrit (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()
    elif(c.lower()=="theatrix"):
        cur.execute("insert into theatrix (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()
    elif(c.lower()=="tnt"):
        cur.execute("insert into tnt (name,date,time,organiser,location) values (%s,%s,%s,%s,%s)",(n,d,t,o,l))
        mydb.commit()


    

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clubbuttons')
def club_buttons():
    return render_template('club_buttons.html')


@app.route('/events/<clubname>')
def Events(clubname):
    EVENTS = get_events(clubname)  # Fetch events from the database
    
    return render_template('events.html', events=EVENTS)

# Route for rendering the sign-in form (GET request)
@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('sign_in_page.html')  # Render the sign-in HTML form

# Route for handling the form submission (POST request)
@app.route('/signinform', methods=['POST'])
def signin():
    admin_name = request.form['admin_name']
    password = request.form['password']
    
    # Example validation (just a simple check for illustration)
    if admin_name == 'admin' and password == 'password123':
        return redirect(url_for('success'))  # Redirect to a success page
    else:
        return "Invalid credentials", 400  # Handle invalid credentials

# A simple success page after successful login
@app.route('/success')
def success():
    return render_template('input_event.html')


@app.route('/add_event', methods=['POST'])
def add_event():
    if request.method == 'POST':
        event_name = request.form['event_name']
        event_date = request.form['event_date']
        event_time = request.form['event_time']
        event_location = request.form['event_location']
        event_organizer = request.form['event_organizer']
        club=request.form['event_club']
        
        put_event(club,event_name,event_date,event_time,event_location,event_organizer)

        
        
        
    return redirect(url_for('club_buttons'))

    


    



if __name__ == '__main__':
    app.run(debug=True)