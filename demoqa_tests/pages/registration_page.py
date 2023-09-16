from selene import browser, have, by
import os

from selene.core.command import js

import tests
import pytest

from demoqa_tests.data.users import User


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def set_gender(self, value):
        browser.all("[for^=gender-radio]").element_by(have.exact_text(value)).click()
        return self

    def fill_phone_number(self, value):
        browser.element("#userNumber").type("8999123212")
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.all(".react-datepicker__month-select>option").element_by(
            have.exact_text(month)
        ).click()
        browser.all(".react-datepicker__year-select>option").element_by(
            have.exact_text(year)
        ).click()
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_subject(self, value):
        browser.element("#subjectsInput").type("History").press_enter()
        return self

    def select_hobby(self, value):
        browser.all(".custom-checkbox").element_by(have.exact_text("Sports")).click()
        return self

    def add_picture(self, file_name):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f"resources/{file_name}")
            )
        )
        return self

    def fill_current_adress(self, value):
        browser.element("#currentAddress").type("Testovaya st. 43-33")
        return self

    def select_state(self, value):
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text("NCR")
        ).click()
        return self

    def select_city(self, value):
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text("Delhi")
        ).click()
        return self

    def submit(self):
        browser.element("#submit").perform(command=js.click)
        return self

    @property
    def registration_user_data(self):
        return browser.element(".table").all("td").even

    @property
    def table_title_name(self):
        return browser.element("#example-modal-sizes-title-lg")

    def register_user(self, user: User):
        (
            self.fill_first_name(user.first_name)
            .fill_last_name(user.last_name)
            .fill_email(user.email)
            .set_gender(user.gender)
            .fill_phone_number(user.phone_number)
            .fill_date_of_birth(user.birth_year, user.birth_month, user.birth_day)
            .fill_subject(user.subject)
            .select_hobby(user.hobby)
            .add_picture(user.picture)
            .fill_current_adress(user.current_adress)
            .select_state(user.state)
            .select_city(user.city)
            .submit()
        )

    def should_have_registered(self, user: User):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.phone_number,
                f"{user.birth_day} {user.birth_month},{user.birth_year}",
                user.subject,
                user.hobby,
                user.picture,
                user.current_adress,
                f"{user.state} {user.city}",
            )
        )
