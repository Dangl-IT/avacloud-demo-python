# avacloud-demo-python

[**AVA**Cloud](https://www.dangl-it.com/products/avacloud-gaeb-saas/) is a web based Software as a Service (SaaS) offering for [GAEB files](https://www.dangl-it.com/articles/what-is-gaeb/).  
The GAEB standard is a widely used format to exchange tenderings, bills of quantities and contracts both in the construction industry and in regular commerce. **AVA**Cloud uses the [GAEB & AVA .Net Libraries](https://www.dangl-it.com/products/gaeb-ava-net-library/) and makes them available to virtually all programming frameworks via a web service.

This project here contains example code in Python to read and convert GAEB files. The client code is generated from the [**AVA**Cloud Swagger Specification](https://avacloud-api.dangl-it.com/swagger).

## Step-By-Step Tutorial

[Please find here a step-by-step tutorial how to use the Python client.](https://www.dangl-it.com/articles/create-edit-and-convert-gaeb-files-with-python-and-the-avacloud-api/)

## Build

Ensure that the client dependency is installed:

    pip install git+https://github.com/Dangl-IT/avacloud-client-python.git
    pip install requests

> Tip: When installing the `avacloud-client-python` dependency, you can optionally use a fixed version instead of the latest by appending `@{version}` at the end, e.g. `pip install git+https://github.com/Dangl-IT/avacloud-client-python.git@1.5.1`

## Run

Execute the following command in the root directory of the project:

    python hello_avacloud.py

At the top of the `hello_avacloud.py` file, the following parameters must be defined by you:

    client_id = 'use_your_own_value'
    client_secret = 'use_your_own_value'

These are the credentials of your [**Dangl.Identity**](https://identity.dangl-it.com) OAuth2 client that is configured to access **AVA**Cloud.  
If you don't have values for `ClientId` and `ClientSecret` yet, you can [check out the documentation](https://docs.dangl-it.com/Projects/AVACloud/latest/howto/registration/developer_signup.html) for instructions on how to register for **AVA**Cloud and create an OAuth2 client.

This example app does three operations:

1. The local GAEB file is transformed to Excel and saved next to the input file.
2. The local GAEB file is converted to the unified **Dangl.AVA** format and printed to the console.
3. A new GAEB file is created and saved in the project directory.

---
[License](./LICENSE.md)