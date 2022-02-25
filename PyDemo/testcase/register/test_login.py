# -*- coding:utf-8 -*-
# @Time    : 2022/02/25
# @Author  : Wang GuoSheng
# @File    : test_login
# ****************************
import os
import allure
import pytest
from comm.utils.readYaml import read_yaml_data
from comm.unit.initializePremise import init_premise
from comm.unit.apiSend import send_request
from comm.unit.checkResult import check_result
file_path = os.path.realpath(__file__).replace('\\', '/')
case_yaml = file_path.replace('/testcase/', '/page/').replace('.py', '.yaml')
case_data = read_yaml_data(case_yaml)


@allure.feature(case_data["test_info"]["title"])
class TestRegister:

    @pytest.mark.parametrize("test_case", case_data["test_case"])
    @allure.story("test_login")
    def test_login(self,test_case):
        test_info ,test_case = init_premise(case_data["test_info"],test_case,case_yaml)
        code , date =send_request(test_info,test_case)

        check_result(test_case,code,date)


