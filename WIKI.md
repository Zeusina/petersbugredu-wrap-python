# Petersburgedu Wrap Wiki

## Overview

`petersburgedu_wrap` is a Python client library for working with the Petersburg education portal API.

The package currently provides:
- authentication with login/password or JWT token
- fetching linked children
- fetching teachers for a child
- fetching marks by date period
- fetching lessons by date period
- typed dataclass models for API entities

## Installation

```bash
pip install petersburgedu_wrap
```

The package requires:
- Python `>=3.7`

## Package structure

### Main modules
- `petersburgedu_wrap.client` — main API client
- `petersburgedu_wrap.types` — dataclasses for API entities
- `petersburgedu_wrap.utils` — endpoints and request headers
- `petersburgedu_wrap.errors` — custom exceptions

## Authentication

### `Client.login(login: str, password: str) -> None`

Authenticates a user using email/login and password.

#### Behavior
- Sends a `POST` request to the login endpoint
- Expects a `200` response with a JWT token in `response.json()["data"]["token"]`
- Stores the token internally in the client instance

#### Errors
- `InvalidLoginOrPasswordException` — when the server returns status code `400`
- `IndexError` — if the response does not contain a token
- `ValueError` — for unexpected status codes

#### Example
```python
from petersburgedu_wrap.client import Client

client = Client()
client.login("user@example.com", "password")
```

### `Client.login_by_token(token: str) -> None`

Stores an already obtained JWT token in the client.

#### Example
```python
client.login_by_token("your-jwt-token")
```

## Client API

### `Client.get_child_list() -> list[Child]`

Fetches the list of related children from the portal.

#### Behavior
- Sends a `GET` request using the stored JWT token in the `X-JWT-Token` cookie
- Returns a list of `Child` objects
- Returns an empty list if the request fails with a non-200 status code

#### Returned data
Each child contains:
- `firstname`
- `surname`
- `middlename`
- `educations`
- `hash_uid`
- `action_payload`
- `identity`
- `_token` stored internally inside the child object

#### Example
```python
children = client.get_child_list()
```

## Child API

The `Child` model exposes methods for fetching data for a specific student.

### `Child.get_teacher_list() -> list[Teacher]`

Returns the list of teachers for the child.

#### Behavior
- Uses the first education in `child.educations`
- Sends a `GET` request to the teacher list endpoint
- Returns a list of `Teacher` objects
- Returns an empty list on non-200 responses

#### Example
```python
teachers = child.get_teacher_list()
```

### `Child.get_mark_list_by_period(date_from, date_to, education_number=0) -> list[MarkEntry]`

Returns marks for the selected education and date range.

#### Parameters
- `date_from` — start date (`datetime.date`)
- `date_to` — end date (`datetime.date`)
- `education_number` — index of the education in `child.educations`

#### Behavior
- Requests marks page by page
- Combines all pages into one list
- Converts API payloads into `MarkEntry` objects

#### Example
```python
import datetime

marks = child.get_mark_list_by_period(
    datetime.date(2024, 9, 1),
    datetime.date(2024, 9, 30),
)
```

### `Child.get_lesson_list_by_period(date_from, date_to, education_number=0) -> list[LessonEntry]`

Returns lessons for the selected education and date range.

#### Parameters
- `date_from` — start date (`datetime.date`)
- `date_to` — end date (`datetime.date`)
- `education_number` — index of the education in `child.educations`

#### Behavior
- Requests lessons page by page
- Combines all pages into one list
- Converts API payloads into `LessonEntry` objects

#### Example
```python
lessons = child.get_lesson_list_by_period(
    datetime.date(2024, 9, 1),
    datetime.date(2024, 9, 30),
)
```

## Data models

### `Child`
Represents a child entity returned by the API.

Fields:
- `firstname: str`
- `middlename: str`
- `surname: str`
- `educations: list[Education]`
- `action_payload: ActionPayload`
- `hash_uid: str`
- `identity: Identity`
- `token: str` — removed after initialization and stored internally as `_token`

### `Education`
Represents a school education record.

Fields:
- `push_subscribe: bool`
- `education_id: int`
- `group_id: int`
- `group_name: str`
- `institution_id: int`
- `institution_name: str`
- `jurisdiction_id: int`
- `jurisdiction_name: str`
- `is_active: Any`
- `distance_education: bool`
- `distance_education_updated_at: str`
- `parent_firstname: str`
- `parent_surname: str`
- `parent_middlename: str`
- `parent_email: str`

### `ActionPayload`
Represents action permissions returned by the API.

Fields:
- `can_apply_for_distance: bool = True`
- `can_print: bool = True`
- `can_add_homework: bool = True`

### `Identity`
Represents an identity object.

Fields:
- `id: int`
- `uid: str = None`

### `Teacher`
Represents a teacher entity.

Fields:
- `firstname: str`
- `surname: str`
- `middlename: str`
- `position_name: str`
- `subjects: list[dict]`

### `MarkEntry`
Represents one mark record.

Fields:
- `id: int`
- `education_id: int`
- `lesson_id: int`
- `subject_id: int`
- `subject_name: str`
- `date: datetime.datetime`
- `estimate_value_code: str`
- `estimate_value_name: str`
- `estimate_type_code: str`
- `estimate_type_name: str`
- `estimate_comment: str`

### `LessonEntry`
Represents one lesson record.

Fields:
- `identity: Identity`
- `number: int`
- `datetime_from: datetime.datetime`
- `datetime_to: datetime.datetime`
- `subject_id: int`
- `subject_name: str`
- `content_name: str`
- `content_description: Any`
- `content_additional_material: Any`
- `tasks: list[Task]`
- `estimates: list[Estimate]`
- `action_payload: ActionPayload`

### `Task`
Represents a lesson task.

Fields:
- `task_name: str`
- `task_code: Any`
- `task_kind_code: str`
- `task_kind_name: str`
- `files: list`

### `Estimate`
Represents a lesson estimate.

Fields:
- `estimate_type_code: str`
- `estimate_type_name: str`
- `estimate_value_code: str`
- `estimate_value_name: str`
- `estimate_comment: Any`

## Errors

### `InvalidLoginOrPasswordException`
Raised when login credentials are invalid.

## Endpoints

The library uses these API endpoints:
- `LOGIN_URL`
- `RELATED_CHILD_LIST_URL`
- `TEACHER_LIST_URL`
- `MARKS_BY_DATE_URL`
- `LESSONS_BY_DATE_URL`

They are defined in `petersburgedu_wrap.utils.endpoints`.

## Request headers

Default headers are defined in `petersburgedu_wrap.utils.request_parameters`:
- `User-Agent`
- `Accept`
- `Content-Type`

## Usage example

```python
import datetime
from petersburgedu_wrap.client import Client

client = Client()
client.login("user@example.com", "password")

children = client.get_child_list()
if children:
    child = children[0]
    teachers = child.get_teacher_list()
    marks = child.get_mark_list_by_period(datetime.date(2024, 9, 1), datetime.date(2024, 9, 30))
    lessons = child.get_lesson_list_by_period(datetime.date(2024, 9, 1), datetime.date(2024, 9, 30))
```
