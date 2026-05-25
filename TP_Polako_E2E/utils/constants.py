sections_mapping = {
    "events": "#events",
    "prices": "pricing",
    "tickets": "https://polako-tickets.rs/index-ru.html",
    "certificates": "services",
    "news": "news",
    "about": "about",
    "analytics": "analytics",
}


expected_markers = {
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
