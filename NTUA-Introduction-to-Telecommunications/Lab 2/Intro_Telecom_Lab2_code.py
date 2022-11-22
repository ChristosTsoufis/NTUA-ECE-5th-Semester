from scipy.special import erfc
import numpy as np
import matplotlib.pyplot as plt
import binascii
from scipy.io import wavfile

#Ερώτημα 1ο
#Παραγωγή τυχαίας ακολουθίας
rng = np.random.default_rng()
num_seq = rng.choice(2, 36, replace=True, p=[0.5, 0.5])
Tb = 0.2 #Διάρκεια Ψηφίου
#Δημιουργία διαγράμματος απεικόνισης της ακολουθίας ψηφίων
'''
προσθετουμε στο num_seq ένα ακόμα στοιχείο (ίσο με το τελευταίο bit) γιατί η step με where='post'
απαιτεί στην περίπτωση μας ένα παραπάνω στοιχείο για να λειτουργήσει με τον επιθυμητό τρόπο
'''
num_seq = np.append(num_seq,num_seq[35])
t = np.linspace(0, 36*Tb, 37)
plt.step(t,num_seq, where='post')
plt.grid()
plt.xticks(np.arange(0,37*Tb, Tb))
plt.yticks([0,1])
plt.xlabel("Time [s]")
plt.ylabel("Bit")
plt.title("Random Bit Stream")
plt.show()

#Ερώτημα 1α
A=5 #κοινό και για τους δύο φοιτητές
#Το B-PAM ισοδυναμεί με NRZ-POLAR
bpam_stream=[]
for i in range(36):
    if (num_seq[i]==1):
        bpam_stream.append(A)
    else:
        bpam_stream.append(-A)
#Δημιουργία διαγράμματος απεικόνισης της ακολουθίας ψηφίων κατά B-PAM πλάτους Α
'''
προσθετουμε στο bpam_stream ένα ακόμα στοιχείο (ίσο με το τελευταίο) γιατί η step με where='post'
απαιτεί στην περίπτωση μας ένα παραπάνω στοιχείο για να λειτουργήσει με τον επιθυμητό τρόπο
'''
bpam_stream = np.append(bpam_stream,bpam_stream[35])
t = np.linspace(0, 36*Tb, 37)
plt.step(t,bpam_stream, where='post')
plt.grid()
plt.xticks(np.arange(0,37*Tb, Tb))
plt.yticks([-A,A])
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("B-PAM Modulated Signal")
plt.show()

#Ερώτημα 1β
#Το διάγραμμα αστερισμού αναπαριστά το σήμα διαμορφωμένο κατά BPAM
#Επειδή το σήμα είναι δυαδικό θα έχουμε δύο σημεία αστερισμού στον άξονα x με διαφορά π
#To δυαδικό 1 αντιστοιχεί σε φάση 0 και το δυαδικό 0 σε φάση π
bit_1 = complex(A,np.sin(0))
bit_0 = complex(-A,np.sin(np.pi))
real = [bit_1.real, bit_0.real]
img = [bit_1.imag, bit_0.imag]
plt.scatter(real, img)
plt.title('Constellation Diagram of B-PAM Modulated Signal')
plt.xlabel('In-phase Amplitude(I)')
plt.ylabel('Quadrature Amplitude(Q)')
plt.xticks(np.arange(-A,A+1))
plt.yticks(np.arange(-A,A+1))
plt.axvline(c='grey', lw=1)
plt.axhline(c='grey', lw=1)
plt.annotate('1', xy=(-A, 0),  xytext=(A + 0.05, -0.25))
plt.annotate('0', xy=(A, 0), xytext=(-A + 0.05, -0.25))
plt.show()

#Επαναφέρω το διαμορφωμένο σήμα στην αρχική του κατάσταση αφερόντας το τελευταίο στοιχείο που πρόσθεσα για να λειτουργεί το plt.step κατάλληλα
bpam_stream = np.delete(bpam_stream,36)

#Ερώτημα 1γ
#Δημιουργία AWGN για 6dB
No = A*A*Tb/(10**0.6)
noise_1 = np.random.normal(0, np.sqrt(No/2), 36) + 1j*np.random.normal(0, np.sqrt(No/2), 36)
signal_1 = noise_1 + bpam_stream
#Όπως και στο ερώτημα 1β προσθέτω ένα στοιχείο για να λειτουργεί κατάλληλα η plt.step
signal_1 = np.append(signal_1, signal_1[35])

#Δημιουργία διαγράμματος για το πραγματικό μέρος του θορύβου
t = np.linspace(0, 36*Tb, 37)
plt.step(t,np.real(signal_1), where='post')
plt.grid()
plt.xticks(np.arange(0,37*Tb, Tb))
plt.yticks([-A,A])
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("B-PAM modulated signal + AWGN of 6dB SNR/bit")
plt.show()

#Δημιουργία AWGN για 12dB
No = A*A*Tb/(10**1.2)
noise_2 = np.random.normal(0, np.sqrt(No/2), 36) + 1j*np.random.normal(0, np.sqrt(No/2), 36)
signal_2 = noise_2 + bpam_stream
#Όπως και στο ερώτημα 1β προσθέτω ένα στοιχείο για να λειτουργεί κατάλληλα η plt.step
signal_2 = np.append(signal_2, signal_2[35])

#Δημιουργία διαγράμματος για το πραγματικό μέρος του θορύβου
t = np.linspace(0, 36*Tb, 37)
plt.step(t,np.real(signal_2), where='post')
plt.grid()
plt.xticks(np.arange(0,37*Tb, Tb))
plt.yticks([-A,A])
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("B-PAM modulated signal + AWGN of 12dB SNR/bit")
plt.show()

#Επαναφορά των σημάτων με θόρυβων στην αρχική κατάσταση για τον ίδιο λόγο του ερωτήματος 1β
signal_1 = np.delete(signal_1, 36)
signal_2 = np.delete(signal_2,36)

#Ερώτημα 1δ
#Για τα ζητούμενα διαγράμματα αστερισμού θα απεικονίσουμε τα signal_1, signal_2 σε scatter plot
plt.scatter(np.real(signal_1), np.imag(signal_1), s=10, label='Modulated Signal + AWGN')
plt.scatter(real, img, c='red', s=12, label='Modulated Signal')
plt.xticks(np.arange(-A-1,A+2))
plt.yticks(np.arange(-A-1,A+2))
plt.axvline(c='grey', lw=1)
plt.axhline(c='grey', lw=1)
plt.annotate('1', xy=(-A, 0),  xytext=(A + 0.05, -0.25))
plt.annotate('0', xy=(A, 0), xytext=(-A + 0.05, -0.25))
plt.title('Constellation Diagram of B-PAM Modulated Signal + AWGN of 6dB SNR/bit')
plt.xlabel('In-phase Amplitude(I)')
plt.ylabel('Quadrature Amplitude(Q)')
plt.legend()
plt.show()

plt.scatter(np.real(signal_2), np.imag(signal_2), s=10, label='Modulated Signal + AWGN')
plt.scatter(real, img, c='red', s=12, label='Modulated Signal')
plt.xticks(np.arange(-A-1,A+2))
plt.yticks(np.arange(-A-1,A+2))
plt.axvline(c='grey', lw=1)
plt.axhline(c='grey', lw=1)
plt.annotate('1', xy=(-A, 0),  xytext=(A + 0.05, -0.25))
plt.annotate('0', xy=(A, 0), xytext=(-A + 0.05, -0.25))
plt.title('Constellation Diagram of B-PAM Modulated Signal + AWGN of 12dB SNR/bit')
plt.xlabel('In-phase Amplitude(I)')
plt.ylabel('Quadrature Amplitude(Q)')
plt.legend()
plt.show()

#Ερώτημα 1ε
BER = []
s = 100000
#Δημιουργία Random Ακολουθίας s δειγμάτων
rng = np.random.default_rng()
num_seq_e = rng.choice(2, s, replace=True, p=[0.5, 0.5])
#B-PAM Διαμόρφωση
bpam_stream_e = []
for i in range(s):
    if (num_seq_e[i]==1):
        bpam_stream_e.append(A)
    else:
        bpam_stream_e.append(-A)
    
for i in range(16):
    #Δημιουργία AWGN
    No =   A**2 / 10**(i / 10)
    noise_e = np.random.normal(0, np.sqrt(No/2), s) + 1j*np.random.normal(0, np.sqrt(No/2), s)

    signal = noise_e + bpam_stream_e
    '''
    Το διαμορφωμένο σήμα + AWGN θα σταλεί σε αποκωδικοποιητή. Τα αποτελέσματα που θα προκύψουν από τον αποκωδικοποοιητη
    θα τα συγκρίνουμε με το signal και θα βρούμε σε πόσα bit έχουμε διαφορά
    '''
    #Δημιουργία αποκωδικοποιημένου σήματος
    decoded_signal = []
    for j in range(s):
        if (signal[j].real>0):
            decoded_signal.append(1)
        else:
            decoded_signal.append(0)
    
    #Σύγκριση ακολουθίας bit και αποκωδικοποιημένου σήματος και υπολογισμος errors
    errors = np.sum(num_seq_e ^ decoded_signal)       
    
    #Υπολογισμός του BER για i dB
    BER.append(errors*1.0/s)

#Υπολογισμός θεωρητικού BER
x = np.linspace(0,15, 16)
BER_th = 0.5*erfc(np.sqrt(10**(x/10)))

#Σχεδιασμός του γραφήματος
plt.scatter(x,BER, c='r', label='Experimental Results')
plt.plot(x, BER_th, label='Theoretical Curve')
plt.yscale('log')
plt.xlabel("Eb/No (dB)")
plt.ylabel("BER")
plt.title("Bit Error Diagram")
plt.legend()
plt.show()

#Ερώτημα 2ο
fc=3
#Ερώτημα 2α
#Διαμόρφωση BPSK
bpsk_stream = []
bpsk_symbol_seq = []
for i in range(36):
    t = np.linspace(i*Tb, (i+1)*Tb, 100) #Επιλέγω 100 δείγματα ανά bit
    if (num_seq[i]==1):
        bpsk_stream.append(A*np.cos(2*np.pi*fc*t))
        bpsk_symbol_seq.append('1')
    else:
        bpsk_stream.append(-A*np.cos(2*np.pi*fc*t))
        bpsk_symbol_seq.append('0')

#Προκύπτουσα Ακολουθία BPSK
print("BPSK Symbol Sequence: ",bpsk_symbol_seq, sep=" ")

#Διαμόρφωση QPSK
qpsk_stream = []
qpsk_symbol_seq = []
for i in range(0,36,2):
    t = np.linspace(i*Tb, (i+2)*Tb, 200) #Επιλέγω 100 δείγματα ανά bit
    #00
    if (num_seq[i]==0 and num_seq[i+1]==0):
        qpsk_stream.append(A*np.cos(2*np.pi*fc*t))
        qpsk_symbol_seq.append('00')
    #01
    elif (num_seq[i]==0 and num_seq[i+1]==1):
        qpsk_stream.append(A*np.cos(2*np.pi*fc*t-np.pi/2))
        qpsk_symbol_seq.append('01')
    #11
    elif (num_seq[i]==1 and num_seq[i+1]==1):
        qpsk_stream.append(A*np.cos(2*np.pi*fc*t-np.pi))
        qpsk_symbol_seq.append('11')
    #10
    else:
        qpsk_stream.append(A*np.cos(2*np.pi*fc*t-3*np.pi/2))
        qpsk_symbol_seq.append('10')

#Προκύπτουσα Ακολουθία QPSK
print("QPSK Symbol Sequence: ",qpsk_symbol_seq, sep=" ")

#Διαμόρφωση 8-PSK
psk_8_stream = []
psk_8_symbol_seq = []
for i in range (0,36,3):
    t = np.linspace(i*Tb, (i+3)*Tb, 300) ##Επιλέγω 100 δείγματα ανά bit
    #000
    if (num_seq[i]==0 and num_seq[i+1]==0 and num_seq[i+2]==0):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t))
        psk_8_symbol_seq.append('000')
    #001
    elif (num_seq[i]==0 and num_seq[i+1]==0 and num_seq[i+2]==1):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t-np.pi/4))
        psk_8_symbol_seq.append('001')
    #011
    elif (num_seq[i]==0 and num_seq[i+1]==1 and num_seq[i+2]==1):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t-np.pi/2))
        psk_8_symbol_seq.append('011')
    #010
    elif (num_seq[i]==0 and num_seq[i+1]==1 and num_seq[i+2]==0):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t-3*np.pi/4))
        psk_8_symbol_seq.append('010')
    #110
    elif (num_seq[i]==1 and num_seq[i+1]==1 and num_seq[i+2]==0):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t-np.pi))
        psk_8_symbol_seq.append('110')
    #111
    elif (num_seq[i]==1 and num_seq[i+1]==1 and num_seq[i+2]==1):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t-5*np.pi/4))
        psk_8_symbol_seq.append('111')
    #101
    elif (num_seq[i]==1 and num_seq[i+1]==0 and num_seq[i+2]==1):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t-3*np.pi/2))
        psk_8_symbol_seq.append('101')
    #100
    elif (num_seq[i]==1 and num_seq[i+1]==0 and num_seq[i+2]==0):
        psk_8_stream.append(A*np.cos(2*np.pi*fc*t-7*np.pi/4))
        psk_8_symbol_seq.append('100')

#Προκύπτουσα Ακολουθία 8-PSK
print("8-PSK Symbol Sequence: ", psk_8_symbol_seq, sep=" ")

#Ερώτημα 2β
#Κυματομορφή μετάδοσης για BPSK
#Ένωση των στοιχείων του πίνακα bpsk_stream σε ένα ενιαίο πίνακα
bpsk_plotted_signal = []
for i in range(36):
    bpsk_plotted_signal.extend(bpsk_stream[i])

#Δημιουργία Διαγράμματος
t = np.linspace(0, 36*Tb, 3600) #100*36=3600 δείγματα
plt.plot(t, bpsk_plotted_signal)
plt.grid()
plt.xticks(np.arange(0,37*Tb, Tb))
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("B-PSK Modulated signal with fc=3Hz and Ts=0.2s")
plt.show()

#Κυματομορφή μετάδοσης για QPSK
#Ένωση των στοιχείων του πίνακα qpsk_stream σε ένα ενιαίο πίνακα
qpsk_plotted_signal = []
for i in range(18):
    qpsk_plotted_signal.extend(qpsk_stream[i])

#Δημιουργία Διαγράμματος
t = np.linspace(0, 36*Tb, 3600) #200*18=3600 δείγματα
plt.plot(t, qpsk_plotted_signal)
plt.grid()
plt.xticks(np.arange(0,37*Tb, 2*Tb))
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Q-PSK Modulated signal with fc=3Hz and Ts=0.4s")
plt.show()

#Κυματομορφή μετάδοσης για 8-PSK
#Ένωση των στοιχείων του πίνακα psk_8_stream σε ένα ενιαίο πίνακα
psk_8_plotted_signal = []
for i in range(12):
    psk_8_plotted_signal.extend(psk_8_stream[i])

#Δημιουργία Διαγράμματος
t = np.linspace(0, 36*Tb, 3600) #300*12=3600 δείγματα
plt.plot(t, psk_8_plotted_signal)
plt.grid()
plt.xticks(np.arange(0,37*Tb, 3*Tb))
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("8-PSK Modulated signal with fc=3Hz and Ts=0.6s")
plt.show()

#Ερώτημα 3ο
#Ερώτημα 3α
#Διαμόρφωση QPSK
qpsk_stream = []
constellation_points = []
constellation_points_1 = [] 
constellation_points_2 = [] 
flag = True #Σημαία αλλαγής timeslot (True=1st timeslot)(False=2nd timeslot)
for i in range(0,36,2):
    t = np.linspace(i*Tb, (i+2)*Tb, 200) #Επιλέγω 100 δείγματα ανά bit
    #00
    if (num_seq[i]==0 and num_seq[i+1]==0):
        constellation_points.append(complex(A,np.sin(0)))
        if(flag==True):
            constellation_points_1.append(complex(A,np.sin(0)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t))
        else:
            constellation_points_2.append(complex(A*np.cos(np.pi/4),A*np.sin(np.pi / 4)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t-np.pi/4))
        flag = not flag
    #01
    elif (num_seq[i]==0 and num_seq[i+1]==1):
        constellation_points.append(complex(0,A*np.sin(np.pi/2)))
        if(flag==True):
            constellation_points_1.append(complex(0,A*np.sin(np.pi/2)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t-np.pi/2))
        else:
            constellation_points_2.append(complex(A*np.cos(3*np.pi/4),A*np.sin(3*np.pi / 4)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t-3*np.pi/4))
        flag = not flag
    #11
    elif (num_seq[i]==1 and num_seq[i+1]==1):
        constellation_points.append(complex(-A,np.sin(np.pi)))
        if(flag==True):
            constellation_points_1.append(complex(-A,np.sin(np.pi)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t-np.pi))
        else:
            constellation_points_2.append(complex(A*np.cos(5*np.pi/4),A*np.sin(5*np.pi / 4)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t-5*np.pi/4))
        flag = not flag
    #10
    else:
        constellation_points.append(complex(0,A*np.sin(3*np.pi/2)))
        if(flag==True):
            constellation_points_1.append(complex(0,A*np.sin(3*np.pi/2)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t-3*np.pi/2))
        else:
            constellation_points_2.append(complex(A*np.cos(7*np.pi/4),A*np.sin(7*np.pi / 4)))
            qpsk_stream.append(A*np.cos(2*np.pi*fc*t-7*np.pi/4))
        flag = not flag

#Κυματομορφή μετάδοσης για QPSK
#Ένωση των στοιχείων του πίνακα qpsk_stream σε ένα ενιαίο πίνακα
qpsk_plotted_signal = []
for i in range(18):
    qpsk_plotted_signal.extend(qpsk_stream[i])

#Δημιουργία Διαγράμματος Σήματος π/4-QPSK
t = np.linspace(0, 36*Tb, 3600) #200*18=3600 δείγματα
plt.plot(t, qpsk_plotted_signal)
plt.grid()
plt.xticks(np.arange(0,37*Tb, 2*Tb))
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("QPSK Modulated signal with fc=3Hz and Ts=0.4s")
plt.tight_layout()
plt.show()

#Δημιουργια διαγραμματος αστερισμού
plt.scatter(np.real(constellation_points_1), np.imag(constellation_points_1), c='blue')
plt.scatter(np.real(constellation_points_2), np.imag(constellation_points_2), c='green')
def const_points():
    for i in range (9):
        if(np.real(constellation_points_1[i])==A):
            plt.annotate('00', xy=(A, 0),  xytext=(A + 0.05, -0.25))

        if(np.real(constellation_points_2[i])==A*np.cos(np.pi/4)):
            plt.annotate('00', xy=(A*np.cos(np.pi/4), A*np.sin(np.pi/4)),  xytext=(A*np.cos(np.pi/4) + 0.05, A*np.sin(np.pi/4)-0.25))

        if(np.imag(constellation_points_1[i])==A):
            plt.annotate('01', xy=(0, A),  xytext=( 0.05, A-0.25))

        if(np.real(constellation_points_2[i])==A*np.cos(3*np.pi/4)):
            plt.annotate('01', xy=(A*np.cos(3*np.pi/4), A*np.sin(3*np.pi/4)),  xytext=(A*np.cos(3*np.pi/4) + 0.05, A*np.sin(3*np.pi/4)-0.25))

        if(np.real(constellation_points_1[i])==-A):
            plt.annotate('11', xy=(-A, 0), xytext=(-A + 0.05, -0.25))

        if(np.real(constellation_points_2[i])==A*np.cos(5*np.pi/4)):
            plt.annotate('11', xy=(A*np.cos(5*np.pi/4), A*np.sin(5*np.pi/4)),  xytext=(A*np.cos(5*np.pi/4) + 0.05, A*np.sin(5*np.pi/4)-0.25))

        if(np.imag(constellation_points_1[i])==-A):
            plt.annotate('10', xy=(0, -A),  xytext=(0.05, -A-0.25))

        if (np.real(constellation_points_2[i])==A*np.cos(7*np.pi/4)):
            plt.annotate('10', xy=(A*np.cos(7*np.pi/4), A*np.sin(7*np.pi/4)),  xytext=(A*np.cos(7*np.pi/4) + 0.05, A*np.sin(7*np.pi/4)-0.25))

const_points()
plt.xticks(np.arange(-A,A+1))
plt.yticks(np.arange(-A,A+1))
plt.axvline(c='grey', lw=1)
plt.axhline(c='grey', lw=1)
plt.title('Constellation Diagram of π/4-QPSK Modulated Signal')
plt.xlabel('In-phase Amplitude(I)')
plt.ylabel('Quadrature Amplitude(Q)')
plt.show()

#Ερώτημα 3β
#Για 6dB
No = A*A*Tb/(10**0.6)
noise_1 = np.random.normal(0, np.sqrt(No/2), 18) + 1j*np.random.normal(0, np.sqrt(No/2), 18)
signal_1 = noise_1 + constellation_points

#Για 12dB
No = A*A*Tb/(10**1.2)
noise_2 = np.random.normal(0, np.sqrt(No/2), 18) + 1j*np.random.normal(0, np.sqrt(No/2), 18)
signal_2 = noise_2 + constellation_points

#Για τα ζητούμενα διαγράμματα αστερισμού θα απεικονίσουμε τα signal_1, signal_2 σε scatter plot
plt.scatter(np.real(signal_1), np.imag(signal_1), s=10, label='Modulated Signal + AWGN')
plt.scatter(np.real(constellation_points_1), np.imag(constellation_points_1), c='blue')
plt.xticks(np.arange(-A-1,A+2))
plt.yticks(np.arange(-A-1,A+2))
plt.axvline(c='grey', lw=1)
plt.axhline(c='grey', lw=1)
plt.annotate('00', xy=(A, 0),  xytext=(A + 0.05, -0.25))
plt.annotate('01', xy=(0, A),  xytext=( 0.05, A-0.25))
plt.annotate('11', xy=(-A, 0), xytext=(-A + 0.05, -0.25))
plt.annotate('10', xy=(0, -A),  xytext=(0.05, -A-0.25))
plt.title('Constellation Diagram of Q-PSK Modulated Signal + AWGN of 6dB SNR/bit')
plt.xlabel('In-phase Amplitude(I)')
plt.ylabel('Quadrature Amplitude(Q)')
plt.legend()
plt.show()

plt.scatter(np.real(signal_2), np.imag(signal_2), s=10, label='Modulated Signal + AWGN')
plt.scatter(np.real(constellation_points_1), np.imag(constellation_points_1), c='blue')
plt.xticks(np.arange(-A-1,A+2))
plt.yticks(np.arange(-A-1,A+2))
plt.axvline(c='grey', lw=1)
plt.axhline(c='grey', lw=1)
plt.annotate('00', xy=(A, 0),  xytext=(A + 0.05, -0.25))
plt.annotate('01', xy=(0, A),  xytext=( 0.05, A-0.25))
plt.annotate('11', xy=(-A, 0), xytext=(-A + 0.05, -0.25))
plt.annotate('10', xy=(0, -A),  xytext=(0.05, -A-0.25))
plt.title('Constellation Diagram of Q-PSK Modulated Signal + AWGN of 12dB SNR/bit')
plt.xlabel('In-phase Amplitude(I)')
plt.ylabel('Quadrature Amplitude(Q)')
plt.legend()
plt.show()

#Ερώτημα 3γ
#Παραγωγή τυχαίας ακολουθίας
s=10000
rng = np.random.default_rng()
num_seq_e = rng.choice(2, s, replace=True, p=[0.5, 0.5])
BER = []
#Διαμόρφωση QPSK
constellation_points = []

for i in range(0,s,2):
    t = np.linspace(i*Tb, (i+2)*Tb, 200) #Επιλέγω 100 δείγματα ανά bit
    #00
    if (num_seq_e[i]==0 and num_seq_e[i+1]==0):
        constellation_points.append(complex(A,np.sin(0)))
        
    #01
    elif (num_seq_e[i]==0 and num_seq_e[i+1]==1):
        constellation_points.append(complex(0,A*np.sin(np.pi/2)))
        
    #11
    elif (num_seq_e[i]==1 and num_seq_e[i+1]==1):
        constellation_points.append(complex(-A,np.sin(np.pi)))
        
    #10
    else:
        constellation_points.append(complex(0,A*np.sin(3*np.pi/2)))

for i in range(16):
    #Δημιουργία AWGN
    No =   A**2 / 10**(i / 10)
    noise_e = np.random.normal(0, np.sqrt(No/2), s//2) + 1j*np.random.normal(0, np.sqrt(No/2), s//2)

    signal = noise_e + constellation_points
    '''
    Το διαμορφωμένο σήμα + AWGN θα σταλεί σε αποκωδικοποιητή. Τα αποτελέσματα που θα προκύψουν από τον αποκωδικοποοιητη
    θα τα συγκρίνουμε με το signal και θα βρούμε σε πόσα bit έχουμε διαφορά
    '''
    #Δημιουργία αποκωδικοποιημένου σήματος
    decoded_signal = []
    const_points= [complex(A,0),complex(0,A), complex(-A,0), complex(0,-A)]
    for j in range(s//2):
        #Υπολογισμός μικρότερης απόστασης
        for i in range(4):
            d=np.sqrt((np.real(const_points[i])-np.real(signal[j]))**2 + (np.imag(const_points[i])-np.imag(signal[j]))**2)
            if (i==0):
                dmin=d
                guard=0
            if (d<dmin):
                dmin=d
                guard=i
        if (guard==0):
            decoded_signal.append(0)
            decoded_signal.append(0)
        elif (guard==1):
            decoded_signal.append(0)
            decoded_signal.append(1)
        elif (guard==2):
            decoded_signal.append(1)
            decoded_signal.append(1)
        elif (guard==3):
            decoded_signal.append(1)
            decoded_signal.append(0)
    
    #Σύγκριση ακολουθίας bit και αποκωδικοποιημένου σήματος και υπολογισμος errors
    errors = np.sum(num_seq_e ^ decoded_signal)       
    #Υπολογισμός του BER για i dB
    BER.append(errors*1.0/s)

#Υπολογισμός θεωρητικού BER
x = np.linspace(0,15, 16)
BER_th = 0.5*erfc(np.sqrt(10**(x/10)/2))

#Σχεδιασμός του γραφήματος
plt.scatter(x,BER, c='r', label='Experimental Results')
plt.plot(x, BER_th, label='Theoretical Curve')
plt.yscale('log')
plt.xlabel("Eb/No (dB)")
plt.ylabel("BER")
plt.title("Bit Error Diagram")
plt.legend()
plt.show()

#Ερώτημα 3δ
#Ερώτημα i
f = open('clarke_relays_odd.txt')
file_content = f.read()
def split(word): 
    return [char for char in word]
binary_data = split(file_content)
#Μετατροπή σε binary
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
binary_data = text_to_bits(file_content)
bit_array = []
for i in range(len(binary_data)):
    if(binary_data[i]=='0'):
        bit_array.append(0)
    else:
        bit_array.append(1)

#Ερώτημα ii
#Δημιουργία 8-bit string που αποθηκευέονται στον bit_string
bit_string = []
for i in range(0,len(bit_array),8):
    bit_8_package=bit_array[i]
    for j in range(1,8):
        bit_8_package= str(bit_array[j+i])+str(bit_8_package)
    bit_string.append(bit_8_package)

#Ολοι οι συνδυασμοι 8bit σε binary  με την σειρα στον πινακα bin_8_all
bin_8_all = []
for i in range(256):
    string_8_bit = bin(i)
    string_8_bit = string_8_bit[2:]
    while(len(string_8_bit)<8):
        string_8_bit = str(0) + string_8_bit
    bin_8_all.append(string_8_bit)

#Quantizer creation
signal = []
Q=1/255.5
for i in range(len(bit_string)):
	for j in range(len(bin_8_all)):
		if (bit_string[i] == bin_8_all[j]):
			signal.append(Q*(j+1/2)) #οι σταθμες που θελουμε ειναι πολλαπλασια του Q/2

signal.append(signal[599])
t=np.linspace(0,4800*Tb, 601)
plt.step(t,signal, where='post')
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Quantized signal")
plt.show()

#Ερώτημα 4
#Το πρόγραμμα διαβάζει το WAV αρχείο
frequency, signal = wavfile.read("soundfile1_lab2.wav")

duration = 1.0*len(signal)/frequency  #βρίσκουμε την ακριβή διάρκεια του wav file
t = np.linspace (0, duration, len(signal))  #διαμερίζουμε τον χρόνο κατάλληλα

#Ερώτημα α
#γραφική απεικόνιση σήματος
plt.plot (t, signal, label='The Signal')
plt.grid()
plt.xlabel("Time (Sec)")
plt.ylabel("Amplitude")
plt.title("PCM 16-Bit Mono 44100 Hz")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

#Ερώτημα β
#το σήμα περνάει από κβάντιση και κανονικοποιείται στην ίδια εντολή 
quantizedsignal = (signal / 256) + 128

#το κβαντισμένο σήμα
plt.plot(t, quantizedsignal, label='The Signal')
plt.grid()
plt.xlabel("Time (Sec)")
plt.ylabel("Amplitude")
plt.title("The Signal after passing through an 8-bit Quantizer")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()