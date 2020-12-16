import os
from pathlib import Path

if os.getenv('NO_EXEC') == None:
  creds_file = input("AWS credentials file path: (~/.aws/credentials)")
  profile = input("AWS profile name: (default)")

  home = str(Path.home())
  if os.getenv('DRY_RUN') == None:
    Config(creds_file or (home+'/.aws/credentials')).fire_saml_login(profile or 'default')
