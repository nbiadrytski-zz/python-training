## Rest API Test Automation framework
Simple Rest API Test Automation framework.
Supports _Python 3.6+_.

#### Description
Uses:

1. ```pytest``` as test runner
2. Python ```requests``` module to perform HTTP requests
3. ```allure``` for reporting

Is able to perform HTTP GET, POST, OPTIONS requests (can be extended) and validate responses.

Tests are in ```tests``` folder, codebase is in ```utils``` folder. Test data and data config(s) are in ```resources``` folder. Logs are available both in console and in ```pytest.log``` file.

#### Usage
Run tests:

```python3 -m pytest -m package --env=dev --alluredir reports -nauto``` where

**-m package** is a tests group (see ```pytest.ini``` for available group markers)

**--env=dev** - desired environment (see ```hosts_config.py``` for available environments) 

**--alluredir reports** - folder to store Allure test data

**---nauto** - to parallelize tests execution using ```pytest-xdist```(```auto```, ```NUM``` value is CPUs number)

For test report install ```allure``` (for Mac OS):
1. ```brew install allure```
2. ```open .bash_profile```
3. Add allure to your path, e.g. ```export PATH="/usr/local/Cellar/allure/2.10.0/libexec/bin:$PATH"```

To generate **allure html report** run tests, e.g.:
1. ```python3 -m pytest -m package --env=dev --alluredir reports``` from framework root folder. ```reports``` folder with allure data will be created under framework root folder.
2. Run ```allure generate rest_api_test_framework/reports -c -o rest_api_test_framework/reports/html_report``` to generate allure html report, where ```rest_api_test_framework/reports``` is path to the folder with allure data (generated in step 1) and ```rest_api_test_framework/reports/html_report``` is path to the folder where html report will be generated.
3. Open ```index.html``` file located in ```reports/html_report``` folder to see generated html report
 