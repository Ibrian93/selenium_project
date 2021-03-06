from Backend.Services.account import Account

class TestClass:

    account_service = Account()

    def test_post_generation_token_successful(self):
        data = {"userName": "ibrian93", "password": "MyTesting83!"}
        req = self.account_service.post_generate_token(data)
        assert req.status_code == 200
        assert req.json() is not None
        assert isinstance(req.json()["token"], str)
        assert isinstance(req.json()["expires"], str)
        assert isinstance(req.json()["status"], str)
        assert isinstance(req.json()["result"], str)
        assert req.json()["status"] == "Success" and req.json()["result"] == "User authorized successfully."


    def test_post_generation_wrong_header(self):
        data = {"userName": "ibrian93", "password": "MyTesting83!"}
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        req = self.account_service.post_generate_token(data=data, headers=headers)
        assert req.status_code == 400

    def test_post_generation_user_does_not_exist(self):
        data= {"userName": "FakeUser", "password": "FakePassword"}
        req = self.account_service.post_generate_token(data)
        assert req.status_code == 200, "This is the status code reported: " + req.status_code
        assert req.json() is not None
        assert req.json()["status"] == "Failed" and req.json()["result"] == "User authorization failed."

    def test_post_generation_invalid_body(self):
        req = self.account_service.post_generate_token(data=[])
        assert req.status_code == 400
        assert req.json() is not None
        assert req.json()["code"] == "1200"
        assert req.json()["message"] == "UserName and Password required."
