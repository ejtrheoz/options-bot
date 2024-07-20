import sqlite3
from datetime import datetime

def new_record(worker, amount, part, service, currency):
   conn = sqlite3.connect("rating.db")
   cursor = conn.cursor()
   
   date = datetime.now()
   date = date.strftime("%Y-%m-%d")


   cursor.execute("""
                  INSERT INTO workers (worker, amount, part, service, date, currency) VALUES (?, ?, ?, ?, ?, ?)
""", (worker, amount, part, service, date, currency ))

   conn.commit()

   cursor.close()
   conn.close()


def get_global_top():


   conn = sqlite3.connect("rating.db")
   cursor = conn.cursor()

   cursor.execute("""
                  SELECT worker, 
                         COUNT(worker),
                         SUM(amount),
                         DENSE_RANK() OVER(ORDER BY SUM(amount) DESC) 
                  FROM workers
                  GROUP BY worker
                  """)

   data = cursor.fetchall()

   cursor.close()
   conn.close()

   return data



def get_stat_per_user(name):
   conn = sqlite3.connect("rating.db")
   cursor = conn.cursor()


   date = datetime.now()
   date = date.strftime("%Y-%m-%d")

   cursor.execute("""
                     WITH now_date AS (
                     SELECT ? AS date_today
                     ),
                     total AS (
                     SELECT worker, SUM(amount), COUNT(worker)
                     FROM workers
                     WHERE worker = ?
                     GROUP BY worker
                     ),
                     month AS (
                     SELECT worker, SUM(amount)
                     FROM workers
                     JOIN now_date
                     WHERE worker = ? AND julianday(date) - julianday(date_today) <= 30
                     GROUP BY worker
                     ),
                     week AS (
                     SELECT worker, SUM(amount)
                     FROM workers
                     JOIN now_date
                     WHERE worker = ? AND julianday(date) - julianday(date_today) <= 7
                     GROUP BY worker
                     ),
                     work_profits AS (
                     SELECT worker, SUM(amount) AS total_profit
                     FROM workers
                     GROUP BY worker
                     ),
                     work_rank AS (
                        SELECT worker,  
                               DENSE_RANK() OVER (ORDER BY total_profit DESC)
                        FROM work_profits
                     )
                  
                     SELECT *
                     FROM total, month, week
                     JOIN work_rank
                     ON total.worker = work_rank.worker


                  """, (date, name, name, name))
   
   data = cursor.fetchone()

   cursor.close()
   conn.close()

   return data

