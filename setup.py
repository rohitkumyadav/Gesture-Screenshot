from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.3.3'
DESCRIPTION = 'Screenshot using Gesture hand detection'
LONG_DESCRIPTION = open("README.md").read()

# Setting up
setup(
    name="rk_screenshot",
    version=VERSION,
    author="Rohit Kumar Yadav",
    author_email="<rohitkuyadav2003@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    license="MIT",  # Add the license type here
    license_files=("LICENSE",), 
    install_requires=['pyscreenshot', 'opencv-python', 'mediapipe'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)
