# Инна Попова, 30-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import data
import configuration
import sender_stand_request

def get_new_order(order_body):
    response = sender_stand_request.post_new_order(order_body)
    assert response.status_code == 201 
    return response.json()


def order_track(track):
    order_response = sender_stand_request.get_order_track(track)
    return order_response


def test_create_and_get_order():
    order_body = data.order_body  
    order_response = get_new_order(order_body)
    track_number = order_response.get("track")
    print(f"Трек-номер: {track_number}")
    order_data = order_track(track_number)
    assert order_data.status_code == 200
