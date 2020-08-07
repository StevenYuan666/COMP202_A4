#this is the third part of Assignment3, construct_patient
#Name: Ye Yuan
#Student ID: 260921269
import doctest
import datetime
import numpy as np
import matplotlib.pyplot as plt

########SOME GLOBAL CONSTANTS HERE#############
NUMBERS=['0','1','2','3','4','5','6','7','8','9']
###############################################


########SOME HELPER FUNCTION HERE##############
def convert_to_celsius(temp_in_F):
    '''
    (flt) -> flt
    take an input above 45 and transfer it to celsius degrees
    >>> convert_to_celsius(102.2)
    39.0
    '''
    #use the formula to transfer it to celsius degrees
    C=(temp_in_F-32)*5/9
    #and round it to two decimal numbers
    return round(C,2)

def round_age(input_age):
    '''
    (int) -> int
    take a integer as input, and round it to nearest five
    >>> round_age(23)
    25
    >>> round_age(2)
    0
    >>> round_age(28)
    30
    >>> round_age(7)
    5
    >>> round_age(8)
    10
    >>> round_age(88)
    90
    '''
    #change the input to string
    age=str(input_age)
    #check if it is two decimal place
    if len(age)==2:
            #round it to nearest five
            if age[1] in ['3','4','5','6','7']:
                age=age[0]+'5'
            if age[1] in ['0','1','2']:
                age=age[0]+'0'
            if age[1] in ['8','9']:
                age=str((int(age[0])+1))+'0'
    #check if it it one decimal place
    elif len(age)==1:
        #round it to nearest five
        if age in ['0','1','2']:
            age='0'
        if age in ['3','4','5','6','7']:
            age='5'
        if age in ['8','9']:
            age='10'
    #change it back to integer
    return int(age)
###############################################

class Patient:
    
    def __init__(self,num,day_diagnosed,age,\
                 sex_gender,postal,state,temps,days_symptomatic):
        '''
        (str,str,str,str,str,str,str,str) -> Patient
        assign num,day_diagnosed and age as integer, change all the sex_gender
        to M,F or X, check if the postal code is valid, assign it as postal
        attribute. Transfer the degrees to celsius if it is not. Assign the
        days_symptomatic as integer.
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t39.0'
        >>> p = Patient('0', '0', '42', 'Non-Binary', 'YYDZX', 'R', '102，2C', '12')
        >>> str(p)
        '0\\t42\\tX\\t000\\t0\\tR\\t12\\t39.0'
        >>> p = Patient('0', '0', '42', 'Non-Binary', 'YYDZX', 'R', 'N-A', '12')
        >>> str(p)
        '0\\t42\\tX\\t000\\t0\\tR\\t12\\t0.0'
        '''
        self.num=int(num)
        self.day_diagnosed=int(day_diagnosed)
        self.age=int(age)
        #initilize the sex_gender as F if it is female or women
        if sex_gender[0]=='F' or sex_gender[0]=='W':
            self.sex_gender='F'
        #initilize the sex_gender as M if it is man or homme
        elif sex_gender[0]=='M' or sex_gender[0]=='H':
            self.sex_gender='M'
        #initilize the sex_gender as X if it is non binary gender
        else:
            self.sex_gender='X'
        #check if the postal code is valid, initilize the postal code as
        #the first three characters
        if postal[0]=='H' and (postal[1] in NUMBERS) and (postal[2] not in NUMBERS):
            self.postal=postal[0:3]
        #if it is not valid, initialize the postal code as 000
        else:
            self.postal='000'
        self.state=state
        #check if the tempreture is not valid
        if '0' not in temps and '1' not in temps and '2' not in temps\
           and '3' not in temps and '4' not in temps and '5' not in temps\
           and '6' not in temps and '7' not in temps and '8' not in temps\
           and '9' not in temps:
            #initialize zero if it is not valid
            self.temps=[0.0]
        #initialize as tempreture otherwise
        else:
            temps=temps.replace('-','.')
            temps=temps.replace('，','.')
            temps=temps.replace(',','.')
            temp=''
            #change it to celsius degrees if it is not
            #remove the unit
            for digit in temps:
                if digit=='.' or digit in NUMBERS:
                    temp+=digit
            temps=float(temp)
            #convert if need
            if temps>45:
                self.temps=[convert_to_celsius(temps)]
            else:
                self.temps=[temps]
        self.days_symptomatic=int(days_symptomatic)
    def __str__(self):
        '''
        (Patient) -> str
        return the patient object's attributes  in series: num,age,sex_gender,
        postal_code,day_diagnosed,state,days_symptomatic and every tempretures
        in the temp list.
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t39.0'
        >>> p = Patient('0', '0', '42', 'Non-Binary', 'YYDZX', 'R', '102，2C', '12')
        >>> str(p)
        '0\\t42\\tX\\t000\\t0\\tR\\t12\\t39.0'
        >>> p = Patient('0', '0', '42', 'Non-Binary', 'YYDZX', 'R', 'N-A', '12')
        >>> str(p)
        '0\\t42\\tX\\t000\\t0\\tR\\t12\\t0.0'
        '''
        #take the first seven attribute to the info first
        info=str(self.num)+'\t'+str(self.age)+'\t'+self.sex_gender+'\t'+self.postal+\
              '\t'+str(self.day_diagnosed)+'\t'+self.state+'\t'+\
              str(self.days_symptomatic)+'\t'
        #check if there is only one tempreture in the list
        if len(self.temps)==1:
            info+=str(self.temps[0])
        else:
            #use ; to connect each element otherwise
            temps=(str(temp) for temp in self.temps)
            temps=';'.join(temps)
            #then add the temps in the end of the info
            info+=temps
        #return the info
        return info
    def update(self,other):
        '''
        (Patient,Patient)
        update the state and symptomatic days if the two input patient is same, and
        add the tempreture to the attribute list
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40，0 C', '13')
        >>> p.update(p1)
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t13\\t39.0;40.0'
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'R', '40-0 C', '13')
        >>> p.update(p1)
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tR\\t13\\t39.0;40.0'
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3H', 'R', '40-0 C', '13')
        >>> p.update(p1)
        Traceback (most recent call last):
        AssertionError: num, gender, and postal code are not same
        '''
        #check if the number, sex gender and postal code are same
        if self.num==other.num and self.sex_gender==other.sex_gender and\
           self.postal==other.postal:
            #update the symptomatic days and state
            self.days_symptomatic=other.days_symptomatic
            self.state=other.state
            #add the temps to the attribute list
            self.temps.extend(other.temps)
        #raise an error otherwise
        else:
            raise AssertionError('num, gender, and postal code are not same')
def stage_four(input_filename, output_filename):
    '''
    (str,str) -> dict
    take the input_filename and the output filename as inputs, and create a
    patient object each line, finally return a dictionary
    >>> p=stage_four('test1_1_1.tsv', 'test1_1_1_1.tsv')
    >>> len(p)
    7
    >>> str(p[0])
    '0\\t76\\tF\\tH3B\\t0\\tD\\t2\\t41.5;0.0'
    >>> p2=stage_four('test2_2_2.tsv', 'test2_2_2_2.tsv')
    >>> len(p2)
    1746
    >>> str(p2[1])
    '1\\t63\\tF\\tH1X\\t1\\tR\\t6\\t39.2;39.0;38.3;38.0;38.0'
    '''
    #open the input file and read a line
    input_f=open(input_filename,'r',encoding='utf-8')
    line=input_f.readline()
    #create a new file to write the changed line
    output_f=open(output_filename,'w',encoding='utf-8')
    #create a dictionary to store the value
    final_dict={}
    #iterate the file
    while(line!=''):
        #change the line to list
        line_list=line.split('\t')
        #create a patient object for the line
        patient=Patient(str(line_list[1]),str(line_list[2]),str(line_list[3]),\
                        str(line_list[4]),str(line_list[5]),str(line_list[6]),\
                        str(line_list[7]),str(line_list[8]))
        #add the object to the dictionary
        if patient.num not in final_dict:
            final_dict[patient.num]=patient
        #if it is already in dictionary,then update it
        elif patient.num in final_dict:
            final_dict[patient.num].update(patient)
        #read a new line
        line=input_f.readline()
    #sort the dictionary in increasing order
    key_list=[]
    for key in final_dict:
        key_list.append(key)
    key_list.sort()
    final={}
    for key in key_list:
        final[key]=final_dict[key]
    #write every changed line to the new file
    for key in final:
        output_f.write(str(final[key])+'\n')
    #close and save the files
    input_f.close()
    output_f.close()
    #return the final dictionary
    return final

def fatality_by_age(dict_of_patients):
    '''
    >>> p2=stage_four('test2_2_2.tsv', 'test2_2_2_2.tsv')
    >>> fatality_by_age(p2)
    [1.0, 1.0, 0.7857142857142857, 0.8125, 1.0, 0.9411764705882353, 0.9473684210526315, 0.9444444444444444, 0.9, 0.9, 1.0, 0.9583333333333334, 0.8181818181818182, 0.9230769230769231, 1.0, 0.9166666666666666, 1.0, 1.0, 1.0]
    '''
    #create two dictionary to count the number of dead and recovered people at
    #different age state
    dead_dict={}
    dead_recovered_dict={}
    #round every patient age to nearest five, by calling the helper function
    for num in dict_of_patients:
        dict_of_patients[num].age=round_age(dict_of_patients[num].age)
    #calculate how many people dead at different age, store it to the dead dictionary
    for num in dict_of_patients:
        if dict_of_patients[num].state=='D':
            if dict_of_patients[num].age in dead_dict:
                dead_dict[dict_of_patients[num].age]+=1
            else:
                dead_dict[dict_of_patients[num].age]=1
    #calculate how many people dead at different age, store it to the second dictionary
    for num in dict_of_patients:
        if dict_of_patients[num].state=='D':
            if dict_of_patients[num].age in dead_recovered_dict:
                dead_recovered_dict[dict_of_patients[num].age]+=1
            else:
                dead_recovered_dict[dict_of_patients[num].age]=1
    #calculate how many people recovered at different age,
    #add it to the second dictionary            
    for num in dict_of_patients:
        if dict_of_patients[num].state=='R':
            if dict_of_patients[num].age in dead_recovered_dict:
                dead_recovered_dict[dict_of_patients[num].age]+=1
            else:
                dead_recovered_dict[dict_of_patients[num].age]=1
    #sort the key in increasing order, so we can sort the dictionary
    key_list=[]
    for key in dead_dict:
        key_list.append(key)
    key_list.sort()
    #sort the value of the dead and recovered people in the two dictioanries
    final_dead_dict={}
    final_dead_recovered_dict={}
    for key in key_list:
        final_dead_dict[key]=dead_dict[key]
        final_dead_recovered_dict[key]=dead_recovered_dict[key]
    dead_rate=[]
    for key in final_dead_dict:
        dead_rate.append(final_dead_dict[key]/final_dead_recovered_dict[key])
    #find the key of the dictionary and sort it, as the x-axis of the graph
    x_list=[]
    for key in dead_dict:
        x_list.append(key)
    x_list.sort()
    #change both x axis and y axis lists to array
    x_coord=np.array(x_list)
    y_coord=np.array(dead_rate)
    #set the y axis from 0 to 1.2
    plt.ylim((0, 1.2))
    #plot the graph
    plt.plot(x_coord,y_coord)
    #lable the graph
    plt.title("Probabilty of death vs age, by Ye Yuan")
    plt.xlabel('Age (To Nearest Five)')
    plt.ylabel('Deaths / (Deaths+Recoveries)')
    #save the graph
    plt.savefig("fatality_by_age.png")
    #return the list
    return dead_rate


if __name__=='__main__':
    doctest.testmod()
    
