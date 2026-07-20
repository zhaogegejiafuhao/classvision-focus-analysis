import api from './index'

/** 获取可扫描批改的考试列表（教师身份自动过滤，含 has_template 状态） */
export function listScannableExams() {
  return api.get('/answer-sheet/exams')
}

/** 获取考试题目列表（用于模板编辑器中选择题号） */
export function listExamQuestions(examId) {
  return api.get(`/answer-sheet/exams/${examId}/questions`)
}

/** 获取试卷模板（编辑模式回填，404 时不弹全局错误以便探测） */
export function getPaperTemplate(examId) {
  return api.get(`/answer-sheet/templates/${examId}`, {
    _skipGlobalError: true,
  })
}

/** 创建/更新试卷模板（FormData: exam_id + blank_file + regions_json + 可选 anchor_points_json） */
export function savePaperTemplate({ examId, blankFile, regions, anchorPoints }) {
  const fd = new FormData()
  fd.append('exam_id', examId)
  fd.append('blank_file', blankFile)
  fd.append('regions_json', JSON.stringify(regions))
  if (anchorPoints) fd.append('anchor_points_json', JSON.stringify(anchorPoints))
  return api.post('/answer-sheet/templates', fd, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 60000,
  })
}

/** 删除试卷模板 */
export function deletePaperTemplate(examId) {
  return api.delete(`/answer-sheet/templates/${examId}`)
}

/** 扫描整卷并批改（FormData: file + student_id，后端处理可能耗时，超时设为 5 分钟） */
export function scanAndGrade({ examId, file, studentId }) {
  const fd = new FormData()
  fd.append('file', file)
  fd.append('student_id', studentId)
  return api.post(`/answer-sheet/scan/${examId}`, fd, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 300000,
  })
}

/** 独立气泡检测（调试用，返回检测到的答案 + 调试可视化图） */
export function detectBubbles({ file, templateType = 'standard_5x10x4' }) {
  const fd = new FormData()
  fd.append('file', file)
  fd.append('template_type', templateType)
  return api.post('/answer-sheet/detect-bubbles', fd, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 60000,
  })
}

// ============ 批量能力增强 ============

/**
 * B. 试卷模板预设一键生成
 * 上传空白卷 + 选择布局，系统自动按布局为 exam 所有题目生成 regions
 * @param {Object} params
 * @param {number} params.examId - 考试 ID
 * @param {File} params.blankFile - 空白卷图片文件
 * @param {string} [params.layout='standard_5col'] - 预设布局名
 *   可选：standard_5col / standard_4col / standard_3col / standard_2col / single_col
 * @param {number[]} [params.questionIds] - 可选，按指定顺序使用题目；不传则按 Question.order
 * @param {number} [params.topMarginRatio=0.05] - 顶部留白比例
 * @param {number} [params.bottomMarginRatio=0.03] - 底部留白比例
 * @param {number} [params.sideMarginRatio=0.03] - 左右留白比例
 */
export function autoGenerateTemplate({
  examId,
  blankFile,
  layout = 'standard_5col',
  questionIds = null,
  topMarginRatio = 0.05,
  bottomMarginRatio = 0.03,
  sideMarginRatio = 0.03,
}) {
  const fd = new FormData()
  fd.append('blank_file', blankFile)
  fd.append('layout', layout)
  if (questionIds && questionIds.length) {
    fd.append('question_ids_json', JSON.stringify(questionIds))
  }
  fd.append('top_margin_ratio', topMarginRatio)
  fd.append('bottom_margin_ratio', bottomMarginRatio)
  fd.append('side_margin_ratio', sideMarginRatio)
  return api.post(`/answer-sheet/templates/${examId}/auto-generate`, fd, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 60000,
  })
}

/**
 * C. 模板区域批量更新（事务内 upsert）
 * @param {Object} params
 * @param {number} params.examId - 考试 ID
 * @param {Array} params.regions - 区域列表，每项 {region_id?, question_id, region_type, bbox, order}
 * @param {boolean} [params.deleteMissing=false] - True 时删除不在列表中的现有 region
 */
export function batchUpdateRegions({ examId, regions, deleteMissing = false }) {
  const fd = new FormData()
  fd.append('regions_json', JSON.stringify(regions))
  fd.append('delete_missing', deleteMissing)
  return api.put(`/answer-sheet/templates/${examId}/regions/batch`, fd, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 30000,
  })
}

/**
 * A. 多学生批量扫描批改
 * 一次上传 N 份答卷 + 对应 student_id 列表，顺序批改，单个失败不阻塞其他
 * @param {Object} params
 * @param {number} params.examId - 考试 ID
 * @param {File[]} params.files - 多份答卷图片（顺序与 studentIds 对应）
 * @param {number[]} params.studentIds - 学生 ID 列表（RegisteredPerson.id）
 */
export function scanBatch({ examId, files, studentIds }) {
  const fd = new FormData()
  files.forEach((f) => fd.append('files', f))
  fd.append('student_ids', studentIds.join(','))
  // N 份答卷顺序批改可能耗时较长，超时设为 30 分钟
  return api.post(`/answer-sheet/scan-batch/${examId}`, fd, {
    headers: { 'Content-Type': 'multipart/form-data' },
    timeout: 1800000,
  })
}

/**
 * D. 批量 Excel 报告导出（ZIP 包）
 * 一次导出多个 submission 的 Excel 报告，打包为 ZIP
 * @param {number[]} submissionIds - submission ID 列表（最多 100 个）
 * @returns {Promise<Blob>} ZIP 文件 Blob（含 N 个 .xlsx）
 *   响应 header 中含 X-Batch-Total / X-Batch-Success / X-Batch-Failed / X-Batch-Failed-Detail
 */
export function exportExcelBatch(submissionIds) {
  return api.get('/answer-sheet/export/excel-batch', {
    params: { submission_ids: submissionIds.join(',') },
    responseType: 'blob',
    timeout: 300000,
  })
}

/** 单个 submission Excel 报告导出（已存在的 /export/excel/{id} 前端封装） */
export function exportExcelReport(submissionId) {
  return api.get(`/answer-sheet/export/excel/${submissionId}`, {
    responseType: 'blob',
    timeout: 60000,
  })
}

/**
 * D. 教师人工补录学生答案并重新判分
 * 当 OCR 双引擎均失败或置信度过低导致 is_correct=null 时使用
 * @param {number} submissionId - 提交 ID
 * @param {number} questionId - 题目 ID
 * @param {string} studentAnswer - 教师输入的学生答案
 * @returns {Promise<Object>} 更新后的批改结果
 *   { submission_id, question_id, student_answer, standard_answer, score, max_score,
 *     is_correct, total_score, manual_input, graded_at }
 */
export function manualInputAnswer(submissionId, questionId, studentAnswer) {
  const fd = new FormData()
  fd.append('student_answer', studentAnswer)
  return api.post(
    `/answer-sheet/submissions/${submissionId}/questions/${questionId}/manual-input`,
    fd,
    {
      headers: { 'Content-Type': 'multipart/form-data' },
      timeout: 30000,
      _skipGlobalError: true,  // 由组件自己处理错误提示
    },
  )
}

/**
 * E. 大题/作文 LLM 重批改
 * scan_and_grade 完成后，教师对某道大题重新触发 LLM 批改：
 * - studentText 模式：教师手输学生答案文字，跳过 OCR，直接走 LLM
 * - imageFile 模式：重新上传图片，重新走 OCR + LLM
 * - forceEssay=true：强制按作文批改（默认按 _is_essay_question 自动路由）
 *
 * @param {number} submissionId - 提交 ID
 * @param {number} questionId - 题目 ID
 * @param {Object} params
 * @param {string} [params.studentText] - 学生答案文字（与 imageFile 二选一）
 * @param {File} [params.imageFile] - 学生答案图片（与 studentText 二选一）
 * @param {boolean} [params.forceEssay=false] - 强制按作文批改
 * @returns {Promise<Object>} 完整批改详情
 *   { submission_id, question_id, student_answer, standard_answer, score, max_score,
 *     is_correct, total_score, regrade, is_essay, model_key, grading_method,
 *     comment, grading, error_cause, knowledge_points, writing_attribution, graded_at }
 */
export function regradeEssay(submissionId, questionId, { studentText, imageFile, forceEssay = false } = {}) {
  const fd = new FormData()
  if (studentText !== undefined && studentText !== null) {
    fd.append('student_text', studentText)
  }
  if (imageFile) {
    fd.append('image_file', imageFile)
  }
  fd.append('force_essay', forceEssay ? 'true' : 'false')
  // LLM 调用可能耗时较长（多模型并行竞速 + 写作归因），超时设为 3 分钟
  return api.post(
    `/answer-sheet/submissions/${submissionId}/questions/${questionId}/regrade-essay`,
    fd,
    {
      headers: { 'Content-Type': 'multipart/form-data' },
      timeout: 180000,
      _skipGlobalError: true,  // 由组件自己处理错误提示
    },
  )
}

/**
 * F. 获取某题的重批改历史记录
 * @param {number} submissionId - 提交 ID
 * @param {number} questionId - 题目 ID
 * @param {Object} [opts]
 * @param {boolean} [opts.detail=false] - true 时返回完整 grading_json/writing_attribution_json/student_text
 * @param {number} [opts.limit=100] - 最多返回条数（上限 500）
 * @param {number} [opts.offset=0] - 分页偏移
 * @returns {Promise<Object>} { submission_id, question_id, total, limit, offset, records: [...] }
 *   records 每项含：id, operator_id, operator_name, operator_role, regrade_method,
 *     input_mode, force_essay, before_score, after_score, before_is_correct, after_is_correct,
 *     max_score, before_total_score, after_total_score, is_essay, model_key, grading_method,
 *     error_cause, comment, created_at, student_text_head (前100字), knowledge_points (数组)
 *   detail=true 时额外含：student_text (全文), grading_json, writing_attribution_json
 */
export function listRegradeHistory(submissionId, questionId, { detail = false, limit = 100, offset = 0 } = {}) {
  return api.get(
    `/answer-sheet/submissions/${submissionId}/questions/${questionId}/regrade-history`,
    {
      params: { detail, limit, offset },
      timeout: 15000,
      _skipGlobalError: true,  // 由组件自己处理错误提示
    },
  )
}
