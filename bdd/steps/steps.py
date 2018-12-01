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
    time.sleep(1)


@then('the home page is displayed')
def step_impl(context):
    context.browser.find_element_by_xpath(
        '//table[@id="customers"]'
    )


@when('I click {"add-new-car"} button')
def step_impl(context, button_id):
    login_btn = context.browser.find_element_by_xpath(
        '//button[@id="{add-new-car}"]'.format(button_id=button_id)
    )
    login_btn.click()
    time.sleep(1)


@when('I select "{value}" from "{select_id}" select')
def step_impl(context, value, select_id):
    sel = context.browser.find_element_by_xpath(
        '//select[@id="{select_id}"]/option[text()="{value}"]'
        .format(select_id=select_id, value=value)
    )
    sel.click()
    time.sleep(1)


@when('I click Zapisz')
def step_impl(context):
    zapisz_button = context.browser.find_element_by_xpath(
        '//button[text()="Zapisz"]'
    )
    zapisz_button.click()
    time.sleep(1)


@then('there is a car: brand "{brand}", model "{model}", year "{year}"')
def step_impl(context, brand, model, year):
    context.browser.find_element_by_xpath(
        '//table[@id="customers"]'
        '//tr[td[@class="brand"][text()="{brand}"]]'
        '[td[@class="model"][text()="{model}"]]'
        '[td[@class="year"][text()="{year}"]]'
        .format(brand=brand, model=model, year=year)
    )
