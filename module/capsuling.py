from selene.support.shared import browser
from selene import have, command
import files
from pathlib import Path
from selenium.webdriver import Keys


def open_form():
    browser.open("/automation-practice-form")


def writ_data(*, name, lastname):
    browser.element('[id="firstName"]').type(name)  # записывает имя
    browser.element('[id="lastName"]').type(lastname)  # записывает фамилию


def email(*, email):
    browser.element('[id="userEmail"]').type(email)  # записывает почту


def male(*, Male):
    browser.element('[class="custom-control-label"]').should(have.text(Male)).click()  # выбирает пол


def number(*, phone):
    browser.element('[id="userNumber"]').type(phone)  # пишет номер


def hobbies(*, hobbi):
    if hobbi.lower() == 'sports':
        browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).click()  # хобби
    elif hobbi.lower() == 'reading':
        browser.element('[for="hobbies-checkbox-2"]').perform(command.js.scroll_into_view).click()
    elif hobbi.lower() == 'music':
        browser.element('[for="hobbies-checkbox-3"]').perform(command.js.scroll_into_view).click()


def subjects(*, subject):
    browser.element('[id="subjectsInput"]').type(subject).press_enter()


def birthInput(*, date):
    import sys
    browser.element('#dateOfBirthInput').send_keys(
        Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL, 'a'
    ).type(date).press_enter()


def resurse(*, photo):
    browser.element('#uploadPicture').set_value(
        str(Path(files.__file__).joinpath(photo).absolute()))


def address(*, Address):
    browser.element('[id="currentAddress"]').type(Address)


def state_city(*, state, city):
    browser.element('[id="react-select-3-input"]').type(state).press_enter()
    browser.element('[id="react-select-4-input"]').type(city).press_enter()
    browser.element('[id="submit"]').click()
