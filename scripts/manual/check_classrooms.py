import sqlite3
conn = sqlite3.connect("D:/ClassVision/classvision.db")
cursor = conn.cursor()
cursor.execute("SELECT id, name, teacher, total_students, avg_attention, duration FROM classroom ORDER BY id DESC LIMIT 10")
rows = cursor.fetchall()
for r in rows:
    print(f"ID={r[0]} | name={r[1]} | teacher={r[2]} | students={r[3]} | attention={r[4]} | duration={r[5]}")
conn.close()
