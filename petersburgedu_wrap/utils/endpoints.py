"""
File with URL endpoints for petersburg education portal
"""

LOGIN_URL = "https://dnevnik2.petersburgedu.ru/api/user/auth/login"
RELATED_CHILD_LIST_URL = "https://dnevnik2.petersburgedu.ru/api/journal/person/related-child-list"
TEACHER_LIST_URL="https://dnevnik2.petersburgedu.ru/api/journal/teacher/list?p_page={{page}}&p_educations%5B%5D={{education_id}}"
MARKS_BY_DATE_URL="https://dnevnik2.petersburgedu.ru/api/journal/estimate/table?p_educations%5B%5D={{education_id}}&p_date_from={{date_from}}&p_date_to={{date_to}}&p_limit=100&p_page={{page}}"
LESSONS_BY_DATE_URL="https://dnevnik2.petersburgedu.ru/api/journal/lesson/list-by-education?p_page={{page}}&p_datetime_from={{date_from}}%2000:00:00&p_datetime_to={{date_to}}%2023:59:59&p_educations%5B%5D={{education_id}}"
