import allure

from demoqa_tests.data.users import student_filatova
from demoqa_tests.pages.registration_page import RegistrationPage

@allure.tag('Web')
@allure.label('owner', 'Karelova Ekaterina')
@allure.feature('Регистрация пользователя')
@allure.link('https://demoqa.com/automation-practice-form')
def test_registration_form(setup_browser):
    registration_page = RegistrationPage()

    with allure.step('Открываем страницу для заполнения формы регистрации'):
        registration_page.open()

    with allure.step(f'Заполняем форму регистрации данными пользователя "{student_filatova.last_name}"'):
        registration_page.fill_registration_form(student_filatova)

    with allure.step('Подтверждение успешной регистрации пользователя'):
        registration_page.should_title_registered_the_form()

    with allure.step('Проверяем, что отправленные данные о пользователе корректны'):
        registration_page.should_registered_user_with(student_filatova)
