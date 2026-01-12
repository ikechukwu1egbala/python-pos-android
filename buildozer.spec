[app]
title = Python POS
package.name = pythonpos
package.domain = org.example
source.dir = .
source.include_exts = py
version = 0.1

requirements = python3==3.10.13,kivy,sqlalchemy,requests,pydantic
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

orientation = landscape
fullscreen = 1
android.permissions = INTERNET

[buildozer]
log_level = 2
p4a.branch = v2023.09.16
