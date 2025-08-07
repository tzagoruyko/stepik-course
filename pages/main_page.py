from .base_page import BasePage

class MainPage(BasePage): #так как мы перенесли все методы класса в base_page, то тут оставили просто заглушку
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

