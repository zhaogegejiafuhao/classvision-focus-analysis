"""验证 AnswerRegradeHistory 表能正确建表"""
from sqlalchemy import create_engine, inspect
from backend.models.tables import Base

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(bind=engine)
insp = inspect(engine)
tables = insp.get_table_names()

assert 'answer_regrade_history' in tables, '❌ 表未创建'
print('✅ answer_regrade_history 表已创建')

cols = [c['name'] for c in insp.get_columns('answer_regrade_history')]
print(f'字段数: {len(cols)}')
print(f'字段: {cols}')

indexes = insp.get_indexes('answer_regrade_history')
print(f'索引: {[(i["name"], i["column_names"]) for i in indexes]}')

# 验证关键字段都存在
required = {
    'id', 'submission_id', 'question_id', 'operator_id',
    'regrade_method', 'input_mode', 'force_essay',
    'before_score', 'after_score', 'before_is_correct', 'after_is_correct',
    'max_score', 'before_total_score', 'after_total_score',
    'student_text', 'is_essay', 'model_key', 'grading_method',
    'error_cause', 'knowledge_points_json', 'grading_json',
    'writing_attribution_json', 'comment', 'created_at',
}
missing = required - set(cols)
assert not missing, f'❌ 缺失字段: {missing}'
print(f'✅ 所有 {len(required)} 个必需字段都存在')

# 验证复合索引
idx_names = [i['name'] for i in indexes]
assert 'ix_answer_regrade_history_sub_q' in idx_names, '❌ 复合索引未创建'
print('✅ 复合索引 ix_answer_regrade_history_sub_q 已创建')
