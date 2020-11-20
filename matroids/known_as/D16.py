from matroids.CircuitsMatroid import CircuitsMatroid

class D16(CircuitsMatroid):
    def __init__(self):
        pass

    @property
    def ground_set(self) -> list[set[int]]:
        return {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}

    @property
    def size(self) -> int:
        return 16

    @property
    def circuits(self) -> list[set[int]]:
        return [
            {1,2,3,13},{1,2,4,14},{16,1,2,15},{1,3,4,15},{16,1,3,14},{16,1,4,13},{1,13,14,15},
            {16,2,3,4},{2,3,14,15},{2,4,13,15},{16,2,13,14},{3,4,13,14},{16,3,13,15},{16,4,14,15},
            {1,6,8,9,11},{2,5,7,8,11},{3,5,9,10,11},{4,6,7,8,12},{5,7,10,12,15},{5,8,9,12,14},
            {6,7,10,11,13},{6,9,10,12,16},{1,2,5,6,7,9},{1,3,5,6,8,10},{1,4,7,9,11,12},{1,5,6,11,12,14},
            {1,7,8,9,10,13},{1,8,10,11,12,16},{2,3,7,8,9,10},{2,4,5,6,11,12},{2,5,6,8,10,13},{2,7,9,11,12,14},
            {2,8,10,11,12,15},{3,5,6,7,9,13},{3,5,6,11,12,16},{3,7,9,11,12,15},{3,8,10,11,12,14},{4,5,6,7,9,14},
            {4,5,6,8,10,15},{4,7,8,9,10,16},{4,8,10,11,12,13},{5,6,7,9,15,16},{5,6,8,10,14,16},{5,6,11,12,13,15},
            {7,8,9,10,14,15},{7,9,11,12,13,16},{1,2,3,6,7,10,11},{1,2,4,5,8,9,12},{1,2,5,7,10,12,16},
            {1,2,5,9,10,11,13},{1,2,6,7,8,12,14},{1,2,6,9,10,12,15},{1,3,4,5,7,10,12},{1,3,5,7,8,11,13},
            {1,3,5,8,9,12,16},{1,3,6,7,8,12,15},{1,3,6,9,10,12,14},{1,4,5,7,8,11,14},{1,4,5,9,10,11,15},
            {1,4,6,7,10,11,16},{1,4,6,9,10,12,13},{1,5,7,8,11,15,16},{1,5,7,10,12,13,14},{1,5,8,9,12,13,15},
            {1,5,9,10,11,14,16},{1,6,7,8,12,13,16},{1,6,7,10,11,14,15},{2,3,4,6,9,10,12},{2,3,5,7,10,12,14},
            {2,3,5,8,9,12,15},{2,3,6,7,8,12,16},{2,3,6,8,9,11,13},{2,4,5,7,10,12,13},{2,4,5,9,10,11,16},
            {2,4,6,7,10,11,15},{2,4,6,8,9,11,14},{2,5,8,9,12,13,16},{2,5,9,10,11,14,15},{2,6,7,8,12,13,15},
            {2,6,7,10,11,14,16},{2,6,8,9,11,15,16},{2,6,9,10,12,13,14},{3,4,5,7,8,11,16},{3,4,5,8,9,12,13},
            {3,4,6,7,10,11,14},{3,4,6,8,9,11,15},{3,5,7,8,11,14,15},{3,5,7,10,12,13,16},{3,6,7,8,12,13,14},
            {3,6,7,10,11,15,16},{3,6,8,9,11,14,16},{3,6,9,10,12,13,15},{4,5,7,8,11,13,15},{4,5,7,10,12,14,16},
            {4,5,8,9,12,15,16},{4,5,9,10,11,13,14},{4,6,8,9,11,13,16},{4,6,9,10,12,14,15},{5,7,8,11,13,14,16},
            {5,9,10,11,13,15,16},{6,7,8,12,14,15,16},{6,8,9,11,13,14,15},{1,2,3,4,8,10,11,12},{1,2,3,5,6,11,12,15},
            {1,2,3,7,9,11,12,16},{1,2,4,5,6,8,10,16},{1,2,4,7,8,9,10,15},{1,2,5,6,8,10,14,15},{1,2,5,6,11,12,13,16},
            {1,2,7,8,9,10,14,16},{1,2,7,9,11,12,13,15},{1,2,8,10,11,12,13,14},{1,3,4,5,6,7,9,16},{1,3,4,5,6,11,12,13},
            {1,3,4,7,8,9,10,14},{1,3,5,6,7,9,14,15},{1,3,7,8,9,10,15,16},{1,3,7,9,11,12,13,14},{1,3,8,10,11,12,13,15},
            {1,4,5,6,7,9,13,15},{1,4,5,6,8,10,13,14},{1,4,5,6,11,12,15,16},{1,4,8,10,11,12,14,15},{1,5,6,7,9,13,14,16},
            {1,5,6,8,10,13,15,16},{1,7,9,11,12,14,15,16},{2,3,4,5,6,7,9,15},{2,3,4,5,6,8,10,14},{2,3,4,7,9,11,12,13},
            {2,3,5,6,7,9,14,16},{2,3,5,6,8,10,15,16},{2,3,5,6,11,12,13,14},{2,3,8,10,11,12,13,16},{2,4,5,6,7,9,13,16},
            {2,4,7,8,9,10,13,14},{2,4,7,9,11,12,15,16},{2,4,8,10,11,12,14,16},{2,5,6,7,9,13,14,15},{2,5,6,11,12,14,15,16},
            {2,7,8,9,10,13,15,16},{3,4,5,6,8,10,13,16},{3,4,5,6,11,12,14,15},{3,4,7,8,9,10,13,15},{3,4,7,9,11,12,14,16},
            {3,4,8,10,11,12,15,16},{3,5,6,8,10,13,14,15},{3,7,8,9,10,13,14,16},{4,5,6,11,12,13,14,16},{4,7,9,11,12,13,14,15},
            {8,10,11,12,13,14,15,16}
        ]
    
    @property
    def hyperplanes(self) -> list[set[int]]:
        return [
            {1,2,5,6,8,12,15,16},{1,2,5,6,10,11,15,16},{1,2,5,8,9,10,15,16},{1,2,5,9,11,12,15,16},{1,2,6,7,8,10,15,16},
            {1,2,6,7,11,12,15,16},{1,2,7,8,9,12,15,16},{1,2,7,9,10,11,15,16},{1,3,4,5,6,7,11,15},{1,3,4,5,6,9,12,15},
            {1,3,4,5,7,8,9,15},{1,3,4,5,8,11,12,15},{1,3,4,6,7,9,10,15},{1,3,4,6,10,11,12,15},{1,3,4,7,8,10,11,15},
            {1,3,4,8,9,10,12,15},{1,5,6,7,8,13,14,15},{1,5,6,9,10,13,14,15},{1,5,7,9,11,13,14,15},{1,5,8,10,11,13,14,15},
            {1,6,7,9,12,13,14,15},{1,6,8,10,12,13,14,15},{1,7,8,11,12,13,14,15},{1,9,10,11,12,13,14,15},{2,3,4,5,6,7,10,16},
            {2,3,4,5,6,8,9,16},{2,3,4,5,7,9,12,16},{2,3,4,5,8,10,12,16},{2,3,4,6,7,9,11,16},{2,3,4,6,8,10,11,16},
            {2,3,4,7,10,11,12,16},{2,3,4,8,9,11,12,16},{2,5,6,7,12,13,14,16},{2,5,6,9,11,13,14,16},{2,5,7,9,10,13,14,16},
            {2,5,10,11,12,13,14,16},{2,6,7,8,9,13,14,16},{2,6,8,11,12,13,14,16},{2,7,8,10,12,13,14,16},{2,8,9,10,11,13,14,16},
            {3,4,5,6,8,11,13,14},{3,4,5,6,10,12,13,14},{3,4,5,7,8,10,13,14},{3,4,5,7,11,12,13,14},{3,4,6,8,9,10,13,14},
            {3,4,6,9,11,12,13,14},{3,4,7,8,9,11,13,14},{3,4,7,9,10,12,13,14},{1,2,3,5,6,7,9,12,13},{1,2,3,5,6,8,10,12,13},
            {1,2,3,5,7,8,11,12,13},{1,2,3,5,9,10,11,12,13},{1,2,3,6,7,10,11,12,13},{1,2,3,6,8,9,11,12,13},{1,2,3,7,8,9,10,12,13},
            {1,2,4,5,6,7,9,10,14},{1,2,4,5,6,10,11,12,14},{1,2,4,5,7,8,10,11,14},{1,2,4,5,8,9,10,12,14},{1,2,4,6,7,8,10,12,14},
            {1,2,4,6,8,9,10,11,14},{1,2,4,7,9,10,11,12,14},{1,3,5,6,7,8,10,14,16},{1,3,5,6,7,11,12,14,16},{1,3,5,7,8,9,12,14,16},
            {1,3,5,7,9,10,11,14,16},{1,3,6,7,8,9,11,14,16},{1,3,6,7,9,10,12,14,16},{1,3,7,8,10,11,12,14,16},{1,4,5,6,7,8,12,13,16},
            {1,4,5,6,7,10,11,13,16},{1,4,5,6,8,9,11,13,16},{1,4,5,6,9,10,12,13,16},{1,4,5,7,8,9,10,13,16},{1,4,5,7,9,11,12,13,16},
            {1,4,5,8,10,11,12,13,16},{2,3,5,6,7,8,11,14,15},{2,3,5,6,7,10,12,14,15},{2,3,5,6,8,9,12,14,15},{2,3,5,6,9,10,11,14,15},
            {2,3,6,7,8,9,10,14,15},{2,3,6,7,9,11,12,14,15},{2,3,6,8,10,11,12,14,15},{2,4,5,6,8,9,10,13,15},{2,4,5,6,9,11,12,13,15},
            {2,4,5,7,8,9,11,13,15},{2,4,5,7,9,10,12,13,15},{2,4,6,7,8,9,12,13,15},{2,4,6,7,9,10,11,13,15},{2,4,8,9,10,11,12,13,15},
            {3,5,6,7,8,9,13,15,16},{3,5,6,8,11,12,13,15,16},{3,5,7,8,10,12,13,15,16},{3,5,8,9,10,11,13,15,16},{3,6,7,8,10,11,13,15,16},
            {3,6,8,9,10,12,13,15,16},{3,7,8,9,11,12,13,15,16},{4,5,6,7,9,11,14,15,16},{4,5,6,8,10,11,14,15,16},{4,5,7,10,11,12,14,15,16},
            {4,5,8,9,11,12,14,15,16},{4,6,7,8,11,12,14,15,16},{4,6,9,10,11,12,14,15,16},{4,7,8,9,10,11,14,15,16},{1,2,5,6,7,8,9,11,15,16},
            {1,2,5,6,7,9,10,12,15,16},{1,2,5,7,8,10,11,12,15,16},{1,2,6,8,9,10,11,12,15,16},{1,3,4,5,6,7,8,10,12,15},{1,3,4,5,6,8,9,10,11,15},
            {1,3,4,5,7,9,10,11,12,15},{1,3,4,6,7,8,9,11,12,15},{1,5,6,7,10,11,12,13,14,15},{1,5,6,8,9,11,12,13,14,15},{1,5,7,8,9,10,12,13,14,15},
            {1,6,7,8,9,10,11,13,14,15},{2,3,4,5,6,7,8,11,12,16},{2,3,4,5,6,9,10,11,12,16},{2,3,4,5,7,8,9,10,11,16},{2,3,4,6,7,8,9,10,12,16},
            {2,5,6,7,8,10,11,13,14,16},{2,5,6,8,9,10,12,13,14,16},{2,5,7,8,9,11,12,13,14,16},{2,6,7,9,10,11,12,13,14,16},{3,4,5,6,7,8,9,12,13,14},
            {3,4,5,6,7,9,10,11,13,14},{3,4,5,8,9,10,11,12,13,14},{3,4,6,7,8,10,11,12,13,14},{1,2,3,5,6,7,8,9,10,11,13},{1,2,4,5,6,7,8,9,11,12,14},
            {1,3,5,6,8,9,10,11,12,14,16},{1,4,6,7,8,9,10,11,12,13,16},{2,3,5,7,8,9,10,11,12,14,15},{2,4,5,6,7,8,10,11,12,13,15},
            {3,5,6,7,9,10,11,12,13,15,16},{4,5,6,7,8,9,10,12,14,15,16},{1,2,3,4,5,6,7,9,13,14,15,16},{1,2,3,4,5,6,8,10,13,14,15,16},
            {1,2,3,4,5,6,11,12,13,14,15,16},{1,2,3,4,5,7,8,11,13,14,15,16},{1,2,3,4,5,7,10,12,13,14,15,16},{1,2,3,4,5,8,9,12,13,14,15,16},
            {1,2,3,4,5,9,10,11,13,14,15,16},{1,2,3,4,6,7,8,12,13,14,15,16},{1,2,3,4,6,7,10,11,13,14,15,16},{1,2,3,4,6,8,9,11,13,14,15,16},
            {1,2,3,4,6,9,10,12,13,14,15,16},{1,2,3,4,7,8,9,10,13,14,15,16},{1,2,3,4,7,9,11,12,13,14,15,16},{1,2,3,4,8,10,11,12,13,14,15,16}
        ]
    
    @property
    def cocircuits(self) -> list[set[int]]:
        return [
            {9,5,6,7},{8,10,5,6},{11,12,5,6},{8,11,5,7},{10,12,5,7},{8,9,12,5},{9,10,11,5},{8,12,6,7},{10,11,6,7},{8,9,11,6},{9,10,12,6},{8,9,10,7},
            {9,11,12,7},{8,10,11,12},{1,2,3,11,13},{1,2,4,8,14},{1,3,9,14,16},{1,4,6,13,16},{2,3,5,14,15},{2,4,7,13,15},{3,10,13,15,16},{4,12,14,15,16},
            {1,2,5,9,15,16},{1,2,6,7,15,16},{1,2,8,12,15,16},{1,2,10,11,15,16},{1,3,4,5,8,15},{1,3,4,6,10,15},{1,3,4,7,11,15},{1,3,4,9,12,15},
            {1,5,11,13,14,15},{1,6,12,13,14,15},{1,7,8,13,14,15},{1,9,10,13,14,15},{2,3,4,5,12,16},{2,3,4,6,11,16},{2,3,4,7,10,16},{2,3,4,8,9,16},
            {2,5,10,13,14,16},{2,6,8,13,14,16},{2,7,12,13,14,16},{2,9,11,13,14,16},{3,4,5,7,13,14},{3,4,6,9,13,14},{3,4,8,11,13,14},{3,4,10,12,13,14},
            {1,2,3,5,6,12,13},{1,2,3,5,7,8,13},{1,2,3,5,9,10,13},{1,2,3,6,7,10,13},{1,2,3,6,8,9,13},{1,2,3,7,9,12,13},{1,2,3,8,10,12,13},{1,2,4,5,6,10,14},
            {1,2,4,5,7,11,14},{1,2,4,5,9,12,14},{1,2,4,6,7,12,14},{1,2,4,6,9,11,14},{1,2,4,7,9,10,14},{1,2,4,10,11,12,14},{1,3,5,6,7,14,16},{1,3,5,8,12,14,16},
            {1,3,5,10,11,14,16},{1,3,6,8,11,14,16},{1,3,6,10,12,14,16},{1,3,7,8,10,14,16},{1,3,7,11,12,14,16},{1,4,5,7,9,13,16},{1,4,5,8,10,13,16},
            {1,4,5,11,12,13,16},{1,4,7,8,12,13,16},{1,4,7,10,11,13,16},{1,4,8,9,11,13,16},{1,4,9,10,12,13,16},{2,3,6,7,9,14,15},{2,3,6,8,10,14,15},
            {2,3,6,11,12,14,15},{2,3,7,8,11,14,15},{2,3,7,10,12,14,15},{2,3,8,9,12,14,15},{2,3,9,10,11,14,15},{2,4,5,6,9,13,15},{2,4,5,8,11,13,15},
            {2,4,5,10,12,13,15},{2,4,6,8,12,13,15},{2,4,6,10,11,13,15},{2,4,8,9,10,13,15},{2,4,9,11,12,13,15},{3,5,6,8,13,15,16},{3,5,7,12,13,15,16},
            {3,5,9,11,13,15,16},{3,6,7,11,13,15,16},{3,6,9,12,13,15,16},{3,7,8,9,13,15,16},{3,8,11,12,13,15,16},{4,5,6,11,14,15,16},{4,5,7,10,14,15,16},
            {4,5,8,9,14,15,16},{4,6,7,8,14,15,16},{4,6,9,10,14,15,16},{4,7,9,11,14,15,16},{4,8,10,11,14,15,16},{1,2,5,6,8,11,15,16},{1,2,5,6,10,12,15,16},
            {1,2,5,7,8,10,15,16},{1,2,5,7,11,12,15,16},{1,2,6,8,9,10,15,16},{1,2,6,9,11,12,15,16},{1,2,7,8,9,11,15,16},{1,2,7,9,10,12,15,16},{1,3,4,5,6,7,12,15},
            {1,3,4,5,6,9,11,15},{1,3,4,5,7,9,10,15},{1,3,4,5,10,11,12,15},{1,3,4,6,7,8,9,15},{1,3,4,6,8,11,12,15},{1,3,4,7,8,10,12,15},{1,3,4,8,9,10,11,15},
            {1,5,6,7,10,13,14,15},{1,5,6,8,9,13,14,15},{1,5,7,9,12,13,14,15},{1,5,8,10,12,13,14,15},{1,6,7,9,11,13,14,15},{1,6,8,10,11,13,14,15},
            {1,7,10,11,12,13,14,15},{1,8,9,11,12,13,14,15},{2,3,4,5,6,7,8,16},{2,3,4,5,6,9,10,16},{2,3,4,5,7,9,11,16},{2,3,4,5,8,10,11,16},{2,3,4,6,7,9,12,16},
            {2,3,4,6,8,10,12,16},{2,3,4,7,8,11,12,16},{2,3,4,9,10,11,12,16},{2,5,6,7,11,13,14,16},{2,5,6,9,12,13,14,16},{2,5,7,8,9,13,14,16},{2,5,8,11,12,13,14,16},
            {2,6,7,9,10,13,14,16},{2,6,10,11,12,13,14,16},{2,7,8,10,11,13,14,16},{2,8,9,10,12,13,14,16},{3,4,5,6,8,12,13,14},{3,4,5,6,10,11,13,14},{3,4,5,8,9,10,13,14},
            {3,4,5,9,11,12,13,14},{3,4,6,7,8,10,13,14},{3,4,6,7,11,12,13,14},{3,4,7,8,9,12,13,14},{3,4,7,9,10,11,13,14}
        ]
    
    def is_binary(self) -> bool:
        return True

    def is_ternary(self) -> bool:
        return False