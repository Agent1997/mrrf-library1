from typing import Any
from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from web.webactions import WebActions
from SwagLabsLibrary.locators.productslocators import PAGE_TITLE

from SwagLabsLibrary.timeouts import GLOBAL_SWAGLABS_TIMEOUT

class Products:

    def __init__(self, selib: SeleniumLibrary):
        self.__wa = WebActions(ctx=selib, timeout=GLOBAL_SWAGLABS_TIMEOUT)

    @keyword(tags=("ProductsKeywords",))
    def wait_until_products_page_is_visible(self, timeout: Any = None):
        """Wait until product page is visible.

            Arguments:
            - ``timeout``: Specific maximum time to wait before raising an exception if not visible. Defaults to None.

            Example:
            | Wait Until Products Page Is Visible | timeout=5s |
            | Wait Until Products Page Is Visible |            |
        """
        self.__wa.wait_until_visible(locator=PAGE_TITLE)