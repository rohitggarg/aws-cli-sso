from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from urllib import parse
import boto3

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

class Login:
  def __init__(self, sso_url, role, principal, duration):
    self.url = sso_url
    self.role = role
    self.principal = principal
    self.duration = int(duration)

  def go(self):
    chrome = webdriver.Chrome
    driver = webdriver.Chrome(desired_capabilities=caps)
    driver.get(self.url)
    message = None
    while message is None:
      for log in driver.get_log('performance'):
        if 'https://signin.aws.amazon.com/saml' in log.get('message') and 'SAMLResponse' in log.get('message'):
          message = json.loads(log.get('message'))['message']
          break
      time.sleep(1)
    response = parse.parse_qs(message['params']['request']['postData'])

    driver.quit()

    sts_client = boto3.client('sts')
    assumed_role_object=sts_client.assume_role_with_saml(
      RoleArn=self.role,
      PrincipalArn=self.principal,
      SAMLAssertion=response['SAMLResponse'][0],
      DurationSeconds=self.duration
    )
    return assumed_role_object
