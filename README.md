## GFI course structure with current responsible


``` mermaid
flowchart TB
    
    MAT111 --> MAT112
    MAT111 --> MAT121
    MAT111 --> PHYS111
    MAT112 --> MAT212
    MAT111 --> GEOF105
    GEOF100 --> GEOF105
    MAT112 --> GEOF105
    MAT121 --> GEOF105
    MAT131 --> GEOF105
    PHYS111 --> GEOF105
    INF100 --> GEOF105
    PHYS111 --> PHYS113
    MAT111 --> STAT110

    subgraph 1st semester
    MAT111
    INF100
    MAT111 --> GEOF100
    end
    
    subgraph 2nd semester
    MAT112
    MAT121
    PHYS111
    end
    
    subgraph 3rd semester
    MAT212
    GEOF105
    PHYS113-- or ---STAT110
    KJEM110
    end
    
    subgraph 4th semester
    GEOF110
    MAT131
    EXPHIL-MNSEM
    end
    
    subgraph 5th semester
    GEOF210
    GEOF212
    GEOF213
    GOEF236
    end
    
    subgraph 6th semester
    GEOF220
    GEOF211
    GEOF232
    end
```