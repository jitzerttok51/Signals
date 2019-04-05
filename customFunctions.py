import numpy as np

def gausualSignal(time, discretiNaPeriod, koefZapulvane=0.5, ampUp=1, ampDown=0):
    signal = np.zeros(time.size)
    fi=0
    for i in range(0, time.size):
        if(i%discretiNaPeriod<=discretiNaPeriod*koefZapulvane):
            signal[i]=ampUp*np.sin(np.pi*fi/(discretiNaPeriod*koefZapulvane))
            fi = fi + 1
        else:
            fi=0
            signal[i]=ampDown
    return signal
	
def squareSignal(time, discretiNaPeriod, koefZapulvane=0.5, ampUp=1, ampDown=0):
    signal = np.zeros(time.size)
    for i in range(0, time.size):
        if(i%discretiNaPeriod<=discretiNaPeriod*koefZapulvane):
            signal[i]=ampUp
        else:
            signal[i]=ampDown
    return sign

def sineSignal(time, discretiNaPeriod, amp=1):
    signal = np.zeros(time.size)
    for i in range(0, time.size):
        signal[i]=amp*np.sin(2*np.pi*(i%discretiNaPeriod)/(discretiNaPeriod-1))
    return signal

def getSinglePeriod(time, signal, discretiNaPeriod):
    return (time[:discretiNaPeriod], signal[:discretiNaPeriod])

