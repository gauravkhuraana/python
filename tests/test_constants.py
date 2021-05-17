from tests.temp_env_var import userName,password
from tests.test_Classes import A
import os

def test_printTempVariables():
  print("User Name is ",userName)
  print("Password from constants file",password)
  print(dict(os.environ))
  obj = A()
  obj.test_remainder(100, 11)