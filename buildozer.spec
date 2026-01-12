[app]
title = Python POS
package.name = pythonpos
package.domain = org.example
source.dir = .
source.include_exts = py
version = 0.1

requirements = python3==3.10.13,kivy==2.3.0,pyjnius==1.5.0,sqlalchemy,requests,pydantic

orientation = landscape
fullscreen = 1
android.permissions = INTERNET
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
p4a.branch = v2023.09.16
cython = 0.29.36
