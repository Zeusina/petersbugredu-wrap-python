---
description: Метод для входа в систему
---

# Login

Вы можете войти в систему, используя 2 разных варианта метода login

### login

```python
import petersburgedu_wrap

client = petersburgedu_wrap.client.Client() # Создание экземпляра класса Client
client.login(login="Ваша почта", password="Ваш пароль") # Вход в систему
```

В примере кода выше вы можете видеть вход через почту и пароль.&#x20;

Аргументы:

* login - почта
* password - пароль

Возвращаемое значение:

* Отсутствует

### login\_by\_token

```python
import petersburgedu_wrap

client = petersburgedu_wrap.client.Client() # Создание экземпляра класса Client
client.login(login="Ваша почта", password="Ваш пароль") # Вход в систему
```

В примере выше вы можете произвести вход, используя полученный каким-либо способом действительный JWT токен

Аргументы:

* token - JWT токен

Возвращаемое значение:

* Отсутствует
