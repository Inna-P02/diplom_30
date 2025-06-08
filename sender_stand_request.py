import configuration
import requests
import data



def post_new_order(order_body):
    order_body = data.order_body
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  
                         json=order_body,
                         )  
    return response





