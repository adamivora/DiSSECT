# DiSSECT: Distinguisher of Standard & Simulated Elliptic Curves through Testing

[![pipeline status](https://gitlab.fi.muni.cz/x408178/curve_analyzer/badges/master/pipeline.svg)](https://gitlab.fi.muni.cz/x408178/curve_analyzer/-/commits/master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://gitlab.fi.muni.cz/x408178/curve_analyzer/-/blob/master/LICENSE)
[![language](https://badgen.net/badge/language/python,sage/purple?list=/)](https://www.sagemath.org/)
[![tests](https://badgen.net/badge/tests/13/blue)](https://gitlab.fi.muni.cz/x408178/curve_analyzer/-/tree/master/curve_analyzer/tests)
[![curves](https://badgen.net/badge/curves/158%20std,%20217188%20sim?list=|)](https://github.com/J08nY/std-curves)

# Setup

From the root directory, run `sage --python3 setup.py develop --user` to initialize the project.

**Virtual environment with sage**: 

- Create virtual environment for python in sage: `sage --python3 -m venv --system-site-packages environment`

- Set environment variable: `os.environ['SAGE_LOCAL'] = 'your_sage_directory/local'`

  You can set it **permanently** (for each python startup) by creating a file in `environment/lib/python3.7/sitepackages` with `import os; os.environ['SAGE_LOCAL'] = 'your_sage_directory/local'` in the directory `environment/lib/python3.7/site-packages/`

- Activate the environment `source environment/bin/activate`

- Run `pip3 install --editable .` in curve_analyzer folder

## Testing the curves

Run `./run_tests.py` in directory `tests`. Use the `-h` flag to get the help menu. To merge the results of a test (a05 in this case) into single file, run `./merge_test_results.py -n a05`.

### Example usage

To run test a05 on all standard curves of bitsizes up to 192 with cofactor 1 or 2 in verbose mode using 3 cores and 100 jobs, run `./run_tests.py -n a05 -c std -v -b 192 -a 1 2 -t 3 -j 100`.

### Supported curve sets

- std: all standard curves
- sim: all simulated curves
- sample: curves secp112r1, secp192r1, secp256r1
- all: all curves in the database

## Overview of available tests

| name    | description                                                                       | implemented        |  computed\*        |time req.\*\* |memory req.\*\*\*
|:-------:| ----------------------------------------------------------------------------------|:------------------:|:------------------:|:------------:|:---------:   
a01    | group stucture of the curve in field extensions                                   | :white_check_mark: | :x:                | high         | low
a02    | CM discriminant, its factorizations and max conductors in field extensions        | :white_check_mark: | :white_check_mark:                | high         | medium
a04    | factorizations of $`kn\pm 1`$                                                     | :white_check_mark: | :white_check_mark:                | high         | high
a05    | field extensions containing nontrivial/full $`l`$-torsion                         | :white_check_mark: | :white_check_mark: | medium       | low
   a06    | Kronecker symbols of CM discriminants in field extensions w.r.t. small primes     | :white_check_mark: | :white_check_mark: | high         | medium
   a08    | class number of the maximal order of the endomorphism ring                        | :white_check_mark: | :x:                | extreme      | low
a12    | multiplicative orders of small primes modulo curve order                          | :white_check_mark: | :white_check_mark: | medium       | medium
a22    | factorizations of small division polynomials                                      | :white_check_mark: | :white_check_mark:             | high         | high
a23    | volcano depth and crater degree in the $`l`$-isogeny graph                        | :white_check_mark: | :white_check_mark: | high         | low
a24    | field extensions containing nontrivial/full number of $`l`$-isogenies             | :white_check_mark: | :white_check_mark:             | medium       | low
a25    | trace in field extensions and its factorization                                   | :white_check_mark: | :white_check_mark: | low          | low
i06    | square parts of $`4q-1`$ and $`4n-1`$                                             | :white_check_mark: | :x:                | low          | low
i07    | distance of $`n`$ from the nearest power of two and multiple of 32/64             | :white_check_mark: | :white_check_mark:             | low          | low

Notation: $`n`$ is the curve order, $`q`$ is the order of the base field  
\* on sim and std curves with at most 256 bits
\*\* this is very rough and subjective  
\*\*\* on the above dataset: low is  <100 MB, medium is 100-500 MB, high is >500 MB (measuring JSONs)

## Overview of planned tests

| name    | description                                                                       | fully specified        
|:-------:| ----------------------------------------------------------------------------------|:------------------:
   a03    | distribution and sizes of isogeny classes                                         | :x: 
   a07    | lifts of curves to other fields                                                   | :x: 
   a09    | existence of pairing-friendly cycles                                              | :x: 
   a10    | existence of factorization bases                                                  | :x: 
   a11    | minimal codewords in elliptic codes                                               | :x: 
   a13    | images of points under pairings                                                   | :x: 
   a14    | conductor and modularity                                                          | :x: 
   a15    | the lattice associated to the curve over $`C`$                                    | :x: 
   a16    | the Neron model                                                                   | :x: 
   a17    | the L-series                                                                      | :x: 
   a18    | the invariant differential                                                        | :x: 
   a19    | local heights                                                                     | :x: 
   a20    | $`S`$-integral points                                                             | :x: 
   a21    | Galois groups of various polynomials                                              | :x:
   a22    | the embedding degree                                                              | :x:
   i01    | curves under parameter bitflips                                                   | :x:
   i02    | curves with the same $`j`$-invariant/group order, but different $`q`$             | :x:
   i03    | the number of modular reductions in various computations                          | :x:
   i04    | the coordinates of special scalar multiples                                       | :x:
   i05    | vulnerability against $`\rho`$ and kangaroo                                       | :x:
i08    | properties of quadratic twists                                                    | :x:
i09    | quadratic residuosity of $`b`$                                                    | :x:
s01    | statistical properties of scalar multiplication                                   | :x:
s02    | distribution of point coordinates in various intervals                            | :x:
   s03    | properties of other curve models                                                  | :x:
   s04    | modular polynomials in given $`j`$-invariant                                      | :x:
   s05    | images of points under isogenies                                                  | :x:
   s06    | summation polynomials                                                             | :x:
   s07    | distributions of curves with similar properties                                   | :x:
   s08    | properties of the function shifting a point by the generator                      | :x:


## Unit tests
Run `sage --python3 -m unittest discover` in directory `tests/unit_tests/`. Only unit tests starting with `test` will be run; those starting with `local` have to be run manually (as they require resources not available on the server).


## Parameters and structure
From directory `tests`, parameter files can be (re)generated by `sage --python3 params.py` and structure files can be (re)generated by `sage --python3 tests/tests_structures.py -t all` (both of these are already done during the setup).
