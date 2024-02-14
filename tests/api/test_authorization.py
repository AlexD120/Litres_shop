import os
import allure
from dotenv import load_dotenv
from litres_shop_test.schema import schemas
from jsonschema import validate


@allure.title('Successful user authentication via email')
@allure.feature('Email Authentication')
@allure.story('User, to successfully authenticated using email credentials.')
@allure.label('API')
@allure.tag('smoke', 'regress', 'API', 'registration')
@allure.severity('critical')
@allure.label("owner", "Davydov")
def test_authorization(api_request):
    load_dotenv()
    login = os.getenv('LOGIN_USER')
    password = os.getenv('PASSWORD_USER')

    url = "/auth/login"
    data = {"login": login, "password": password}
    response = api_request(url, method='POST', data=data)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.post_authorization_schema)
    assert body['error'] is None
