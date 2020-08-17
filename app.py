import streamlit as st
import pandas as pd
import numpy as np 
import time
import module.ed_triage as modu
from PIL import Image
from sklearn.preprocessing import StandardScaler


#streamlit
st.title("Alder Hey Emergency Triage App")


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)


image = Image.open('alderhey.jpeg')
st.image(image, caption= "Alder Hey Children's Hospital, Liverpool",use_column_width=True)
									

zero_list=(0,0,0,0,0,0,0,0,0,0)
test_df=pd.DataFrame([zero_list],columns=['Transport','Age','Gender','Visit_Reason','REFER_SOURCE','AVPU','PulseRate','RespiratoryRate','SP02','Temperature'])

#pclass/fare,pclass=1&2&3 Cheapest fare(converted)=£2100 & £1900 & £600，The average fare in the data is £84/£21/£14
fare_option=st.selectbox(' Arrival. ',
('Other','Ambulance','Helicopter'))

'You selected:', fare_option
test_df['Transport']=fare_option

	
#gender
gender_option = st.selectbox('Please select your gender.',('Male','Female'))

'You selected:', gender_option

if (gender_option=='Male'):
	test_df['Gender']='male'
else:
	test_df['Gender']='female'
	

#Age
Age = st.slider('How old?', min_value=0, max_value=20, value=6)
st.write(Age, 'years old')

test_df['Age']=Age

#
spouse_option = st.slider('PulseRate', min_value=40, max_value=150, value=70)
test_df['PulseRate']=spouse_option



RespiratoryRate = st.slider('RespiratoryRate', min_value=10, max_value=40, value=25)
test_df['RespiratoryRate']=RespiratoryRate



Temperature = st.slider('Temperature', min_value=34, max_value=40, value=37)
test_df['Temperature']=Temperature

#children
children=st.number_input('SP02?',min_value=34,max_value=100, value=100, step=1)
#st.write('The current number is ', children)
test_df['SP02']=children
#parents
parent_option=st.selectbox('Visit_Reason?',('Allergy (Including Anaphylaxis)'
,'Bites/Stings'
,'Burns and Scalds'
,'Cardiac Conditions'
,'Central Nervous System Conditions (Excluding Strokes)'
,'Cerebro-Vascular Conditions'
,'Contusion/Abrasion'
,'Dermatological Conditions'
,'Diabetes and Other Endocrinological Conditions'
,'Diagnosis Not Classifiable'
,'Dislocation/Fracture/Joint Injury/Amputation'
,'ENT Conditions'
,'Facio-Maxillary Conditions'
,'Foreign Body'
,'Gastrointestinal Conditions'
,'Gynaecological Conditions'
,'Haematological Conditions'
,'Head Injury'
,'Infectious Disease'
,'Laceration'
,'Local Infection'
,'Muscle/Tendon Injury'
,'Near Drowning'
,'Nerve Injury'
,'Nothing Abnormal Detected'
,'Obstetric Conditions'
,'Ophthalmological Conditions'
,'Other Vascular Conditions'
,'Poisoning (Including Overdose)'
,'Psychiatric Conditions'
,'Respiratory Conditions'
,'Social Problem (Includes Chronic Alcoholism and Homelessness)'
,'Soft Tissue Inflammation'
,'Sprain/Ligament Injury'
,'Urological Conditions (Including Cystitis)'
,'Vascular Injury'
,'Visceral Injury'
))

test_df['Visit_Reason']=parent_option

#test_df=modu.preprocessing(test_df)


REFER_SOURCE=st.selectbox('REFER_SOURCE?',('SELF' ,'AE','CONS IN HOSP','OTHER'))

test_df['REFER_SOURCE']=REFER_SOURCE

AVPU=st.selectbox('AVPU?',('Alert','Pain','Unresponsive','Verbal'))

test_df['AVPU']=AVPU


#test_df.to_csv('tester.csv')

prob=modu.makeprediction(test_df)

##Show survival probability
if st.checkbox(' Show the Result ! '):
	st.subheader('Result')
	st.write('Likelihood Urgent Risk (out of 100) = %0.0f , Likelihood Non-Urgent Risk (out of 100) = %0.0f'%(prob[1]*100,prob[0]*100))
