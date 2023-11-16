import pygame
from PIL import Image

"""
def find_smallest_missing_number(nums):
    sorted_nums = sorted(nums)

    smallest_missing = 1
    for num in sorted_nums:
        if num == smallest_missing:
            smallest_missing += 1
        elif num > smallest_missing:
            break

    return smallest_missing

print(find_smallest_missing_number([1, 2, 3, 4, 5, 6, 7]))"""



# Teeb PIL image objekti pygame surface objektiks.
def PILpiltPinnaks(PILpilt):
    image_data = PILpilt.tobytes()
    image_dimensions = PILpilt.size
    pygame_surface = pygame.image.fromstring(image_data, image_dimensions, "RGBA")
    return pygame_surface