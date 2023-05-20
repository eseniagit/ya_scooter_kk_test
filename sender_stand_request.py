import requests
import configuration


def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


def order_info(parameter):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=parameter)
