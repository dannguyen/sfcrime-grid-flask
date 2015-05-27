import csv
import os.path
import pandas as pd

BBOX = ((-122.514683, 37.707461), (-122.356754,37.808894))
BBGRID = (4, 4) # i.e. how many boxes wide and tall
DATA_SAMPLE_FILENAME = os.path.join(os.path.dirname(__file__), 'data/sfcrimeincidents-sample.csv')

def make_grid_boxes(rows = BBGRID[0], cols = BBGRID[1], bbox = BBOX):
    """
    returns a 2-D list, with rows and cols as dimensions
    [[(0, 0), (0, 1)], [(1, 0), (1, 1)]]
    """
    topleft, bottomright = BBOX
    boxw = (bottomright[0] - topleft[0]) / cols
    boxh = (bottomright[1] - topleft[1]) / rows
    grid = []
    for r in range(rows):
        row = []
        x = r * boxw + topleft[0]
        for c in range(cols):
            y = c * boxh + topleft[1]
            row.append((x, y))
        grid.append(row)
    return grid

def divvy_crime_data(grid, data_fname = DATA_SAMPLE_FILENAME):
    pd.load_csv()
