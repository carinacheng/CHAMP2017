# Reionization Theory and 21cmFAST

This session will recap on some cosmology from [Lesson 1](Lesson1_21cmCosmo), and go
into more detail about the theory of reionization -- the role of Hydrogen in the 
Universe, the spin-flip (21cm) transition, sources of (re)ionization, and the history
of structure formation.

To bring these ideas to life, we will concurrently introduce and demonstrate the
state-of-the-art simulator [21cmFAST](https://github.com/21cmFAST/21cmFAST) to produce
views into the Universe at different stages of its formation.

The presentation slides can be found [here](https://docs.google.com/presentation/d/1jWLQjym993eqXkbzp5phoTTw6hALMFRjHyJcjaA5xqA/edit?usp=sharing).

During the presentation, we will be creating a Jupyter notebook to generate and view the 
outputs of 21cmFAST. A template copy of this notebook is in this repo [here](reionization_theory_tute.ipynb).
A [solutions notebook](reionization_theory_tute_solutions.ipynb) is also available, but
we strongly recommend you use that only *after* the tutorial for reference.


## Required Setup

To follow this tutorial, you'll need to have Anaconda python installed, with the 
`jupyter` package. This should already be installed from other previous sessions.

In addition, you'll need to install `21cmFAST`. There are instructions for this in
the [21cmFAST Documentation](https://21cmfast.readthedocs.io/en/latest/installation.html),
but we will try to condense them for you here. 


**Note:** it is possible that before our session `21cmFAST` will become directly available
as a `conda` package. Before trying any of the instructions below, you should try doing
simply `conda install -c conda-forge 21cmFAST`. Then test if it worked by doing
`python -c "import py21cmfast`. I will try to update these instructions if/when this
happens.

Also note that @steven-murray will be available on the Champ Zoom room for the two hours
before the session if you are having any problems installing.

### Installation on Linux

You should be able to copy and paste the following two lines. If you know you already
have `gcc` installed (try `which gcc` and see if it errors) then you don't need the `gcc`
or `CC=` parts of the commands, though it won't hurt.

```bash
conda install -c conda-forge click scipy pyyaml cffi astropy h5py cached-property fftw gsl gcc
CC=$CONDA_PREFIX/bin/gcc LIB=$CONDA_PREFIX/lib INC=$CONDA_PREFIX/include pip install 21cmFAST
```

### Installation on MacOS

MacOS has a nice C compiler that unfortunately doesn't play well with `21cmFAST` (or a 
lot of other libraries). For relatively recent versions of MacOS the following
instructions should work:

```bash
xcode-select --install
conda install -c conda-forge click scipy pyyaml cffi astropy h5py cached-property fftw gsl gcc
CFLAGS="-isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk" CC=$CONDA_PREFIX/bin/gcc LIB=$CONDA_PREFIX/lib INC=$CONDA_PREFIX/include pip install 21cmFAST
```

If you encounter errors in this process, feel free to peruse [this issue](https://github.com/21cmfast/21cmFAST/issues/84)
(and post your own solution there!), and @steven-murray will also be available on Zoom
the morning of the session for the preceding two hours.

