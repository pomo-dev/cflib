.. PoMo documentation master file, created by
   sphinx-quickstart on Fri Dec 13 15:06:09 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the documentation of `cflib`!
========================================

This library provides functions and classes to handle file conversion
between standard formats (e.g., fasta or VCF files) to counts files
that are used by `IQ-TREE <http://www.cibiv.at/software/iqtree/>`_
with `PoMo
<http://www.cibiv.at/software/iqtree/doc/Polymorphism-Aware-Models/>`_,
and implementation of a polymorphism aware phylogenetic model.

Created by:
  * Dominik Schrempf

For a reference, please see and cite: Schrempf, D., Minh, B. Q., De
Maio, N., von Haeseler, A., & Kosiol, C. (2016). Reversible
Polmorphism-Aware Phylotenetic Models and their Application to Tree
Inference. Journal of Theoretical Biology, in press.

Feel free to post any suggestions, doubts and bugs.

cflib
=====

`cflib` contains several modules that ease the handling and
preparation of data files in variant call format (vcf), fasta format
and counts format (cf).

The *libPoMo* package is split into the following modules:
  * :doc:`main <main>`: Contains functions that are used by PoMo.
  * :doc:`seqbase <seqbase>`: Provides basic functions and classes
    needed to work with sequence data.
  * :doc:`fasta <fasta>`: Provides functions to read, write and access
    fasta files.
  * :doc:`vcf <vcf>`: Provides functions to read, write and access vcf
    files.
  * :doc:`cf <cf>`: Provides functions to read, write and access files
    that are in counts format.

Contents
=========
.. toctree::
   :maxdepth: 2

   main
   seqbase
   fasta
   vcf
   cf

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
