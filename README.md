# AWS SAML Login

## Prerequisites

Need to install
* Chromedriver
* Google Chrome
* Python 3

Make sure all the above software are setup properly in PATH variable

## Executing

Add properties to your AWS credentials file

```
[some-profile]
saml_sso_url
 = <url you use for saml>
saml_role_arn
 = <your iam role to assume>
saml_principal_arn = <your saml app's arn>
saml_duration = <duration of session in seconds>
```

Run
* pip install -r requirements.txt
* python config.py