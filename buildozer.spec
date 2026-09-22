[app]
title = App da Mae
package.name = appdamae
package.domain = com.appdamae
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_patterns =.github,venv,bin,build
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
[buildozer]
log_level = 2
warn_on_root = 1
[app:permissions]
android.permissions = INTERNET
[app:android]
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False
