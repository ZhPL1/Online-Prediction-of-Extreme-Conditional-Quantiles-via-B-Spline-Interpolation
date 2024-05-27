from amplpy import AMPL, Environment
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline


# B-spline interpolation
def bspline_interpolation(obs_x, y, new_x, k=3):
    splines = []
    for i in range(x.shape[1]):
        unique_x = np.unique(obs_x[:, i])
        spline = make_interp_spline(unique_x, y, k=k)
        splines.append(spline)

    interpolated_values = [spline(new_x[:, i]) for i, spline in enumerate(splines)]
    return np.mean(interpolated_values, axis=0)


# Import solver
Path = ''
ampl = AMPL(Environment(Path))
ampl.set_option('solver', 'knitro')

# Load data and MPEC model
ampl.read_data('./Observation.dat')
ampl.read('./MPEC.mod')
x = loadmat('./Observation_X.mat')
x = x['x']

# Parameter setting
alpha = 0.5
beta = 0.5
tau = 0.99
tau_thresh = 0.8
n = x.shape[0]
m = x.shape[1]

# Solver begin
gamma_est = []
sigma_est = []
for j in range(n):
    x_j = ampl.get_parameter('X0')
    x_j.set_values(x[j])

    variables = ["alpha", "beta", "gamma", "sigma"]
    for var_name in variables:
        var = ampl.getVariable(var_name)
        var.setValue(1)

    ampl.solve()

    a_j = alpha.value()
    b_j = beta.value()
    gamma.append(gamma.value())
    sigma.append(sigma.value())

est_a = a_j
est_b = b_j

# Test
test_x = np.random.uniform(0, 1, (1, m))
est_gamma = bspline_interpolation(x, gamma, test_x)
est_sigma = bspline_interpolation(x, sigma, test_x)

# Calculate Q and Q_hat
Q = est_a + np.dot(est_b, new_x)
Q_hat = Q + est_sigma / est_gamma * (((1 - tau_thresh) / (1 - tau)) ** est_gamma - 1)
print(Q_hat)
