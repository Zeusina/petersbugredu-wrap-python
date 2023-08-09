"""
File with URL endpoints for petersburg education portal
"""

LOGIN_URL = "https://dnevnik2.petersburgedu.ru/api/user/auth/login"
RELATED_CHILD_LIST_URL = "https://dnevnik2.petersburgedu.ru/api/journal/person/related-child-list"
TEACHER_LIST_URL="https://dnevnik2.petersburgedu.ru/api/journal/teacher/list?p_page={{page}}&p_educations%5B%5D={{education_id}}"
