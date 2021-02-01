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

`cflib` requires [`python` (Version 3.x)](https://www.python.org/) to be
installed. `cflib` also uses the following python libraries that will be
automatically pulled when installing `cflib`:

- [scipy](http://www.scipy.org/),
- [numpy](http://www.numpy.org/) and
- [pysam](http://code.google.com/p/pysam/).

# Installation

Install `cflib` and the conversion scripts with

```sh
pip install --user cflib-pomo
```

Note that the name of `cflib` on the PyPI repository (which is used by `pip`) is
`cflib-pomo`, since the name `cflib` was taken!

If the standard Python version of your operation system is still 2.x (e.g.,
OSX), make sure that you use, `pip3`.

The `--user` flag is optional and tells Python to install `cflib` and
the scripts only for this user but not system wide.

If you want to uninstall `cflib`,

```sh
pip uninstall cflib-pomo
```

The [conversion scripts](#Conversion scripts) should be directly available if
your `PATH` environment variable is setup correctly. For my Linux installation,
the Python path `~/.local/bin` had to be included. This may vary for your
operating system.

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

# Note on IUPAC codes

IUPAC codes are supported and handled adequately.

In particular,

- `N` can be used to denote any base or that the base is unknown; the letter `*`
  can also be used in this case, although it is non-standard;

- `-` or `.` denote a gap or a deletion.

Also the other IUPAC codes are supported.

# Conversion scripts

- [CountsToFasta.py](./scripts/CountsToFasta.py): Convert a counts file to a
  fasta file.
- [FastaToCounts.py](./scripts/FastaToCounts.py): Convert a fasta file to counts
  format.
- [FastaToVCF.py](./scripts/FastaToVCF.py): Convert a fasta file to variant call
  format.
- [FastaVCFToCounts.py](./scripts/FastaVCFToCounts.py): Convert a fasta
  reference with VCF files to counts format.
- [FilterMSA.py](./scripts/FilterMSA.py): Filter a multiple sequence alignment
  file (apply standard filters; cf. `libPoMo`).
- [GPToCounts.py](./scripts/GPToCounts.py): Experimental. Convert gene
  prediction files with reference to counts format.
- [MSAToCounts.py](./scripts/MSAToCounts.py): Convert multiple sequence
  alignments with VCF files to counts format.

Each script comes with its own documentation. Please execute, e.g.,

```sh
FastaToCounts.py --help
```

All conversion scripts can be found in the [scripts](./scripts) folder.


# Documentation

If you are interested in `cflib` itself, please refer to the
[cflib reference manual](http://cflib.readthedocs.io/en/latest/).
