# cflib #

`cflib` provides scripts to convert between fasta, VCF and counts
files.  Counts files are used by
[PoMo](http://www.cibiv.at/software/iqtree/doc/Polymorphism-Aware-Models/),
an implementation of a polymorphism-aware phylogenetic model.

For a reference, please see and cite Schrempf, D., Minh, B. Q., De
Maio, N., von Haeseler, A., & Kosiol, C. (2016). Reversible
Polmorphism-Aware Phylotenetic Models and their Application to Tree
Inference. Journal of Theoretical Biology, in press.

# Installation Requirements #

Before installing, check that you have [`git`](https://github.com/)
and [python3](https://www.python.org/) installed.

`cflib` also uses the following python libraries that need to be
installed separately:
- [scipy](http://www.scipy.org/),
- [numpy](http://www.numpy.org/) and
- [pysam](http://code.google.com/p/pysam/)

# Installation #

Download `cflib` with:

```sh
git clone git://github.com/pomo-dev/cflib
```

This will create a folder `cflib` which includes the library and the
conversion scripts.

# Conversion #

Conversion scripts can be found in the [scripts](./scripts/) folder:

* [CountsToFasta.py](./scripts/CountsToFasta.py): Convert a counts
  file to a fasta file.
* [FastaToCounts.py](./scripts/FastaToCounts.py): Convert a fasta file
  to counts format.
* [FastaToVCF.py](./scripts/FastaToVCF.py): Convert a fasta file to
  variant call format.
* [FastaVCFToCounts.py](./scripts/FastaVCFToCounts.py): Convert a
  fasta reference with VCF files to counts format.
* [FilterMSA.py](./scripts/FilterMSA.py): Filter a multiple sequence
  alignment file (apply standard filters; cf. `libPoMo`).
* [GPToCounts.py](./scripts/GPToCounts.py): Experimental.  Convert
  gene prediction files with reference to counts format.
* [MSAToCounts.py](./scripts/MSAToCounts.py): Convert multiple
  sequence alignments with VCF files to counts format.

# Sample Data #

Sample data can be found in [examples](./examples).

# Documentation #

Each of the script comes with its own documentation.  Please execute,
e.g., `./FastaToCounts.py --help`.

If you are interested in `cflib` itself, please refer to the
[cflib reference manual](http://cflib.readthedocs.io/en/latest/).
