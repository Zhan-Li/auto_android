from setuptools import setup

# with open("requirements.txt") as f:
#    REQUIREMENTS = f.read().splitlines()

REQUIREMENTS = [
    "adbutils==1.2.7",
    "apkutils2==1.0.0",
    "cached-property==1.5.2",
    "certifi==2022.12.7",
    "charset-normalizer==3.0.1",
    "cigam==0.0.3",
    "decorator==5.1.1",
    "Deprecated==1.2.13",
    "deprecation==2.1.0",
    "filelock==3.9.0",
    "idna==3.4",
    "imutils==0.5.4",
    "logzero==1.7.0",
    "lxml==4.9.2",
    "numpy==1.24.2",
    "opencv-python==4.7.0.68",
    "packaging==20.9",
    "pandas==1.5.3",
    "Pillow==9.4.0",
    "progress==1.6",
    "py==1.11.0",
    "pyelftools==0.29",
    "pyparsing==3.0.9",
    "python-dateutil==2.8.2",
    "pytz==2022.7.1",
    "requests==2.28.2",
    "retry==0.9.2",
    "six==1.16.0",
    "uiautomator2==2.16.22",
    "urllib3==1.26.14",
    "whichcraft==0.6.1",
    "wrapt==1.14.1",
    "xmltodict==0.13.0",
]

setup(
    name="auto_android",
    version="0.2",
    long_description="Base android automation class.",
    install_requires=REQUIREMENTS,
)
