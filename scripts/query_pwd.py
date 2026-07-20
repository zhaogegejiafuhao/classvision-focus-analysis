"""查询密码哈希"""
import sqlite3

conn = sqlite3.connect('classvision.db')
cur = conn.cursor()
cur.execute("SELECT id, username, role, password_hash, phone, email FROM registered_person WHERE id IN (2, 3, 14)")
rows = cur.fetchall()
for r in rows:
    print(f"id={r[0]} username={r[1]!r} role={r[2]} pwd_head={(r[3] or '')[:50]!r} phone={r[4]!r} email={r[5]!r}")
conn.close()
