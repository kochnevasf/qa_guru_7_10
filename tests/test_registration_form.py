import pytest
from selene import browser, have, by
from selene.core.command import js
from selenium import webdriver
from demoqa_tests.pages.registration_page import RegistrationPage

browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)


def test_success_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.fill_first_name("Klava")
    registration_page.fill_last_name("Ivanova")
    registration_page.fill_email("ak_test@test.ru")

    registration_page.set_gender("Female")

    registration_page.fill_phone_number("8999123212")

    registration_page.fill_date_of_birth("2002", "September", "7")

    registration_page.fill_subject("History")
    registration_page.select_hobby("Sports")

    registration_page.add_picture("student.jpeg")

    registration_page.fill_current_adress("Testovaya st. 43-33")

    registration_page.select_state("NCR")
    registration_page.select_city("Delhi")

    browser.element("#submit").perform(command=js.click)

    # THEN
    registration_page.table_title_name.should(
        have.text("Thanks for submitting the form")
    )

    registration_page.registration_user_data.should(
        have.exact_texts(
            "Klava Ivanova",
            "ak_test@test.ru",
            "Female",
            "8999123212",
            "07 September,2002",
            "History",
            "Sports",
            "student.jpeg",
            "Testovaya st. 43-33",
            "NCR Delhi",
        )
    )
