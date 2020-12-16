# AWS SAML Login

Works cross platform (Win, Unix, MacOS)
Was having a real hard time trying to get cli credentials via SAML SSO so thought about writing this small utility.
I can run this daily every morning to get a 12 hour session for myself. Hope you'd find it interesting and useful.

Looking forward to contributions!!

## Prerequisites

Need to install
* Chromedriver [?](https://chromedriver.chromium.org/downloads)
* Google Chrome [?](https://www.google.com/chrome/thank-you.html?statcb=0&installdataindex=empty&defaultbrowser=0)
* Python 2/3 [?](https://www.python.org/downloads/)
* AWS Cli [?](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

Make sure all the above software are setup properly in `PATH` environment variable

## Executing

Add properties to your AWS credentials file

```ini
[some-profile]
saml_sso_url = <url you use for saml, either okta saml or whatever you use>
saml_role_arn = <your iam role to assume>
saml_principal_arn = <your saml idp arn>
saml_duration = <duration of session in seconds, check iam role for maximum value>
```

Run
```shell
python -m aws-saml
```

Warning: This will change your credentials file. If you don't want to do that, you can use `DRY_RUN=Y python -m aws-saml` which will only print the values.

## Installation
```pip install aws-cli-sso```

## Local development/testing
* ```pip install -r requirements.txt```
* ```python -m aws-saml```
