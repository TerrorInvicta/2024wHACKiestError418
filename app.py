from flask import Flask, render_template
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sa123"
)

app = Flask(__name__)
clubname="ieee"

# Database connection function
def get_events(club):
    cursorObject = mydb.cursor()
    cursorObject.execute("use clubs")
    cursorObject.execute(f"select * from {club} ")
    table=cursorObject.fetchall()
    j=table[0]
    d=[{"name":j[1],"date":j[2],"time":j[3],"organiser":j[4]}]
    return d
    

@app.route('/')
def club_buttons():
    return render_template('club_buttons.html')


@app.route('/events/<clubname>')
def Events(clubname):
    EVENTS = get_events(clubname)  # Fetch events from the database
    
    return render_template('events.html', events=EVENTS)



if __name__ == '__main__':
    app.run(debug=True)