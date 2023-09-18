# FileAPI - THanksDev

![License](https://img.shields.io/pypi/l/your-package-name) ![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FTyHanks%2Fosf-hackathon-api%2Fblob%2Fmain%2Fpyproject.toml)

This is an API designed for managing an online forum using disk-persistent storage and HTTP requests.

## Table of Contents

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [Documentation](#documentation)
* [License](#license)

## About

This script creates a basic HTTP server with routes for handling GET, POST, and DELETE requests to manage an online forum-like website. It uses JSON as disk storage for the API and can be customized as required for posts or comments.

## Installation

You can install FileApi by cloning the repo need to have python 3.0+ installed.

``` bash
git@github.com:TyHanks/osf-hackathon-api.git
#or
https://github.com/TyHanks/osf-hackathon-api.git
```

## Usage

Start http server using the following

```bash
cd osf-hackathon-api/src/fileapi_package_THanksDev
python fileapi.py
```

Please try sending GET, POST, and DELETE requests by opening a new terminal while the server is running. Use the following commands as a reference. Ensure that you uncomment or modify the 'example.py' file to perform various tests.

```bash
cd test
python example.py
```

## License

``` bash
MIT License

Copyright (c) 2023 Ty Hanks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```