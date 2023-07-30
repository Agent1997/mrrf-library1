from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import keyword
from web.webactions import WebActions
from web.browserconfig import chrome_options

from SwagLabsLibrary.timeouts import GLOBAL_SWAGLABS_TIMEOUT
from SwagLabsLibrary.url import URLS

class Browser:
    
    def __init__(self, selib: SeleniumLibrary, env: str, is_headless: bool, is_incognito: bool):
        self.__env = env
        self.__is_headless = is_headless
        self.__is_incognito = is_incognito
        self.__wa = WebActions(ctx=selib, timeout=GLOBAL_SWAGLABS_TIMEOUT)
     
    @keyword(tags=("BrowserKeywords",))   
    def open_swaglabs_in_browser(self, is_headless: bool = None, browser: str = 'chrome'):
        """Opens the Swaglabs website in a browser.

            Arguments:
            - ``is_headless``: Whether to run the browser in headless mode. If None, will follow the configuration set when `Importing` the library.
            - ``browser``: The browser to use. Defaults to 'chrome'.

            Example:
            | Open Swaglabs in Browser | is_headless=${True} | browser=firefox |
        """
        is_headless = is_headless if is_headless is not None else self.__is_headless
        
        url = URLS.get(self.__env)
        
        if url is None:
            raise Exception(f"No url configured for {self.__env} environment.")
        
        if browser == 'chrome':
            options = chrome_options(is_headless=is_headless, is_incognito=self.__is_incognito)
        else:
            raise Exception(f"{browser} is not supported.")
        
        self.__wa.open_browser(url=url, browser=browser, options=options)
        
    @keyword
    def close_all_swaglabs_browser(self):
        """Close all swaglabs browser opened by this instance of the library.

            Example:
            | Close All Swaglabs Browser |
        """
        self.__wa.close_all_browsers()
        
    @keyword
    def reload_swaglabs_browser(self):
        """Reload current page.

            Example:
            | Reload Swaglabs Browser |
        """
        self.__wa.reload_browser()