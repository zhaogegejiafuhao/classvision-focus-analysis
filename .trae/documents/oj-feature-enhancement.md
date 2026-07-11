# OJ 判题功能完善计划

## Context

当前 OJ 功能只有一个简单的代码编辑器（Frame281780.vue），支持代码运行（调用 judger `/run`）但缺少核心 OJ 功能：题目列表、题目详情、提交判题、提交记录。judger 容器（端口 12345）已运行，支持 `/ping`、`/run`（同步运行）、`/judge`（异步判题+回调，但 SpringBoot 后端未运行）。OJ MySQL 有 11 个预置题目但与 ClassVision SQLite 数据库分离。

**决策**：在 ClassVision SQLite 数据库中新增 Problem/Submission 表，预置几道题目，使用 judger `/run` 端点进行同步判题（对每个测试用例运行代码并比较输出）。不依赖 OJ MySQL 和 SpringBoot，保持架构简单。

## 实现步骤

### 1. 后端：新增数据表（tables.py）

在 `backend/models/tables.py` 末尾新增三个表：

- `OjProblem`：id, title, description, input_format, output_format, sample_input, sample_output, hint, time_limit(默认1000ms), memory_limit(默认256MB), difficulty(简单/中等/困难), created_at
- `OjTestCase`：id, problem_id(FK), input, expected_output, is_sample(布尔)
- `OjSubmission`：id, user_id(FK→registered_person), problem_id(FK), language, source_code, status(AC/WA/TLE/MLE/RE/CE/Pending), cpu_time, memory, error_message, submitted_at

### 2. 后端：新增 Pydantic 模型（schemas.py）

在 `backend/models/schemas.py` 新增：
- `OjProblemOut`：id, title, difficulty, accepted_count, submitted_count（列表用）
- `OjProblemDetail`：完整字段 + sample_test_cases 列表
- `OjSubmissionCreate`：problem_id, language, source_code
- `OjSubmissionOut`：id, problem_id, problem_title, language, status, cpu_time, memory, submitted_at

### 3. 后端：新增 API 路由（oj_routes.py）

在 `backend/api/oj_routes.py` 新增端点（均需 `get_current_user` 认证）：
- `GET /api/oj/problems` — 题目列表（含通过率统计）
- `GET /api/oj/problems/{pid}` — 题目详情（含样例测试用例）
- `POST /api/oj/submit` — 提交判题：对每个测试用例调用 judger `/run`，比较输出，聚合结果
- `GET /api/oj/submissions` — 当前用户的提交记录（可按 problem_id 筛选）
- `GET /api/oj/submissions/{sid}` — 单条提交详情

**判题逻辑**：
1. 创建 Pending 状态的 submission 记录
2. 遍历该题目的所有测试用例
3. 对每个用例调用 `JUDGER_URL/run`，传入源码和测试输入
4. 比较输出（trim 后逐行比较）
5. 首个失败用例决定最终状态（WA/TLE/MLE/RE/CE）
6. 全部通过则 AC，记录最大 cpu_time 和 memory
7. 更新 submission 记录

### 4. 后端：预置题目数据（main.py）

在 `main.py` 的 `lifespan` 中添加 `_seed_oj_problems()` 函数，启动时检查并插入 5 道基础题目（每题含 3-5 个测试用例）：
1. A+B 问题（简单）
2. 数组求和（简单）
3. 字符串反转（简单）
4. 寻找最大值（中等）
5. 斐波那契数列（中等）

### 5. 前端：新增路由（router/index.js）

```
/oj           → OjProblemList.vue   （题目列表）
/oj/:id       → OjProblemDetail.vue  （题目详情+做题）
/oj/run       → Frame281780.vue      （自由代码运行，现有页面）
/oj/submissions → OjSubmissions.vue  （提交记录）
```

### 6. 前端：新增页面

**OjProblemList.vue**（题目列表）：
- a-table 展示题目：题号、标题、难度（a-tag 颜色）、通过率、状态
- 点击题目跳转 `/oj/:id`
- 顶部 a-page-header + 两个按钮（自由运行、提交记录）

**OjProblemDetail.vue**（题目详情+做题）：
- 左侧：题目描述、输入输出格式、样例（a-card）
- 右侧：语言选择 + a-textarea 代码编辑器（复用 Frame281780 的暗色样式）+ 提交按钮
- 底部：判题结果展示（状态 a-tag、耗时、内存、错误信息）

**OjSubmissions.vue**（提交记录）：
- a-table 展示提交记录：提交时间、题目、语言、状态（a-tag）、耗时、内存
- 点击可展开查看源代码

### 7. 前端：更新 MainLayout 侧边栏

将 OJ 菜单项改为指向 `/oj`（题目列表），不新增子菜单，保持侧边栏简洁。

## 关键文件

| 文件 | 操作 |
|------|------|
| `backend/models/tables.py` | 新增 OjProblem, OjTestCase, OjSubmission |
| `backend/models/schemas.py` | 新增 OjProblemOut, OjProblemDetail, OjSubmissionCreate, OjSubmissionOut |
| `backend/api/oj_routes.py` | 新增 5 个 API 端点 + 判题逻辑 |
| `backend/main.py` | 新增 _seed_oj_problems() |
| `frontend/src/router/index.js` | 新增 4 条 OJ 子路由 |
| `frontend/src/views/OjProblemList.vue` | 新建 |
| `frontend/src/views/OjProblemDetail.vue` | 新建 |
| `frontend/src/views/OjSubmissions.vue` | 新建 |

## 验证方式

1. 启动后端，检查 SQLite 中 oj_problem 等表已创建且有 5 道题目
2. 访问 `GET /api/oj/problems` 确认返回题目列表
3. 登录学生账号，访问 `/oj` 看到题目列表
4. 点击题目进入 `/oj/:id`，编写代码并提交
5. 确认识别 AC/WA 等状态正确
6. 访问 `/oj/submissions` 看到提交记录
7. 访问 `/oj/run` 确认原有自由运行功能仍可用
