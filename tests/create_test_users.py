import sys
sys.path.insert(0, '.')
from backend.core.database import SessionLocal, init_db
from backend.models.tables import RegisteredPerson
from backend.core.security import hash_password

init_db()
db = SessionLocal()

test_users = [
    {'name': '测试教师', 'username': 'teacher', 'password': '123456', 'role': 'teacher'},
    {'name': '测试学生', 'username': 'student', 'password': '123456', 'role': 'student'},
    {'name': '测试管理员', 'username': 'admin', 'password': '123456', 'role': 'admin'},
]

for u in test_users:
    existing = db.query(RegisteredPerson).filter(RegisteredPerson.username == u['username']).first()
    if existing:
        existing.password_hash = hash_password(u['password'])
        existing.name = u['name']
        existing.role = u['role']
        print(f'更新用户: {u["username"]} ({u["role"]})')
    else:
        person = RegisteredPerson(
            name=u['name'],
            username=u['username'],
            password_hash=hash_password(u['password']),
            role=u['role'],
        )
        db.add(person)
        print(f'创建用户: {u["username"]} ({u["role"]})')

db.commit()
db.close()
print('测试用户创建完成')
