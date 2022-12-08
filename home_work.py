
def function_for_print(func, *args):
    name_function = func.__name__
    spysok = name_function.capitalize().split("_")
    print_name_function = " ".join(spysok)
    print(print_name_function, *args)


def open_browser(browser_name):
    function_for_print(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    function_for_print(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    function_for_print(find_registration_button_on_login_page, page_url, button_text)


if __name__ == '__main__':
    open_browser(browser_name="qa.guru")
    go_to_companyname_homepage(page_url="https://qa.guru")
    find_registration_button_on_login_page(page_url="https://qa.guru", button_text="Личный кабинет")