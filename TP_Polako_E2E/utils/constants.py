from pathlib import Path

sections_mapping = {
            "events": "#events",
            "prices": "pricing",
            "tickets": "https://polako-tickets.rs/index-ru.html",
            "certificates": "services",
            "news": "news",
            "about": "about",
            "analytics": "analytics"
        }


expected_markers = {
            "telegram": "t.me/polakohedonist",
            "instagram_ru": "instagram.com/polakohedonist/",
            "instagram_sr": "instagram.com/polakohedonist.dogadjaji",
            "email": "mailto:support@polakohedonist.rs",
            "viber": "viber://chat",
            "whatsapp": "whatsapp.com"
        }


event_name = "test_event"
event_description ="test_description"
event_location = "Test Location (NS)"
event_duration = "60"
event_cost = "100"
event_to_delete = event_name
ROOT_DIR = Path(__file__).resolve().parent.parent
image_path = ROOT_DIR / "test_data" / "test_events_foto.png"
title_text_result = "The event title is empty."