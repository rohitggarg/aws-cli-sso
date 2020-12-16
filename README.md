# AWS SAML Login
Works cross platform (Win, Unix, MacOS)
Was having a real hard time trying to get cli credentials via SAML SSO so thought about writing this small utility.
I can run this daily every morning to get a 12 hour session for myself. Hope you'd find it interesting and useful.

Looking forward to contributions!!

## Prerequisites

Need to install
* Chromedriver
* Google Chrome
* Python 2/3

Make sure all the above software are setup properly in `PATH` environment variable

## Executing

Add properties to your AWS credentials file

```ini
[some-profile]
saml_sso_url = <url you use for saml>
saml_role_arn = <your iam role to assume>
saml_principal_arn = <your saml app arn>
saml_duration = <duration of session in seconds>
```

Run
```shell
python -m aws-saml
```

## Installation
```pip install aws-cli-sso```

## Local development/testing
* ```pip install -r requirements.txt```
* ```python -m aws-saml```
