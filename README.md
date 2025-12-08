# Фреймворк для автоматизации тестирования сайта "godev.agency"
> <a target="_blank" href="https://godev.agency/">godev.agency</a>

![main page screenshot](page_elements/add_files_in_form_request/godev_logo.jpg)

----

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов в Selenoid
* Запуск тестов на dev и prod контурах

### Список проверок, реализованных в web/UI автотестах

- [x] Проверки метатегов - title, descr, canonical
- [x] Проверки линков на всех страницах
- [x] Проверка успешной отправки заявки
- [x] Проверка негативных кейсов отправки заявок
- [x] Проверка работоспособности меню


----

### Используемый стэк

<img title="Python" src="page_elements/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="page_elements/icons/pytest-original.svg" height="40" width="40"/> <img title="Jira" src="page_elements/icons/jira-original.svg" height="40" width="40"/> <img title="Allure Report" src="page_elements/icons/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="page_elements/icons/AllureTestOps.png" height="40" width="40"/> <img title="GitHub" src="page_elements/icons/github-original.svg" height="40" width="40"/> <img title="Selenoid" src="page_elements/icons/selenoid.png" height="40" width="40"/> <img title="Selenium" src="page_elements/icons/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="page_elements/icons/selene.png" height="40" width="40"/> <img title="Pycharm" src="page_elements/icons/pycharm.png" height="40" width="40"/> <img title="Telegram" src="page_elements/icons/tg.png" height="40" width="40"/> <img title="Jenkins" src="page_elements/icons/jenkins-original.svg" height="40" width="40"/>

----

### Локальный запуск автотестов

#### Для запуска web/UI автотестов выполнить в cli:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests
```

#### Получение отчёта:
```bash
allure allure serve tests/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/">Ссылка</a>

#### Параметры сборки
```python
ENVIRONMENT = ['development', 'PROD_PAGE'] # Окружение
BROWSER_VERSION = '127.0' # Версия браузера хром. Можно запускать на 128.0
```
#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/">проект</a>

![jenkins project main page](/page_elements/allure_report_and_jenkins/jenkins_project_main_page.png)

1. Нажать "Build with Parameters"
2. Из списка "ENVIRONMENT" выбрать окружение
3. В поле "BROWSER_VERSION" ввести версию браузера (запуск возможен в 128.0 и 127.0 версиях)
4. Нажать "Build"

![jenkins_build](/page_elements/allure_report_and_jenkins/start_job_in_jenkins.png)

----

### Allure отчет

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/">Открытие отчета после сборки</a>
![allure_report_after_work_job](/page_elements/allure_report_and_jenkins/allure_report_after_work_job.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/24/allure/">Общие результаты</a>
![allure_report_overview](/page_elements/allure_report_and_jenkins/allure_report_overview.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/Ivi-mobile-and-UI-Auto-Tests/15/allure/#suites">Результаты прохождения теста</a>

![allure_reports_behaviors](/page_elements/allure_report_and_jenkins/allure_reports_behaviors.png)

#### <a target="_blank" href="https://jenkins.autotests.cloud/job/godev_agency_tests/24/allure/#graph">Графики</a>


![allure_reports_graphs](/page_elements/allure_report_and_jenkins/allure_reports_graphs_1.png)
![allure_reports_graphs](/page_elements/allure_report_and_jenkins/allure_reports_graphs_2.png)

----

### Оповещения в Telegram
![telegram_allert](/page_elements/allure_report_and_jenkins/telegram_allert.png)

----

### Видео прохождения web/UI автотеста
![autotest_gif](/page_elements/allure_report_and_jenkins/autotest.gif)

----
