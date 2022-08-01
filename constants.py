import os

POSSIBLE_CHOICES = [[1, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]
REDUNDANCY_CHOICES = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9]]

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_FILE = os.path.join(DATA_DIR, "image_source.jpg")
DATA_FILE = os.path.join(DATA_DIR, "bestTime.json")

SIZE_IMAGE = 500

SHUFFLE_NB = 15

