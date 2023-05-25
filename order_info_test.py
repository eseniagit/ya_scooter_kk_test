import data
import sender_stand_request

def get_new_track_number(body):
    order_response = sender_stand_request.create_new_order(body)
    new_track_number = data.track_number.copy()
    new_track_number["t"] = order_response.json()["track"]
    return new_track_number

def test_get_order_info():
    new_track_number = get_new_track_number(data.new_order_body)
    response = sender_stand_request.order_info(new_track_number)

    assert response.status_code == 200
