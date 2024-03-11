import matplotlib.pyplot as plt
from matplotlib import pyplot as patches
import mplcursors
import numpy as np
import random

browser_market_share = {
    'browsers': ['firefox', 'chrome', 'safari', 'edge', 'ie', 'opera'],
    'market_share': [8.61, 15.55, 8.36, 4.12, 2.76, 2.43],
    'color': ['#5A69AF', '#579E65', '#F9C784', '#FC944A', '#F24C00', '#00B825']
}


class WordBubbles:

    minSize = 0
    
    def __init__(self, values):
        self.values = values
        self.values.sort(reverse=True)
        self.bubbles_radius = [(self.values[i] + self.minSize) for i in range(len(self.values))]
        self.bubbles = []
        self.calculate_bubbles()

    def calculate_bubbles(self):
        for i in range(len(self.bubbles_radius)):
            if i == 0:
                self.bubbles.append((0, 0, self.bubbles_radius[i]))
                continue
            else:
                self.place_bubble(self.bubbles_radius[i])

    def place_bubble(self, place_radius):
        angle = random.uniform(0, 2 * np.pi)

        x = np.cos(angle) * (place_radius + self.bubbles[-1][2] + 1) + self.bubbles[-1][0]
        y = np.sin(angle) * (place_radius + self.bubbles[-1][2] + 1) + self.bubbles[-1][1]

        for _ in self.bubbles:
            if not self.is_overlapping(x, y, place_radius):
                return self.bubbles.append((x, y, place_radius))
        self.place_bubble(place_radius)

    def is_overlapping(self, x, y, radius):
        for bubble in self.bubbles:
            val1 = (bubble[0] - x) ** 2 + (bubble[1] - y) ** 2
            val2 = (bubble[2] + radius) ** 2

            if (bubble[0] - x) ** 2 + (bubble[1] - y) ** 2 < (bubble[2] + radius) ** 2:
                return True
        return False

    def plot(self, ax, labels, colors):
        for i in range(len(self.bubbles)):
            circle = plt.Circle((self.bubbles[i][0], self.bubbles[i][1]), self.bubbles[i][2], color="#5A69AF")
            ax.add_patch(circle)
            ax.text(*(self.bubbles[i][0], self.bubbles[i][1]), "ABC", horizontalalignment='center', verticalalignment="center")

if __name__ == "__main__": 
    wb = WordBubbles(browser_market_share['market_share'])

    fig, ax = plt.subplots()

    wb.plot(ax, "", "")
    ax.axis("off")
    ax.relim()
    ax.autoscale_view()
    ax.set_title("Gute Titel")

    plt.show()