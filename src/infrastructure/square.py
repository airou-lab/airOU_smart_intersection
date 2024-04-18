def find_other_corners(corner1, corner3):
    """
    Given two opposite corners of a square, find the other two corners.

    Parameters:
    - corner1: Tuple representing the coordinates of one corner (x1, y1)
    - corner2: Tuple representing the coordinates of the opposite corner (x2, y2)

    Returns:
    - List containing coordinates of the other two corners [(x3, y3), (x4, y4)]
    """
    x1, y1 = corner1
    x3, y3 = corner3

    # Find the midpoint between the two corners
    midpoint = ((x1 + x3) / 2, (y1 + y3) / 2)

    # Find the vector from the center to one corner
    radius = [(midpoint[0] - x1), (midpoint[1] - y1)]

    # Calculate the coordinates of the other corners using symmetry
    x2 = midpoint[0] - radius[1]
    y2 = midpoint[1] + radius[0]

    x4 = midpoint[0] + radius[1]
    y4 = midpoint[1] - radius[0]

    return [(x2,y2), (x4, y4)]

if __name__ == "__main__":
    # Example usage:
    corner1 = (1, -2)
    corner2 = (1, -3)
    print(find_other_corners(corner1, corner2))
