import requests


def ask_model(prompt):
    url = "http://127.0.0.1:11434/api/generate"
    payload = {
        "model": "qwen2.5-coder:3b",
        "prompt": prompt,
        "stream": False
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("response", "")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")
        return None

def generate_task():
    prompt = """
    Сгенерируй математическую задачу. 
    Она должна быть не сложной.
    Проанализируй задание и напиши короткий ответ на нее.
    """

    task = ask_model(prompt)


if __name__ == "__main__":
    while True:
        user_input = input("Ваш запрос: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            break
        answer = ask_model(user_input)
        print(f"Ответ: {answer}\n")
