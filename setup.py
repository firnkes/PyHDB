# Copyright 2014, 2015 SAP SE.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import os
import codecs
from setuptools import setup, find_packages

source_location = os.path.abspath(os.path.dirname(__file__))


def get_version():
    with open(os.path.join(source_location, "VERSION")) as version:
        return version.readline().strip()


def get_long_description():
    with codecs.open(os.path.join(source_location, "README.rst"), 'r', 'utf-8') as readme:
        return readme.read()

setup(
    name="pyhdb-sap-prod",
    version=get_version(),
    license="Apache License Version 2.0",
    url="https://github.wdf.sap.corp/hana-infrastructure/PyHDB",
    author="Patrick Firnkes",
    author_email="patrick.firnkes@sap.com",
    description="SAP HANA Database Client for Python",
    include_package_data=True,
    long_description=get_long_description(),
    packages=find_packages(exclude=("tests", "tests.*",)),
    zip_safe=False,
    provides=["pyhdb"],
    obsoletes=["pyhdb"],
    tests_require=[
        "pytest>=2.5.2",
        "mock>=1.0.1"
    ],
    classifiers=[  # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: SQL',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
