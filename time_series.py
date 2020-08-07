#this is the second part of Assignment 4, time_series
#Name: Ye Yuan
#Student ID:260921269

import doctest
import datetime
import numpy as np
import matplotlib.pyplot as plt

def date_diff(date1,date2):
    '''
    (str,str) -> int
    Input two different dates in ISO format, calculate the difference between
    these two dates. If the first date is earlier, the difference should be
    positive, otherwise should be negative.
    >>> date_diff('2019-10-31', '2019-11-2')
    2
    >>> date_diff('2019-11-2', '2019-10-31')
    -2
    '''
    #split the data by -, transfer it to a list
    date1=date1.split('-')
    #create a date type object for it
    date_one=datetime.date(int(date1[0]),int(date1[1]),int(date1[2]))
    #similarly for the second data
    date2=date2.split('-')
    date_two=datetime.date(int(date2[0]),int(date2[1]),int(date2[2]))
    #the difference is the first one minus the second one
    diff=date_two-date_one
    #then return the diff in days
    return diff.days

def get_age(date1,date2):
    '''
    (str,str) -> int
    Input two different dates in ISO format, calculate the difference between
    these two dates and transfer the result to years. If the first date is
    earlier, the difference should be positive, otherwise should be negative.
    >>> get_age('2018-10-31', '2019-11-2')
    1
    >>> get_age('2018-10-31', '2000-11-2')
    -17
    '''
    #create a year constant
    YEAR_CONST=365.2425
    #calculate the difference in days
    date_difference=date_diff(date1,date2)
    #return the diff in years, so that it is the age
    return int(date_difference/YEAR_CONST)

def stage_three(input_filename,output_filename):
    '''
    (str,str) -> dict
    input the input_filename and the output_filename, change each line in the
    file so that change the record date to the difference between the record
    date and the index date, and change the birthdate to the age on the index
    date. Finally, return a dictionary record The keys are each day of the
    pandemic (integer).The values are a dictionary,with how many people
    are in each state on that day.
    >>> stage_three('test1_1.tsv', 'test1_1_1.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}, 2: {'I': 6, 'D': 0, 'R': 0}}
    >>> stage_three('test2_2.tsv', 'test2_2_2.tsv')
    {0: {'I': 1, 'D': 0, 'R': 0}, 1: {'I': 2, 'D': 1, 'R': 0}, 2: {'I': 6, 'D': 0, 'R': 0}, 3: {'I': 15, 'D': 0, 'R': 0}, 4: {'I': 31, 'D': 4, 'R': 0}, 5: {'I': 68, 'D': 7, 'R': 1}, 6: {'I': 154, 'D': 14, 'R': 0}, 7: {'I': 348, 'D': 28, 'R': 1}, 8: {'I': 788, 'D': 49, 'R': 7}, 9: {'I': 1353, 'D': 114, 'R': 8}}
    '''
    #open the input file and read all lines
    input_f=open(input_filename)
    lines=input_f.readlines()
    #find the index date, which is the date in the first line
    index_date_line=lines[0].split('\t')
    index_date=index_date_line[2]
    #create a new file to write the changed line
    output_f=open(output_filename,'w',encoding='utf-8')
    #create an empty dictionary
    stats={}
    #iterate all lines in the input file
    for line in lines:
        #split the line by \t
        line=line.split('\t')
        #calculate the date difference and age, and assign them correspondingly
        line[2]=date_diff(index_date,line[2])
        line[3]=get_age(line[3],index_date)
        #then add it to the created dictionary
        if line[2] not in stats:
            stats[line[2]]={'I':0,'D':0,'R':0}
        #change the patient state by using just one letter
        if line[6][0]=='I':
            line[6]='I'
        elif line[6][0]=='R':
            line[6]='R'
        else:
            line[6]='D'
        #add one to the corresponding value in the dictionary
        stats[line[2]][line[6]]+=1
        #change the type of the value back to string
        line[2]=str(line[2])
        line[3]=str(line[3])
        #transfer the list to string
        write_line='\t'.join(line)
        #write the line to the new file
        output_f.write(write_line)
    #close and save the files
    input_f.close()
    output_f.close()
    #return the dictionary
    return stats

def plot_time_series(input_dict):
    '''
    input a dictionary formmated like the result of stage3, return a list
    including the value of infected people, recovered people and dead people.
    Then draw a plot of the result.
    >>> d2=stage_three('test2_2.tsv', 'test2_2_2.tsv')
    >>> plot_time_series(d2)
    [[1, 0, 0], [2, 0, 1], [6, 0, 0], [15, 0, 0], [31, 0, 4], [68, 1, 7], [154, 0, 14], [348, 1, 28], [788, 7, 49], [1353, 8, 114]]
    '''
    #create an empty list
    result_list=[]
    #iterate the input dictionary
    for day in input_dict:
        #create the temporary list to store every value corresponding to states
        temp=[input_dict[day]['I'],input_dict[day]['R'],input_dict[day]['D']]
        #add the temporary list to the created final list
        result_list.append(temp)
    #create an empty list for the x-axis
    x_list=[]
    #the x-axis is the key of the input dictionary
    for key in input_dict:
        x_list.append(key)
    #transfer the list to array
    x_coord=np.array(x_list)
    #create empty lists for y-axis, infected, recovered and dead
    infected_list=[]
    recovered_list=[]
    dead_list=[]
    #store the values of each state to the created lists
    for value in result_list:
        infected_list.append(value[0])
        recovered_list.append(value[1])
        dead_list.append(value[2])
    #transfer the lists to arrays
    infected_y_coord=np.array(infected_list)
    recovered_y_coord=np.array(recovered_list)
    dead_y_coord=np.array(dead_list)
    #plot the graph
    plt.plot(x_coord, infected_y_coord,'b')
    plt.plot(x_coord, recovered_y_coord,'r')
    plt.plot(x_coord, dead_y_coord,'g')
    #label the graph
    plt.legend(['Infected', 'Recovered', 'Dead'])
    plt.title("Time series of early pandemic, by Ye Yuan")
    plt.xlabel('Days into Pandemic')
    plt.ylabel('Number of People')
    #save the graph
    plt.savefig("time_series.png")
    #return the list
    return result_list
    

if __name__=='__main__':
    doctest.testmod()
    
