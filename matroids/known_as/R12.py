from matroids.Matroid import Matroid

class R12(Matroid):
    def __init__(self):
        pass

    @property
    def ground_set(self) -> set[int]:
        return {1,2,3,4,5,6,7,8,9,10,11,12}
    
    @property
    def size(self) -> int:
        return 12
    
    @property
    def independent_sets(self) -> list[set[int]]:
        return [
            set(),{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{1,2},{1,3},{1,4},
            {1,5},{1,6},{1,7},{8,1},{1,9},{1,10},{1,11},{1,12},{2,3},{2,4},{2,5},{2,6},
            {2,7},{8,2},{9,2},{2,10},{2,11},{2,12},{3,4},{3,5},{3,6},{3,7},{8,3},{9,3},
            {10,3},{11,3},{3,12},{4,5},{4,6},{4,7},{8,4},{9,4},{10,4},{11,4},{4,12},
            {5,6},{5,7},{8,5},{9,5},{10,5},{11,5},{12,5},{6,7},{8,6},{9,6},{10,6},
            {11,6},{12,6},{8,7},{9,7},{10,7},{11,7},{12,7},{8,9},{8,10},{8,11},{8,12},
            {9,10},{9,11},{9,12},{10,11},{10,12},{11,12},{1,2,3},{1,2,4},{1,2,5},
            {1,2,6},{1,2,7},{8,1,2},{1,2,9},{1,2,10},{1,2,11},{1,2,12},{1,3,4},
            {1,3,5},{1,3,6},{1,3,7},{8,1,3},{1,3,9},{1,10,3},{11,1,3},{1,3,12},
            {1,4,5},{1,4,6},{1,4,7},{8,1,4},{1,4,9},{1,10,4},{1,11,4},{1,4,12},
            {1,5,6},{1,5,7},{8,1,5},{1,10,5},{1,11,5},{1,12,5},{1,6,7},{8,1,6},
            {1,6,9},{1,10,6},{1,11,6},{1,12,6},{8,1,7},{1,9,7},{1,10,7},{1,11,7},
            {1,12,7},{8,1,9},{8,1,10},{8,1,11},{8,1,12},{1,10,9},{1,11,9},{1,12,9},
            {1,10,11},{1,10,12},{1,11,12},{2,3,4},{2,3,5},{2,3,6},{2,3,7},{8,2,3},
            {9,2,3},{10,2,3},{11,2,3},{2,3,12},{2,4,5},{2,4,6},{2,4,7},{8,2,4},{9,2,4},
            {2,10,4},{2,11,4},{2,4,12},{2,5,6},{2,5,7},{8,2,5},{9,2,5},{2,10,5},
            {2,11,5},{2,12,5},{2,6,7},{8,2,6},{9,2,6},{2,11,6},{2,12,6},{8,2,7},
            {9,2,7},{2,10,7},{2,11,7},{2,12,7},{8,9,2},{8,2,10},{8,2,11},{8,2,12},
            {9,2,10},{9,2,11},{9,2,12},{11,2,10},{2,10,12},{2,11,12},{3,4,5},{3,4,6},
            {3,4,7},{8,3,4},{9,3,4},{10,3,4},{11,3,4},{3,4,12},{3,5,6},{3,5,7},{8,3,5},
            {9,3,5},{10,3,5},{11,3,5},{3,12,5},{3,6,7},{8,3,6},{9,3,6},{10,3,6},
            {11,3,6},{3,12,6},{8,3,7},{9,3,7},{10,3,7},{11,3,7},{3,12,7},{8,9,3},
            {8,10,3},{8,11,3},{8,3,12},{9,10,3},{11,9,3},{9,3,12},{11,10,3},{10,3,12},
            {11,3,12},{4,5,6},{4,5,7},{8,4,5},{9,4,5},{10,4,5},{11,4,5},{12,4,5},
            {4,6,7},{8,4,6},{9,4,6},{10,4,6},{11,4,6},{4,12,6},{8,4,7},{9,4,7},{10,4,7},
            {11,4,7},{4,12,7},{8,9,4},{8,10,4},{8,11,4},{8,4,12},{9,10,4},{9,11,4},
            {9,4,12},{10,11,4},{10,4,12},{11,4,12},{5,6,7},{8,5,6},{9,5,6},{10,5,6},
            {11,5,6},{12,5,6},{8,5,7},{9,5,7},{10,5,7},{11,5,7},{12,5,7},{8,9,5},
            {8,10,5},{8,11,5},{8,12,5},{9,10,5},{9,11,5},{9,12,5},{10,11,5},{10,12,5},
            {11,12,5},{8,6,7},{9,6,7},{10,6,7},{11,6,7},{12,6,7},{8,9,6},{8,10,6},
            {8,11,6},{8,12,6},{9,10,6},{9,11,6},{9,12,6},{10,11,6},{10,12,6},{11,12,6},
            {8,9,7},{8,10,7},{8,11,7},{8,12,7},{9,10,7},{9,11,7},{9,12,7},{10,11,7},
            {10,12,7},{11,12,7},{8,9,10},{8,9,11},{8,9,12},{8,10,11},{8,10,12},
            {8,11,12},{9,10,11},{9,10,12},{9,11,12},{10,11,12},{1,2,3,4},{1,2,3,5},
            {1,2,3,6},{8,1,2,3},{1,2,3,9},{10,1,2,3},{11,1,2,3},{1,2,3,12},{1,2,4,5},
            {1,2,4,6},{1,2,4,7},{1,2,4,9},{1,2,10,4},{1,2,11,4},{1,2,4,12},{1,2,5,6},
            {1,2,5,7},{8,1,2,5},{1,2,10,5},{1,2,11,5},{1,2,12,5},{1,2,6,7},{8,1,2,6},
            {1,2,6,9},{1,2,11,6},{1,2,12,6},{8,1,2,7},{1,2,9,7},{1,2,10,7},{1,2,11,7},
            {1,2,12,7},{8,1,2,9},{8,1,2,10},{8,1,2,11},{8,1,2,12},{1,2,10,9},{1,2,11,9},
            {1,2,12,9},{11,1,2,10},{1,2,10,12},{1,2,11,12},{1,3,4,5},{1,3,4,6},
            {1,3,4,7},{8,1,3,4},{1,3,4,9},{1,10,3,4},{11,1,3,4},{1,3,4,12},{1,3,5,6},
            {1,3,5,7},{8,1,3,5},{1,10,3,5},{11,1,3,5},{1,3,12,5},{1,3,6,7},{8,1,3,6},
            {1,3,6,9},{1,10,3,6},{11,1,3,6},{1,3,12,6},{8,1,3,7},{1,3,9,7},{1,10,3,7},
            {11,1,3,7},{1,3,12,7},{8,1,3,9},{8,1,10,3},{8,1,3,11},{8,1,3,12},{1,10,3,9},
            {11,1,3,9},{1,3,12,9},{11,1,10,3},{1,10,3,12},{11,1,3,12},{1,4,5,6},
            {1,4,5,7},{8,1,4,5},{1,10,4,5},{1,11,4,5},{1,12,4,5},{1,4,6,7},{8,1,4,6},
            {1,4,6,9},{1,10,4,6},{1,11,4,6},{1,4,12,6},{8,1,4,7},{1,4,9,7},{1,10,4,7},
            {1,11,4,7},{1,4,12,7},{8,1,4,9},{8,1,10,4},{8,1,11,4},{8,1,4,12},{1,10,4,9},
            {1,11,4,9},{1,4,12,9},{1,10,11,4},{1,10,4,12},{1,11,4,12},{1,5,6,7},
            {8,1,5,6},{1,10,5,6},{1,11,5,6},{1,12,5,6},{8,1,5,7},{1,10,5,7},{1,11,5,7},
            {1,12,5,7},{8,1,10,5},{8,1,11,5},{8,1,12,5},{1,10,11,5},{1,10,12,5},
            {1,11,12,5},{8,1,6,7},{1,9,6,7},{1,10,6,7},{1,11,6,7},{1,12,6,7},{8,1,6,9},
            {8,1,10,6},{8,1,11,6},{8,1,12,6},{1,10,6,9},{1,11,6,9},{1,12,6,9},
            {1,10,11,6},{1,10,12,6},{1,11,12,6},{8,1,9,7},{8,1,10,7},{8,1,11,7},
            {8,1,12,7},{1,10,9,7},{1,11,9,7},{1,12,9,7},{1,10,11,7},{1,10,12,7},
            {1,11,12,7},{8,1,10,9},{8,1,11,9},{8,1,12,9},{8,1,10,11},{8,1,10,12},
            {8,1,11,12},{1,10,11,9},{1,10,12,9},{1,11,12,9},{1,10,11,12},{2,3,4,5},
            {2,3,4,6},{2,3,4,7},{8,2,3,4},{9,2,3,4},{10,2,3,4},{11,2,3,4},{2,3,4,12},
            {2,3,5,6},{2,3,5,7},{8,2,3,5},{9,2,3,5},{10,2,3,5},{11,2,3,5},{2,3,12,5},
            {2,3,6,7},{8,2,3,6},{9,2,3,6},{11,2,3,6},{2,3,12,6},{8,2,3,7},{9,2,3,7},
            {10,2,3,7},{11,2,3,7},{2,3,12,7},{8,9,2,3},{8,10,2,3},{8,11,2,3},{8,2,3,12}
            ,{10,9,2,3},{11,9,2,3},{9,2,3,12},{10,11,2,3},{10,2,3,12},{11,2,3,12},
            {2,4,5,6},{2,4,5,7},{8,2,4,5},{9,2,4,5},{2,10,4,5},{2,11,4,5},{2,12,4,5},
            {2,4,6,7},{8,2,4,6},{9,2,4,6},{2,11,4,6},{2,4,12,6},{8,2,4,7},{9,2,4,7},
            {2,10,4,7},{2,11,4,7},{2,4,12,7},{8,9,2,4},{8,2,10,4},{8,2,11,4},{8,2,4,12},
            {9,2,10,4},{9,2,11,4},{9,2,4,12},{11,2,10,4},{2,10,4,12},{2,11,4,12},{2,5,6,7},
            {8,2,5,6},{9,2,5,6},{2,11,5,6},{2,12,5,6},{8,2,5,7},{9,2,5,7},{2,10,5,7},
            {2,11,5,7},{2,12,5,7},{8,9,2,5},{8,2,10,5},{8,2,11,5},{8,2,12,5},{9,2,10,5},
            {9,2,11,5},{9,2,12,5},{11,2,10,5},{2,10,12,5},{2,11,12,5},{8,2,6,7},{9,2,6,7},
            {2,11,6,7},{2,12,6,7},{8,9,2,6},{8,2,11,6},{8,2,12,6},{9,2,11,6},{9,2,12,6},
            {2,11,12,6},{8,9,2,7},{8,2,10,7},{8,2,11,7},{8,2,12,7},{9,2,10,7},{9,2,11,7},
            {9,2,12,7},{11,2,10,7},{2,10,12,7},{2,11,12,7},{8,9,2,10},{8,9,2,11},
            {8,9,2,12},{8,11,2,10},{8,2,10,12},{8,2,11,12},{11,9,2,10},{9,2,10,12},
            {9,2,11,12},{11,2,10,12},{3,4,5,6},{3,4,5,7},{8,3,4,5},{9,3,4,5},{10,3,4,5},
            {11,3,4,5},{12,3,4,5},{3,4,6,7},{8,3,4,6},{9,3,4,6},{10,3,4,6},{11,3,4,6},
            {3,4,12,6},{9,3,4,7},{10,3,4,7},{11,3,4,7},{3,4,12,7},{8,9,3,4},{8,10,3,4},
            {8,11,3,4},{8,3,4,12},{9,10,3,4},{11,9,3,4},{9,3,4,12},{11,10,3,4},
            {10,3,4,12},{3,5,6,7},{8,3,5,6},{9,3,5,6},{10,3,5,6},{3,12,5,6},{8,3,5,7},
            {9,3,5,7},{10,3,5,7},{11,3,5,7},{3,12,5,7},{8,9,3,5},{8,10,3,5},{8,11,3,5},
            {8,3,12,5},{9,10,3,5},{11,9,3,5},{9,3,12,5},{11,10,3,5},{10,3,12,5},
            {11,3,12,5},{8,3,6,7},{9,3,6,7},{10,3,6,7},{11,3,6,7},{3,12,6,7},{8,9,3,6},
            {8,10,3,6},{8,11,3,6},{8,3,12,6},{9,10,3,6},{11,9,3,6},{9,3,12,6},
            {11,10,3,6},{10,3,12,6},{11,3,12,6},{8,9,3,7},{8,10,3,7},{8,11,3,7},
            {8,3,12,7},{9,10,3,7},{11,9,3,7},{9,3,12,7},{11,10,3,7},{10,3,12,7},
            {11,3,12,7},{8,9,10,3},{8,9,3,11},{8,9,3,12},{8,11,10,3},{8,10,3,12},
            {8,11,3,12},{11,9,10,3},{9,10,3,12},{11,9,3,12},{11,10,3,12},{4,5,6,7},
            {8,4,5,6},{9,4,5,6},{10,4,5,6},{11,4,5,6},{8,4,5,7},{9,4,5,7},{10,4,5,7},
            {11,4,5,7},{12,4,5,7},{8,9,4,5},{8,10,4,5},{8,11,4,5},{8,12,4,5},{9,10,4,5},
            {9,11,4,5},{9,12,4,5},{10,11,4,5},{10,12,4,5},{12,11,4,5},{8,4,6,7},
            {9,4,6,7},{10,4,6,7},{11,4,6,7},{4,12,6,7},{8,9,4,6},{8,10,4,6},
            {8,11,4,6},{8,4,12,6},{9,10,4,6},{9,11,4,6},{9,4,12,6},{10,11,4,6},
            {10,4,12,6},{11,4,12,6},{8,9,4,7},{8,10,4,7},{8,11,4,7},{8,4,12,7},
            {9,10,4,7},{9,11,4,7},{9,4,12,7},{10,11,4,7},{10,4,12,7},{11,4,12,7},
            {8,9,10,4},{8,9,11,4},{8,9,4,12},{8,10,11,4},{8,10,4,12},{8,11,4,12},
            {9,10,11,4},{9,10,4,12},{9,11,4,12},{10,11,4,12},{8,5,6,7},{9,5,6,7},
            {10,5,6,7},{11,5,6,7},{12,5,6,7},{8,9,5,6},{8,10,5,6},{8,11,5,6},
            {8,12,5,6},{9,10,5,6},{9,11,5,6},{9,12,5,6},{10,11,5,6},{10,12,5,6},
            {11,12,5,6},{8,9,5,7},{8,10,5,7},{8,11,5,7},{8,12,5,7},{9,10,5,7},
            {9,11,5,7},{9,12,5,7},{10,11,5,7},{10,12,5,7},{11,12,5,7},{8,9,10,5},
            {8,9,11,5},{8,9,12,5},{8,10,11,5},{8,10,12,5},{8,11,12,5},{9,10,11,5},
            {9,10,12,5},{9,11,12,5},{10,11,12,5},{8,9,6,7},{8,10,6,7},{8,11,6,7},
            {8,12,6,7},{9,10,6,7},{9,11,6,7},{9,12,6,7},{10,11,6,7},{10,12,6,7},
            {11,12,6,7},{8,9,10,6},{8,9,11,6},{8,9,12,6},{8,10,11,6},{8,10,12,6},
            {8,11,12,6},{9,10,11,6},{9,10,12,6},{9,11,12,6},{10,11,12,6},{8,9,10,7},
            {8,9,11,7},{8,9,12,7},{8,10,11,7},{8,10,12,7},{9,10,12,7},{9,11,12,7},
            {10,11,12,7},{8,9,10,11},{8,9,11,12},{8,10,11,12},{9,10,11,12},{1,2,3,4,5},
            {1,2,3,4,6},{1,2,3,4,9},{1,2,3,4,10},{1,2,3,4,11},{1,2,3,4,12},{1,2,3,5,6},
            {1,2,3,5,8},{1,2,3,5,10},{1,2,3,5,11},{1,2,3,5,12},{1,2,3,6,8},{1,2,3,6,9},
            {1,2,3,6,11},{1,2,3,6,12},{1,2,3,8,9},{1,2,3,8,10},{1,2,3,8,11},
            {1,2,3,8,12},{1,2,3,9,10},{1,2,3,9,11},{1,2,3,9,12},{1,2,3,10,11},
            {1,2,3,10,12},{1,2,3,11,12},{1,2,4,5,6},{1,2,4,5,7},{1,2,4,5,10},
            {1,2,4,5,11},{1,2,4,5,12},{1,2,4,6,7},{1,2,4,6,9},{1,2,4,6,11},
            {1,2,4,6,12},{1,2,4,7,9},{1,2,4,7,10},{1,2,4,7,11},{1,2,4,7,12},
            {1,2,4,9,10},{1,2,4,9,11},{1,2,4,9,12},{1,2,4,10,11},{1,2,4,10,12},
            {1,2,4,11,12},{1,2,5,6,7},{1,2,5,6,8},{1,2,5,6,11},{1,2,5,6,12},{1,2,5,7,8},
            {1,2,5,7,10},{1,2,5,7,11},{1,2,5,7,12},{1,2,5,8,10},{1,2,5,8,11},
            {1,2,5,8,12},{1,2,5,10,11},{1,2,5,10,12},{1,2,5,11,12},{1,2,6,7,8},
            {1,2,6,7,9},{1,2,6,7,11},{1,2,6,7,12},{1,2,6,8,9},{1,2,6,8,11},
            {1,2,6,8,12},{1,2,6,9,11},{1,2,6,9,12},{1,2,6,11,12},{1,2,7,8,9},
            {1,2,7,8,10},{1,2,7,8,11},{1,2,7,8,12},{1,2,7,9,10},{1,2,7,9,11},
            {1,2,7,9,12},{1,2,7,10,11},{1,2,7,10,12},{1,2,7,11,12},{1,2,8,9,10},
            {1,2,8,9,11},{1,2,8,9,12},{1,2,8,10,11},{1,2,8,10,12},{1,2,8,11,12},
            {1,2,9,10,11},{1,2,9,10,12},{1,2,9,11,12},{1,2,10,11,12},{1,3,4,5,6},
            {1,3,4,5,7},{1,3,4,5,8},{1,3,4,5,10},{1,3,4,5,11},{1,3,4,5,12},
            {1,3,4,6,7},{1,3,4,6,8},{1,3,4,6,9},{1,3,4,6,10},{1,3,4,6,11},
            {1,3,4,6,12},{1,3,4,7,9},{1,3,4,7,10},{1,3,4,7,11},{1,3,4,7,12},
            {1,3,4,8,9},{1,3,4,8,10},{1,3,4,8,11},{1,3,4,8,12},{1,3,4,9,10},
            {1,3,4,9,11},{1,3,4,9,12},{1,3,4,10,11},{1,3,4,10,12},{1,3,5,6,7},
            {1,3,5,6,8},{1,3,5,6,10},{1,3,5,6,12},{1,3,5,7,8},{1,3,5,7,10},
            {1,3,5,7,11},{1,3,5,7,12},{1,3,5,8,10},{1,3,5,8,11},{1,3,5,8,12},
            {1,3,5,10,11},{1,3,5,10,12},{1,3,5,11,12},{1,3,6,7,8},{1,3,6,7,9},
            {1,3,6,7,11},{1,3,6,7,12},{1,3,6,8,9},{1,3,6,8,10},{1,3,6,8,11},
            {1,3,6,8,12},{1,3,6,9,10},{1,3,6,9,12},{1,3,6,10,11},{1,3,6,10,12},
            {1,3,6,11,12},{1,3,7,8,9},{1,3,7,8,10},{1,3,7,8,11},{1,3,7,8,12},
            {1,3,7,9,10},{1,3,7,9,11},{1,3,7,9,12},{1,3,7,10,11},{1,3,7,10,12},
            {1,3,7,11,12},{1,3,8,9,10},{1,3,8,9,11},{1,3,8,9,12},{1,3,8,10,11},
            {1,3,8,10,12},{1,3,8,11,12},{1,3,9,10,11},{1,3,9,10,12},{1,3,9,11,12},
            {1,3,10,11,12},{1,4,5,6,7},{1,4,5,6,8},{1,4,5,6,10},{1,4,5,6,11},
            {1,4,5,7,8},{1,4,5,7,10},{1,4,5,7,11},{1,4,5,7,12},{1,4,5,8,10},
            {1,4,5,8,11},{1,4,5,8,12},{1,4,5,10,11},{1,4,5,10,12},{1,4,5,11,12},
            {1,4,6,7,8},{1,4,6,7,9},{1,4,6,7,10},{1,4,6,7,11},{1,4,6,7,12},
            {1,4,6,8,9},{1,4,6,8,11},{1,4,6,8,12},{1,4,6,9,10},{1,4,6,9,11},
            {1,4,6,10,11},{1,4,6,10,12},{1,4,6,11,12},{1,4,7,8,9},{1,4,7,8,10},
            {1,4,7,8,11},{1,4,7,8,12},{1,4,7,9,10},{1,4,7,9,11},{1,4,7,9,12},
            {1,4,7,10,11},{1,4,7,10,12},{1,4,7,11,12},{1,4,8,9,10},{1,4,8,9,11},
            {1,4,8,9,12},{1,4,8,10,11},{1,4,8,10,12},{1,4,8,11,12},{1,4,9,10,11},
            {1,4,9,10,12},{1,4,9,11,12},{1,4,10,11,12},{1,5,6,7,8},{1,5,6,7,10},
            {1,5,6,7,11},{1,5,6,7,12},{1,5,6,8,10},{1,5,6,8,11},{1,5,6,8,12},
            {1,5,6,10,11},{1,5,6,10,12},{1,5,6,11,12},{1,5,7,8,10},{1,5,7,8,11},
            {1,5,7,8,12},{1,5,7,10,12},{1,5,7,11,12},{1,5,8,10,11},{1,5,8,11,12},
            {1,5,10,11,12},{1,6,7,8,9},{1,6,7,8,10},{1,6,7,8,11},{1,6,7,8,12},
            {1,6,7,9,10},{1,6,7,9,11},{1,6,7,9,12},{1,6,7,10,11},{1,6,7,10,12},
            {1,6,7,11,12},{1,6,8,9,10},{1,6,8,9,11},{1,6,8,9,12},{1,6,8,10,11},
            {1,6,8,10,12},{1,6,8,11,12},{1,6,9,10,11},{1,6,9,10,12},{1,6,9,11,12},
            {1,6,10,11,12},{1,7,8,9,10},{1,7,8,9,11},{1,7,8,9,12},{1,7,8,10,11},
            {1,7,8,10,12},{1,7,9,10,12},{1,7,9,11,12},{1,7,10,11,12},{1,8,9,10,11},
            {1,8,9,11,12},{1,8,10,11,12},{1,9,10,11,12},{2,3,4,5,6},{2,3,4,5,7},
            {2,3,4,5,8},{2,3,4,5,9},{2,3,4,5,10},{2,3,4,5,11},{2,3,4,5,12},
            {2,3,4,6,7},{2,3,4,6,8},{2,3,4,6,9},{2,3,4,6,11},{2,3,4,6,12},
            {2,3,4,7,9},{2,3,4,7,10},{2,3,4,7,11},{2,3,4,7,12},{2,3,4,8,9},
            {2,3,4,8,10},{2,3,4,8,11},{2,3,4,8,12},{2,3,4,9,10},{2,3,4,9,11},
            {2,3,4,9,12},{2,3,4,10,11},{2,3,4,10,12},{2,3,5,6,7},{2,3,5,6,8},
            {2,3,5,6,9},{2,3,5,6,12},{2,3,5,7,8},{2,3,5,7,10},{2,3,5,7,11},
            {2,3,5,7,12},{2,3,5,8,9},{2,3,5,8,10},{2,3,5,8,11},{2,3,5,8,12},
            {2,3,5,9,10},{2,3,5,9,11},{2,3,5,9,12},{2,3,5,10,12},{2,3,5,11,12},
            {2,3,6,7,8},{2,3,6,7,9},{2,3,6,7,11},{2,3,6,7,12},{2,3,6,8,9},
            {2,3,6,8,11},{2,3,6,8,12},{2,3,6,9,11},{2,3,6,9,12},{2,3,6,11,12},
            {2,3,7,8,9},{2,3,7,8,10},{2,3,7,8,11},{2,3,7,8,12},{2,3,7,9,10},
            {2,3,7,9,11},{2,3,7,9,12},{2,3,7,10,11},{2,3,7,10,12},{2,3,7,11,12},
            {2,3,8,9,10},{2,3,8,9,11},{2,3,8,9,12},{2,3,8,10,11},{2,3,8,10,12},
            {2,3,8,11,12},{2,3,9,10,11},{2,3,9,10,12},{2,3,9,11,12},{2,3,10,11,12},
            {2,4,5,6,7},{2,4,5,6,8},{2,4,5,6,9},{2,4,5,6,11},{2,4,5,7,8},{2,4,5,7,9},
            {2,4,5,7,10},{2,4,5,7,11},{2,4,5,7,12},{2,4,5,8,10},{2,4,5,8,11},
            {2,4,5,8,12},{2,4,5,9,10},{2,4,5,9,11},{2,4,5,9,12},{2,4,5,10,11},
            {2,4,5,11,12},{2,4,6,7,8},{2,4,6,7,9},{2,4,6,7,11},{2,4,6,7,12},
            {2,4,6,8,9},{2,4,6,8,11},{2,4,6,8,12},{2,4,6,9,11},{2,4,6,9,12},
            {2,4,6,11,12},{2,4,7,8,9},{2,4,7,8,10},{2,4,7,8,11},{2,4,7,8,12},
            {2,4,7,9,10},{2,4,7,9,11},{2,4,7,9,12},{2,4,7,10,11},{2,4,7,10,12},
            {2,4,7,11,12},{2,4,8,9,10},{2,4,8,9,11},{2,4,8,9,12},{2,4,8,10,11},
            {2,4,8,10,12},{2,4,8,11,12},{2,4,9,10,11},{2,4,9,10,12},{2,4,9,11,12},
            {2,4,10,11,12},{2,5,6,7,8},{2,5,6,7,9},{2,5,6,7,11},{2,5,6,7,12},
            {2,5,6,8,9},{2,5,6,8,11},{2,5,6,8,12},{2,5,6,9,11},{2,5,6,9,12},
            {2,5,6,11,12},{2,5,7,8,9},{2,5,7,8,10},{2,5,7,8,11},{2,5,7,8,12},
            {2,5,7,9,10},{2,5,7,9,11},{2,5,7,9,12},{2,5,7,10,11},{2,5,7,10,12},
            {2,5,7,11,12},{2,5,8,9,10},{2,5,8,9,11},{2,5,8,9,12},{2,5,8,10,11},
            {2,5,8,10,12},{2,5,8,11,12},{2,5,9,10,11},{2,5,9,10,12},{2,5,9,11,12},
            {2,5,10,11,12},{2,6,7,8,9},{2,6,7,8,11},{2,6,7,8,12},{2,6,7,9,12},
            {2,6,7,11,12},{2,6,8,9,11},{2,6,8,11,12},{2,6,9,11,12},{2,7,8,9,10},
            {2,7,8,9,11},{2,7,8,9,12},{2,7,8,10,11},{2,7,8,10,12},{2,7,9,10,12},
            {2,7,9,11,12},{2,7,10,11,12},{2,8,9,10,11},{2,8,9,11,12},{2,8,10,11,12},
            {2,9,10,11,12},{3,4,5,6,7},{3,4,5,6,8},{3,4,5,6,9},{3,4,5,6,10},
            {3,4,5,7,9},{3,4,5,7,10},{3,4,5,7,11},{3,4,5,7,12},{3,4,5,8,9},
            {3,4,5,8,10},{3,4,5,8,11},{3,4,5,8,12},{3,4,5,9,10},{3,4,5,9,11},
            {3,4,5,9,12},{3,4,5,10,11},{3,4,5,10,12},{3,4,6,7,9},{3,4,6,7,10},
            {3,4,6,7,11},{3,4,6,7,12},{3,4,6,8,9},{3,4,6,8,10},{3,4,6,8,11},
            {3,4,6,8,12},{3,4,6,9,10},{3,4,6,9,11},{3,4,6,9,12},{3,4,6,10,11},
            {3,4,6,10,12},{3,4,7,9,10},{3,4,7,9,11},{3,4,7,9,12},{3,4,7,10,11},
            {3,4,7,10,12},{3,4,8,9,10},{3,4,8,9,11},{3,4,8,9,12},{3,4,8,10,11},
            {3,4,8,10,12},{3,4,9,10,11},{3,4,9,10,12},{3,5,6,7,8},{3,5,6,7,9},
            {3,5,6,7,10},{3,5,6,7,12},{3,5,6,8,9},{3,5,6,8,10},{3,5,6,8,12},
            {3,5,6,9,10},{3,5,6,9,12},{3,5,6,10,12},{3,5,7,8,9},{3,5,7,8,10},
            {3,5,7,8,11},{3,5,7,8,12},{3,5,7,9,10},{3,5,7,9,11},{3,5,7,9,12},
            {3,5,7,10,11},{3,5,7,10,12},{3,5,7,11,12},{3,5,8,9,10},{3,5,8,9,11},
            {3,5,8,9,12},{3,5,8,10,11},{3,5,8,10,12},{3,5,8,11,12},{3,5,9,10,11},
            {3,5,9,10,12},{3,5,9,11,12},{3,5,10,11,12},{3,6,7,8,9},{3,6,7,8,10},
            {3,6,7,8,11},{3,6,7,8,12},{3,6,7,9,10},{3,6,7,9,11},{3,6,7,9,12},
            {3,6,7,10,11},{3,6,7,10,12},{3,6,7,11,12},{3,6,8,9,10},{3,6,8,9,11},
            {3,6,8,9,12},{3,6,8,10,11},{3,6,8,10,12},{3,6,8,11,12},{3,6,9,10,11},
            {3,6,9,10,12},{3,6,9,11,12},{3,6,10,11,12},{3,7,8,9,10},{3,7,8,9,11},
            {3,7,8,9,12},{3,7,8,10,11},{3,7,8,10,12},{3,7,9,10,12},{3,7,9,11,12},
            {3,7,10,11,12},{3,8,9,10,11},{3,8,9,11,12},{3,8,10,11,12},{3,9,10,11,12},
            {4,5,6,7,8},{4,5,6,7,9},{4,5,6,7,10},{4,5,6,7,11},{4,5,6,8,9},{4,5,6,8,10},
            {4,5,6,8,11},{4,5,6,9,10},{4,5,6,9,11},{4,5,6,10,11},{4,5,7,8,9},
            {4,5,7,8,10},{4,5,7,8,11},{4,5,7,8,12},{4,5,7,9,10},{4,5,7,9,11},
            {4,5,7,9,12},{4,5,7,10,11},{4,5,7,10,12},{4,5,7,11,12},{4,5,8,9,10},
            {4,5,8,9,11},{4,5,8,9,12},{4,5,8,10,11},{4,5,8,10,12},{4,5,8,11,12},
            {4,5,9,10,11},{4,5,9,10,12},{4,5,9,11,12},{4,5,10,11,12},{4,6,7,8,9},
            {4,6,7,8,10},{4,6,7,8,11},{4,6,7,8,12},{4,6,7,9,10},{4,6,7,9,11},
            {4,6,7,9,12},{4,6,7,10,11},{4,6,7,10,12},{4,6,7,11,12},{4,6,8,9,10},
            {4,6,8,9,11},{4,6,8,9,12},{4,6,8,10,11},{4,6,8,10,12},{4,6,8,11,12},
            {4,6,9,10,11},{4,6,9,10,12},{4,6,9,11,12},{4,6,10,11,12},{4,7,8,9,10},
            {4,7,8,9,11},{4,7,8,9,12},{4,7,8,10,11},{4,7,8,10,12},{4,7,9,10,12},
            {4,7,9,11,12},{4,7,10,11,12},{4,8,9,10,11},{4,8,9,11,12},{4,8,10,11,12},
            {4,9,10,11,12},{5,6,7,8,9},{5,6,7,8,10},{5,6,7,8,11},{5,6,7,8,12},
            {5,6,7,9,10},{5,6,7,9,11},{5,6,7,9,12},{5,6,7,10,11},{5,6,7,10,12},
            {5,6,7,11,12},{5,6,8,9,10},{5,6,8,9,11},{5,6,8,9,12},{5,6,8,10,11},
            {5,6,8,10,12},{5,6,8,11,12},{5,6,9,10,11},{5,6,9,10,12},{5,6,9,11,12},
            {5,6,10,11,12},{5,7,8,9,10},{5,7,8,9,11},{5,7,8,9,12},{5,7,8,10,11},
            {5,7,8,10,12},{5,7,9,10,12},{5,7,9,11,12},{5,7,10,11,12},{5,8,9,10,11},
            {5,8,9,11,12},{5,8,10,11,12},{5,9,10,11,12},{6,7,8,9,10},{6,7,8,9,11},
            {6,7,8,9,12},{6,7,8,10,11},{6,7,8,10,12},{6,7,9,10,12},{6,7,9,11,12},
            {6,7,10,11,12},{6,8,9,10,11},{6,8,9,11,12},{6,8,10,11,12},{6,9,10,11,12},
            {1,2,3,4,5,6},{1,2,3,4,5,10},{1,2,3,4,5,11},{1,2,3,4,5,12},{1,2,3,4,6,9},
            {1,2,3,4,6,11},{1,2,3,4,6,12},{1,2,3,4,9,10},{1,2,3,4,9,11},{1,2,3,4,9,12},
            {1,2,3,4,10,11},{1,2,3,4,10,12},{1,2,3,5,6,8},{1,2,3,5,6,12},{1,2,3,5,8,10},
            {1,2,3,5,8,11},{1,2,3,5,8,12},{1,2,3,5,10,12},{1,2,3,5,11,12},{1,2,3,6,8,9},
            {1,2,3,6,8,11},{1,2,3,6,8,12},{1,2,3,6,9,12},{1,2,3,6,11,12},{1,2,3,8,9,10},
            {1,2,3,8,9,11},{1,2,3,8,9,12},{1,2,3,8,10,11},{1,2,3,8,10,12},{1,2,3,9,10,12},
            {1,2,3,9,11,12},{1,2,3,10,11,12},{1,2,4,5,6,7},{1,2,4,5,6,11},{1,2,4,5,7,10},
            {1,2,4,5,7,11},{1,2,4,5,7,12},{1,2,4,5,10,11},{1,2,4,5,11,12},{1,2,4,6,7,9},
            {1,2,4,6,7,11},{1,2,4,6,7,12},{1,2,4,6,9,11},{1,2,4,6,11,12},{1,2,4,7,9,10},
            {1,2,4,7,9,11},{1,2,4,7,9,12},{1,2,4,7,10,11},{1,2,4,7,10,12},{1,2,4,9,10,11},
            {1,2,4,9,11,12},{1,2,4,10,11,12},{1,2,5,6,7,8},{1,2,5,6,7,12},{1,2,5,6,8,11},
            {1,2,5,6,11,12},{1,2,5,7,8,10},{1,2,5,7,8,11},{1,2,5,7,8,12},{1,2,5,7,10,12},
            {1,2,5,7,11,12},{1,2,5,8,10,11},{1,2,5,8,11,12},{1,2,5,10,11,12},{1,2,6,7,8,9},
            {1,2,6,7,8,11},{1,2,6,7,8,12},{1,2,6,7,9,12},{1,2,6,7,11,12},{1,2,6,8,9,11},
            {1,2,6,8,11,12},{1,2,6,9,11,12},{1,2,7,8,9,10},{1,2,7,8,9,11},{1,2,7,8,9,12},
            {1,2,7,8,10,11},{1,2,7,8,10,12},{1,2,7,9,10,12},{1,2,7,9,11,12},{1,2,7,10,11,12},
            {1,2,8,9,10,11},{1,2,8,9,11,12},{1,2,8,10,11,12},{1,2,9,10,11,12},{1,3,4,5,6,7},
            {1,3,4,5,6,8},{1,3,4,5,6,10},{1,3,4,5,7,10},{1,3,4,5,7,11},{1,3,4,5,7,12},
            {1,3,4,5,8,10},{1,3,4,5,8,11},{1,3,4,5,8,12},{1,3,4,5,10,11},{1,3,4,5,10,12},
            {1,3,4,6,7,9},{1,3,4,6,7,11},{1,3,4,6,7,12},{1,3,4,6,8,9},{1,3,4,6,8,11},
            {1,3,4,6,8,12},{1,3,4,6,9,10},{1,3,4,6,10,11},{1,3,4,6,10,12},{1,3,4,7,9,10},
            {1,3,4,7,9,11},{1,3,4,7,9,12},{1,3,4,7,10,11},{1,3,4,7,10,12},{1,3,4,8,9,10},
            {1,3,4,8,9,11},{1,3,4,8,9,12},{1,3,4,8,10,11},{1,3,4,8,10,12},{1,3,4,9,10,11},
            {1,3,4,9,10,12},{1,3,5,6,7,8},{1,3,5,6,7,12},{1,3,5,6,8,10},{1,3,5,6,8,12},
            {1,3,5,6,10,12},{1,3,5,7,8,10},{1,3,5,7,8,11},{1,3,5,7,8,12},{1,3,5,7,10,12},
            {1,3,5,7,11,12},{1,3,5,8,10,11},{1,3,5,8,11,12},{1,3,5,10,11,12},{1,3,6,7,8,9},
            {1,3,6,7,8,11},{1,3,6,7,8,12},{1,3,6,7,9,12},{1,3,6,7,11,12},{1,3,6,8,9,10},
            {1,3,6,8,9,12},{1,3,6,8,10,11},{1,3,6,8,10,12},{1,3,6,8,11,12},{1,3,6,9,10,12},
            {1,3,6,10,11,12},{1,3,7,8,9,10},{1,3,7,8,9,11},{1,3,7,8,9,12},{1,3,7,8,10,11},
            {1,3,7,8,10,12},{1,3,7,9,10,12},{1,3,7,9,11,12},{1,3,7,10,11,12},{1,3,8,9,10,11},
            {1,3,8,9,11,12},{1,3,8,10,11,12},{1,3,9,10,11,12},{1,4,5,6,7,8},{1,4,5,6,7,10},
            {1,4,5,6,7,11},{1,4,5,6,8,11},{1,4,5,6,10,11},{1,4,5,7,8,10},{1,4,5,7,8,11},
            {1,4,5,7,8,12},{1,4,5,7,10,12},{1,4,5,7,11,12},{1,4,5,8,10,11},{1,4,5,8,11,12},
            {1,4,5,10,11,12},{1,4,6,7,8,9},{1,4,6,7,8,11},{1,4,6,7,8,12},{1,4,6,7,9,10},
            {1,4,6,7,9,11},{1,4,6,7,10,11},{1,4,6,7,10,12},{1,4,6,7,11,12},{1,4,6,8,9,11},
            {1,4,6,8,11,12},{1,4,6,9,10,11},{1,4,6,10,11,12},{1,4,7,8,9,10},{1,4,7,8,9,11},
            {1,4,7,8,9,12},{1,4,7,8,10,11},{1,4,7,8,10,12},{1,4,7,9,10,12},{1,4,7,9,11,12},
            {1,4,7,10,11,12},{1,4,8,9,10,11},{1,4,8,9,11,12},{1,4,8,10,11,12},{1,4,9,10,11,12},
            {1,5,6,7,8,10},{1,5,6,7,8,11},{1,5,6,7,8,12},{1,5,6,7,10,12},{1,5,6,7,11,12},
            {1,5,6,8,10,11},{1,5,6,8,11,12},{1,5,6,10,11,12},{1,6,7,8,9,10},{1,6,7,8,9,11},
            {1,6,7,8,9,12},{1,6,7,8,10,11},{1,6,7,8,10,12},{1,6,7,9,10,12},{1,6,7,9,11,12},
            {1,6,7,10,11,12},{1,6,8,9,10,11},{1,6,8,9,11,12},{1,6,8,10,11,12},{1,6,9,10,11,12},
            {2,3,4,5,6,7},{2,3,4,5,6,8},{2,3,4,5,6,9},{2,3,4,5,7,10},{2,3,4,5,7,11},{2,3,4,5,7,12},
            {2,3,4,5,8,10},{2,3,4,5,8,11},{2,3,4,5,8,12},{2,3,4,5,9,10},{2,3,4,5,9,11},
            {2,3,4,5,9,12},{2,3,4,6,7,9},{2,3,4,6,7,11},{2,3,4,6,7,12},{2,3,4,6,8,9},
            {2,3,4,6,8,11},{2,3,4,6,8,12},{2,3,4,6,9,11},{2,3,4,6,9,12},{2,3,4,7,9,10},
            {2,3,4,7,9,11},{2,3,4,7,9,12},{2,3,4,7,10,11},{2,3,4,7,10,12},{2,3,4,8,9,10},
            {2,3,4,8,9,11},{2,3,4,8,9,12},{2,3,4,8,10,11},{2,3,4,8,10,12},{2,3,4,9,10,11},
            {2,3,4,9,10,12},{2,3,5,6,7,8},{2,3,5,6,7,12},{2,3,5,6,8,9},{2,3,5,6,8,12},
            {2,3,5,6,9,12},{2,3,5,7,8,10},{2,3,5,7,8,11},{2,3,5,7,8,12},{2,3,5,7,10,12},
            {2,3,5,7,11,12},{2,3,5,8,9,10},{2,3,5,8,9,11},{2,3,5,8,9,12},{2,3,5,8,10,12},
            {2,3,5,8,11,12},{2,3,5,9,10,12},{2,3,5,9,11,12},{2,3,6,7,8,9},{2,3,6,7,8,11},
            {2,3,6,7,8,12},{2,3,6,7,9,12},{2,3,6,7,11,12},{2,3,6,8,9,11},{2,3,6,8,11,12},
            {2,3,6,9,11,12},{2,3,7,8,9,10},{2,3,7,8,9,11},{2,3,7,8,9,12},{2,3,7,8,10,11},
            {2,3,7,8,10,12},{2,3,7,9,10,12},{2,3,7,9,11,12},{2,3,7,10,11,12},{2,3,8,9,10,11},
            {2,3,8,9,11,12},{2,3,8,10,11,12},{2,3,9,10,11,12},{2,4,5,6,7,8},{2,4,5,6,7,9},
            {2,4,5,6,7,11},{2,4,5,6,8,11},{2,4,5,6,9,11},{2,4,5,7,8,10},{2,4,5,7,8,11},
            {2,4,5,7,8,12},{2,4,5,7,9,10},{2,4,5,7,9,11},{2,4,5,7,9,12},{2,4,5,7,10,11},
            {2,4,5,7,11,12},{2,4,5,8,10,11},{2,4,5,8,11,12},{2,4,5,9,10,11},{2,4,5,9,11,12},
            {2,4,6,7,8,9},{2,4,6,7,8,11},{2,4,6,7,8,12},{2,4,6,7,9,12},{2,4,6,7,11,12},
            {2,4,6,8,9,11},{2,4,6,8,11,12},{2,4,6,9,11,12},{2,4,7,8,9,10},{2,4,7,8,9,11},
            {2,4,7,8,9,12},{2,4,7,8,10,11},{2,4,7,8,10,12},{2,4,7,9,10,12},{2,4,7,9,11,12},
            {2,4,7,10,11,12},{2,4,8,9,10,11},{2,4,8,9,11,12},{2,4,8,10,11,12},{2,4,9,10,11,12},
            {2,5,6,7,8,9},{2,5,6,7,8,11},{2,5,6,7,8,12},{2,5,6,7,9,12},{2,5,6,7,11,12},
            {2,5,6,8,9,11},{2,5,6,8,11,12},{2,5,6,9,11,12},{2,5,7,8,9,10},{2,5,7,8,9,11},
            {2,5,7,8,9,12},{2,5,7,8,10,11},{2,5,7,8,10,12},{2,5,7,9,10,12},{2,5,7,9,11,12},
            {2,5,7,10,11,12},{2,5,8,9,10,11},{2,5,8,9,11,12},{2,5,8,10,11,12},{2,5,9,10,11,12},
            {3,4,5,6,7,9},{3,4,5,6,7,10},{3,4,5,6,8,9},{3,4,5,6,8,10},{3,4,5,6,9,10},
            {3,4,5,7,9,10},{3,4,5,7,9,11},{3,4,5,7,9,12},{3,4,5,7,10,11},{3,4,5,7,10,12},
            {3,4,5,8,9,10},{3,4,5,8,9,11},{3,4,5,8,9,12},{3,4,5,8,10,11},{3,4,5,8,10,12},
            {3,4,5,9,10,11},{3,4,5,9,10,12},{3,4,6,7,9,10},{3,4,6,7,9,11},{3,4,6,7,9,12},
            {3,4,6,7,10,11},{3,4,6,7,10,12},{3,4,6,8,9,10},{3,4,6,8,9,11},{3,4,6,8,9,12},
            {3,4,6,8,10,11},{3,4,6,8,10,12},{3,4,6,9,10,11},{3,4,6,9,10,12},{3,5,6,7,8,9},
            {3,5,6,7,8,10},{3,5,6,7,9,12},{3,5,6,7,10,12},{3,5,6,8,9,10},{3,5,6,8,9,12},
            {3,5,6,8,10,12},{3,5,6,9,10,12},{3,5,7,8,9,10},{3,5,7,8,9,11},{3,5,7,8,9,12},
            {3,5,7,8,10,11},{3,5,7,8,10,12},{3,5,7,9,10,12},{3,5,7,9,11,12},{3,5,7,10,11,12},
            {3,5,8,9,10,11},{3,5,8,9,11,12},{3,5,8,10,11,12},{3,5,9,10,11,12},{3,6,7,8,9,10},
            {3,6,7,8,9,11},{3,6,7,8,9,12},{3,6,7,8,10,11},{3,6,7,8,10,12},{3,6,7,9,10,12},
            {3,6,7,9,11,12},{3,6,7,10,11,12},{3,6,8,9,10,11},{3,6,8,9,11,12},{3,6,8,10,11,12},
            {3,6,9,10,11,12},{4,5,6,7,8,9},{4,5,6,7,8,10},{4,5,6,7,9,10},{4,5,6,7,9,11},
            {4,5,6,7,10,11},{4,5,6,8,9,11},{4,5,6,8,10,11},{4,5,6,9,10,11},{4,5,7,8,9,10},
            {4,5,7,8,9,11},{4,5,7,8,9,12},{4,5,7,8,10,11},{4,5,7,8,10,12},{4,5,7,9,10,12},
            {4,5,7,9,11,12},{4,5,7,10,11,12},{4,5,8,9,10,11},{4,5,8,9,11,12},{4,5,8,10,11,12},
            {4,5,9,10,11,12},{4,6,7,8,9,10},{4,6,7,8,9,11},{4,6,7,8,9,12},{4,6,7,8,10,11},
            {4,6,7,8,10,12},{4,6,7,9,10,12},{4,6,7,9,11,12},{4,6,7,10,11,12},{4,6,8,9,10,11},
            {4,6,8,9,11,12},{4,6,8,10,11,12},{4,6,9,10,11,12},{5,6,7,8,9,10},{5,6,7,8,9,11},
            {5,6,7,8,9,12},{5,6,7,8,10,11},{5,6,7,8,10,12},{5,6,7,9,10,12},{5,6,7,9,11,12},
            {5,6,7,10,11,12},{5,6,8,9,10,11},{5,6,8,9,11,12},{5,6,8,10,11,12},{5,6,9,10,11,12}
        ]
    
    @property
    def bases(self) -> list[set[int]]:
        return [
            {1,2,3,4,5,6},{1,2,3,4,5,10},{1,2,3,4,5,11},{1,2,3,4,5,12},{1,2,3,4,6,9},
            {1,2,3,4,6,11},{1,2,3,4,6,12},{1,2,3,4,9,10},{1,2,3,4,9,11},{1,2,3,4,9,12},
            {1,2,3,4,10,11},{1,2,3,4,10,12},{1,2,3,5,6,8},{1,2,3,5,6,12},{1,2,3,5,8,10},
            {1,2,3,5,8,11},{1,2,3,5,8,12},{1,2,3,5,10,12},{1,2,3,5,11,12},{1,2,3,6,8,9},
            {1,2,3,6,8,11},{1,2,3,6,8,12},{1,2,3,6,9,12},{1,2,3,6,11,12},{1,2,3,8,9,10},
            {1,2,3,8,9,11},{1,2,3,8,9,12},{1,2,3,8,10,11},{1,2,3,8,10,12},{1,2,3,9,10,12},
            {1,2,3,9,11,12},{1,2,3,10,11,12},{1,2,4,5,6,7},{1,2,4,5,6,11},{1,2,4,5,7,10},
            {1,2,4,5,7,11},{1,2,4,5,7,12},{1,2,4,5,10,11},{1,2,4,5,11,12},{1,2,4,6,7,9},
            {1,2,4,6,7,11},{1,2,4,6,7,12},{1,2,4,6,9,11},{1,2,4,6,11,12},{1,2,4,7,9,10},
            {1,2,4,7,9,11},{1,2,4,7,9,12},{1,2,4,7,10,11},{1,2,4,7,10,12},{1,2,4,9,10,11},
            {1,2,4,9,11,12},{1,2,4,10,11,12},{1,2,5,6,7,8},{1,2,5,6,7,12},{1,2,5,6,8,11},
            {1,2,5,6,11,12},{1,2,5,7,8,10},{1,2,5,7,8,11},{1,2,5,7,8,12},{1,2,5,7,10,12},
            {1,2,5,7,11,12},{1,2,5,8,10,11},{1,2,5,8,11,12},{1,2,5,10,11,12},{1,2,6,7,8,9},
            {1,2,6,7,8,11},{1,2,6,7,8,12},{1,2,6,7,9,12},{1,2,6,7,11,12},{1,2,6,8,9,11},
            {1,2,6,8,11,12},{1,2,6,9,11,12},{1,2,7,8,9,10},{1,2,7,8,9,11},{1,2,7,8,9,12},
            {1,2,7,8,10,11},{1,2,7,8,10,12},{1,2,7,9,10,12},{1,2,7,9,11,12},{1,2,7,10,11,12},
            {1,2,8,9,10,11},{1,2,8,9,11,12},{1,2,8,10,11,12},{1,2,9,10,11,12},{1,3,4,5,6,7},
            {1,3,4,5,6,8},{1,3,4,5,6,10},{1,3,4,5,7,10},{1,3,4,5,7,11},{1,3,4,5,7,12},
            {1,3,4,5,8,10},{1,3,4,5,8,11},{1,3,4,5,8,12},{1,3,4,5,10,11},{1,3,4,5,10,12},
            {1,3,4,6,7,9},{1,3,4,6,7,11},{1,3,4,6,7,12},{1,3,4,6,8,9},{1,3,4,6,8,11},
            {1,3,4,6,8,12},{1,3,4,6,9,10},{1,3,4,6,10,11},{1,3,4,6,10,12},{1,3,4,7,9,10},
            {1,3,4,7,9,11},{1,3,4,7,9,12},{1,3,4,7,10,11},{1,3,4,7,10,12},{1,3,4,8,9,10},
            {1,3,4,8,9,11},{1,3,4,8,9,12},{1,3,4,8,10,11},{1,3,4,8,10,12},{1,3,4,9,10,11},
            {1,3,4,9,10,12},{1,3,5,6,7,8},{1,3,5,6,7,12},{1,3,5,6,8,10},{1,3,5,6,8,12},
            {1,3,5,6,10,12},{1,3,5,7,8,10},{1,3,5,7,8,11},{1,3,5,7,8,12},{1,3,5,7,10,12},
            {1,3,5,7,11,12},{1,3,5,8,10,11},{1,3,5,8,11,12},{1,3,5,10,11,12},{1,3,6,7,8,9},
            {1,3,6,7,8,11},{1,3,6,7,8,12},{1,3,6,7,9,12},{1,3,6,7,11,12},{1,3,6,8,9,10},
            {1,3,6,8,9,12},{1,3,6,8,10,11},{1,3,6,8,10,12},{1,3,6,8,11,12},{1,3,6,9,10,12},
            {1,3,6,10,11,12},{1,3,7,8,9,10},{1,3,7,8,9,11},{1,3,7,8,9,12},{1,3,7,8,10,11},
            {1,3,7,8,10,12},{1,3,7,9,10,12},{1,3,7,9,11,12},{1,3,7,10,11,12},{1,3,8,9,10,11},
            {1,3,8,9,11,12},{1,3,8,10,11,12},{1,3,9,10,11,12},{1,4,5,6,7,8},{1,4,5,6,7,10},
            {1,4,5,6,7,11},{1,4,5,6,8,11},{1,4,5,6,10,11},{1,4,5,7,8,10},{1,4,5,7,8,11},
            {1,4,5,7,8,12},{1,4,5,7,10,12},{1,4,5,7,11,12},{1,4,5,8,10,11},{1,4,5,8,11,12},
            {1,4,5,10,11,12},{1,4,6,7,8,9},{1,4,6,7,8,11},{1,4,6,7,8,12},{1,4,6,7,9,10},
            {1,4,6,7,9,11},{1,4,6,7,10,11},{1,4,6,7,10,12},{1,4,6,7,11,12},{1,4,6,8,9,11},
            {1,4,6,8,11,12},{1,4,6,9,10,11},{1,4,6,10,11,12},{1,4,7,8,9,10},{1,4,7,8,9,11},
            {1,4,7,8,9,12},{1,4,7,8,10,11},{1,4,7,8,10,12},{1,4,7,9,10,12},{1,4,7,9,11,12},
            {1,4,7,10,11,12},{1,4,8,9,10,11},{1,4,8,9,11,12},{1,4,8,10,11,12},{1,4,9,10,11,12},
            {1,5,6,7,8,10},{1,5,6,7,8,11},{1,5,6,7,8,12},{1,5,6,7,10,12},{1,5,6,7,11,12},
            {1,5,6,8,10,11},{1,5,6,8,11,12},{1,5,6,10,11,12},{1,6,7,8,9,10},{1,6,7,8,9,11},
            {1,6,7,8,9,12},{1,6,7,8,10,11},{1,6,7,8,10,12},{1,6,7,9,10,12},{1,6,7,9,11,12},
            {1,6,7,10,11,12},{1,6,8,9,10,11},{1,6,8,9,11,12},{1,6,8,10,11,12},{1,6,9,10,11,12},
            {2,3,4,5,6,7},{2,3,4,5,6,8},{2,3,4,5,6,9},{2,3,4,5,7,10},{2,3,4,5,7,11},{2,3,4,5,7,12},
            {2,3,4,5,8,10},{2,3,4,5,8,11},{2,3,4,5,8,12},{2,3,4,5,9,10},{2,3,4,5,9,11},{2,3,4,5,9,12},
            {2,3,4,6,7,9},{2,3,4,6,7,11},{2,3,4,6,7,12},{2,3,4,6,8,9},{2,3,4,6,8,11},{2,3,4,6,8,12},
            {2,3,4,6,9,11},{2,3,4,6,9,12},{2,3,4,7,9,10},{2,3,4,7,9,11},{2,3,4,7,9,12},{2,3,4,7,10,11},
            {2,3,4,7,10,12},{2,3,4,8,9,10},{2,3,4,8,9,11},{2,3,4,8,9,12},{2,3,4,8,10,11},
            {2,3,4,8,10,12},{2,3,4,9,10,11},{2,3,4,9,10,12},{2,3,5,6,7,8},{2,3,5,6,7,12},
            {2,3,5,6,8,9},{2,3,5,6,8,12},{2,3,5,6,9,12},{2,3,5,7,8,10},{2,3,5,7,8,11},
            {2,3,5,7,8,12},{2,3,5,7,10,12},{2,3,5,7,11,12},{2,3,5,8,9,10},{2,3,5,8,9,11},
            {2,3,5,8,9,12},{2,3,5,8,10,12},{2,3,5,8,11,12},{2,3,5,9,10,12},{2,3,5,9,11,12},
            {2,3,6,7,8,9},{2,3,6,7,8,11},{2,3,6,7,8,12},{2,3,6,7,9,12},{2,3,6,7,11,12},
            {2,3,6,8,9,11},{2,3,6,8,11,12},{2,3,6,9,11,12},{2,3,7,8,9,10},{2,3,7,8,9,11},
            {2,3,7,8,9,12},{2,3,7,8,10,11},{2,3,7,8,10,12},{2,3,7,9,10,12},{2,3,7,9,11,12},
            {2,3,7,10,11,12},{2,3,8,9,10,11},{2,3,8,9,11,12},{2,3,8,10,11,12},{2,3,9,10,11,12},
            {2,4,5,6,7,8},{2,4,5,6,7,9},{2,4,5,6,7,11},{2,4,5,6,8,11},{2,4,5,6,9,11},{2,4,5,7,8,10},
            {2,4,5,7,8,11},{2,4,5,7,8,12},{2,4,5,7,9,10},{2,4,5,7,9,11},{2,4,5,7,9,12},
            {2,4,5,7,10,11},{2,4,5,7,11,12},{2,4,5,8,10,11},{2,4,5,8,11,12},{2,4,5,9,10,11},
            {2,4,5,9,11,12},{2,4,6,7,8,9},{2,4,6,7,8,11},{2,4,6,7,8,12},{2,4,6,7,9,12},
            {2,4,6,7,11,12},{2,4,6,8,9,11},{2,4,6,8,11,12},{2,4,6,9,11,12},{2,4,7,8,9,10},
            {2,4,7,8,9,11},{2,4,7,8,9,12},{2,4,7,8,10,11},{2,4,7,8,10,12},{2,4,7,9,10,12},
            {2,4,7,9,11,12},{2,4,7,10,11,12},{2,4,8,9,10,11},{2,4,8,9,11,12},{2,4,8,10,11,12},
            {2,4,9,10,11,12},{2,5,6,7,8,9},{2,5,6,7,8,11},{2,5,6,7,8,12},{2,5,6,7,9,12},
            {2,5,6,7,11,12},{2,5,6,8,9,11},{2,5,6,8,11,12},{2,5,6,9,11,12},{2,5,7,8,9,10},
            {2,5,7,8,9,11},{2,5,7,8,9,12},{2,5,7,8,10,11},{2,5,7,8,10,12},{2,5,7,9,10,12},
            {2,5,7,9,11,12},{2,5,7,10,11,12},{2,5,8,9,10,11},{2,5,8,9,11,12},{2,5,8,10,11,12},
            {2,5,9,10,11,12},{3,4,5,6,7,9},{3,4,5,6,7,10},{3,4,5,6,8,9},{3,4,5,6,8,10},{3,4,5,6,9,10},
            {3,4,5,7,9,10},{3,4,5,7,9,11},{3,4,5,7,9,12},{3,4,5,7,10,11},{3,4,5,7,10,12},
            {3,4,5,8,9,10},{3,4,5,8,9,11},{3,4,5,8,9,12},{3,4,5,8,10,11},{3,4,5,8,10,12},
            {3,4,5,9,10,11},{3,4,5,9,10,12},{3,4,6,7,9,10},{3,4,6,7,9,11},{3,4,6,7,9,12},
            {3,4,6,7,10,11},{3,4,6,7,10,12},{3,4,6,8,9,10},{3,4,6,8,9,11},{3,4,6,8,9,12},
            {3,4,6,8,10,11},{3,4,6,8,10,12},{3,4,6,9,10,11},{3,4,6,9,10,12},{3,5,6,7,8,9},
            {3,5,6,7,8,10},{3,5,6,7,9,12},{3,5,6,7,10,12},{3,5,6,8,9,10},{3,5,6,8,9,12},
            {3,5,6,8,10,12},{3,5,6,9,10,12},{3,5,7,8,9,10},{3,5,7,8,9,11},{3,5,7,8,9,12},
            {3,5,7,8,10,11},{3,5,7,8,10,12},{3,5,7,9,10,12},{3,5,7,9,11,12},{3,5,7,10,11,12},
            {3,5,8,9,10,11},{3,5,8,9,11,12},{3,5,8,10,11,12},{3,5,9,10,11,12},{3,6,7,8,9,10},
            {3,6,7,8,9,11},{3,6,7,8,9,12},{3,6,7,8,10,11},{3,6,7,8,10,12},{3,6,7,9,10,12},
            {3,6,7,9,11,12},{3,6,7,10,11,12},{3,6,8,9,10,11},{3,6,8,9,11,12},{3,6,8,10,11,12},
            {3,6,9,10,11,12},{4,5,6,7,8,9},{4,5,6,7,8,10},{4,5,6,7,9,10},{4,5,6,7,9,11},
            {4,5,6,7,10,11},{4,5,6,8,9,11},{4,5,6,8,10,11},{4,5,6,9,10,11},{4,5,7,8,9,10},
            {4,5,7,8,9,11},{4,5,7,8,9,12},{4,5,7,8,10,11},{4,5,7,8,10,12},{4,5,7,9,10,12},
            {4,5,7,9,11,12},{4,5,7,10,11,12},{4,5,8,9,10,11},{4,5,8,9,11,12},{4,5,8,10,11,12},
            {4,5,9,10,11,12},{4,6,7,8,9,10},{4,6,7,8,9,11},{4,6,7,8,9,12},{4,6,7,8,10,11},
            {4,6,7,8,10,12},{4,6,7,9,10,12},{4,6,7,9,11,12},{4,6,7,10,11,12},{4,6,8,9,10,11},
            {4,6,8,9,11,12},{4,6,8,10,11,12},{4,6,9,10,11,12},{5,6,7,8,9,10},{5,6,7,8,9,11},
            {5,6,7,8,9,12},{5,6,7,8,10,11},{5,6,7,8,10,12},{5,6,7,9,10,12},{5,6,7,9,11,12},
            {5,6,7,10,11,12},{5,6,8,9,10,11},{5,6,8,9,11,12},{5,6,8,10,11,12},{5,6,9,10,11,12}
        ]

    @property
    def circuits(self) -> list[set[int]]:
        return [
            {1,5,9},{2,10,6},{1,2,3,7},{8,1,2,4},{8,3,4,7},{11,3,4,12},{11,3,5,6},{12,4,5,6},
            {8,11,12,7},{9,10,11,7},{8,9,10,12},{1,3,6,7,10},{1,3,6,9,11},{1,4,6,8,10},{1,4,6,9,12},
            {1,5,7,10,11},{1,5,8,10,12},{2,3,5,7,9},{2,3,5,10,11},{2,4,5,8,9},{2,4,5,10,12},
            {2,6,7,9,11},{2,6,8,9,12},{1,2,3,8,11,12},{1,2,3,9,10,11},{1,2,4,7,11,12},
            {1,2,4,9,10,12},{1,2,5,6,7,11},{1,2,5,6,8,12},{3,4,7,9,10,12},{3,4,8,9,10,11},
            {3,5,6,7,8,12},{3,5,6,7,9,10},{4,5,6,7,8,11},{4,5,6,8,9,10},{1,3,4,5,7,10,12},
            {1,3,4,5,8,10,11},{1,3,6,7,8,9,12},{1,3,6,8,10,11,12},{1,4,6,7,8,9,11},
            {1,4,6,7,10,11,12},{2,3,4,6,7,9,12},{2,3,4,6,8,9,11},{2,3,5,7,8,10,12},
            {2,3,5,8,9,11,12},{2,4,5,7,8,10,11},{2,4,5,7,9,11,12}
        ]
    
    @property
    def hyperplanes(self) -> list[set[int]]:
        return [
            {1,3,6,8,12},{1,3,8,10,11},{1,4,6,7,11},{1,4,7,10,12},{2,3,5,8,12},{2,3,8,9,11},
            {2,4,5,7,11},{2,4,7,9,12},{3,5,7,10,12},{3,6,7,9,12},{4,5,8,10,11},{4,6,8,9,11},
            {1,2,5,9,11,12},{1,2,6,10,11,12},{1,3,4,5,9,10},{1,3,4,10,11,12},{1,5,6,7,8,9},
            {1,6,7,8,11,12},{2,3,4,6,9,10},{2,3,4,9,11,12},{2,5,6,7,8,10},{2,5,7,8,11,12},
            {3,4,5,7,8,10},{3,4,6,7,8,9},{1,2,3,5,7,9,12},{1,2,3,6,7,10,12},{1,2,4,5,8,9,11},
            {1,2,4,6,8,10,11},{1,3,5,6,8,9,11},{1,3,5,8,9,10,12},{1,4,5,6,7,9,12},
            {1,4,5,7,9,10,11},{2,3,5,6,8,10,11},{2,3,6,8,9,10,12},{2,4,5,6,7,10,12},
            {2,4,6,7,9,10,11},{1,2,3,4,5,7,8,9},{1,2,3,4,6,7,8,10},{1,2,3,4,7,8,11,12},
            {1,3,4,5,6,9,11,12},{1,5,7,8,9,10,11,12},{2,3,4,5,6,10,11,12},{2,6,7,8,9,10,11,12},
            {3,4,5,6,7,8,11,12},{3,4,7,8,9,10,11,12},{1,2,3,5,6,7,9,10,11},{1,2,4,5,6,8,9,10,12}
        ]
    
    @property
    def cocircuits(self) -> list[set[int]]:
        return [
            {11,3,7},{8,4,12},{1,2,5,6},{1,2,10,9},{1,3,4,5},{8,1,9,7},{2,3,4,6},{8,2,10,7},
            {9,10,5,6},{9,11,12,5},{10,11,12,6},{1,3,5,8,12},{1,3,8,9,11},{1,4,5,7,11},
            {1,4,7,9,12},{2,3,6,8,12},{2,3,8,10,11},{2,4,6,7,11},{2,4,7,10,12},{3,5,7,9,12},
            {3,6,7,10,12},{4,5,8,9,11},{4,6,8,10,11},{1,2,5,10,11,12},{1,2,6,9,11,12},
            {1,3,4,6,9,10},{1,3,4,9,11,12},{1,5,6,7,8,10},{1,5,7,8,11,12},{2,3,4,5,9,10},
            {2,3,4,10,11,12},{2,5,6,7,8,9},{2,6,7,8,11,12},{3,4,5,7,8,9},{3,4,6,7,8,10},
            {1,2,3,5,7,10,12},{1,2,3,6,7,9,12},{1,2,4,5,8,10,11},{1,2,4,6,8,9,11},
            {1,3,5,6,8,10,11},{1,3,6,8,9,10,12},{1,4,5,6,7,10,12},{1,4,6,7,9,10,11},
            {2,3,5,6,8,9,11},{2,3,5,8,9,10,12},{2,4,5,6,7,9,12},{2,4,5,7,9,10,11}
        ]
    
    def is_binary(self) -> bool:
        return True

    def is_ternary(self) -> bool:
        return True