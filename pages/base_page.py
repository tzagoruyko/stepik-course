from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException #это для метода solve_quiz_and_get_code
import math
class BasePage():
    def __init__(self, browser, url, timeout=10): # Здесь timeout=10 — это значение по умолчанию, т.е если ты не укажешь timeout при создании объекта, он автоматически будет равен 10
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # этот метод нужен был для заданий, где нужно посчитать результат математического выражения из алерта и ввести ответ
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

