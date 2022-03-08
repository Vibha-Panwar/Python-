# https://www.w3resource.com/python-exercises/python-basic-exercise-43.php
# Write a Python program to get OS name, platform and release information.

import platform
import os
print("Name of the Operating System:",os.name)
print("Name of the OS System :",platform.system())
print("Version of the Operating System :" ,platform.release())