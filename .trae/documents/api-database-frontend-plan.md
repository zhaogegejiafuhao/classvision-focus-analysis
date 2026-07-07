# ClassVision 全量接口定义 + 数据库设计 + 前端路由计划

## Context

项目骨架已搭建完成（后端FastAPI + CV引擎 + 前端Vue3），但缺少：
1. 完整的REST API接口（目前只有WebSocket骨架）
2. 数据库表结构和ORM模型
3. 前端多页面路由
4. WebSocket与数据库的衔接逻辑

本计划定义所有接口的请求/响应格式、数据库表结构、前后端对接方式，确保三人团队可并行开发。

---

## 一、数据库表设计（4张表）

### 1. classroom 课堂表
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer PK | 自增主键 |
| name | String(100) | 课程名称 |
| teacher | String(50) | 教师名称 |
| started_at | DateTime | 开始时间 |
| ended_at | DateTime nullable | 结束时间（null=正在进行） |
| duration | Integer default 0 | 时长（分钟） |
| avg_attention | Float default 0 | 平均注意力 |
| total_students | Integer default 0 | 检测到的人数 |

### 2. student 学生表
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer PK | 自增主键 |
| classroom_id | Integer FK | 所属课堂 |
| track_id | Integer | YOLOv8跟踪ID |
| name | String(50) nullable | 姓名（默认"学生N"） |

### 3. attention_record 注意力记录表
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer PK | 自增主键 |
| student_id | Integer FK | 所属学生 |
| classroom_id | Integer FK | 所属课堂 |
| timestamp | DateTime | 记录时间 |
| attention_score | Float | 总注意力分 |
| pitch / yaw / roll | Float | 姿态角 |
| ear | Float | 眨眼率 |
| is_blinking | Boolean | 是否眨眼 |
| blink_count | Integer | 累计眨眼 |
| gaze_score / pose_score / fatigue_score | Float | 各子项分数 |

### 4. report 报告表
| 字段 | 类型 | 说明 |
|------|------|------|
| id | Integer PK | 自增主键 |
| classroom_id | Integer FK unique | 所属课堂 |
| content | Text | AI报告Markdown |
| created_at | DateTime | 生成时间 |

---

## 二、接口定义

### 2.1 WebSocket 实时接口（已有骨架，需增强）

**WS /ws/video?classroom_id={id}**

请求（前端 → 后端）：
```json
{ "frame": "base64编码的JPEG" }
```

响应（后端 → 前端）：
```json
{
  "faces": [
    {
      "track_id": 1,
      "bbox": [x1, y1, x2, y2],
      "attention_score": 72.5,
      "pose": { "pitch": 5.2, "yaw": -3.1, "roll": 0.8 },
      "fatigue": { "ear": 0.28, "is_blinking": false, "blink_count": 3 },
      "gaze_score": 75.0,
      "pose_score": 68.4,
      "fatigue_score": 74.0
    }
  ],
  "count": 1,
  "classroom_id": 5,
  "frame_seq": 127
}
```

改动点：
- 增加 `classroom_id` 参数，WebSocket连接时绑定课堂
- 增加 `frame_seq` 帧序号，前端用于同步
- 后端每30帧写入一次数据库（约1秒1次），而非每帧写入
- 修复 `tracker.update()` bug：改为调用 `tracker.track(frame)`

### 2.2 REST API 接口

#### 课堂管理

**POST /api/classrooms** — 创建/开始课堂
```json
// 请求
{ "name": "高等数学A", "teacher": "张老师" }
// 响应
{ "id": 5, "name": "高等数学A", "teacher": "张老师", "started_at": "2026-07-06T10:00:00", "ended_at": null }
```

**GET /api/classrooms** — 课堂列表
```json
// 响应
[
  { "id": 5, "name": "高等数学A", "teacher": "张老师", "started_at": "...", "ended_at": "...", "duration": 45, "avg_attention": 68.2, "total_students": 30 }
]
```

**GET /api/classrooms/{id}** — 课堂详情
```json
// 响应（含学生列表和统计）
{
  "id": 5, "name": "高等数学A", "teacher": "张老师",
  "started_at": "...", "ended_at": "...", "duration": 45,
  "avg_attention": 68.2, "total_students": 30,
  "stats": {
    "head_down_count": 12, "head_turn_count": 8, "fatigue_count": 3,
    "attention_distribution": { "high": 15, "medium": 10, "low": 5 }
  }
}
```

**PUT /api/classrooms/{id}/end** — 结束课堂
```json
// 响应
{ "id": 5, "ended_at": "2026-07-06T10:45:00", "duration": 45, "avg_attention": 68.2 }
```

#### 统计数据

**GET /api/classrooms/{id}/timeline** — 注意力时间线
```json
// 响应（每分钟一条）
[
  { "timestamp": "10:01", "avg_attention": 75.2, "student_count": 28 },
  { "timestamp": "10:02", "avg_attention": 72.1, "student_count": 30 }
]
```

**GET /api/classrooms/{id}/students** — 学生列表及统计
```json
[
  { "id": 1, "track_id": 3, "name": "学生3", "avg_attention": 82.5, "head_down_count": 1, "blink_count": 5 }
]
```

#### AI报告

**POST /api/classrooms/{id}/report** — 生成AI报告
```json
// 响应
{ "id": 1, "classroom_id": 5, "content": "# 课堂分析报告\n...", "created_at": "..." }
```

**GET /api/classrooms/{id}/report** — 获取已有报告
```json
// 响应（同上，若未生成则返回404）
```

---

## 三、前端页面路由

| 路径 | 组件 | 说明 |
|------|------|------|
| / | HomePage.vue | 首页，开始课堂/历史列表入口 |
| /live/:id | LivePage.vue | 实时检测页（当前App.vue增强版） |
| /classrooms | ClassroomList.vue | 历史课堂列表 |
| /classrooms/:id | ClassroomDetail.vue | 课堂详情+图表+AI报告 |

前端新增依赖：vue-router

---

## 四、需修改的文件清单

### 新建文件
| 文件 | 说明 |
|------|------|
| backend/models/tables.py | SQLAlchemy ORM模型（4张表） |
| backend/models/schemas.py | Pydantic请求/响应模型 |
| backend/api/classroom_routes.py | 课堂CRUD路由 |
| backend/api/stats_routes.py | 统计+报告路由 |
| frontend/src/router/index.js | vue-router配置 |
| frontend/src/views/HomePage.vue | 首页 |
| frontend/src/views/LivePage.vue | 实时检测页 |
| frontend/src/views/ClassroomList.vue | 课堂列表页 |
| frontend/src/views/ClassroomDetail.vue | 课堂详情页 |

### 修改文件
| 文件 | 改动 |
|------|------|
| backend/main.py | 注册新路由 |
| backend/api/routes.py | 修复tracker bug + 增加classroom_id参数 + 数据库写入逻辑 |
| backend/core/config.py | 默认改用SQLite（简化部署） |
| backend/core/database.py | 建表逻辑 |
| frontend/package.json | 添加vue-router依赖 |
| frontend/src/main.js | 注册router |

---

## 五、验证方式

1. 启动后端：`uvicorn backend.main:app --reload`，访问 `http://localhost:8000/docs` 查看Swagger文档确认所有接口
2. 创建课堂 → WebSocket连接 → 开摄像头检测 → 结束课堂 → 查看时间线数据
3. 生成AI报告 → 查看报告内容
4. 前端 `npm run dev`，访问各页面确认路由和数据显示
