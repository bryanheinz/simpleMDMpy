#!/usr/bin/env python3

import plistlib
import settings
import unittest
import SimpleMDMpy


@unittest.skipIf(settings.profile_id == '',
    "profile_id not specified in settings.py.")
class TestCustomConfigurationProfiles(unittest.TestCase):
    def test_get_profile(self):
        profile_found = False
        all_profiles = SimpleMDMpy.CustomConfigurationProfiles(
            settings.api_key).get_profiles()
        for prof in all_profiles:
            prof_id = str(prof.get('id', ''))
            if prof_id == settings.profile_id: profile_found = True
        self.assertTrue(profile_found)
    
    def test_download_profile(self):
        # if settings.profile_id == '':
        profile = SimpleMDMpy.CustomConfigurationProfiles(settings.api_key) \
            .download_profile(settings.profile_id)
        self.assertIsInstance(plistlib.loads(profile), dict)


if __name__ == '__main__':
    unittest.main()
