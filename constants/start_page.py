class StartPageConst:
    """Stores constants related to start page"""

    # Sign In
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT = 'Sign In'
    SIGN_IN_BUTTON_XPATH = f".//button[text()='{SIGN_IN_BUTTON_TEXT}']"
    SIGN_IN_ERROR_TEXT = "Error"
    SIGN_IN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"

    # Sign Up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    # Sign Up USING Empty Fields
    SIGN_UP_USERNAME_EMPTY_TEXT = 'Username must be at least 3 characters'
    SIGN_UP_USERNAME_EMPTY_XPATH = f".//div[contains(text(),'{SIGN_UP_USERNAME_EMPTY_TEXT}')]"
    SIGN_UP_EMAIL_EMPTY_TEXT = 'You must provide a valid email address.'
    SIGN_UP_EMAIL_EMPTY_XPATH = f".//div[contains(text(),'{SIGN_UP_EMAIL_EMPTY_TEXT}')]"
    SIGN_UP_PASSWORD_EMPTY_TEXT = 'Password must be at least 12 characters.'
    SIGN_UP_PASSWORD_EMPTY_XPATH = f".//div[contains(text(),'{SIGN_UP_PASSWORD_EMPTY_TEXT}')]"
    # Sign Up USING Exists Data
    SIGN_UP_USERNAME_EXIST_TEXT = 'That username is already taken.'
    SIGN_UP_USERNAME_EXIST_XPATH = f".//div[contains(text(),'{SIGN_UP_USERNAME_EXIST_TEXT}')]"
    SIGN_UP_EMAIL_EXIST_TEXT = 'That email is already being used.'
    SIGN_UP_EMAIL_EXIST_XPATH = f".//div[contains(text(),'{SIGN_UP_EMAIL_EXIST_TEXT}')]"
    # Sign Up USING Invalid Data
    SIGN_UP_USERNAME_INVALID_DATA_TEXT = 'Username can only contain letters and numbers.'
    SIGN_UP_USERNAME_INVALID_XPATH = f".//div[contains(text(),'{SIGN_UP_USERNAME_INVALID_DATA_TEXT}')]"
    SIGN_UP_EMAIL_INVALID_DATA_TEXT = 'You must provide a valid email address.'
    SIGN_UP_EMAIL_INVALID_DATA_XPATH = f".//div[contains(text(),'{SIGN_UP_EMAIL_INVALID_DATA_TEXT}')]"
    SIGN_UP_PASSWORD_INVALID_DATA_TEXT = 'Password must be at least 12 characters.'
    SIGN_UP_PASSWORD_INVALID_DATA_XPATH = f".//div[contains(text(),'{SIGN_UP_PASSWORD_INVALID_DATA_TEXT}')]"
