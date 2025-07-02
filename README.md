# Pipetting Optimization Simulator

Simulate and optimize pipetting steps for liquid handling workflows (e.g., Hamilton, Tecan, Bravo) using Python.

## Features
- Volume normalization based on max pipette capacity
- 96/384 well plate planning
- Transfer plan generation from CSV input
- Serial dilution simulation across 96-well plates
- Optional interactive visualization with Streamlit

---

## 🔬 Serial Dilution Simulator

Simulates 1:2 serial dilutions down each column of a 96-well plate. Each well's concentration is tracked and visualized as a heatmap.

### Interactive Streamlit App

Launch a web-based app with sliders for:
- Starting concentration
- Dilution factor
- Transfer volume
- Color map selection


📍 **Try it live:**  
[https://pipetting-simulator-gxeqmdutemkxqsuxijttcu.streamlit.app/](https://pipetting-simulator-gxeqmdutemkxqsuxijttcu.streamlit.app/)

### Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
