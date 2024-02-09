## Рогачев Александр, 13-я когорта - Финальный проект, инжинер по тестированию плюс
import main
import data

def test1_check_track_order(): ## Проверка получение заказа по трек номеру
    new_order = main.post_new_order(data.new_order)
    track = new_order.json()['track']
    check_order = main.get_check_track(track)
    assert new_order.status_code == 201
    assert  check_order.status_code == 200




