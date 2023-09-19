from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage

def test_success_registration_form():
    registration_page = RegistrationPage()
    student = User(
        first_name="Sveta",
        last_name="Ko",
        email="sko@test.com",
        gender="Female",
        phone_number="8999222334",
        birth_year="2000",
        birth_month="September",
        birth_day="1",
        subject="History",
        hobby="Sports",
        picture="student.jpeg",
        current_adress="First 11-1",
        state="NCR",
        city="Delhi",
    )

    registration_page.open()

    registration_page.register_user(student)

    registration_page.should_have_registered(student)

