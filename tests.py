import json
import unittest
import receiver


class WebhookTest(unittest.TestCase):
    def setUp(self):
        self.app = receiver.app.test_client()
        self.data = '{"repository": {"name": "test"}}'

    def test_get_index_returns_ok(self):
        response = self.app.get("/")
        assert 200 == response.status_code

    def test_post_index_returns_ok(self):
        response = self.app.post('/',
                                 data=self.data,
                                 headers={'content-type': 'application/json'})

if __name__ == '__main__':
    unittest.main()
