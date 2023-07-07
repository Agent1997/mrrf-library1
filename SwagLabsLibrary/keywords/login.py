from typing import Any
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from web.webactions import WebActions
from corelibs.AssertsLibrary import assert_equal
from SwagLabsLibrary.locators.loginlocators import ERROR_DISPLAY, LOGIN_BTN, PASSWORD_FLD, USERNAME_FLD

from SwagLabsLibrary.timeouts import GLOBAL_SWAGLABS_TIMEOUT

class Login:

    def __init__(self, selib: SeleniumLibrary):
        self.__wa = WebActions(ctx=selib, timeout=GLOBAL_SWAGLABS_TIMEOUT)
        
    @keyword(tags=("LoginKeywords",))
    def wait_until_login_page_is_visible(self, timeout: Any = None):
        """Wait until login page is visible.

            Arguments:
            - ``timeout``: Specific maximum time to wait before raising an exception if not visible. Defaults to None.

            Example:
            | Wait Until Login Page Is Visible | timeout=5s |
            | Wait Until Login Page Is Visible |            |
        """
        self.__wa.wait_until_visible(locator=LOGIN_BTN)

    @keyword(tags=("LoginKeywords",))
    def login_to_swaglabs(self, username: str = None, password: str = None):
        """Login to Swaglabs using the provided ``username`` and ``password``. This will click the login button
           even when no ``username`` and/or ``password`` were provided.

            Arguments:
            - ``username``: Username to use for login.
            - ``password``: Password to use for login.
            
            Example:
            | Login To SwagLabs | username=standard_user | password=secret_sauce |
        """
        self.wait_until_login_page_is_visible()

        if username is not None:
            self.__wa.input_text(locator=USERNAME_FLD, text=username)
        if password is not None:
            self.__wa.input_text(locator=PASSWORD_FLD, text=password)
        self.__wa.click(locator=LOGIN_BTN)
        
    @keyword(tags=("LoginKeywords", "AssertionKeywords"))
    def login_error_msg_should_be(self, err_msg: str):
        """Validates that the displayed error message in the login page match ``err_msg``.

            Arguments:
            - ``err_msg``: The exepcted error message.
            
            Example:
            | Login Error Msg Should Be | err_msg=Username is required. |
        """
        act_err = self.__wa.get_text(locator=ERROR_DISPLAY)
        assert_equal(actual=act_err, exp=err_msg)
