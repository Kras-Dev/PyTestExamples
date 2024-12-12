# PyTest Examples Project

This is a project that contains tests for the pet store API and UI profile functionality.

## Description

This project implements tests using the `pytest` `requests` `allure` libraries. The tests check the following aspects:

- User profile functionality.
- API for managing pet data in the store.

## Resources Tested

We tested the following resources in our automated tests:
- [Swagger Petstore](https://petstore.swagger.io/#/): Used for API testing.
- [OrangeHRM](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login): Used for web interface testing.

## How to start

1. Clone the repository to your local computer.
2. Install the required dependencies.
```pip install -r requirements.txt```
3. To run tests, use the following command:
```python -m pytest --alluredir=allure-results```
4. To view Allure reports after running tests, run the following commands:
```allure serve allure-results```