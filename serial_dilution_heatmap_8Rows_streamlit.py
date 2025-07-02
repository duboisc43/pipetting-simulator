import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

# Pipette logic
class Pipette:
    def __init__(self, max_volume=200, error_rate=0.01):
        self.max_volume = max_volume
        self.error_rate = error_rate
        self.current_volume = 0

    def aspirate(self, volume):
        if volume > self.max_volume:
            raise ValueError("Volume exceeds pipette capacity.")
        error = volume * random.uniform(-self.error_rate, self.error_rate)
        self.current_volume = volume + error
        return self.current_volume

    def dispense(self):
        dispensed_volume = self.current_volume
        self.current_volume = 0
        return dispensed_volume

# Simulation function
def simulate_plate(start_conc=100.0, dilution_factor=2.0, transfer_volume=100.0):
    plate = np.zeros((8, 12))  # 96-well layout
    pipette = Pipette()

    for col in range(12):
        plate[0, col] = start_conc
        for row in range(1, 8):
            pipette.aspirate(transfer_volume)
            pipette.dispense()
            plate[row, col] = plate[row - 1, col] / dilution_factor

    return plate

# Plotting function
def plot_plate(plate_data, cmap="plasma"):
    fig, ax = plt.subplots(figsize=(10, 5))
    cax = ax.imshow(plate_data, cmap=cmap, interpolation="nearest")

    # Label axes
    ax.set_xticks(np.arange(12))
    ax.set_yticks(np.arange(8))
    ax.set_xticklabels([str(i+1) for i in range(12)])
    ax.set_yticklabels(["A", "B", "C", "D", "E", "F", "G", "H"])

    for i in range(8):
        for j in range(12):
            val = plate_data[i, j]
            label = f"{val:.1f}" if val > 0 else ""
            color = "white" if val > 50 else "black"
            ax.text(j, i, label, ha="center", va="center", color=color, fontsize=7)

    ax.set_title("Serial Dilution Heatmap")
    fig.colorbar(cax, label="Concentration")
    return fig

# Streamlit App
st.title("🔬 96-Well Plate Serial Dilution Simulator")

# User controls
start_conc = st.slider("Starting Concentration", 10.0, 500.0, 100.0, step=10.0)
dilution_factor = st.slider("Dilution Factor", 1.1, 10.0, 2.0, step=0.1)
transfer_volume = st.slider("Transfer Volume (µL)", 10.0, 200.0, 100.0, step=10.0)
colormap = st.selectbox("Colormap", ["viridis", "plasma", "inferno", "coolwarm", "Blues", "magma", "YlGnBu"])

# Run simulation
plate = simulate_plate(start_conc, dilution_factor, transfer_volume)
fig = plot_plate(plate, cmap=colormap)
st.pyplot(fig)
