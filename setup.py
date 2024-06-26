import os
import platform

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="whisperx_greenw0lf",
    py_modules=["whisperx_greenw0lf"],
    version="0.0.2",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    readme="README.md",
    python_requires=">=3.8",
    author="Dragos Balan",
    url="https://github.com/greenw0lf/whisperx",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
    + [f"pyannote.audio==3.1.1"],
    entry_points={
        "console_scripts": ["whisperx=whisperx.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
