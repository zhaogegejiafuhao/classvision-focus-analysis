"""查询 registered_person 表的教师账号"""
import sqlite3

conn = sqlite3.connect('classvision.db')
cur = conn.cursor()
cur.execute("SELECT id, username, role, name FROM registered_person WHERE role IN ('teacher', 'admin') LIMIT 20")
rows = cur.fetchall()
print(f'Teachers/Admins (count={len(rows)}):')
for r in rows:
    print(f'  id={r[0]} username={r[1]!r} role={r[2]} name={r[3]!r}')

# 也看下 exam 表
print()
cur.execute("SELECT id, title, teacher_id FROM exam LIMIT 10")
exams = cur.fetchall()
print(f'Exams (count={len(exams)}):')
for e in exams:
    print(f'  id={e[0]} title={e[1]!r} teacher_id={e[2]}')

# exam_submission
print()
cur.execute("SELECT id, exam_id, student_id, score, status FROM exam_submission LIMIT 10")
subs = cur.fetchall()
print(f'exam_submission (count={len(subs)}):')
for s in subs:
    print(f'  id={s[0]} exam_id={s[1]} student_id={s[2]} score={s[3]} status={s[4]!r}')

# answer_regrade_history
print()
cur.execute("SELECT COUNT(*) FROM answer_regrade_history")
cnt = cur.fetchone()[0]
print(f'answer_regrade_history count: {cnt}')

# question
print()
cur.execute("SELECT id, exam_id, type, score, substr(content, 1, 40) FROM question WHERE type='essay' LIMIT 10")
qs = cur.fetchall()
print(f'essay questions (count={len(qs)}):')
for q in qs:
    print(f'  id={q[0]} exam_id={q[1]} type={q[2]} score={q[3]} content_head={q[4]!r}')

conn.close()
