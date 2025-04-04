import requests

def fox():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)

    # Проверка статуса ответа
    if response.status_code == 200:
        try:
            data = response.json()
            return data.get('image')  # Обработка данных
        except ValueError:
            print("Ошибка декодирования JSON")
    else:
        print(f"Ошибка: {response.status_code}, содержимое: {response.text}")
if   __name__ == '__main__':
    fox()

