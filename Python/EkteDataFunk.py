import numpy as np
import requests
import io
import matplotlib.pyplot as plt

def loadData(file,rydd='Y'):
    
    '''
    # NO
    Denne funksjonen skal
    - Lese inn et datasett fra github mappen til Ekte Data.
    - Returnere en tidsvektor og en matrise med selve verdiene.

    Input 
    file     : Navnet på .txt-filen (ikke inkluder stien her, kun filnavnet)
    rydd : 'Y' (yes, default) hvis jeg vil at datasettet skal være noenlunde
    ferdig ryddet ved innlasting. 'N' (no, eller hva som helst annet enn 'Y') 
    hvis dette er en del av oppgaven.
    
    Output
    data      : En vektor eller matrise (avhengig av om datasettet som leses inn
    er årlig eller månedlige gjennomsnitt) med alle verdiene i datasettet
    tid     : Tidsvektoren til datasettet.
    
    data : Hvis rydd != 'Y' returneres hele datasettet som en matrise.

    
    # EN
    This function shall
     - Import a data set from the github folder to Ekte Data.
     - Return a time vector and a matrix with the values themselves.

     Input
     file : The name of the .txt file (don't include the path here, just the filename)
     clear : 'Y' (yes, default) if I want the data set to be more or less
     fully cleared when loading. 'N' (no, or anything other than 'Y') if this is
     part of the assignment.
    
     Output
     data : A vector or array (depending on whether the data set being read in
     are annual or monthly averages) with all the values in the data set
     time : The time vector of the dataset.
    
     data : If clear != 'Y' the entire dataset is returned as an array.

    (Vår Dundas 2021)
    '''
    

    # Simply using genfromtxt doesn't work due to caching issues. We need to 
    # read the data from url to a file and THEN give this string to genfromtxt.
    #url = 'https://raw.githubusercontent.com/irendundas/EkteData/main/'+file
    url = 'https://raw.githubusercontent.com/irendundas/EkteData/main/data/'+file
    
    req = requests.get(url)
    f = io.StringIO(req.text)

    f.seek(0) # set cursor to the top
    data=np.genfromtxt(f,dtype=float)
    
    #=================================
    # NO
    # Last inn dataene med np.genfromtxt som vi har brukt før
    # Prøv først å laste det inn uten å opggi info om delimeter og skip_header
    # EN
    # Load the data with np.genfromtxt which we have used before
    # First try to load it without providing info about delimeter and skip_header

    # NO
    # Sjekk om dette funket eller om alt ble NaN.  Dersom alt ble NaN laster vi
    # inn datasettet på nytt og inkluderer info om delimeter og skip_header
    # EN
    # Check if this worked or if everything became NaN. If everything turned out to
    # be NaN, we reload the data set and include info about delimeter and skip_header
    if len(data) == len(np.nonzero(data)[0]):
        f.seek(0) # set cursor to the top
        data = np.genfromtxt(f, dtype=float, delimiter=',',skip_header=1)
    
    # NO
    # Default er 'Y' - stort sett vil jeg ha ferdig ryddede data, men for  
    # eksempelet RyddDatasett er dette en del av oppgaven.
    # EN
    # Default is 'Y' - mostly I want completely cleaned data, but for the example
    # CleanDataset, this is part of the task.
    if rydd=='Y':
        # NO
        # Sett eventuelle "fyll-verdier" til NaN
        # EN
        # Set eventual "fill-values" to NaN (Not a Number)
        data[data==-999.99]=np.nan     
    
        # NO
        # Tidsvektor med desimaler
        # EN
        # Time-vector with decimals
        tid=data[:,0]
    
        # NO
        # Selve dataene
        # EN
        # The data itself
        data=data[:,1:]
        return data, tid
    else:
        return data


# Eksempel/Example 1:
#data=loadData('TempBergenYearlyNonan.txt',rydd='N')
#plt.plot(data[:,0],data[:,1])
#plt.show()
    
# Eksempel/Example 2:
#temp,tid=loadData('TempBergenYearlyNonan.txt')
#plt.plot(tid,temp)
#plt.show()