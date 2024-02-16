from selenium import webdriver
from selenium.webdriver.common.by import By

from models.books import Book
from pages.base.base_component import Button, Text, Input, Image
from pages.base.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver: webdriver, base_url):
        super().__init__(driver, base_url)

    def open_page(self, route='profile'):
        super().open_page(route)

        self.log_out = Button(self._driver,
                              locator="//button[@id='submit']",
                              name='Log out')

        self.username = Text(self._driver,
                             locator="//*[@id='userName-value']",
                             name='username')
        self.delete_account = Button(self._driver,
                                     locator="//*[@class='text-right button di']//button[@class='btn btn-primary']",
                                     name='Delete Account')
        self.input_search_book = Input(self._driver,
                                       locator="//input[@id='searchBox']",
                                       name='Search Books')

        self.image_book = Image(self._driver, locator="//div[@class='rt-tr-group']['{line}']//img",
                                name='Image book "{line}"')
        self.title_book = Text(self._driver,
                               locator="//div[@class='rt-tr-group']['{line}']//*[contains(@id, 'see-book-{title}')]",
                               name='Title book')

        self.author_book = Text(self._driver,
                                locator="//div[@class='rt-tr-group']['{line}']//div[text()='{author}']",
                                name='Author book')
        self.publisher = Text(self._driver,
                              locator="//div[@class='rt-tr-group']['{line}']//div[text()='{publisher}']",
                              name='Publisher')

    def assert_book_in_table(self, book: Book, line=1):
        self.image_book.assert_visibility(line=line)
        self.title_book.assert_visibility(line=line, title=book.title)
        self.author_book.assert_visibility(line=line, author=book.author)
        self.publisher.assert_visibility(line=line, publisher=book.publisher)


