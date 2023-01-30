"""Tests related to chat"""
import logging
from asyncio import sleep

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestChat:
    log = logging.getLogger("[CreatePostPage]")

    @pytest.fixture()
    def hello_page(self, start_page, random_user):
        """Sign Up as the user and return the page"""
        return start_page.sign_up_and_verify(random_user)

    def test_chat(self, hello_page):
        """
        - Pre-conditions:
            - Sign Up/Sign In as an user
        - Steps:
            - Open chat
            - Send message
            - Verify message
            - Send one more message
            - Verify messages
        """
        # Open chat
        chat = hello_page.header.open_chat()

        expected_messages = []

        # Send message
        for index in range(20)
            message = f"Hello{index}"

            # Send message
            expected_messages.append(message)
            hello_page.chat.send_message(text=message)

            # Verify message
            hello_page.chat.verify_messages(expected_messages)

        sleep(5)
