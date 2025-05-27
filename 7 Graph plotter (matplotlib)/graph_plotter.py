import matplotlib.pyplot as plt
import numpy as np

def plot_sine_wave():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.title("Sinüs Dalgası / Sine Wave")
    plt.xlabel("X ekseni")
    plt.ylabel("Y ekseni")
    plt.grid(True)
    plt.show()

def main():
    plot_sine_wave()

if __name__ == "__main__":
    main()
