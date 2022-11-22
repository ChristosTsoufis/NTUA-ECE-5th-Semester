from scipy import signal 
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from sympy.combinatorics.graycode import GrayCode
from scipy.signal import butter, lfilter, freqz

#Ορισμός χρήσιμων τιμών
fm=5*1000 
fs1=25*fm
fs2=60*fm
fs=5*fm

#Άσκηση 1
#Α Μέρος
#Ερώτημα (i)
t1=np.linspace(0, 4/fm, 4/fm*fs1) #Από 0 μέχρι 4*T=4*(1/fm) παίρνουμε δείγματα N*T=fs1*4*(1/fm)
triangle1=2*signal.sawtooth(2*np.pi*fm/2*t1, 0.5) #τριγωνικός παλμός (duty cycle=0.5) με συχνότητα fm/2 και πλάτος 2V
sq_triangle1=triangle1*triangle1 #προκύπτει σήμα πλάτους 4V και συχνότητας fm
plt.scatter(t1, sq_triangle1, s=4, color='blue', marker=',') #χρήση scatter για εμφάνιση μεμονομένων σημείων
plt.xlabel("Time [s]") #τίτλος x άξονα
plt.ylabel("Amplitude [V]") #τίτλος y άξονα
plt.title("sq_triangle(t), fs1 = 125 kHz") #τίτλος γραφήματος
plt.xlim(-0.00001, 4/fm+0.00001) #οριοθέτηση για εμφάνιση 4 περιόδων
plt.show()

#Ερώτημα (ii)
t2=np.linspace(0, 4/fm, 4/fm*fs2)
triangle2=2*signal.sawtooth(2*np.pi*fm/2*t2, 0.5)
sq_triangle2=triangle2*triangle2
plt.scatter(t2, sq_triangle2, s=4, color='red', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("sq_triangle(t), fs2 = 300 kHz")
plt.xlim(-0.00001, 4/fm+0.00001)
plt.show()

#Ερώτημα (iii)
plt.scatter(t1, sq_triangle1, s=15, color='blue', marker='*', label='fs1 = 125kHz')
plt.scatter(t2, sq_triangle2, s=15, color='red', marker='X', label='fs2 = 300kHz')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("sq_triangle(t), fs1 & fs2")
plt.legend(loc="upper right") #δημιουργία υπομνήματος
plt.xlim(-0.00001, 4/fm+0.00001)
plt.show()

#B Μέρος
t=np.linspace(0, 4/fm, 4/fm*fs)
triangle=2*signal.sawtooth(2*np.pi*fm/2*t, 0.5)
sq_triangle=triangle*triangle
plt.scatter(t, sq_triangle, s=4, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("sq_triangle(t), fs = 25 kHz")
plt.xlim(-0.00001, 4/fm+0.00001)
plt.show()

#Fourier Transform στην sq_triangle(t) 
#Χρησιμοποιούμε την sq_triangle(t) με δειγματοληψία fs2 για να εχουμε περισσότερα δείγματα
#και άρα μεγαλύτερη ακρίβεια στην επιλογή της ελάχιστης fs
sq_trianglef2=fft(sq_triangle2)
tf2=np.linspace(0, fs2/2, 4/fm*fs2/2)
#fs2/2 γιατί θέλουμε διάγραμμα από το 0 μέχρι το B (Bandwidth)
# και αντίστοιχα αριθμός_δειγμάτων/2 γιατί για τον ίδιο λόγο θέλουμε τα μισά
plt.plot(tf2,np.abs(sq_trianglef2[0:int(4/fm*fs2/2)]))  #
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [V]")
plt.title("Frequency Spectrum of sampled signal (fs2)")
plt.xlim(-1000, 100001)
plt.show()

#Παρατηρούμε ότι για πάνω από 60kHz το φάσμα είναι περίπου μηδέν
#Για πλήρη(μερική) ανακατασκευή του σήματος πρέπει fs=2*60kHz=120kHz
fs0= 120*1000
t0=np.linspace(0, 4/fm, 4/fm*fs0)
triangle0=2*signal.sawtooth(2*np.pi*fm/2*t0, 0.5)
sq_triangle0=triangle0*triangle0
plt.plot(t0, sq_triangle0, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("sq_triangle(t), fs = 120 kHz")
plt.show()

#Γ Μέρος
#Ερώτημα (i)
#Δειγματοληψία του z(t) με fs1 
t1=np.linspace(0, 4/fm, 4/fm*fs1)
sine1=np.sin(2*np.pi*fm*t1)
plt.scatter(t1, sine1, s=4, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("z(t), fs1 = 125 kHz")
plt.xlim(-0.00001, 4/fm+0.00001)
plt.show()

#Δειγματοληψία του z(t) με fs2
t2=np.linspace(0, 4/fm, 4/fm*fs2)
sine2=np.sin(2*np.pi*fm*t2)
plt.scatter(t2, sine2, s=4, color='red', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("z(t), fs2 = 300 kHz")
plt.xlim(-0.00001, 4/fm+0.00001)
plt.show()

#Κοινό διάγραμμα 
plt.scatter(t1, sine1, s=15, color='blue', marker='*', label='fs1 = 125kHz')
plt.scatter(t2, sine2, s=15, color='red', marker='X', label='fs2 = 300kHz')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("z(t), fs1 & fs2")
plt.legend(loc="upper right")
plt.xlim(-0.00001, 4/fm+0.00001)
plt.show()

#Δειγματοληψία του z(t) με fs
t=np.linspace(0, 4/fm, 4/fm*fs)
sine=np.sin(2*np.pi*fm*t)
plt.scatter(t, sine, s=4, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("z(t), fs = 25 kHz")
plt.xlim(-0.00001, 4/fm+0.00001)
plt.show()

#Fourier Transform στο z(t)=sine2 με δειγματοληψία fs2 για μεγαλύτερη ακρίβεια
sinef2=fft(sine2)
tf2=np.linspace(0, fs2/2, 4/fm*fs2/2)
plt.plot(tf2,np.abs(sinef2[0:int(4/fm*fs2/2)]))
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [V]")
plt.title("Frequency Spectrum of sampled signal (fs2)")
plt.xlim(-1000, 100001)
plt.show()

#Παρατηρούμε ότι για πάνω από 30kHz το φάσμα είναι περίπου μηδέν
#Για πλήρη(μερική) ανακατασκευή του σήματος πρέπει fs=2*30kHz=60kHz
fs0= 60*1000
t0=np.linspace(0, 4/fm, 4/fm*fs0)
sine0=np.sin(2*np.pi*fm*t0)
plt.plot(t0, sine0, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("z(t), fs = 60 kHz")
plt.show()

#Ερώτημα (ii)
fm3 = fm + 1000
#Δειγματοληψία του q(t) με fs1 
tq1=np.linspace(0, 1/1000, 1/1000*fs1)
q1=np.sin(2*np.pi*fm*tq1) + np.sin(2*np.pi*fm3*tq1)
plt.scatter(tq1, q1, s=4, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("q(t), fs1 = 125 kHz")
plt.xlim(-0.00001, 1/1000+0.00001)
plt.show()

#Δειγματοληψία του q(t) με fs2
tq2=np.linspace(0, 1/1000, 1/1000*fs2)
q2=np.sin(2*np.pi*fm*tq2) + np.sin(2*np.pi*fm3*tq2)
plt.scatter(tq2, q2, s=4, color='red', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("q(t), fs2 = 300 kHz")
plt.xlim(-0.00001, 1/1000+0.00001)
plt.show()

#Κοινό διάγραμμα
plt.scatter(tq1, q1, s=15, color='blue', marker='*', label='fs1 = 125kHz')
plt.scatter(tq2, q2, s=15, color='red', marker='X', label='fs2 = 300kHz')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("q(t), fs1 & fs2")
plt.legend(loc="upper right")
plt.xlim(-0.00001, 1/1000+0.00001)
plt.show()

#Δειγματοληψία του q(t) με fs
tq=np.linspace(0, 1/1000, 1/1000*fs)
q=np.sin(2*np.pi*fm*tq) + np.sin(2*np.pi*fm3*tq)
plt.scatter(tq, q, s=4, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("q(t), fs = 25 kHz")
plt.xlim(-0.00001, 1/1000+0.00001)
plt.show()

#Fourier Transform στο q(t)=q2 με δειγματοληψία fs2 για μεγαλύτερη ακρίβεια
qf2=fft(q2)
tf2=np.linspace(0, fs2/2, 1/1000*fs2/2)
plt.plot(tf2,np.abs(qf2[0:int(1/1000*fs2/2)]))
plt.grid()
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude [V]")
plt.title("Frequency Spectrum of sampled signal (fs2)")
plt.xlim(-1000, 81000)
plt.show()

#Παρατηρούμε ότι για πάνω από 30kHz το φάσμα είναι περίπου μηδέν
#Για πλήρη(μερική) ανακατασκευή του σήματος πρέπει fs=2*30kHz=60kHz
fs0= 60*1000
tq0=np.linspace(0, 1/1000, 1/1000*fs0)
q0=np.sin(2*np.pi*fm*tq0) + np.sin(2*np.pi*fm3*tq0)
plt.plot(tq0, q0, color='blue', marker=',')
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("q(t), fs = 60 kHz")
plt.show()

#Άσκηση 2
#A Μέρος
#Συνάρτηση που υλοποιεί τον mid-riser quantizer
Q=4/31.5 #βήμα κβάντισης (Χώρισε τα 4V σε 31,5 κομμάτια)
def midrise_quantizer(x, Q):
    x = np.copy(x)
    idx = np.where(np.abs(x) > 4) #κοβει όλες τις τιμες πάνω από 4
    x[idx] = np.sign(x[idx])
    xQ = Q * (np.floor(x/Q) + 0.5) #πραγματοποίηση της κβάντισης όλων των δειγμάτων στην κοντινότερη στάθμη και δημιουργία xQ με μόνο κβαντισμένες τιμές
    return xQ

#Δειγματοληψία sq_triangle(t) με fs1=45fm
fs21=45*fm
t1=np.linspace(0, 2/fm, 2/fm*fs21)
triangle1=2*signal.sawtooth(2*np.pi*fm/2*t1, 0.5)
sq_triangle1=triangle1*triangle1
xQ=midrise_quantizer(sq_triangle1, Q)
plt.figure(figsize=(12,6))
plt.yticks(np.arange(0+Q/2, 4, Q),['00000', '00001', '00011','00010', '00110', '00111', '00101', '00100', '01100', '01101', '01111', '01110', '01010', '01011', '01001', '01000', '11000', '11001', '11011', '11010', '11110', '11111', '11101', '11100', '10100', '10101', '10111', '10110', '10010', '10011', '10001', '10000'])
#χωρίζουμε το διάστημα [0+Q/2, 4] με βήμα Q και δίνουμε σε κάθε στάθμη το όνομα σε Gray Code π.χ. στο Q/2 δίνουμε το '00000'
plt.plot(t1,xQ)
plt.grid()
plt.xlabel("Time [s]")
plt.ylabel("Gray Code 5-bit")
plt.title("Mid-rise Quantizer")
plt.show()

#B Μέρος
#Ερώτημα (i) (10 δείγματα)
av1=0
sum1=0
#Υπολογισμός error
e = xQ-sq_triangle1 #Το σφάλμα προκύπτει από την αφαίρεση του αρχικού σήματος από το κβαντισμένο

#Υπολογισμός μέσης τιμής
for i in range(10):
    av1 += e[i]

#Υπολογισμός τυπικής απόκλισης
for i in range(10):
    sum1=+ (e[i]-av1)*(e[i]-av1)

standard_deviation1=np.sqrt(1/9*sum1)
print("Standard Deviation (10samples): " + str(standard_deviation1))

#Ερώτημα (ii) (20 δείγματα)
av2=0
sum2=0
#Υπολογισμός error
e = xQ-sq_triangle1

#Υπολογισμός μέσης τιμής
for i in range(20):
    av2 += e[i]

#Υπολογισμός τυπικής απόκλισης
for i  in range(20):
    sum2+=(e[i]-av2)*(e[i]-av2)

standard_deviation2=np.sqrt(1/19*sum2)
print("Standard Deviation (20samples): " + str(standard_deviation2))

#Ερώτημα (iii)
f1=0
e1=0
#Υπολογισμός μέσης τιμής τετραγώνων (10 δείγματα)
for i in range(10):
    f1 += sq_triangle1[i]*sq_triangle1[i]
    e1 += e[i]*e[i]

snr1=f1/e1
print("SNR of 10 samples: " + str(snr1))

f2=0
e2=0
#Υπολογισμός μέσης τιμής τετραγώνων (20 δείγματα)
for i in range(20):
    f2 += sq_triangle1[i]*sq_triangle1[i]
    e2 += e[i]*e[i]

snr2=f2/e2
print("SNR of 20 samples: " + str(snr2))

#Γ Μέρος
gray_code=['00000', '00001', '00011', '00010', '00110', '00111', '00101', '00100', '01100', '01101', '01111', '01110', '01010', '01011', '01001', '01000', '11000', '11001', '11011', '11010', '11110', '11111', '11101', '11100', '10100', '10101', '10111', '10110', '10010', '10011', '10001', '10000']
b=np.arange(0+Q/2, 4, Q) #δημιουργία πίνακα με κβαντισμένες τιμές σε αύξουσα σειρά
bipolar = []

for i in range(45): #Για κάθε δείγμα του κβαντισμένου σήματος βρίσκουμε σε ποιο στοιχείο του πίνακα b αντιστοιχεί και κρατάμε τη θέση του j 
    j=0
    while xQ[i] != b[j]: 
        j+=1
    bipolar.append(gray_code[j]) #Επειδή το j στοιχείο του b αντιστοιχεί στο j στοιχείο του gray_code πινακα αφού και οι 2 είναι σε αύξουσα σειρά, 
								 #θα βάλουμε στον bipolar πινακα το σωστό στοιχείο του gray_code πινακα
#ο bipolar πίνακας που δημιουργείται περιέχει τις τιμές gray code που αντιστοιχούν στο κβαντισμένο σήμα xQ

seq= []
#Με την παρακάτω διαδικασία σπάμε τον gray code που είναι σε string σε μεμονωμένα 0 ή 1 (Το μέγεθος του πίνακα είναι 45(#δειγμάτων)*5(5-bit Gray code)=225)
for i in range(45):
    for j in range(5):
        seq.append(bipolar[i][j])

#Bipolar RZ plot
#Κάθε bit αναπαρίσταται από περίοδο 1msec
#Σπάμε την περίοδο σε 2 μέρη για να διευκολύνουμε την αναπαράσταση
bit_rate=[]
flag=0 #χρήση flag για να ελέγχουμε πότε θα έχουμε 5V και πότε -5V στο πρώτο μισό της περιόδου
for i in range(225):
    n=seq[i]
    if(n=='0'): #αν έχουμε 0 τότε ολόκληρο το 1msec θα είναι 0V
        bit_rate.append(0)
        bit_rate.append(0)
    elif(n=='1' and flag==0): #αν έχουμε 1 τότε για 0,5msec 5V και για 0,5msec 0V
        bit_rate.append(5)
        bit_rate.append(0)
        flag=1
    elif(n=='1' and flag==1): #αν έχουμε 1 τότε για 0,5msec -5V και για 0,5msec 0V
        bit_rate.append(0)
        bit_rate.append(-5)
        flag=0
    	
x=np.linspace(0,0.225, 450) #Αφού ο bit rate έχει 450 στοιχεία τόσα και τα δειγματά μας, καθέ ενα από αυτά θα διαρκεί 0,0005 sec
plt.step(x,bit_rate,where='post') #Χρησιμοποιούμε την step με where='post' γιατι προσφέρει το ζητούμενο αποτέλεσμα
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [A]")
plt.title("Bit stream (Bipolar RZ)")
plt.show()

#Άσκηση 3
#A Μέρος
fs=130*fm
t31=np.linspace(0, 4/35, 4/35*fs) #η περίοδος του διαμορφωμένου είναι ίση με του
sine31=np.sin(2*np.pi*fm*t31) #φερον σήμα
m=np.sin(2*np.pi*35*t31) #σήμα πληροφορίας
c=(1+0.5*m)*sine31 #χρήση τύπου 3.1 βιβλίο με κατάλληλη προσαρμογή και k=0,5
plt.plot(t31,c)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [V]")
plt.title("AM output")
plt.show()

#B Μέρος
#Δημιουργία βαθυπερατού φίλτρου
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff/nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b,a = butter_lowpass(cutoff,fs,order=order)
    y = lfilter(b,a,data) #εφαρμογή του φίλτρου στο σημα
    return y

order = 1   
cutoff = 90  # συχνότητα αποκοπής

temp = abs(c) #ανόρθωση διαμορφωμένου σήματος
demod_sig = butter_lowpass_filter(temp, cutoff, fs, order) #φιλτράρισμα του σήματος μετά την ανόρθωση
demod_sig_1 = demod_sig - np.mean(demod_sig) #βγάζουμε την dc συνιστώσα που προστέθηκε απο την διαμόρφωση
demod_sig_1 = demod_sig_1 * 3.38# ενίσχυση του σήματος για να επανέλθει ύστερα από τις απώλειες του lpf
plt.plot(t31, demod_sig_1, 'b-')
plt.xlabel('Time[s]')
plt.title('Demodulated Signal')
plt.ylabel('Amplitude[V]')
plt.grid()
plt.ylim(-1-0.2, 1+0.2)
plt.show()

