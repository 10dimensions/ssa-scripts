import numpy as np
import matplotlib.pyplot as plt
 
def compute1DKalmanFilter(noisy_measurements, x, F, P, Q, H, R ):
  filtered_positions = []
  filtered_velocities = []
  
  for z in noisy_measurements:
      # --- PREDICT STEP ---
      # 1. Predict the new state
      x = F @ x
      
      # 2. Predict the new uncertainty (covariance grows)
      P = F @ P @ F.T + Q
      
      # --- UPDATE STEP ---
      # 3. Calculate the "Innovation" (difference between measurement and prediction)
      # H @ x is our predicted measurement. z is the actual noisy measurement.
      y = z - (H @ x)
      
      # 4. Calculate the Innovation Covariance (S)
      S = H @ P @ H.T + R
    
      # 5. Calculate the Kalman Gain (K)
      # K determines how much we trust the new measurement vs. our prediction.
      K = P @ H.T @ np.linalg.inv(S)
      
      # 6. Update the state estimate
      x = x + (K @ y)
      
      # 7. Update the uncertainty (covariance shrinks after a measurement!)
      I = np.eye(2)
      P = (I - K @ H) @ P
      
      # Store for plotting
      filtered_positions.append(x[0])
      filtered_velocities.append(x[1])

  return filtered_positions
  return filtered_velocities
  

def plot1DKalmanFilter(time, true_position, noisy_measurements, filtered_positions, filtered_velocities):
  plt.figure(figsize=(12, 6))
  
  # Plot Position
  plt.subplot(2, 1, 1)
  plt.plot(time, true_position, label='True Orbit (Hidden from Filter)', color='green', linewidth=2)
  plt.scatter(time, noisy_measurements, label='Noisy Radar Measurements', color='red', alpha=0.4, s=10)
  plt.plot(time, filtered_positions, label='Kalman Filter Estimate', color='blue', linewidth=2)
  plt.title("1D Kalman Filter: Smoothing Noisy Radar Range Data", fontsize=14)
  plt.ylabel("Range (km)")
  plt.legend()
  plt.grid(True, alpha=0.3)
  
  # Plot Velocity (to show the filter learning the hidden state!)
  plt.subplot(2, 1, 2)
  plt.axhline(true_velocity, label='True Velocity (2.0 km/s)', color='green', linestyle='--')
  plt.plot(time, filtered_velocities, label='Kalman Filter Estimated Velocity', color='blue', linewidth=2)
  plt.title("Bonus: The Filter Learns the Hidden Velocity State", fontsize=14)
  plt.xlabel("Time (seconds)")
  plt.ylabel("Velocity (km/s)")
  plt.legend()
  plt.grid(True, alpha=0.3)
  
  plt.tight_layout()
  plt.show()

print(f"Final Estimated Velocity: {filtered_velocities[-1]:.2f} km/s (True: {true_velocity} km/s)")
