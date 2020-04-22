import sys
def my_except_hook(exctype, value, traceback):
        print('There has been an error in the system')
sys.excepthook = my_except_hook
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
import parselmouth
from parselmouth.praat import call, run_file
import glob
import errno
import csv,sys
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import time
import os
from subprocess import check_output
from sklearn import preprocessing
import queue
import sounddevice as sd
import soundfile as sf
import _thread  
import pickle
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
from pandas import read_csv

pathy = input("Enter the path to the Auto-Speech_Rater directory: ")
name = input("what is your name?    ")
t0 = int(input("Your desired Recording time in seconds:    "))
levvel=int(input("Pick degree of difficulties between 0 to 100:    "))

pa00=pathy+"/"+"dataset"+"/"+"audioFiles"+"/"
pa0=pathy+"/"+"dataset"+"/"+"audioFiles"+"/"+name+".wav"
pa1=pathy+"/"+"dataset"+"/"+"datanewchi22.csv"
pa2=pathy+"/"+"dataset"+"/"+"stats.csv"
pa3=pathy+"/"+"dataset"+"/"+"datacorrP.csv"
pa4=pathy+"/"+"dataset"+"/"+"datanewchi.csv"
pa5=pathy+"/"+"dataset"+"/"+"datanewchi33.csv"
pa6=pathy+"/"+"dataset"+"/"+"datanewchi33.csv"
pa7=pathy+"/"+"dataset"+"/"+"datanewchi44.csv"
pa8=pathy+"/"+"dataset"+"/"+"essen"+"/"+"MLTRNL.praat"
pa9=pathy+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"

rere=pa0

RECORD_TIME = t0

def countdown(p,q,w):
    i=p
    j=q
    z=w
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):  
            print(str(k)+str(i)+ " : " +str(j), "\t", end="\r")
        else:
            print(str(k)+str(i)+" : " + str(k)+str(j), "\t", end="\r")
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
    if(i==0 and j==-1):
        if z==0:
            huf="Go ahead!"
            print(huf)
        if z==1:
            huf="Time up!"
        # time.sleep(1)

print("===========================================")
print("HOLD ON!! get ready, 5 seconds to go!")
print("===========================================")
countdown(0,5,0) #countdown(min,sec)	


q = queue.Queue()
rec_start = int(time.time())

dev_info = sd.query_devices(2,'input')
#dev_info = default.device()
# samplerate = int(dev_info['default_samplerate'])
samplerate = 48000

def data_callback(input_data, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(input_data.copy())

with sf.SoundFile(rere, mode='x', samplerate=samplerate, channels=2) as file:
    with sd.InputStream(samplerate=samplerate, device=2, channels=2, callback=data_callback,blocksize=20500):
        rec_time = int(time.time()) - rec_start
        _thread.start_new_thread(countdown,(0,t0,1))
        while rec_time <= RECORD_TIME:
            file.write(q.get())
            rec_time = int(time.time()) - rec_start
                            
result_array = np.empty((0, 100))
path = pa0
files = glob.glob(path)
result_array = np.empty((0, 27))

try:
	def mysppron(m,p,q):
		sound=m
		sourcerun=p 
		path=q
		objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
		print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z2=z1.strip().split()
		z3=int(z2[13]) # will be the integer number 10
		z4=float(z2[14]) # will be the floating point number 8.3
		db= binom.rvs(n=10,p=z4,size=10000)
		a=np.array(db)
		b=np.mean(a)*100/10
		print ("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (b))
		return;
	
	def myspp(m,p,q):
		sound=m
		sourcerun=p 
		path=q
		objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
		print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z2=z1.strip().split()
		z3=int(z2[13]) # will be the integer number 10
		z4=float(z2[14]) # will be the floating point number 8.3
		db= binom.rvs(n=10,p=z4,size=10000)
		a=np.array(db)
		b=np.mean(a)*100/10
		return b
	
	def myspgend(m,p,q):
		sound=m
		sourcerun=p 
		path=q
		objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
		print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z2=z1.strip().split()
		z3=float(z2[8]) # will be the integer number 10
		z4=float(z2[7]) # will be the floating point number 8.3 
		
		if z4<=114:
			g=101
			j=3.4
		elif z4>114 and z4<=135:
			g=128
			j=4.35
		elif z4>135 and z4<=163:
			g=142
			j=4.85
		elif z4>163 and z4<=197:
			g=182
			j=2.7
		elif z4>197 and z4<=226:
			g=213
			j=4.5
		elif z4>226:
			g=239
			j=5.3
		else:
			print("Voice not recognized")
			exit()
		def teset(a,b,c,d):
			d1=np.random.wald(a, 1, 1000)
			d2=np.random.wald(b,1,1000)
			d3=ks_2samp(d1, d2)
			c1=np.random.normal(a,c,1000)
			c2=np.random.normal(b,d,1000)
			c3=ttest_ind(c1,c2)
			y=([d3[0],d3[1],abs(c3[0]),c3[1]])
			return y
		nn=0
		mm=teset(g,j,z4,z3)
		while (mm[3]>0.05 and mm[0]>0.04 or nn<5):
		   mm=teset(g,j,z4,z3)
		   nn=nn+1
		nnn=nn
		if mm[3]<=0.09:
			mmm=mm[3]
		else:
			mmm=0.35
		if z4>97 and z4<=114:
			print("a Male, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn)) 
		elif z4>114 and z4<=135:
			print("a Male, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>135 and z4<=163:
			print("a Male, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>163 and z4<=197:
			print("a female, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>197 and z4<=226:
			print("a female, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>226 and z4<=245:
			print("a female, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
		else:
			print("Voice not recognized")
	
	for soundi in files:
		objects= run_file(pa8, -20, 2, 0.3, "yes", soundi, pa00, 80, 400, 0.01, capture_output=True)
		#print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z3=z1.strip().split()
		z2=np.array([z3])
		result_array=np.append(result_array,[z3], axis=0)
		
	np.savetxt(pa1,result_array, fmt='%s',delimiter=',')

	#Data and features analysis 
	df = pd.read_csv(pa1,
						 names = ['avepauseduratin','avelongpause','speakingtot','avenumberofwords','articulationrate','inpro','f1norm','mr','q25',
								  'q50','q75','std','fmax','fmin','vowelinx1','vowelinx2','formantmean','formantstd','nuofwrds','npause','ins',
								  'fillerratio','xx','xxx','totsco','xxban','speakingrate'],na_values='?')

	scoreMLdataset=df.drop(['xxx','xxban'], axis=1)
	scoreMLdataset.to_csv(pa7, header=False,index = False)
	newMLdataset=df.drop(['avenumberofwords','f1norm','inpro','q25','q75','vowelinx1','nuofwrds','npause','xx','totsco','xxban','speakingrate','fillerratio'], axis=1)
	newMLdataset.to_csv(pa5, header=False,index = False)
	namess=nms = ['avepauseduratin','avelongpause','speakingtot','articulationrate','mr',
								  'q50','std','fmax','fmin','vowelinx2','formantmean','formantstd','ins',
								  'xxx']
	df1 = pd.read_csv(pa5,
							names = namess)
	df33=df1.drop(['xxx'], axis=1)
	array = df33.values
	array=np.log(array)
	x = array[:,0:13]

	print(" ")
	print(" ")
	print("===========================================")
	p=pa0
	c=pa9
	a=pa00
	bi=myspp(p,c,a)
	if bi<levvel:
		mysppron(p,c,a)
		input("Try again, unnatural-sounding speech detected. No further result. Press any key to exit.")
		exit()
	
	mysppron(p,c,a)
	myspgend(p,c,a)
	
	print(" ")
	print(" ")
	print("====================================================================================================")
	print("HERE ARE THE RESULTS, your spoken language level (speaking skills).")
	print("a: just started, a1: beginner, a2: elementary, b1: intermediate, b2: upper intermediate, c: master") 
	print("====================================================================================================")

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"CART_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("58% accuracy    ",predictions)

	#filename=pathy+"/"+"essen"+"/"+"ETC_model.sav"

	#model = pickle.load(open(filename, 'rb'))
	#predictions = model.predict(x)
	#print("70% accuracy    ",predictions)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"KNN_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("65% accuracy    ",predictions)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"LDA_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("70% accuracy    ",predictions)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"LR_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("67% accuracy    ",predictions)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"NB_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("64% accuracy    ",predictions)

	#filename=pathy+"/"+"essen"+"/"+"PCA_model.sav"

	#model = pickle.load(open(filename, 'rb'))
	#predictions = model.predict(x)
	#print("70% accuracy    ",predictions)

	#filename=pathy+"/"+"essen"+"/"+"RFE_model.sav"

	#model = pickle.load(open(filename, 'rb'))
	#predictions = model.predict(x)
	#print("70% accuracy    ",predictions)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"SVN_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict(x)
	print("63% accuracy    ",predictions)

except:
	print(" ")
	print(" ")
	print("===========================================")
	print("Try again, noisy background or unnatural-sounding speech detected. No result.")
print("===========================================")
input("RECORDING PROCESS IS DONE, press any key to terminate the programe")
