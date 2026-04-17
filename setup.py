from setuptools import setup, find_packages

setup(
    name="octoload",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
        "pyfiglet",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "octoload=octoload.main:main"
        ]
    },
)