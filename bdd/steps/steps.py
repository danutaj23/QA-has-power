from behave import *
import time


@given('the page "{url}" is loaded')
def step_impl(context, url):
    context.browser.get(url)
    time.sleep(1)


@when('I type "{text}" in "{input_id}" input')
def step_impl(context, text, input_id):
    input_field = context.browser.find_element_by_xpath(
        '//input[@id="{input_id_xp}"]'.format(input_id_xp=input_id)
    )
    input_field.send_keys(text)
    time.sleep(1)


@when('I click "{button_id}" button')
def step_impl(context, button_id):
    login_btn = context.browser.find_element_by_xpath(
        '//button[@id="{button_id}"]'.format(button_id=button_id)
    )
    login_btn.click()
    time.sleep(3)


@then('the home page is displayed')
def step_impl(context):
    context.browser.find_element_by_xpath(
        '//table[@id="customers"]'
    )
