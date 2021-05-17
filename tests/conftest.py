import os
import pytest

try:
    from.temp_env_var import userName,password,dictUserName
except ImportError:
    userName=''
    password=''
    dictUserName={}    


@pytest.fixture(scope="session",autouse=True)
def test_setup_and_teardown():
    old_environ = dict(os.environ)
   # print(old_environ)
    os.environ.update(dictUserName)
   # print(dict(os.environ)) 