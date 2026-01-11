[app]
title = Python POS
package.name = pythonpos
package.domain = org.example
source.dir = .
source.include_exts = py
version = 0.1

requirements = python3,kivy,fastapi,uvicorn,sqlalchemy,requests,pydantic

orientation = landscape
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
