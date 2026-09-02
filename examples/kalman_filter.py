import numpy as np
from scripts.kalman_filter_1D import compute1DKalmanFilter, plot1DKalmanFilter

dt = 1.0          # Time step (seconds)
total_time = 100  # Total seconds
time = np.arange(0, total_time, dt)

# True state: Starting at 1000 km, moving away at 2 km/s
true_position = 1000.0 + 2.0 * time
true_velocity = 2.0

# Simulate Radar Measurements: True position + Gaussian Noise (std dev = 5 km)
measurement_noise_std = 5.0
noisy_measurements = true_position + np.random.normal(0, measurement_noise_std, len(time))


# State vector: [position, velocity]
x = np.array([1000.0, 0.0]) # Initial guess (we guess velocity is 0, which is wrong!)

# Covariance matrix (P): Our uncertainty in the state. 
# We are very unsure about our initial guess.
P = np.array([[1000.0, 0.0], 
              [0.0,    100.0]])

# Process Noise (Q): Uncertainty in our physical model (e.g., unmodeled drag).
# We assume our constant-velocity model is pretty good, so Q is small.
Q = np.array([[0.1, 0.0], 
              [0.0, 0.1]])

# Measurement Noise (R): Uncertainty of the radar sensor.
R = np.array([[measurement_noise_std**2]])

# State Transition Matrix (F): How the state evolves over dt
# pos_new = pos_old + vel_old * dt
# vel_new = vel_old
F = np.array([[1.0, dt], 
              [0.0, 1.0]])

# Observation Matrix (H): We only measure position, not velocity.
H = np.array([[1.0, 0.0]])

compute1DKalmanFilter(noisy_measurements, x, F, P, Q, H, R)

plot1DKalmanFilter(time, true_position, noisy_measurements, filtered_positions, filtered_velocities)
