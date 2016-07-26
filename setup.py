#!/usr/bin/env python

from distutils.core import setup

setup(name='cflib',

      version='1.0',

      description='Counts file library.',

      author='Dominik Schrempf',

      author_email='dominik.schrempf@gmail.com',

      url='https://github.com/pomo-dev/cflib',

      packages=['cflib'],

      install_requires=["scipy", "numpy", "pysam"],

      scripts=["scripts/CountsToFasta.py", "scripts/FastaToCounts.py",
               "scripts/FastaToVCF.py", "scripts/FastaVCFToCounts.py",
               "scripts/FilterMSA.py", "scripts/GPToCounts.py",
               "scripts/MSAToCounts.py"])
