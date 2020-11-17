# fastapi-twofactor
This repo is part of a tutorial for implementing two-factor authentication (One-Time Password) for Fast API using PyOTP library. It also includes the code for adding a backend user database with SQLAlchemy.

- **v0** directory: contains the original FastAPI security tutorial without two-factor authentication integrated. 
- **v1** directory: based on this but adds basic two-factor authentication using PyOTP. 
- **v2** directory: enables the use of a sqlite (or other) database and enables user administration such as creating new users and user level access control.

The v2 tutorial is available [here](https://developingfordata.com/2020/11/17/fastapi-security-with-a-user-database/)
The v1 tutorial is available [here](https://developingfordata.com/2020/11/10/getting-started-with-two-factor-authentication-in-fastapi/).

This tutorial assumes you have Python 3 running. 

I suggest making a virtual environment and install the following: 

```
pip install fastapi[all]
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install pyotp
```

Once installed, clone this repo and navigate to the v2 or v1 directory (depending on which tutorial you are following). You can now run the following command to launch the application:

``` uvicorn --reload main:app ```


