from data import DataForOrder, DataForUser, DataForAuth


def modify_crate_user_body(key, value):
    body = DataForUser.CREATE_USER.copy()
    body[key] = value
    return body

def modify_crate_login_body(key, value):
    body = DataForAuth.LOGIN_BODY.copy()
    body[key] = value
    return body

def modify_crate_order_body(key, value):
    body = DataForOrder.CREATE_ORDER_BODY.copy()
    body[key] = value
    return body
