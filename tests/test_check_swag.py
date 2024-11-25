from pages.swag_labs import SwagLabs

def test_icon_exists(driver):
    swag_labs = SwagLabs(driver)
    swag_labs.visit()
    assert swag_labs.exist_icon() == True

def test_username_field_exists(driver):
    swag_labs = SwagLabs(driver)
    swag_labs.visit()
    assert swag_labs.find_element('input#user-name') is not None

def test_password_field_exists(driver):
    swag_labs = SwagLabs(driver)
    swag_labs.visit()
    assert swag_labs.find_element('input#password') is not None