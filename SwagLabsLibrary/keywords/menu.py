from SeleniumLibrary import timedelta, SeleniumLibrary
from robot.api.deco import keyword
from web.webactions import WebActions
from SwagLabsLibrary.locators.menulocators import BURGER_BTN, CLOSE_BTN, LOGOUT, MENU_ITEMS_LABLE

from SwagLabsLibrary.timeouts import GLOBAL_SWAGLABS_TIMEOUT

class Menu:
    
    def __init__(self, selib: SeleniumLibrary):
        self.__wa = WebActions(ctx=selib, timeout=GLOBAL_SWAGLABS_TIMEOUT)
        
    @keyword
    def logout_from_swaglabs(self):
        """Logout from swaglabs.
            
            Example:
            | Logout from swaglabs |
        """
        self.__open_menu()
        self.__wa.click(locator=LOGOUT)
        
    @keyword
    def menu_items_should_have(self, *args):
        """Validates that ``args`` are displayed in the menu.

            Arguments:
            - ``args``: The expected items that should be displayed in the menu.
            
            Example:
            | Menu Items Should Have | About Logout Reset${SPACE}App${SPACE}State |
        """
        self.__open_menu()
        act_texts = [i.text for i in self.__selib.find_elements(locator=MENU_ITEMS_LABLE)]
        if not all(text in act_texts for text in list(args)):
            raise AssertionError("")
        
    def __open_menu(self):
        if self.__wa.is_visible(locator=BURGER_BTN, timeout=timedelta(seconds=2)):
            self.__wa.click(locator=BURGER_BTN)
            self.__wa.wait_until_visible(locator=CLOSE_BTN)