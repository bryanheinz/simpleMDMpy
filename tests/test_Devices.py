#!/usr/bin/env python3
import settings
import unittest
import SimpleMDMpy

class TestDevices(unittest.TestCase):
    def test_get_device(self):
        all_devices = SimpleMDMpy.Devices(
            settings.api_key).get_device(include_awaiting_enrollment=True)
        self.assertGreaterEqual(len(all_devices), 1)
        # print(len(all_devices))
        cid = all_devices[0].get('id')
        self.assertIsNotNone(cid)
        single_device = SimpleMDMpy.Devices(settings.api_key) \
            .get_device(device_id=cid)
        self.assertEqual(single_device.get('id'), cid)
    
    def test_list_profiles(self):
        device_profiles = SimpleMDMpy.Devices(settings.api_key) \
            .list_profiles(settings.device_id)
        self.assertGreaterEqual(len(device_profiles), 1)
    
    def test_list_users(self):
        device_users = SimpleMDMpy.Devices(settings.api_key) \
            .list_users(settings.device_id)
        self.assertGreaterEqual(len(device_users), 1)


if __name__ == '__main__':
    unittest.main()
