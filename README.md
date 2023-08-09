# Petersburgedu wrap
This module is designed for work with petersburgedu internal API.

## English
### Work in progress

## Русский(Russian)
### Работа в процессе

### Быстрый старт
Для быстрого старта в моей библиотеке вы можете воспользоваться минимальным кодом


```python
import petersbugredu_wrap
import logging
# Импорт необходимых библиотек
logging.basicConfig(level=logging.DEBUG) # Настройка логирования


client = petersbugredu_wrap.client.Client() # Создание клиента
client.login_by_token("Ваш токен") # Вход в систему через токен

children = client.get_child_list() # Получить список детей

education_id = children[0].education_id # Получить ученический id у ребенка

teachers = client.get_teacher_list(education_id) # Получение списка учителей
for teacher in teachers: 
    print(f"Имя: {teacher.firstname}, Фамилия: {teacher.surname}, Занимаемая должность: {teacher.position_name}")
```

Как альтернатива логина через токен, который можно получить на сайте петербургского образования можно использовать логин по почте и паролю

```python
import petersbugredu_wrap
import logging
# Импорт необходимых библиотек
logging.basicConfig(level=logging.DEBUG) # Настройка логирования


client = petersbugredu_wrap.client.Client() # Создание клиента
client.login(login="Ваша почта", password="Ваш пароль") # Вход в систему через токен

children = client.get_child_list() # Получить список детей

education_id = children[0].education_id # Получить ученический id у ребенка

teachers = client.get_teacher_list(education_id) # Получение списка учителей
for teacher in teachers: 
    print(f"Имя: {teacher.firstname}, Фамилия: {teacher.surname}, Занимаемая должность: {teacher.position_name}")
```
#### Полная документация будет написана позже