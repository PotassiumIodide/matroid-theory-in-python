from matroids.Matroid import Matroid

class K33dual(Matroid):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "M*(K3, 3): Regular matroid of rank 4 on 9 elements with 81 bases"

    @property
    def ground_set(self) -> set[int]:
        return {1,2,3,4,5,6,7,8,9}
    
    @property
    def size(self) -> int:
        return 9
    
    @property
    def independent_sets(self) -> list[set[int]]:
        return [
            set(),{1},{2},{3},{4},{5},{6},{7},{8},{9},{1,2},{1,3},{1,4},{1,5},{1,6},
            {1,7},{8,1},{1,9},{2,3},{2,4},{2,5},{2,6},{2,7},{8,2},{9,2},{3,4},{3,5},
            {3,6},{3,7},{8,3},{9,3},{4,5},{4,6},{4,7},{8,4},{9,4},{5,6},{5,7},{8,5},
            {9,5},{6,7},{8,6},{9,6},{8,7},{9,7},{8,9},{1,2,4},{1,2,5},{1,2,6},{1,2,7},
            {8,1,2},{1,2,9},{1,3,4},{1,3,5},{1,3,6},{1,3,7},{8,1,3},{1,3,9},{1,4,5},
            {1,4,6},{8,1,4},{1,4,9},{1,5,6},{1,5,7},{8,1,5},{1,5,9},{1,6,7},{8,1,6},
            {1,6,9},{8,1,7},{1,9,7},{8,1,9},{2,3,4},{2,3,5},{2,3,6},{2,3,7},{8,2,3},
            {9,2,3},{2,4,5},{2,4,6},{2,4,7},{8,2,4},{9,2,4},{2,5,6},{2,5,7},{9,2,5},
            {2,6,7},{8,2,6},{9,2,6},{8,2,7},{9,2,7},{8,9,2},{3,4,5},{3,4,6},{3,4,7},
            {8,3,4},{9,3,4},{3,5,6},{3,5,7},{8,3,5},{9,3,5},{3,6,7},{8,3,6},{8,3,7},
            {9,3,7},{8,9,3},{4,5,7},{8,4,5},{9,4,5},{4,6,7},{8,4,6},{9,4,6},{8,4,7},
            {9,4,7},{8,9,4},{5,6,7},{8,5,6},{9,5,6},{8,5,7},{9,5,7},{8,9,5},{8,6,7},
            {9,6,7},{8,9,6},{1,2,4,5},{1,2,4,6},{8,1,2,4},{1,2,4,9},{1,2,5,6},{1,2,5,7},
            {1,2,5,9},{1,2,6,7},{8,1,2,6},{8,1,2,7},{1,2,9,7},{8,1,2,9},{1,3,4,5},
            {1,3,4,6},{8,1,3,4},{1,3,4,9},{1,3,5,6},{1,3,5,7},{1,3,5,9},{1,3,6,7},
            {8,1,3,6},{8,1,3,7},{1,3,9,7},{8,1,3,9},{8,1,4,5},{1,4,5,9},{8,1,4,6},
            {1,4,6,9},{8,1,5,6},{1,5,6,9},{8,1,5,7},{1,5,9,7},{8,1,5,9},{8,1,6,7},
            {1,9,6,7},{8,1,6,9},{2,3,4,5},{2,3,4,6},{8,2,3,4},{9,2,3,4},{2,3,5,6},
            {2,3,5,7},{9,2,3,5},{2,3,6,7},{8,2,3,6},{8,2,3,7},{9,2,3,7},{8,9,2,3},
            {2,4,5,7},{9,2,4,5},{2,4,6,7},{9,2,4,6},{8,2,4,7},{9,2,4,7},{8,9,2,4},
            {2,5,6,7},{9,2,5,6},{8,2,6,7},{9,2,6,7},{8,9,2,6},{3,4,5,7},{8,3,4,5},
            {3,4,6,7},{8,3,4,6},{8,3,4,7},{9,3,4,7},{8,9,3,4},{3,5,6,7},{8,3,5,6},
            {8,3,5,7},{9,3,5,7},{8,9,3,5},{8,4,5,7},{9,4,5,7},{8,9,4,5},{8,4,6,7},
            {9,4,6,7},{8,9,4,6},{8,5,6,7},{9,5,6,7},{8,9,5,6}
        ]
    
    @property
    def bases(self) -> list[set[int]]:
        return [
            {1,2,4,5},{1,2,4,6},{8,1,2,4},{1,2,4,9},{1,2,5,6},{1,2,5,7},{1,2,5,9},
            {1,2,6,7},{8,1,2,6},{8,1,2,7},{1,2,9,7},{8,1,2,9},{1,3,4,5},{1,3,4,6},
            {8,1,3,4},{1,3,4,9},{1,3,5,6},{1,3,5,7},{1,3,5,9},{1,3,6,7},{8,1,3,6},
            {8,1,3,7},{1,3,9,7},{8,1,3,9},{8,1,4,5},{1,4,5,9},{8,1,4,6},{1,4,6,9},
            {8,1,5,6},{1,5,6,9},{8,1,5,7},{1,5,9,7},{8,1,5,9},{8,1,6,7},{1,9,6,7},
            {8,1,6,9},{2,3,4,5},{2,3,4,6},{8,2,3,4},{9,2,3,4},{2,3,5,6},{2,3,5,7},
            {9,2,3,5},{2,3,6,7},{8,2,3,6},{8,2,3,7},{9,2,3,7},{8,9,2,3},{2,4,5,7},
            {9,2,4,5},{2,4,6,7},{9,2,4,6},{8,2,4,7},{9,2,4,7},{8,9,2,4},{2,5,6,7},
            {9,2,5,6},{8,2,6,7},{9,2,6,7},{8,9,2,6},{3,4,5,7},{8,3,4,5},{3,4,6,7},
            {8,3,4,6},{8,3,4,7},{9,3,4,7},{8,9,3,4},{3,5,6,7},{8,3,5,6},{8,3,5,7},
            {9,3,5,7},{8,9,3,5},{8,4,5,7},{9,4,5,7},{8,9,4,5},{8,4,6,7},{9,4,6,7},
            {8,9,4,6},{8,5,6,7},{9,5,6,7},{8,9,5,6}
        ]
    
    @property
    def circuits(self) -> list[set[int]]:
        return [
            {1,2,3},{1,4,7},{8,2,5},{9,3,6},{4,5,6},{8,9,7},{1,2,6,9},{8,1,3,5},
            {8,1,4,9},{1,5,6,7},{2,3,4,7},{8,2,4,6},{9,2,5,7},{9,3,4,5},{8,3,6,7},
            {1,2,4,5,9},{1,2,6,7,8},{1,3,4,6,8},{1,3,5,7,9},{1,5,6,8,9},{2,3,4,8,9},
            {2,3,5,6,7},{2,4,6,7,9},{3,4,5,7,8}
        ]
    
    @property
    def hyperplanes(self) -> list[set[int]]:
        return [
            {1,5,9},{8,1,6},{9,2,4},{2,6,7},{8,3,4},{3,5,7},{1,2,3,4,7},{1,2,3,5,8},
            {1,2,3,6,9},{1,4,5,6,7},{1,4,7,8,9},{2,4,5,6,8},{2,5,7,8,9},{3,4,5,6,9},{3,6,7,8,9}
        ]
    
    @property
    def cocircuits(self) -> list[set[int]]:
        return [
            {1,2,4,5},{8,1,2,7},{1,3,4,6},{1,3,9,7},{2,3,5,6},{8,9,2,3},{8,4,5,7},{9,4,6,7},
            {8,9,5,6},{1,2,4,6,8,9},{1,2,5,6,7,9},{1,3,4,5,8,9},{1,3,5,6,7,8},{2,3,4,5,7,9},{2,3,4,6,7,8}
        ]
    
    def is_binary(self) -> bool:
        return True

    def is_binary(self) -> bool:
        return True