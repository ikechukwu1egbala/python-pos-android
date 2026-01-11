[app]
title = Python POS
package.name = pythonpos
package.domain = org.example
source.dir = .
source.include_exts = py
version = 0.1

requirements = python3==3.10.13,kivy,sqlalchemy,requests,pydantic

orientation = landscape
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
