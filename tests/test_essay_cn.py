import requests, json
r = requests.post('http://localhost:8000/api/auth/login', json={'username':'teacher','password':'teacher123'})
token = r.json()['access_token']
headers = {'Authorization': f'Bearer {token}'}
data = {
    'question': '请以我的家乡为题写一篇记叙文',
    'standard_answer': '主题鲜明，情感真挚；结构完整',
    'total_score': 100,
    'subject_type': 'essay',
    'student_text': '我的家乡是一个位于江南水乡的小镇，那里有小桥流水，有青砖黛瓦。清晨薄雾笼罩着小镇，河面上飘着轻纱般的雾气。春天桃花柳树如诗如画，夏天傍晚凉爽捉鱼摸螺，秋天桂花飘香做桂花糕，冬天银装素裹堆雪人。无论我走到哪里，家乡永远是我最温暖的港湾。',
}
r = requests.post('http://localhost:8000/api/grading/grade', json=data, headers=headers, timeout=300)
res = r.json()
dims = res['grading']['dimensions']
print(f"Score: {res['suggested_score']}/{res['max_score']}")
for k, v in dims.items():
    print(f"  {k}: {v['score']}/{v['max_score']} - {v['error_cause']}")
print(f"Comment: {res['comment'][:80]}")
