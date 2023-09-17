from selene import browser, have
from selene.core.command import js
from demoqa_tests.pages.registration_page import RegistrationPage


def test_success_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.fill_first_name("Sveta")
    registration_page.fill_last_name("Ko")
    registration_page.fill_email("sko@test.ru")

    registration_page.set_gender("Female")

    registration_page.fill_phone_number("89992223344")

    registration_page.fill_date_of_birth("2000", "September", "1")

    registration_page.fill_subject("History")
    registration_page.select_hobby("Sports")

    registration_page.add_picture("student.png")

    registration_page.fill_current_adress("First st. 11-1")

    registration_page.select_state("NCR")
    registration_page.select_city("Moscow")

    browser.element("#submit").perform(command=js.click)

    # THEN
    registration_page.table_title_name.should(
        have.text("Thanks for submitting the form")
    )

    registration_page.registration_user_data.should(
        have.exact_texts(
            "Sveta Ko",
            "skot@test.ru",
            "Female",
            "89992223344",
            "01 September,2000",
            "History",
            "Sports",
            "student.png",
            "First st. 11-1",
            "NCR Moscow",
        )
    )
