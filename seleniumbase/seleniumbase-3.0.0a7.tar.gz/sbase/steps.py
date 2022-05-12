from behave import step


@step("Open '{url}'")
@step('Open "{url}"')
@step("Open URL '{url}'")
@step('Open URL "{url}"')
def open_url(context, url):
    sb = context.sb
    sb.open(url)


@step("Click '{selector}'")
@step('Click "{selector}"')
@step("Click element '{selector}'")
@step('Click element "{selector}"')
def click_element(context, selector):
    sb = context.sb
    sb.click(selector)


@step("Type text '{text}' into '{selector}'")
@step('Type text "{text}" into "{selector}"')
@step("Type text '{text}' into \"{selector}\"")
@step('Type text "{text}" into \'{selector}\'')
def type_text(context, text, selector):
    sb = context.sb
    sb.type(selector, text)


@step("Add text '{text}' into '{selector}'")
@step('Add text "{text}" into "{selector}"')
@step("Add text '{text}' into \"{selector}\"")
@step('Add text "{text}" into \'{selector}\'')
def add_text_into_element(context, text, selector):
    sb = context.sb
    sb.add_text(selector, text)


@step("Into '{selector}' type '{text}'")
@step('Into "{selector}" type "{text}"')
@step("Into '{selector}' type \"{text}\"")
@step('Into "{selector}" type \'{text}\'')
def into_element_type_text(context, selector, text):
    sb = context.sb
    sb.type(selector, text)


@step("Into '{selector}' add '{text}'")
@step('Into "{selector}" add "{text}"')
@step("Into '{selector}' add \"{text}\"")
@step('Into "{selector}" add \'{text}\'')
def into_element_add_text(context, selector, text):
    sb = context.sb
    sb.add_text(selector, text)


@step("Assert element '{selector}'")
@step('Assert element "{selector}"')
def assert_element(context, selector):
    sb = context.sb
    sb.assert_element(selector)


@step("Assert text '{text}' in '{selector}'")
@step('Assert text "{text}" in "{selector}"')
@step("Assert text '{text}' in \"{selector}\"")
@step('Assert text "{text}" in \'{selector}\'')
def assert_text_in_element(context, text, selector):
    sb = context.sb
    sb.assert_text(text, selector)


@step("Assert text '{text}'")
@step('Assert text "{text}"')
def assert_text(context, text):
    sb = context.sb
    sb.assert_text(text)


@step("Assert exact text '{text}' in '{selector}'")
@step('Assert exact text "{text}" in "{selector}"')
def assert_exact_text(context, text, selector):
    sb = context.sb
    sb.assert_exact_text(text, selector)


@step("Highlight '{selector}'")
@step('Highlight "{selector}"')
@step("Highlight element '{selector}'")
@step('Highlight element "{selector}"')
def highlight_element(context, selector):
    sb = context.sb
    sb.highlight(selector)


@step("Click link '{link}'")
@step('Click link "{link}"')
def click_link(context, link):
    sb = context.sb
    sb.click_link(link)


@step("JS click '{selector}'")
@step('JS click "{selector}"')
@step("JS click element '{selector}'")
@step('JS click element "{selector}"')
def js_click(context, selector):
    sb = context.sb
    sb.js_click(selector)


@step("Save screenshot to logs")
@step('Save a screenshot to the logs')
def save_screenshot_to_logs(context):
    sb = context.sb
    sb.save_screenshot_to_logs()


@step("Refresh page")
def refresh_page(context):
    sb = context.sb
    sb.refresh_page()


@step("Go back")
def go_back(context):
    sb = context.sb
    sb.go_back()


@step("Go forward")
def go_forward(context):
    sb = context.sb
    sb.go_forward()


@step("JS type text '{text}' into '{selector}'")
@step('JS type text "{text}" into "{selector}"')
@step("JS type text '{text}' into \"{selector}\"")
@step('JS type text "{text}" into \'{selector}\'')
def js_type(context, text, selector):
    sb = context.sb
    sb.js_type(selector, text)


@step("Set value of '{selector}' to '{text}'")
@step('Set value of "{selector}" to "{text}"')
@step("Set value of \"{selector}\" to '{text}'")
@step('Set value of \'{selector}\' to "{text}"')
def set_value(context, text, selector):
    sb = context.sb
    sb.set_value(selector, text)


@step("Switch to iframe '{frame}'")
@step('Switch to iframe "{frame}"')
@step("Switch to frame '{frame}'")
@step('Switch to frame "{frame}"')
def switch_to_frame(context, frame):
    sb = context.sb
    sb.switch_to_frame(frame)


@step("Switch to default content")
@step("Exit from iframes")
@step("Exit from frames")
def switch_to_default_content(context):
    sb = context.sb
    sb.switch_to_default_content()


@step("Switch to parent frame")
@step("Exit current iframe")
@step("Exit current frame")
def switch_to_parent_frame(context):
    sb = context.sb
    sb.switch_to_parent_frame()


@step("Into '{selector}' enter MFA code '{totp_key}'")
@step('Into "{selector}" enter MFA code "{totp_key}"')
@step("Into '{selector}' enter MFA code \"{totp_key}\"")
@step('Into "{selector}" enter MFA code \'{totp_key}\'')
def enter_mfa_code(context, selector, totp_key):
    sb = context.sb
    sb.enter_mfa_code(selector, totp_key)


@step("Open if not '{url}'")
@step('Open if not "{url}"')
@step("Open if not URL '{url}'")
@step('Open if not URL "{url}"')
def open_if_not_url(context, url):
    sb = context.sb
    sb.open_if_not_url(url)


@step("Select if unselected '{selector}'")
@step('Select if unselected  "{selector}"')
def select_if_unselected(context, selector):
    sb = context.sb
    sb.select_if_unselected(selector)


@step("Unselect if selected '{selector}'")
@step('Unselect if selected  "{selector}"')
def unselect_if_selected(context, selector):
    sb = context.sb
    sb.unselect_if_selected(selector)


@step("Check if unchecked '{selector}'")
@step('Check if unchecked  "{selector}"')
def check_if_unchecked(context, selector):
    sb = context.sb
    sb.check_if_unchecked(selector)


@step("Uncheck if checked '{selector}'")
@step('Uncheck if checked  "{selector}"')
def uncheck_if_checked(context, selector):
    sb = context.sb
    sb.uncheck_if_checked(selector)


@step("Drag '{drag_selector}' into '{drop_selector}'")
@step('Drag "{drag_selector}" into "{drop_selector}"')
@step("Drag '{drag_selector}' into \"{drop_selector}\"")
@step('Drag "{drag_selector}" into \'{drop_selector}\'')
def drag_and_drop(context, drag_selector, drop_selector):
    sb = context.sb
    sb.drag_and_drop(drag_selector, drop_selector)


@step("Hover '{hover_selector}' and click '{click_selector}'")
@step('Hover "{hover_selector}" and click "{click_selector}"')
@step("Hover '{hover_selector}' and click \"{click_selector}\"")
@step('Hover "{hover_selector}" and click \'{click_selector}\'')
def hover_and_click(context, hover_selector, click_selector):
    sb = context.sb
    sb.hover_and_click(hover_selector, click_selector)


@step("Find '{selector}' and select '{text}'")
@step('Find "{selector}" and select "{text}"')
@step("Find '{selector}' and select \"{text}\"")
@step('Find "{selector}" and select \'{text}\'')
def select_option_by_text(context, selector, text):
    sb = context.sb
    sb.select_option_by_text(selector, text)


@step("Find '{selector}' and select '{text}' by {option}")
@step('Find "{selector}" and select "{text}" by {option}')
@step("Find '{selector}' and select \"{text}\" by {option}")
@step('Find "{selector}" and select \'{text}\' by {option}')
def select_option_by_option(context, selector, text, option):
    sb = context.sb
    if option.startswith("'") or option.startswith('"'):
        option = option[1:]
    if option.endswith("'") or option.endswith('"'):
        option = option[:-1]
    if option == "text":
        sb.select_option_by_text(selector, text)
    elif option == "index":
        sb.select_option_by_index(selector, text)
    elif option == "value":
        sb.select_option_by_value(selector, text)
    else:
        raise Exception("Unknown option: %s" % option)


@step("Wait for '{selector}'")
@step('Wait for "{selector}"')
@step("Wait for element '{selector}'")
@step('Wait for element "{selector}"')
def wait_for_element(context, selector):
    sb = context.sb
    sb.wait_for_element(selector)


@step("Double click '{selector}'")
@step('Double click "{selector}"')
@step("Double click element '{selector}'")
@step('Double click element "{selector}"')
def double_click_element(context, selector):
    sb = context.sb
    sb.double_click(selector)


@step("Slow click '{selector}'")
@step('Slow click "{selector}"')
@step("Slow click element '{selector}'")
@step('Slow click element "{selector}"')
def slow_click_element(context, selector):
    sb = context.sb
    sb.slow_click(selector)


@step("Clear text field '{selector}'")
@step('Clear text field "{selector}"')
def clear_text_field(context, selector):
    sb = context.sb
    sb.clear(selector)


@step("Maximize window")
def maximize_window(context):
    sb = context.sb
    sb.maximize_window()


@step("Get new driver")
def get_new_driver(context):
    sb = context.sb
    sb.get_new_driver()


@step("Switch to default driver")
def switch_to_default_driver(context):
    sb = context.sb
    sb.switch_to_default_driver()


@step("Press up arrow")
def press_up_arrow(context):
    sb = context.sb
    sb.press_up_arrow()


@step("Press down arrow")
def press_down_arrow(context):
    sb = context.sb
    sb.press_down_arrow()


@step("Press left arrow")
def press_left_arrow(context):
    sb = context.sb
    sb.press_left_arrow()


@step("Press right arrow")
def press_right_arrow(context):
    sb = context.sb
    sb.press_right_arrow()


@step("Delete cookies")
@step("Delete all cookies")
def delete_all_cookies(context):
    sb = context.sb
    sb.delete_all_cookies()


@step("Clear Local Storage")
def clear_local_storage(context):
    sb = context.sb
    sb.clear_local_storage()


@step("Clear Session Storage")
def clear_session_storage(context):
    sb = context.sb
    sb.clear_session_storage()
