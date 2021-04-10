import os
import pytest
import subprocess


if __name__ == "__main__":
    path = os.path.dirname(__file__)
    html_path = '/'.join(path.split('\\')) + '/Report/html'
    xml_path = '/'.join(path.split('\\')) + '/Report/xml'
    print('html_path:', html_path)
    print('xml_path:', xml_path)
    # '--setup-show'
    pytest.main(["-s", "-v", "test_selenium/testcases/test_add_department.py", "--alluredir", xml_path])
    cmd = "allure generate %s -o %s --clean" % (xml_path, html_path)
    output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8", "ignore")