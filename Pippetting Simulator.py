# pipetting_sim/app.py
import streamlit as st
from pipetting_sim.simulator import PipettingSimulator
from pipetting_sim.visualizer import PlateVisualizer

st.title("Pipetting Optimization Simulator")

st.markdown("""
Simulate and optimize pipetting steps for 96- or 384-well plates.
Upload a CSV file with sample volumes and define source/destination parameters.
""")

uploaded_file = st.file_uploader("Upload sample volume CSV", type="csv")

if uploaded_file:
    simulator = PipettingSimulator(uploaded_file)
    results = simulator.optimize_transfers()
    visual = PlateVisualizer(results)

    st.subheader("Transfer Plan")
    st.dataframe(results)

    st.subheader("Plate Visualization")
    st.pyplot(visual.plot())

