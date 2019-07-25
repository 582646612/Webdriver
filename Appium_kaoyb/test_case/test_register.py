import unittest
from common.myunit import StartEnd
from businessView.registerView import RegisterView, logging, random

class RegisterTest(StartEnd):
    def test_user_register(self):
        logging.info('========test_user_register=========')
        r=RegisterView(self.driver)

        newname = 'william' + str(random.randint(1, 1000)) + 'sss'
        newpass = 'test' + '@' + str(random.randint(1, 1000))
        newemail = 'hellolove' + str(random.randint(1, 1000)) + '@163.com'

        self.assertTrue(r.register_action(newname, newpass, newemail))

if __name__ == '__main__':
    unittest.main()