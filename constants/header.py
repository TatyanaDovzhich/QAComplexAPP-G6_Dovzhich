class HeaderConsts:
    """Stores constants related to header"""

    CREATE_POST_BUTTON_XPATH = ".//a[@href='/create-post']"
    SIGN_OUT_BUTTON_TEXT = 'Sign Out'
    SIGN_OUT_BUTTON_XPATH = f".//button[text()='{SIGN_OUT_BUTTON_TEXT}']"
    # MY_PROFILE_BUTTON_XPATH = ".//a[@class='mr-2']"
    MY_PROFILE_BUTTON_XPATH = ".//a[@href='/profile/{username}']"
    OPEN_CHAT_XPATH = ".//*[@data-icon='comment']"
