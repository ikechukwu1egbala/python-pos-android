[app]
title = Python POS
package.name = pythonpos
package.domain = org.example

source.dir = .
source.include_exts = py
version = 0.1

# ⚠️ DO NOT pin pyjnius
requirements = python3==3.10.13,kivy==2.3.0,sqlalchemy,requests,pydantic

orientation = landscape
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21

# Android toolchain (PINNED & SAFE)
android.ndk = 25b
android.build_tools_version = 33.0.2
bootstrap = sdl2


[buildozer]
log_level = 2

# Stable python-for-android branch
p4a.branch = v2023.09.16

# Cython compatibility (critical)
cython = 0.29.36
