from matroids.Matroid import Matroid

class NotP8(Matroid):
    def __init__(self):
        pass

    @property
    def ground_set(self) -> set[int]:
        return {1,2,3,4,5,6,7,8}

    @property
    def size(self) -> int:
        return 8
    
    @property
    def independent_sets(self) -> list[set[int]]:
        return [
            set(),{1},{2},{3},{4},{5},{6},{7},{8},{1,2},{1,3},{1,4},{1,5},{1,6},{1,7},
            {8,1},{2,3},{2,4},{2,5},{2,6},{2,7},{8,2},{3,4},{3,5},{3,6},{3,7},{8,3},
            {4,5},{4,6},{4,7},{8,4},{5,6},{5,7},{8,5},{6,7},{8,6},{8,7},{1,2,3},{1,2,4},
            {1,2,5},{1,2,6},{1,2,7},{8,1,2},{1,3,4},{1,3,5},{1,3,6},{1,3,7},{8,1,3},
            {1,4,5},{1,4,6},{1,4,7},{8,1,4},{1,5,6},{1,5,7},{8,1,5},{1,6,7},{8,1,6},
            {8,1,7},{2,3,4},{2,3,5},{2,3,6},{2,3,7},{8,2,3},{2,4,5},{2,4,6},{2,4,7},
            {8,2,4},{2,5,6},{2,5,7},{8,2,5},{2,6,7},{8,2,6},{8,2,7},{3,4,5},{3,4,6},
            {3,4,7},{8,3,4},{3,5,6},{3,5,7},{8,3,5},{3,6,7},{8,3,6},{8,3,7},{4,5,6},
            {4,5,7},{8,4,5},{4,6,7},{8,4,6},{8,4,7},{5,6,7},{8,5,6},{8,5,7},{8,6,7},
            {1,2,3,4},{1,2,3,5},{1,2,3,6},{1,2,3,7},{8,1,2,3},{1,2,4,5},{1,2,4,6},{8,1,2,4},
            {1,2,5,6},{1,2,5,7},{8,1,2,5},{1,2,6,7},{8,1,2,7},{1,3,4,5},{1,3,4,7},{8,1,3,4},
            {1,3,5,6},{1,3,5,7},{8,1,3,5},{1,3,6,7},{8,1,3,6},{1,4,5,6},{1,4,5,7},{1,4,6,7},
            {8,1,4,6},{8,1,4,7},{8,1,5,6},{8,1,5,7},{8,1,6,7},{2,3,4,6},{2,3,4,7},{8,2,3,4},
            {2,3,5,6},{2,3,5,7},{8,2,3,5},{8,2,3,6},{8,2,3,7},{2,4,5,6},{2,4,5,7},{8,2,4,5},
            {2,4,6,7},{8,2,4,6},{8,2,4,7},{2,5,6,7},{8,2,5,6},{8,2,6,7},{3,4,5,6},{3,4,5,7},
            {8,3,4,5},{3,4,6,7},{8,3,4,6},{8,3,4,7},{3,5,6,7},{8,3,5,7},{8,3,6,7},{4,5,6,7},
            {8,4,5,6},{8,4,5,7},{8,5,6,7}
        ]
    
    @property
    def bases(self) -> list[set[int]]:
        return [
            {1,2,3,4},{1,2,3,5},{1,2,3,6},{1,2,3,7},{8,1,2,3},{1,2,4,5},{1,2,4,6},{8,1,2,4},
            {1,2,5,6},{1,2,5,7},{8,1,2,5},{1,2,6,7},{8,1,2,7},{1,3,4,5},{1,3,4,7},{8,1,3,4},
            {1,3,5,6},{1,3,5,7},{8,1,3,5},{1,3,6,7},{8,1,3,6},{1,4,5,6},{1,4,5,7},{1,4,6,7},
            {8,1,4,6},{8,1,4,7},{8,1,5,6},{8,1,5,7},{8,1,6,7},{2,3,4,6},{2,3,4,7},{8,2,3,4},
            {2,3,5,6},{2,3,5,7},{8,2,3,5},{8,2,3,6},{8,2,3,7},{2,4,5,6},{2,4,5,7},{8,2,4,5},
            {2,4,6,7},{8,2,4,6},{8,2,4,7},{2,5,6,7},{8,2,5,6},{8,2,6,7},{3,4,5,6},{3,4,5,7},
            {8,3,4,5},{3,4,6,7},{8,3,4,6},{8,3,4,7},{3,5,6,7},{8,3,5,7},{8,3,6,7},{4,5,6,7},
            {8,4,5,6},{8,4,5,7},{8,5,6,7}
        ]
    
    @property
    def circuits(self) -> list[set[int]]:
        return [
            {1,2,4,7},{8,1,2,6},{1,3,4,6},{8,1,3,7},{8,1,4,5},{1,5,6,7},{2,3,4,5},{2,3,6,7},
            {8,2,5,7},{8,3,5,6},{8,4,6,7},{1,2,3,4,8},{1,2,3,5,6},{1,2,3,5,7},{1,2,3,5,8},
            {1,2,4,5,6},{1,3,4,5,7},{2,3,4,6,8},{2,3,4,7,8},{2,4,5,6,7},{2,4,5,6,8},{3,4,5,6,7},{3,4,5,7,8}
        ]
    
    @property
    def hyperplanes(self) -> list[set[int]]:
        return [
            {1,2,3},{1,2,5},{1,3,5},{8,2,3},{2,4,6},{8,2,4},{2,5,6},{3,4,7},{8,3,4},{3,5,7},
            {4,5,6},{4,5,7},{1,2,4,7},{8,1,2,6},{1,3,4,6},{8,1,3,7},{8,1,4,5},{1,5,6,7},
            {2,3,4,5},{2,3,6,7},{8,2,5,7},{8,3,5,6},{8,4,6,7}
        ]
    
    @property
    def cocircuits(self) -> list[set[int]]:
        return [
            {1,2,3,5},{1,2,4,7},{1,3,4,6},{8,1,4,5},{8,1,6,7},{8,2,3,4},{2,3,6,7},{2,4,5,6},
            {8,2,5,7},{3,4,5,7},{8,3,5,6},{1,2,3,6,8},{1,2,3,7,8},{1,2,4,6,8},{1,2,5,6,7},
            {1,2,5,6,8},{1,3,4,7,8},{1,3,5,6,7},{1,3,5,7,8},{1,4,5,6,7},{2,4,6,7,8},{3,4,6,7,8},{4,5,6,7,8}
        ]