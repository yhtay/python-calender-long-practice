from flask import (Blueprint, render_template)
import sqlite3
from datetime import datetime
import os


bp = Blueprint("main", __name__, url_prefix="/")

DB_FILE = os.environ.get("DB_FILE")

@bp.route("/")
def main():
    with sqlite3.connect(DB_FILE) as conn:
        curs = conn.cursor()
        curs.execute('''SELECT id, name, start_datetime, end_datetime
            FROM appointments
            ORDER BY start_datetime;''')
        rows = curs.fetchall()
        # print(rows)
        rows2 = []
        for appt in rows: # [(1, 'My appointment', '«DATE» 14:00:00', '«DATE» 15:00:00')]
            # print(appt) # (1, 'My appointment', '«DATE» 14:00:00', '«DATE» 15:00:00')
            start_date = appt[2]
            end_date = appt[3]
            startdate_obj = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
            # print("start date obj: ", startdate_obj)
            enddate_obj = datetime.strptime(end_date,'%Y-%m-%d %H:%M:%S')
            startdate_obj.strftime("%H:%M")
            # print('strftime: ', startdate_obj.strftime("%H:%M"))
            enddate_obj.strftime("%H:%M")
            
    return render_template("main.html", rows=rows)
