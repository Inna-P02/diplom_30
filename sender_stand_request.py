import configuration
import requests
import data



def post_new_order(order_body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  
                         json=order_body,
                         )  
    return response

def get_order_track(track):
    order_response = requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))
    return order_response




