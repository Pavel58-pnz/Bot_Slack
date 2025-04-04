import requests

# Твой токен бота из Slack
SLACK_BOT_TOKEN = "xoxb-XXXXXXXX-YYYYYYYYYYYYYYY-ZZZZZZZZZZZZZZZZZZZZZZZZ"  # Замените на ваш токен
# Канал, куда отправлять сообщение (например, #general или @username)
SLACK_CHANNEL = "#general"  # Или, например, "@ваше_имя"

# Функция для отправки сообщения в Slack
def send_test_message_to_slack(message):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": SLACK_CHANNEL,
        "text": message
    }

    response = requests.post(url, headers=headers, json=payload)
    
    # Проверяем статус ответа
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("ok"):
            print("Сообщение успешно отправлено в Slack!")
        else:
            print(f"Ошибка Slack API: {response_data.get('error')}")
    else:
        print(f"HTTP ошибка: {response.status_code}, текст: {response.text}")

# Тестовая отправка сообщения
if __name__ == "__main__":
    test_message = "Тест 🤖"
    send_test_message_to_slack(test_message)