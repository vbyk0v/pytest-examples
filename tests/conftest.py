import pytest
import os


#
#
# #  module fixture
# @pytest.fixture(scope='module', autouse=True)
# def module_fixture(request):
#     print('\n   =========module_fixture_start=========')
#     some_code = ''
#
#     def module_fixture_fin():
#         print('\n   =========module_fixture_end=========')
#     request.addfinalizer(module_fixture)

#  session fixture
@pytest.fixture(scope="session", autouse=True)
def session_fixture(request):
    print('\n=========session_fixture_start=========')

    'some_code'

    def session_fixture_fin():
        print('\n=========session_fixture_end=========')
    request.addfinalizer(session_fixture_fin)


#  function fixture
@pytest.fixture(scope='function', autouse=True)
def function_fixture(request):
    print('\n   =========function_fixture_start=========')

    'some_code'

    def function_fixture_end():
        print('\n   =========function_fixture_end=========')
    request.addfinalizer(function_fixture_end)
