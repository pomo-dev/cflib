#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='cflib-pomo',
    version='1.3.0.0',
    author='Dominik Schrempf',
    author_email='dominik.schrempf@gmail.com',
    description='Counts file library and conversion scripts.',
    license="MIT",
    keywords="counts fasta files multi sequence alignments",
    url='https://github.com/pomo-dev/cflib',
    packages=setuptools.find_packages(),
    long_description=open('README.md', 'r').read(),
    long_description_content_type="text/markdown",
    install_requires=["scipy", "numpy", "pysam"],
    classifiers=['Intended Audience :: Science/Research'],
    scripts=["scripts/CountsToFasta.py", "scripts/FastaToCounts.py",
             "scripts/FastaToVCF.py", "scripts/FastaVCFToCounts.py",
             "scripts/FilterMSA.py", "scripts/GPToCounts.py",
             "scripts/MSAToCounts.py"])
