# fastapi-twofactor
This repo is part of a tutorial for implementing two-factor authentication (One-Time Password) for Fast API using PyOTP library. The **v0** directory contains the original FastAPI security tutorial without two-factor authentication integrated. The **v1** directory is based on this but adds basic two-factor authentication using PyOTP.

The full tutorial is available [here](https://developingfordata.com/2020/11/10/getting-started-with-two-factor-authentication-in-fastapi/).

This tutorial assumes you have Python 3 running. 

I suggest making a virtual environment and install the following: 

```
pip install fastapi[all]
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install pyotp
```

Once installed, clone this repo and navigate to the v1 directory. You can now run the following command to launch the application:

``` uvicorn --reload main:app ```


