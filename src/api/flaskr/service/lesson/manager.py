from flaskr.service.view.models import (
    INPUT_TYPE_TEXT,
    InputItem,
    TableColumnItem,
    ViewDef,
    OperationItem,
    OperationType,
)

from .models import AICourse, AILesson, AILessonScript
from .const import LESSON_TYPES


AILessonView = ViewDef(
    "lessonview",
    [
        TableColumnItem(AILesson.lesson_id, "ID"),
        TableColumnItem(
            AILesson.course_id, "课程ID", model=AICourse, display="course_name"
        ),
        TableColumnItem(AILesson.lesson_no, "章节号"),
        TableColumnItem(AILesson.lesson_name, "名称"),
        TableColumnItem(AILesson.lesson_type, "类型", items=LESSON_TYPES),
        TableColumnItem(AILesson.status, "状态", items=LESSON_TYPES),
        TableColumnItem(AILesson.created, "创建时间"),
        TableColumnItem(AILesson.updated, "更新时间"),
    ],
    [
        InputItem("name", "名称", "like", INPUT_TYPE_TEXT),
        InputItem("type", "类型", "like", INPUT_TYPE_TEXT),
        InputItem("status", "状态", "like", INPUT_TYPE_TEXT),
        InputItem("created", "创建时间", "like", INPUT_TYPE_TEXT),
        InputItem("updated", "更新时间", "like", INPUT_TYPE_TEXT),
    ],
    AILesson,
    [
        OperationItem(
            "脚本",
            OperationType.GO_TO_LIST,
            "lessonscriptview",
            "lessonscriptview",
            {"lesson_id": "lesson_id"},
        ),
    ],
)


AICourseView = ViewDef(
    "courseview",
    [
        TableColumnItem(AICourse.course_id, "ID"),
        TableColumnItem(AICourse.course_name, "名称"),
        TableColumnItem(AICourse.course_price, "价格"),
        TableColumnItem(AICourse.course_status, "状态"),
        TableColumnItem(AICourse.created, "创建时间"),
        TableColumnItem(AICourse.updated, "更新时间"),
    ],
    [
        InputItem("id", "ID", "like", INPUT_TYPE_TEXT),
        InputItem("name", "名称", "like", INPUT_TYPE_TEXT),
        InputItem("type", "类型", "like", INPUT_TYPE_TEXT),
        InputItem("status", "状态", "like", INPUT_TYPE_TEXT),
        InputItem("created", "创建时间", "like", INPUT_TYPE_TEXT),
        InputItem("updated", "更新时间", "like", INPUT_TYPE_TEXT),
    ],
    AICourse,
    [
        OperationItem("编辑", OperationType.GO_TO_DETAIL, "edit", "edit", {}),
        OperationItem(
            "课程章节",
            OperationType.GO_TO_LIST,
            "lessonview",
            "lessonview",
            {"course_id": "course_id"},
        ),
    ],
)

AILessonScriptView = ViewDef(
    "lessonscriptview",
    [
        TableColumnItem(AILessonScript.id, "ID"),
        TableColumnItem(AILessonScript.script_name, "名称"),
        TableColumnItem(AILessonScript.script_type, "类型"),
        TableColumnItem(AILessonScript.script_model, "内容"),
        TableColumnItem(AILessonScript.script_index, "序号"),
        TableColumnItem(AILessonScript.script_ui_type, "UI类型"),
        TableColumnItem(AILessonScript.status, "状态"),
        TableColumnItem(AILessonScript.created, "创建时间"),
        TableColumnItem(AILessonScript.updated, "更新时间"),
    ],
    [
        InputItem("id", "ID", "like", INPUT_TYPE_TEXT),
        InputItem("name", "名称", "like", INPUT_TYPE_TEXT),
        InputItem("type", "类型", "like", INPUT_TYPE_TEXT),
        InputItem("status", "状态", "like", INPUT_TYPE_TEXT),
        InputItem("created", "创建时间", "like", INPUT_TYPE_TEXT),
        InputItem("updated", "更新时间", "like", INPUT_TYPE_TEXT),
    ],
    AILessonScript,
)
