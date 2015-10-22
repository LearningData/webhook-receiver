from unittest import TestCase, mock, main
import receiver


class WebhookTest(TestCase):
    def setUp(self):
        self.app = receiver.app.test_client()
        self.data = '{"repository": {\
                        "id": 43555702,\
                        "name": "name",\
                        "full_name": "username/repository",\
                        "owner": {\
                            "name": "username",\
                            "email": "test@test.com"\
                        }}}'
        self.patcher = mock.patch("receiver.Repository")
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_get_index_returns_ok(self):
        response = self.app.get("/")
        assert 200 == response.status_code

    def test_post_index_returns_ok(self):
        response = self.app.post('/',
                                 data=self.data,
                                 headers={'content-type': 'application/json'})
        assert 200 == response.status_code


class RepositoryTest(TestCase):
    def setUp(self):
        self.repository = receiver.Repository("sample")

    def test_application_constructor_path(self):
        assert self.repository.path() == "/tmp/sample"

    def test_application_constructor_origin(self):
        assert self.repository.origin == "git@sample.com:username/repo.git"

    def test_application_constructor_mirror(self):
        assert self.repository.mirror == "git@sample.com:username/mirror.git"

if __name__ == '__main__':
    main()
