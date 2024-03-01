# Project on testing automation of the site [LITRES](https://www.litres.ru/)

<img src="resources/images/ui/main_page_litres.png">

## The checklist
### UI

  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Authorization in the desktop version of the site
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">The search on the site 
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">The product search filter 
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Go through the book catalog 
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">View the description of the book 
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Add the book to your favorites - a bug has been found
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Add the book to your cart

### API
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Аuthorization on the site
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Put the book in the cart
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Add a book to favorites
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Perform a book search 

### Mobile
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Log in to the app
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">Perform an in-app search
  - <img src="resources/images/other/ok.png" height="20" width="20" align="center">To search for a book in the application by an authorized user and put it in the trash

## Technologies and tools

<p align="center">

<img src="resources/images/logo/pycharm.png" width="9%">
<img src="resources/images/logo/python.svg" width="8%">
<img src="resources/images/logo/selene.png" width="9%">
<img src="resources/images/logo/pytest.png" width="9%">
<img src="resources/images/logo/Allure.svg" width="8%">
<img src="resources/images/logo/Allure_TO.svg" width="8%"></br>
<img src="resources/images/logo/GitHub.svg" width="8%">
<img src="resources/images/logo/jenkins.png" width="8%">
<img src="resources/images/logo/appium.png" width="11%">
<img src="resources/images/logo/request.png" width="8%">
<img src="resources/images/logo/bstack.png" width="11%">
<img src="resources/images/logo/selenoid.png" width="8%">
<img src="resources/images/logo/jira.svg" width="8%">
<img src="resources/images/logo/telegram.svg" width="8%">
</p>

## Running tests
#### All UI tests are run remotely on Selenoid
### Locally:
1) Clone the [repository](https://github.com/AlexD120/Litres_shop.git)
2) Open the project in PyCharm
3) Enter the command in the terminal  

```python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
### Remote:
## <img src="resources/images/logo/jenkins.png" height="30" width="30" align="center"> Jenkins

1) To run tests, go to [Jenkins](https://jenkins.autotests.cloud/job/Davydov_litres_shop_/) job and Click 'Build with parameters'

<img src="resources/images/ui/main_page_jenkins.png">

2) Select the necessary parameters and run 'Build'
* To launch, we have the following options:
  - [x] UI tests
  - [x] API tests
  - [x] Mobile tests
  - [x] All tests

<img src="resources/images/ui/build_page_jenkins.png">


## <img src="resources/images/logo/Allure.svg" height="30" width="30" align="center"> Allure

> *Allure Framework is an easy and flexible multi-language test report tool that not only shows a very concise representation of what have been tested in a neat web report form, but it also gives each team member a possibility to extract maximum of useful information from tests execution.*

### There are several ways to run the report, [here](https://jenkins.autotests.cloud/job/Davydov_litres_shop_/allure/) are some of them:
<img src="resources/images/ui/run_allure_of_jenkins.png">

### Overview:
*Graphs, metrics, and statistics let you to analyze test results*

<img src="resources/images/ui/allure_overview.png">

### Suites:
1) *And also the detailed result of the tests is displayed*
<img src="resources/images/ui/allure_suites.png">


2) *For more clarity, a screenshot of the test result is available to you*
<img src="resources/images/ui/allure_screenshot.png">


3) *Video recording of the Web autotest*
<img src="resources/images/ui/allure_video.gif">

4) *And also, a video recording of the passage of mobile autotests through BrowserStack <img src="resources/images/logo/bstack.png" width="6%">* 
<img src="resources/images/mobile/bstack.gif">

## <img src="resources/images/logo/Allure_TO.svg" height="30" width="30" align="center"> Allure Testops
> *It is a Test management System (TMS) that allows you to manage both manual and automated testing. It is focused on automation and DevOps, and provides centralized management of tests, reporting and analytics.*

### There are several ways to run allure testOps, for example by clicking [here](https://allure.autotests.cloud/project/3973/dashboards)
<img src="resources/images/ui/run_alluteto_of_jenkins.png">

### Dashboard:
 *Dashboard with the test cases statuses on Allure TestOps:*
<img src="resources/images/ui/allureto_dashboard.png">

### Test Cases:
<img src="resources/images/ui/allureto_test_cases.png">

## <img src="resources/images/logo/jira.svg" height="30" width="30" align="center"> Jira
> *It is a project management and bug tracking system*

### All tests integrated with Jira to check statuses and activity
<img src="resources/images/ui/jira.png">


## <img src="resources/images/logo/telegram.svg" height="30" width="30" align="center"> Telegram notification
> *Test results notifications to be sent to the specific telegram channel by the telegram bot*

<img src="resources/images/ui/telegram_result.png" width="250" height="300">

