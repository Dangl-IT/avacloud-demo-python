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

> **Note**: There's also `hello_new_project.py` as an example that creates a new GAEB file from JSON input via **AVACloud**.

## AVACloud Key Features

- Can read all GAEB90, GAEB2000 and GAEB XML files. It includes many heuristics and eror corrections that can recover incorrect files
- Hassle-free import: Just pass the file to **AVACloud**, format detection and error recovery happens automatically
- Advanced code, built on years of experience, allows the preservation of most information even when converting to an earlier version of the GAEB standard
- Automatic calculation of prices, quantities and more - **AVACloud** can do much more beyond just converting your data
- Over **250.000** tests are run automatically on every commit. Tests range from unit tests in the conversion code up to full integration tests mirroring a full production environment

### Supported Formats

![AVACloud Features](./img/AVACloud%20Diagram%20EN.png)

**... and many more!**

### UI Components

Easy integration with prebuilt UI components is possible within minutes:

- Either by using our Angular specific `@dangl/angular-ava` package: <https://www.npmjs.com/package/@dangl/angular-ava>
- Or with our framework agnostict Html web component implementation that run anywhere, either in web apps or locally in a web view: <https://www.npmjs.com/package/@dangl/web-components-ava>

---

[License](./LICENSE.md)
