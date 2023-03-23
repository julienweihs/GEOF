## GFI course structure with current responsible


``` mermaid
flowchart TB
    
    Kj>Kjersti] -.- GEOF105
    Kj -.- GEOF232
    
    He>Helge] -.- GEOF346
    He -.- GEOF110

    LaHe>Lars Henrik] -.- GEOF100
    
    HaCh>Hans Christian] -.- GEOF105
    
    As>Asgeir] -.- GEOF100
    
    Th>Thomas]
    
    Le>Lea]
    
    Ca>Camille]
    
    Il>Ilker]

    PROG{Programming}

    MAT111 --> MAT112
    MAT111 --> MAT121
    MAT111 --> PHYS111
    MAT112 --> MAT212
    MAT111 ---> GEOF105
    GEOF100 --> GEOF105
    MAT112 --> GEOF105
    MAT121 --> GEOF105
    MAT131 --> GEOF105
    PHYS111 --> GEOF105
    INF100 ---> GEOF105
    PHYS111 --> PHYS113
    MAT111 --> STAT110
    MAT112 --> GEOF110
    MAT131 --> GEOF110
    MAT212 --> GEOF110
    PHYS111 --> GEOF110
    MAT111 --> MAT131
    MAT112 --> MAT131
    MAT121 --> MAT131
    GEOF105 --> GEOF210
    STAT110 --> GEOF210
    MAT121 --> GEOF210
    GEOF105 --> GEOF212
    GEOF110 --> GEOF212
    GEOF110 --> GEOF213
    MAT212 --> GEOF213
    GEOF105 --> GEOF236
    MAT111 --> GEOF220
    PHYS111 --> GEOF220
    GEOF105 --> GEOF220
    GEOF110 --> GEOF211
    GEOF105 --> GEOF232
    GEOF210 --> GEOF232


    PROG --> GEOF211 & GEOF212
    PROG --> GEOF212

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
    PHYS113-- or ---STAT110-- or ---KJEM110 
    KJEM110-- or ---PHYS113
    end
    
    subgraph 4th semester
    GEOF110
    MAT131
    EXPHIL-MNSEM
    end
    
    subgraph 5th semester
    GEOF210
    GEOF212
    GEOF213-- or ---GEOF236
    end
    
    subgraph 6th semester
    GEOF220
    GEOF211
    GEOF232
    end

    subgraph Master
    GEOF346
    end
```