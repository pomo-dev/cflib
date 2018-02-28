# Counts file library

This python library `cflib` provides scripts to convert between fasta, VCF and
counts files. Counts files are used by
[PoMo](http://www.cibiv.at/software/iqtree/doc/Polymorphism-Aware-Models/), an
implementation of a polymorphism-aware phylogenetic model. We advice you to use
PoMo implemented in [IQ-TREE](http://www.cibiv.at/software/iqtree/).

For a reference, please see and cite:

    Schrempf, D., Minh, B. Q., De Maio, N., von Haeseler, A., &
    Kosiol, C. (2016). Reversible Polmorphism-Aware Phylotenetic
    Models and their Application to Tree Inference. Journal of
    Theoretical Biology, in press.

# Requirements

Before installation, please check that you have [`git`](https://github.com/) and
[`python (Version 3.x)`](https://www.python.org/) installed. `cflib` also uses
the following python libraries that need to be installed separately:

- [scipy](http://www.scipy.org/),
- [numpy](http://www.numpy.org/) and
- [pysam](http://code.google.com/p/pysam/).

# Installation

Download `cflib` with:

```sh
git clone git://github.com/pomo-dev/cflib
```

This will create a folder `cflib` which includes the library and the
conversion scripts.  In the folder `cflib`, execute

```sh
easy_install --user .
```

If the standard Python version of your operation system is still 2.x (e.g.,
OSX), make sure that you use, e.g., `easy_install3`.

The `--user` flag is optional and tells Python to install `cflib` and
the scripts only for this user but not system wide.

If you want to uninstall `cflib`, you can `pip` (or `pip3`)

```sh
pip uninstall cflib
```

# Example

Sample data can be found in [examples](./examples). Assuming that have installed
`cflib` we will now convert [`example.fasta`](./examples/example.fasta) to a
counts file named `example_from_fasta.cf`. The [script](#conversion-scripts)
that we will use is called [`FastaToCounts.py`](./scripts/FastaToCounts.py).
First, we have a look at the help message:

```sh
FastaToCounts.py --help
```

    usage: FastaToCounts.py [-h] [-v] [--iupac] fastaFile output

    Convert fasta to counts format.

    The (aligned) sequences in the fasta file are read in and the data is
    written to a counts format file.

    Sequence names are stripped at the first dash.  If the stripped
    sequence name coincide, individuals are put into the same population.

    E.g., homo_sapiens-XXX and homo_sapiens-YYY will be in the same
    population homo_sapiens.

    Take care with large files, this uses a lot of memory.

    The input as well as the output files can additionally be gzipped
    (indicated by a .gz file ending).

    If heterozygotes are encoded with IUPAC codes (e.g., 'r' for A or G),
    homozygotes need to be counted twice so that the level of polymorphism
    stays correct.  This can be done with the `--iupac` flag.

    positional arguments:
      fastaFile      path to (gzipped) fasta file
      output         name of (gzipped) outputfile in counts format

    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  turn on verbosity (-v or -vv)
      --iupac        heteorzygotes are encoded with IUPAC codes

As requested, the sequence names in `example.fasta` are, e.g.,
`Sheep-1`, `Sheep-2`, and so on.  The following code converts the file
`example.fasta` into the counts file `example_from_fasta.cf`:

```sh
FastaToCounts.py example.fasta example_from_fasta.cf
```

# Conversion scripts

All conversion scripts can be found in the [scripts](./scripts)
folder:

- [CountsToFasta.py](./scripts/CountsToFasta.py): Convert a counts
  file to a fasta file.
- [FastaToCounts.py](./scripts/FastaToCounts.py): Convert a fasta file
  to counts format.
- [FastaToVCF.py](./scripts/FastaToVCF.py): Convert a fasta file to
  variant call format.
- [FastaVCFToCounts.py](./scripts/FastaVCFToCounts.py): Convert a
  fasta reference with VCF files to counts format.
- [FilterMSA.py](./scripts/FilterMSA.py): Filter a multiple sequence
  alignment file (apply standard filters; cf. `libPoMo`).
- [GPToCounts.py](./scripts/GPToCounts.py): Experimental.  Convert
  gene prediction files with reference to counts format.
- [MSAToCounts.py](./scripts/MSAToCounts.py): Convert multiple
  sequence alignments with VCF files to counts format.

Each script comes with its own documentation.  Please execute, e.g.,

```sh
FastaToCounts.py --help
```

# Documentation

If you are interested in `cflib` itself, please refer to the
[cflib reference manual](http://cflib.readthedocs.io/en/latest/).
