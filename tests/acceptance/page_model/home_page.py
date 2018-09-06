from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'


    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)
        # need to pass in *args since find_element is expecting 2 parameters
        # and we are passing in a single tuple
        # this will deconstruct the tuple into 2 single arguments

