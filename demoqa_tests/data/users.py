import dataclasses
import enum


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: str
    mobile: str
    date_of_birth: []
    subject: str
    hobby: enum
    file: str
    address: str
    state: str
    city: str


student_filatova = User(first_name='Veronika',
                        last_name='Filatova',
                        user_email='Veronika_Fila@mail.com',
                        gender='Female',
                        mobile='9999872282',
                        date_of_birth=['21', 'May', '1996'],
                        subject='Chemistry',
                        hobby='Reading',
                        file='girafe.jpg',
                        address='41 Eastern Avenue APT 243 San Francisco, 77338',
                        state='Rajasthan',
                        city='Jaiselmer'
                        )
