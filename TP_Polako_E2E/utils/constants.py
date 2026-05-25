from pathlib import Path

SECTIONS_MAPPING = {
    "events": "#events",
    "prices": "pricing",
    "tickets": "https://polako-tickets.rs/index-ru.html",
    "certificates": "services",
    "news": "news",
    "about": "about",
    "analytics": "analytics",
}


EXPECTED_MARKERS = {
    "telegram": "t.me/polakohedonist",
    "instagram_ru": "instagram.com/polakohedonist/",
    "instagram_sr": "instagram.com/polakohedonist.dogadjaji",
    "email": "mailto:support@polakohedonist.rs",
    "viber": "viber://chat",
    "whatsapp": "whatsapp.com",
}

# LoginPage
TEST_EMAIL = "test@mail.com"
INVALID_PASSWORD = "WrongPassword123"
UNREGISTERED_EMAIL = "not_exist@test.com"
VALID_TEST_PASSWORD = "Password123"
SQL_INJECTION_PAYLOAD = "' OR 1=1 --"
XSS_PAYLOAD = "<script>alert(1)</script>"
EXPECTED_ERROR_TEXT = "Неверный логин или пароль"
EMPTY_PASSWORD = ""
INVALID_EMAILS = [
    "test",
    "test@",
    "@gmail.com",
    "test.gmail.com",
    "test@com",
]


EVENT_NAME = "test_event"
EVENT_DESCRIPTION = "test_description"
EVENT_LOCATION = "Test Location (NS)"
EVENT_DURATION = "60"
EVENT_COST = "100"
EVENT_TO_DELETE = EVENT_NAME
ROOT_DIR = Path(__file__).resolve().parent.parent
IMAGE_PATH = ROOT_DIR / "test_data" / "test_events_foto.png"
TITLE_TEXT_RESULT = "The event title is empty."

VALID_PROFILE_DATA = {
    "first_name": "Ramses",
    "last_name": "Fourth",
    "email": "sergioodessit+1@gmail.com",
    "phone": "+1234567890",
    "instagram": "@ramsey",
    "telegram": "@ram4"
}

PARTIAL_PROFILE_DATA = {
    "first_name": "Привет",
    "last_name": "",
    "email": "hello@icloud.com",
    "phone": "",
    "instagram": "",
    "telegram": "@hello"
}

INVALID_PROFILE_DATA = {
    "first_name": "932c- mv3c kmf in0 \[w [wld][mcna]чьэцуст0ш3ьц0ч3 932c- mv3c kmf in0 \[w [wld][mcna]чьэцуст0ш3ьц0ч3",
    "last_name": "932c- mv3c kmf in0 \[w [wld][mcna]чьэцуст0ш3ьц0ч3 932c- mv3c kmf in0 \[w [wld][mcna]чьэцуст0ш3ьц0ч3",
    "email": """onetwo+simullteniesly.twentyfive-seventyday_samountqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm
    qwertyuiopasdfg@gmail.com""",
    "phone": """+123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012
    3456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567
    8901234567890123456789012345678901234""",
    "instagram": """Пейзик!([#}{2@'%"/|^34*.,`~""",
    "telegram": "ауцтсту.92ьх3ь-!смзц@"
}

VALID_NEW_PASSWORD = 't1T!k@cK%'
INVALID_NEW_PASSWORD = ''
