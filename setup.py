#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Tao Sauvage'


from setuptools import setup, find_packages


setup(
    name="PTP",
    version="0.1.0",
    description="PTP ranks the discoveries listed in security tool reports.",
    author="Tao Sauvage",
    author_email="sauvage.tao@gmail.com",
    license="BSD",
    keywords="PTP Security Automated Ranking",
    url="http://owtf.github.io/ptp",
    packages=find_packages(exclude=['docs']),
    use_2to3 = True,
    install_requires = ["lxml"],
)
