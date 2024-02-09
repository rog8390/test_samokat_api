import requests
import configuration
import data

def post_new_order(new_order): ## Функция создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH, json=new_order)

track_number = post_new_order(data.new_order).json()["track"] ## Получение трек номера
print(track_number)

def get_check_track(number): # Функция получения заказа по трек номеру
    return requests.get(configuration.URL_SERVICE+configuration.CHECK_ORDER + str(number))
response = get_check_track(track_number)
print(response.url)

