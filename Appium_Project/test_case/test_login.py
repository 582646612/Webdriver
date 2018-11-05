from common.common_fun import Common, logging
import unittest
from businessView.loginView import LoginView
from common.myunit import StartEnd


class TestLogin(StartEnd):
    csv_file='../data/account.csv'

    @unittest.skip('skip test_correct_user_and_pass')
    def test_correct_user_and_pass(self):
        logging.info('======test_correct_user_and_pass======')
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file, 1)

        l.login_action(data[0],data[1])
        self.assertTrue(l.check_loginStatus())

    # @unittest.skip('skip test_correct_user_wrong_pass')
    def test_correct_user_wrong_pass(self):
        logging.info('======test_correct_user_wrong_pass======')
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file, 2)

        l.login_action(data[0],data[1])
        self.assertFalse(l.check_loginStatus())

    # @unittest.skip('skip test_wrong_user_wrong_pass')
    def test_wrong_user_wrong_pass(self):
        logging.info('======test_wrong_user_wrong_pass======')
        l=LoginView(self.driver)
        data=l.get_csv_data(self.csv_file, 3)

        l.login_action(data[0],data[1])
        self.assertFalse(l.check_loginStatus(),msg='login fail!')

if __name__ == '__main__':

    unittest.main()





