
from pyscript import document, display
import numpy as np

# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib.font_manager').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

# Preload to avoid font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data globally
days = []
absences = []

def displaying(e):
    day = document.getElementById("days").value
    absence = int(document.getElementById("absences").value)
    # Save data
    days.append(day)
    absences.append(absence)

    # Convert to NumPy array
    converted_absences = np.array(absences)

    # Create a fresh figure for the new plot
    plt.close('all')
    fig, ax = plt.subplots()
    ax.plot(days, converted_absences, marker='o')
    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")
    ax.grid()

    target = document.getElementById('attendance-graph')
    if target is not None:
        target.innerHTML = ''
    display(fig, target='attendance-graph')
    plt.close(fig)