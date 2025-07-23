import streamlit as st
import requests
from datetime import datetime

# --- 🔑 ЗАМЕНИ тези с твоите реални данни ---
NOTION_TOKEN = "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"
DATABASE_ID = "23991f6c1fb780e69125f56067c200ba"

# --- Headers за API заявката ---
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# --- UI в Streamlit ---
st.title("✅ Отбележи урок като прочетен")

student_name = st.text_input("Твоето име:")
lesson_name = st.text_input("Име на урока:")
submit = st.button("📩 Изпрати")

# --- Изпращане към Notion при натискане ---
if submit and student_name and lesson_name:
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Ученик": {
    "rich_text": [{
        "text": { "content": student_name }
    }]
},
            "Урок": {
                "rich_text": [{
                    "text": { "content": lesson_name }
                }]
            },
            "Дата": {
                "date": { "start": datetime.now().isoformat() }
            }
        }
    }

    res = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)

    if res.status_code == 200:
        st.success("✅ Успешно записано!")
    else:
        st.error(f"⚠️ Грешка: {res.text}")
