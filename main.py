import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# -----------------------------
# Provided Data (Soybeans only)
# -----------------------------
markets = [
    "China",
    "Mexico",
    "European Union-27",
    "Egypt",
    "Japan",
    "Indonesia",
    "Bangladesh",
    "Taiwan",
    "Pakistan",
    "Vietnam"
]

oct_2024 = [17070161, 3879430, 3599600, 1629968, 1582041, 2134640, 342266, 728323, 1291, 723424]
oct_2025 = [5931978, 4376494, 3923900, 3316889, 1910346, 1742046, 1179635, 1024339, 946658, 876151]

# -----------------------------
# Function to create chart
# -----------------------------
def create_bar_chart(parent, title, data, color):
    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.barh(markets, data, color=color)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel("Metric Tons")
    ax.set_ylabel("Export Markets")

    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax.text(
            width + max(data) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{width:,}",
            va='center',
            fontsize=8
        )

    ax.invert_yaxis()  # Highest value at top
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# -----------------------------
# Main Tkinter App
# -----------------------------
def main():
    root = tk.Tk()
    root.title("Top 10 U.S. Soybean Export Markets - Oct 2024 vs Oct 2025")
    root.geometry("1200x750")

    # Title label
    title_label = tk.Label(
        root,
        text="Top 10 U.S. Soybean Export Markets by Volume (Metric Tons)",
        font=("Arial", 16, "bold"),
        pady=10
    )
    title_label.pack()

    # Notebook (Tabs)
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # Tab 1 - Oct 2024
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Oct 2024")
    create_bar_chart(tab1, "January-October 2024 Soybean Exports", oct_2024, "skyblue")

    # Tab 2 - Oct 2025
    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Oct 2025")
    create_bar_chart(tab2, "January-October 2025 Soybean Exports", oct_2025, "lightgreen")

    root.mainloop()

if __name__ == "__main__":
    main()
