import unittest
from mock import Mock
from app.account import Account


class TestAccount(unittest.TestCase):
    def test_account_returns_data_for_id_1(self):
        account_data = dict(id=1, name="data")
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        account = Account(mock_data_interface)
        self.assertDictEqual(account_data, account.get_account(1))


if __name__ == "__main__":
    unittest.main()