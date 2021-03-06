
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='trajectory',
    version='0.1.1',
    description="Trajectory data lossy compression format based on Google's Encoded Polyline Algorithm Format",
    python_requires='>=3.6',
    project_urls={"documentation": "https://github.com/adonmo/trajectory", "homepage": "https://github.com/adonmo/trajectory", "repository": "https://github.com/adonmo/trajectory"},
    author='B Krishna Chaitanya',
    author_email='bkchaitan94@gmail.com',
    license='MIT',
    keywords='geo gis postgres mobility trajectory spatiotemporal',
    classifiers=['Development Status :: 3 - Alpha', 'Environment :: Plugins', 'Operating System :: OS Independent', 'Programming Language :: Python', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Intended Audience :: Developers', 'Intended Audience :: Information Technology', 'Intended Audience :: Science/Research', 'License :: OSI Approved :: MIT License', 'Natural Language :: English', 'Topic :: Database :: Database Engines/Servers', 'Topic :: Scientific/Engineering :: GIS'],
    packages=['trajectory'],
    package_dir={"": "."},
    package_data={},
    install_requires=['six==1.*,>=1.14.0'],
    extras_require={"dev": ["black==19.*,>=19.10.0", "dephell==0.7.9", "fissix==19.*,>=19.2.0", "pre-commit==2.*,>=2.1.0", "pytest==5.*,>=5.3.5"]},
)
