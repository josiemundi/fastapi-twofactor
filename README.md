# fastapi-twofactor
This repo is part of a tutorial for implementing two-factor authentication (One-Time Password) for Fast API using PyOTP library. 

- **v0** directory: contains the original FastAPI security tutorial without two-factor authentication integrated. 
- **v1** directory: based on this but adds basic two-factor authentication using PyOTP. 
- **v2** directory: enables the use of a sqlite (or other) database and enables user administration such as creating new users and user level access control.

The v1 tutorial is available [here](https://developingfordata.com/2020/11/10/getting-started-with-two-factor-authentication-in-fastapi/).

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


