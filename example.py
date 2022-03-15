import pybamm

# import model and create an instance
from model import DFN

model = DFN()

# import parameters
from parameters import parameter_values

# create and solve simulation
# 1C constant current discharge
sim = pybamm.Simulation(model, parameter_values=parameter_values)
sim.solve([0, 3600])  # solve for 1 hour

# plot
# note these are mostly dimensionless variables!
vars_to_plot = [
    "Negative particle surface concentration",
    "Electrolyte concentration",
    "Positive particle surface concentration",
    "Current [A]",
    "Negative electrode potential",
    "Electrolyte potential",
    "Positive electrode potential",
    "Terminal voltage",
]
sim.plot(vars_to_plot)
