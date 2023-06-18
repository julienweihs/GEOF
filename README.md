## GFI course structure
%%with current responsible


``` mermaid
flowchart
    
    %%Kj>Kjersti] -.- GEOF105
    %%Kj -.- GEOF232
    
    %%He>Helge] -.- GEOF110
    %%He -.- GEOF346

    %%LaHe>Lars Henrik] -.- GEOF100
    
    %%HaCh>Hans Christian] -.- GEOF105
    
    %%As>Asgeir] -.- GEOF100
    
    %%Th>Thomas]
    
    %%Le>Lea]
    
    %%Ca>Camille]
    
    %%Il>Ilker] -.- GEOF310
    
    %%Jo>Joachim] -.- GEOF310

    PROG{Programming}

    GEOF100 --> GEOF105
    
    GEOF105 --> GEOF210 & GEOF212 & GEOF236 & GEOF220 & GEOF232 & GEOF346

    GEOF110 --> GEOF212 & GEOF213 & GEOF211 & GEOF346 & GEOF339 & GEOF352
    
    GEOF210 --> GEOF232

    GEOF211 --> GEOF321

    GEOF212 --> GEOF348

    GEOF213 --> GEOF339 & GEOF352

    GEOF220 --> GEOF311 & GEOF321 & GEOF322

    GEOF232 --> GEOF322 & GEOF337

    GEOF236 --> GEOF336

    GEOF310 --> GEOF321 & GEOF322 & GEOF337 & GEOF338

    GEOF311 --> GEOF321 & GEOF322

    GEOF339 --> GEOF348

    GEOF346 --> GEOF337

    GEOF352 --> GEOF348

    INF100([INF100]) ---> PROG



    %% MAT111 --> GEOF100 & MAT112 & MAT121 & GEOF105 & MAT131 & GEOF220
    %% MAT112 --> MAT212 & GEOF105 & GEOF110 & MAT131
    %% MAT121 --> GEOF105 & MAT131 & GEOF210
    %% MAT131 --> GEOF105 & GEOF110
    %% MAT212 --> GEOF110 & GEOF213

    %%%%%%%%
    %% MAT111 --> PHYS111 & STAT110
    %% PHYS111 --> GEOF105 & PHYS113 & GEOF110 & GEOF220
    %% STAT110 --> GEOF210
    %%%%%%%%

%% subgraph GEOF courses
    direction TB

    subgraph 1st semester
        MAT111id([MAT111])
        INF100
        GEOF100
    end

    subgraph 2nd semester
        direction TB
        MAT112([MAT112])
        MAT121([MAT121])
        PHYS111([PHYS111])
    end
    
    subgraph 3rd semester
        MAT212([MAT212])
        GEOF105
        PHYS113([PHYS113]) --- |or| STAT110([STAT110]) --- |or| KJEM110([KJEM110]) 
        KJEM110 --- |or| PHYS113
    end
    
    subgraph 4th semester
        GEOF110
        MAT131([MAT131])
        EX([EXPHIL-MNSEM])
    end
    
    subgraph 5th semester
        GEOF210
        GEOF212
        GEOF213 --- |or| GEOF236
    end
    
    subgraph 6th semester
        GEOF220
        GEOF211
        GEOF232
    end

    subgraph Master
    GEOF310
    GEOF311
    GEOF321
    GEOF322
    GEOF336
    GEOF337
    GEOF338
    GEOF339
    GEOF346
    GEOF347
    GEOF348
    GEOF351
    GEOF352
    end

    PROG ==> GEOF211 & GEOF212 & GEOF210 & GEOF110 & GEOF105 & GEOF321 & GEOF346 & GEOF348 & GEOF352

%% end
```
