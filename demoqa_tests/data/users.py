import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subject: str
    hobby: str
    picture: str
    current_adress: str
    state: str
    city: str
