from .funs import update_lesson_info, get_lessons  # noqa: F401
from .const import SCRIPT_TYPES, CONTENT_TYPES, LESSON_TYPES
from .models import *  # noqa: F401
from ..common.dicts import register_dict
from .manager import *  # noqa: F401

register_dict("script_types", "剧本类型", SCRIPT_TYPES)
register_dict("content_types", "内容类型", CONTENT_TYPES)
register_dict("lesston_types", "课程类型", LESSON_TYPES)
