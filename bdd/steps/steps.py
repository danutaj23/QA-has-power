from behave import *
import time


@given('the page is loaded')
def step_impl(context):
    context.browser.get('http://salon.rpgit.pl/')
    time.sleep(3)


@when('I fill username')
def step_impl(context):
    username_input = context.browser.find_element_by_xpath(
        '//input[@id="id_username"]'
    )
    username_input.send_keys('danuta.klos')
    time.sleep(3)


@when('I fill password')
def step_impl(context):
    password_input = context.browser.find_element_by_xpath(
        '//input[@id="id_password"]'
    )
    password_input.send_keys('Welcome1')
    time.sleep(3)


@when('I click Zaloguj')
def step_impl(context):
    login_btn = context.browser.find_element_by_xpath(
        '//button[@id="id_login_btn"]'
    )
    login_btn.click()
    time.sleep(1)


@then('the home page is displayed')
def step_impl(context):
    context.browser.find_element_by_xpath(
        '//table[@id="customers"]'
    )
