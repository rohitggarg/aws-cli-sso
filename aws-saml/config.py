import configparser
from login import Login

class Config:
  def __init__(self, file_path):
    self.config = configparser.ConfigParser()
    self.config.read(file_path)
    self.file_path = file_path
  
  def fire_saml_login(self, profile):
    response = Login(
      self.config[profile]['saml_sso_url'],
      self.config[profile]['saml_role_arn'],
      self.config[profile]['saml_principal_arn'],
      self.config[profile]['saml_duration']
    ).go()
    
    self.config[profile]['aws_access_key_id'] = response['Credentials']['AccessKeyId']
    self.config[profile]['aws_secret_access_key'] = response['Credentials']['SecretAccessKey']
    self.config[profile]['aws_session_token'] = response['Credentials']['SessionToken']
    
    with open(self.file_path, 'w') as configfile:
      self.config.write(configfile)
