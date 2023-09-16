from selene import browser, have, by
import os
import tests
import pytest


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_email(self, value):
        browser.element("#userEmail").type(value)

    def set_gender(self, value):
        browser.all("[for^=gender-radio]").element_by(have.exact_text(value)).click()

    def fill_phone_number(self, value):
        browser.element("#userNumber").type("8999123212")

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.all(".react-datepicker__month-select>option").element_by(
            have.exact_text(month)
        ).click()
        browser.all(".react-datepicker__year-select>option").element_by(
            have.exact_text(year)
        ).click()
        browser.element(f".react-datepicker__day--00{day}").click()

    def fill_subject(self, value):
        browser.element("#subjectsInput").type("History").press_enter()

    def select_hobby(self, value):
        browser.all(".custom-checkbox").element_by(have.exact_text("Sports")).click()

    def add_picture(self, file_name):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f"resources/{file_name}")
            )
        )

    def fill_current_adress(self, value):
        browser.element("#currentAddress").type("Testovaya st. 43-33")

    def select_state(self, value):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text("NCR")
        ).click()

    def select_city(self, value):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text("Delhi")
        ).click()

    @property
    def registration_user_data(self):
        return browser.element(".table").all("td").even

    @property
    def table_title_name(self):
        return browser.element("#example-modal-sizes-title-lg")
