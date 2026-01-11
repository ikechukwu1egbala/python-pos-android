[app]
title = Python POS
package.name = pythonpos
package.domain = org.example
source.dir = .
source.include_exts = py
version = 0.1

android.accept_sdk_license = True

android.sdk = 33
android.build_tools_version = 33.0.2

requirements = python3,kivy,fastapi,uvicorn,sqlalchemy,requests,pydantic

orientation = landscape
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2



