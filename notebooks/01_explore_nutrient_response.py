import sys
from pathlib import Path

# Find the root folder of the repository
project_root = Path(__file__).resolve().parents[1]

# Tell Python where simulate.py lives
sys.path.insert(0, str(project_root / "src"))

from simulate import generate_data, true_response

import numpy as np
import matplotlib.pyplot as plt

data = generate_data(n_samples=100, seed=42)

plt.figure(figsize=(7, 5))
plt.scatter(
    data["nutrient_a"],
    data["nutrient_b"],
    c=data["response"],
    cmap="viridis",
    s=45,
)

plt.xlabel("Nutrient A (scaled)")
plt.ylabel("Nutrient B (scaled)")
plt.title("Synthetic microbial response measurements")
plt.colorbar(label="Measured response")
plt.tight_layout()
plt.show()


#Visualise the underlying system
grid = np.linspace(0, 1, 100)

a, b = np.meshgrid(grid, grid) # 2D grid of nutrient A and nutrient B values
z = true_response(a, b) #expected response values for each combination of nutrient A and nutrient B

plt.figure(figsize=(7, 5))

plt.contourf(a, b, z, levels=25, cmap="viridis") #contour plot. Regions with similar response values have similar colours.
plt.xlabel("Nutrient A (scaled)")
plt.ylabel("Nutrient B (scaled)")
plt.title("Underlying synthetic response landscape")
plt.colorbar(label="Expected response")
plt.tight_layout()
plt.show()