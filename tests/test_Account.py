#!/usr/bin/env python3

import settings
import unittest
import SimpleMDMpy


class TestCustomConfigurationProfiles(unittest.TestCase):
    def test_get_account_details(self):
        account_details = SimpleMDMpy.Account(settings.api_key) \
            .get_account_details()
        account_name = account_details.get('attributes', {}).get('name')
        self.assertIsNotNone(account_name)

if __name__ == '__main__':
    unittest.main()
