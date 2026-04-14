import streamlit as st
import time
import math
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Orbiton", layout="centered")

# Title
st.title("🛰️ Orbiton")
st.markdown("### 🚀 Preventing Space Collisions Before They Happen")

# Initialize satellites
sat1 = {"x": 0, "y": 0, "vx": 0.4, "vy": 0.3}
sat2 = {"x": 10, "y": 10, "vx": -0.3, "vy": -0.4}

# Distance function
def distance(a, b):
    return math.sqrt((a["x"] - b["x"])**2 + (a["y"] - b["y"])**2)

# UI placeholders
chart = st.empty()
info = st.empty()

# Button
if st.button("🚀 Start Simulation"):

    for step in range(60):

        # Update positions
        sat1["x"] += sat1["vx"]
        sat1["y"] += sat1["vy"]

        sat2["x"] += sat2["vx"]
        sat2["y"] += sat2["vy"]

        d = distance(sat1, sat2)

        # Risk calculation
        if d < 2:
            risk = "🔴 HIGH"
            status = "⚠️ Collision Imminent!"
        elif d < 5:
            risk = "🟠 MEDIUM"
            status = "⚠️ Potential Risk Detected"
        else:
            risk = "🟢 LOW"
            status = "✅ Safe Orbit"

        # Plot (no colors specified to follow rules)
        fig, ax = plt.subplots()
        ax.scatter(sat1["x"], sat1["y"])
        ax.scatter(sat2["x"], sat2["y"])

        ax.set_xlim(-5, 15)
        ax.set_ylim(-5, 15)
        ax.set_title("Satellite Movement Simulation")

        chart.pyplot(fig)

        # Info display
        info.markdown(f"""
        **Step:** {step}  
        **Distance:** {d:.2f}  
        **Risk Level:** {risk}  
        **Status:** {status}
        """)

        time.sleep(0.3)

# Footer
st.markdown("---")
st.markdown("💡 *Prototype for hackathon demonstration purposes*")
