# AA Forum

[![Version](https://img.shields.io/pypi/v/aa-forum?label=release)](https://pypi.org/project/aa-forum/)
[![License](https://img.shields.io/github/license/ppfeufer/aa-forum)](https://github.com/ppfeufer/aa-forum/blob/master/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/aa-forum)](https://pypi.org/project/aa-forum/)
[![Django](https://img.shields.io/pypi/djversions/aa-forum?label=django)](https://pypi.org/project/aa-forum/)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)
[![Discord](https://img.shields.io/discord/790364535294132234?label=discord)](https://discord.gg/zmh52wnfvM)

Simple forum app for [Alliance Auth](https://gitlab.com/allianceauth/allianceauth)

## ⚠️ Before you install this module ⚠️

This module needs quite some configuration done before working properly. You need to
modify your Apache/Nginx configuration as well as the global URL config of Alliance
Auth. So please only install if you know what you're doing/feel comfortable to make
these kind of changes. For you own sanity, and mine :-)

## Contents
- [Overview](#overview)
    - Features
    - Screenshots
- [Installation](#installation)
    - [Step 1 - Install the package](#step-1---install-the-package)
    - [Step 2 - Configure Alliance Auth](#step-2---configure-alliance-auth)
    - [Step 3 - Configure your webserver](#step-3---configure-your-webserver)
    - [Step 4 - Finalize the installation](#step-4---finalize-the-installation)
    - [Step 5 - Set up permissions](#step-5---set-up-permissions)
- [Permissions](#permissions)
- [Changelog](#changelog)
- [Contributing](#contributing)


## Overview

Work in progress on this one


## Installation

### ⚠️ This is still in development, so only install it if you know what you're doing ⚠️

**Important**: Please make sure you meet all preconditions before you proceed:

- AA Forum is a plugin for Alliance Auth. If you don't have Alliance Auth running
  already, please install it first before proceeding. (see the official
  [AA installation guide](https://allianceauth.readthedocs.io/en/latest/installation/allianceauth.html)
  or details)
- AA Forum needs a couple of changes made to your Webserver and Alliance Auth
  configuration. So make sure you know how to do so. The steps needed will be
  described in this document, but you need to understand what will be changed.


### Step 1 - Install the package

Make sure you are in the virtual environment (venv) of your Alliance Auth
installation Then install the latest release directly from PyPi.

```shell
pip install aa-forum
```


### Step 2 - Configure Alliance Auth

This is fairly simple, configure your AA settings (`local.py`) as follows:

```python
# AA Forum
INSTALLED_APPS += [
    "ckeditor",
    "ckeditor_uploader",
    "aa_forum",  # https://github.com/ppfeufer/aa-forum
]

MEDIA_URL = "/media/"
MEDIA_ROOT = "/var/www/myauth/media/"

X_FRAME_OPTIONS = "SAMEORIGIN"

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {"default": {"width": "100%", "height": "45vh"}}
```

Now let's move on to editing the global URL configuration of Alliance Auth. To do so,
you need to open `/home/allianceserver/myauth/myauth/urls.py` and change the following:

```python
from django.conf.urls import include, url
from allianceauth import urls

# *** New Imports for cKeditor
from django.urls import re_path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    # *** New URL override for cKeditor BEFORE THE MAIN IMPORT
    re_path(r"^upload/", login_required(ckeditor_views.upload), name="ckeditor_upload"),
    re_path(
        r"^browse/",
        never_cache(login_required(ckeditor_views.browse)),
        name="ckeditor_browse",
    ),
    # Alliance Auth URLs
    url(r"", include(urls)),
]

handler500 = "allianceauth.views.Generic500Redirect"
handler404 = "allianceauth.views.Generic404Redirect"
handler403 = "allianceauth.views.Generic403Redirect"
handler400 = "allianceauth.views.Generic400Redirect"
```


### Step 3 - Configure your webserver

Your webserver needs to know from where to serve the uploaded mages of course, so we
have to tell it.

#### Apache

In your vhost configuration you have a line `ProxyPassMatch ^/static !`, which tells
the server where to find all the static files. We are adding a similar line for the
media, right below that one.

Add the following right below the static proxy match:
```apache
ProxyPassMatch ^/media !
```

Now we also need to let the server know where to find the media directory we just
configured the proxy for. To do so, add a new Alias to your configuration. This can
be done right below the already existing Alias for `/static`:
```apache
Alias "/media" "/var/www/myauth/media/"
```

At last a Directory rule is needed as well. Add the following below the already
existing Directory rule for the static files:

```apache
<Directory "/var/www/myauth/media/">
    Require all granted
</Directory>
```

So the whole block should now look like this:
```apache
ProxyPassMatch ^/static !
ProxyPassMatch ^/media !  # *** NEW proxy rule
ProxyPass / http://127.0.0.1:8000/
ProxyPassReverse / http://127.0.0.1:8000/
ProxyPreserveHost On

Alias "/static" "/var/www/myauth/static/"
Alias "/media" "/var/www/myauth/media/"

<Directory "/var/www/myauth/static/">
    Require all granted
</Directory>

<Directory "/var/www/myauth/media/">
    Require all granted
</Directory>
```

Restart your Apache webserver.


#### Nginx

In order to let Nginx know where to find the uploaded files, you need to add a new
location rule to the configuration.
```nginx
location /media {
    alias /var/www/myauth/media;
    autoindex off;
}
```

Restart your Nginx webserver.


### Step 4 - Finalize the installation

Run static files collection and migrations

```shell
python manage.py collectstatic
python manage.py migrate
```

Restart your supervisor services for Auth


### Step 5 - Set up permissions

Now it's time to set up access permissions for your new module. You can do so in
your admin backend. Read the [Permissions](#permissions) section for more information
about the available permissions.


## Permissions

| ID                    | Description                   | Notes|
|-----------------------|-------------------------------|------|
| `basic_access`        | Can access the AA-Forum module | Grants read access to the forum |
| `manage_forum`        | Can manage the AA-Forum module (Categories, topics and messages)          | User with this permission can create, edit and delete boards and categories in the "Administration" view. They can also modify and delete messages and topics in the "Forum" view from boards they have access to. They cannot see all boards in the "Forum" view and are still bound by the board's groups restrictions. |


## Changelog

See [CHANGELOG.md](CHANGELOG.md)


## Contributing

You want to contribute to this project? That's cool!

Please make sure to read the [contribution guidelines](CONTRIBUTING.md) (I promise,
it's not much, just some basics)
