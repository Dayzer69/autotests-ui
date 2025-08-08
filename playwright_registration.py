# python - m playwright_authorization


from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_field = page.get_by_test_id('registration-form-username-input').locator('input')
    username_field.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()


    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    expect(dashboard_title).to_be_visible()

    page.wait_for_timeout(3000)