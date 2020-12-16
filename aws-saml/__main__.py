from pathlib import Path
from .config import Config

creds_file = input("AWS credentials file path: (~/.aws/credentials)")
profile = input("AWS profile name: (default)")

home = str(Path.home())

Config(creds_file or (home+'/.aws/credentials')).fire_saml_login(profile or 'default')
