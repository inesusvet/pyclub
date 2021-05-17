from typing import List, Tuple, NewType

PointType = NewType('PointType', Tuple[float, float])


def main(points: List[PointType], target: PointType, k: int) -> List[PointType]:
    """
    Build a function which will accept a list of points on a plane and return
    a new list of k points closest to a particular target point.

    >>> main([(1, 1), (2, 1), (2, 2)], (0, 0), 2)
    [(1, 1), (2, 1)]
    """
