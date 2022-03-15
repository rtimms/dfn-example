# PyBaMM DFN example

This repository shows an example of how to define your own model and parameter set to use in PyBaMM simulations. This kind of repository may be useful for sharing results from a particular paper, or hosting standalone PyBaMM models. The file `model.py` defines the DFN in a single script (this is equivalent to `pybamm.lithium_ion.BasicDFN`). The file `parameters.py` defines a set of parameter values for an LG M50 cell taken from the paper 

> Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W. Dhammika Widanage, and Emma Kendrick. ["Development of Experimental Techniques for Parameterization of Multi-scale Lithium-ion Battery Models."](https://iopscience.iop.org/article/10.1149/1945-7111/ab9050) Journal of the Electrochemical Society 167 (2020): 080534

    

## 🚀 Installation
In order to run the models and load in any data you will need to install `pybamm`. The example script `example.py` has been tested on PyBaMM Version 22.2. To install the required python packages on Linux/Mac OS use the following terminal commands:

1. Clone the repository
```bash
https://github.com/rtimms/dfn-example
```
2. Change into the `dfn-example` directory 
```bash
cd dfn-example
```
3. Create a virtual environment (optional)
```bash
virtualenv env
```
4. Activate the virtual environment (optional)
```bash
source env/bin/activate
```
5. Install the required packages
```bash 
pip install -r requirements.txt
```

PyBaMM is available on GNU/Linux, MacOS and Windows. For more detailed instructions on how to install PyBaMM, see [the PyBaMM documentation](https://pybamm.readthedocs.io/en/latest/install/GNU-linux.html#user-install).
