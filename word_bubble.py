import matplotlib.pyplot as plt
#import mplcursors
import math

browser_market_share = {
    'browsers': [chr(ord('A') + i) for i in range(26)],
    'market_share': [i + 1 for i in range(26)],
}

class NoMorePlacesError(Exception):
    """Raised when there are no more places to place circles"""

class WordBubbles:
    minSize = 0
    
    def __init__(self, identifiers, values):
        self.identifiers = identifiers
        self.prev_angle = 0
        self.center_bubble_index = 0
        self.values = values
        #self.values.sort(reverse=True)
        self.bubbles_radius = [(self.values[i] + self.minSize) for i in range(len(self.values))]
        self.bubbles = []
        self.calculate_bubbles()

    def calculate_bubbles(self):
        bubble_count = len(self.bubbles_radius)
        i = 0

        while i < bubble_count:
            if i == 0:
                self.bubbles.append((0, 0, self.bubbles_radius[i]))
                i += 1
                continue
            else:
                if self.place_bubble(radius=self.bubbles_radius[i]):
                    # If center bubble is being changed, reset prev_angle
                    self.prev_angle = 0
                    i += 1
                    continue
                else:
                    self.center_bubble_index += 1
                    if (self.center_bubble_index > bubble_count):
                        raise NoMorePlacesError("No more places to place circles. This should not happen, contact developer immedietly.")

    # Looks a little more random when using prev angle.
    def place_bubble(self, radius):
        stepsize = 1
        if self.prev_angle >= 360-stepsize: self.prev_angle = 0

        # Try to place bubble every x degrees
        for angle in range(self.prev_angle, 360, stepsize): # ToDo: CHANGE, VERY INEFFICIENT
            center_x = self.bubbles[self.center_bubble_index][0]
            center_y = self.bubbles[self.center_bubble_index][1]
            added_radius = self.bubbles[self.center_bubble_index][2] + radius 

            x = math.cos(math.radians(angle)) * added_radius + center_x
            y = math.sin(math.radians(angle)) * added_radius + center_y

            if not self.is_overlapping(x, y, radius):
                self.prev_angle = angle
                self.bubbles.append((x, y, radius))
                return True
        return False

    def is_overlapping(self, x, y, radius):
        for bubble in self.bubbles:
            distance_sq = (bubble[0] - x) ** 2 + (bubble[1] - y) ** 2
            min_distance_sq = (bubble[2] + radius) ** 2

            if distance_sq < min_distance_sq:
                return True
        return False

    def plot(self, ax, colors):
        for i in range(len(self.bubbles)):
            circle = plt.Circle((self.bubbles[i][0], self.bubbles[i][1]), self.bubbles[i][2], color="#5A69AF")
            ax.add_patch(circle)
            ax.text(*(self.bubbles[i][0], self.bubbles[i][1]), self.identifiers[i], horizontalalignment='center', verticalalignment="center")
        ax.axis("off")
        ax.relim()
        ax.autoscale_view()

if __name__ == "__main__": 
    wb = WordBubbles(browser_market_share['browsers'], browser_market_share['market_share'])

    fig, ax = plt.subplots()

    wb.plot(ax, "")
    #ax.set_title("Gute Titel")

    plt.show()