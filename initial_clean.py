#this is the the first part of Assignment 4 initial_clean
#Name: Ye Yuan
#Student ID:260921269

import doctest

def which_delimiter(input_str):
    '''
    (str) -> str
    take a string as a input, and return the most commonly seperator
    in the string. It would be one of comma, space and tab.
    >>> which_delimiter('0 1 2,3')
    ' '
    >>> which_delimiter('0,1,2 3')
    ','
    >>> which_delimiter('0\\t1\\t2 3,4')
    '\\t'
    >>> which_delimiter('1234567890')
    Traceback (most recent call last):
    AssertionError: There is no space,comma and tab at all!
    '''
    #count the number of tab, space and comma first
    num_of_tab=input_str.count('\t')
    num_of_space=input_str.count(' ')
    num_of_comma=input_str.count(',')
    # if the number of space is greater than the other two, return space
    if num_of_space>num_of_comma and num_of_space>num_of_tab:
        return ' '
    # if the number of comma is greater than the other two, return comma
    elif num_of_comma>num_of_tab and num_of_comma>num_of_space:
        return ','
    # if the number of tab is greater than the other two, return tab
    elif num_of_tab>num_of_space and num_of_tab>num_of_comma:
        return '\t'
    #if there is no tab, comma and space, raise an AssertionError
    elif num_of_space==num_of_comma==num_of_tab==0:
        raise AssertionError('There is no space,comma and tab at all!')

def stage_one(input_filename,output_filename):
    '''
    (str,str) -> int
    take an open filename and an out filename as inputs, capitalize all letters
    in the openfile, change the most common delimiter to tab, and change \ and
    . to -. Write all of these changes to the out file, and return how many
    lines in the out file.
    >>> stage_one('260921269-short.txt','test1.tsv')
    10
    >>> stage_one('260921269.txt','test2.tsv')
    3000
    '''
    #open the file and read line by line
    input_f=open(input_filename)
    line=input_f.readline()
    #create a new file to write the line after change
    output_f=open(output_filename,'w',encoding = 'utf-8')
    #create a variable to count the number of the line
    num_of_line=0
    #iterate the open file line by line
    while(line!=''):
        #change all letters to uppercase
        line=line.upper()
        #replace the / and . to -
        line=line.replace('/','-')
        line=line.replace('.','-')
        #change the delimiter to tab if the most common delimiter is others
        if which_delimiter(line)!='\t':
            line=line.replace(which_delimiter(line),'\t')
        #write the changed line to the new file
        output_f.write(line)
        #read a new line
        line=input_f.readline()
        #the number of lines add one
        num_of_line+=1
    #close and save the two files
    input_f.close()
    output_f.close()
    #retunrn the number of the line
    return num_of_line

def stage_two(input_filename,output_filename):
    '''
    (str,str) -> int
    take an open filename and an out filename as inputs, make all of lines is
    nine columns, like 39,2 may be seperated as 39 and 2. Store the changes
    to the output file, return how many lines in the output file.
    >>> stage_two('test1.tsv','test1_1.tsv')
    10
    >>> stage_two('test2.tsv','test2_2.tsv')
    3000
    '''
    #open the input file and read it line by line
    input_f=open(input_filename)
    line=input_f.readline()
    #create a new file to write the changed line
    output_f=open(output_filename,'w',encoding = 'utf-8')
    #create a variable to count the number of the lines
    num_of_line=0
    #count the number of tab, so we can know how many columns are there
    delimiters=line.count('\t')
    #iterate the input file
    while(line!=''):
        #if there are 10 columns, the tempreture must be seperated
        if(delimiters==9):
            #split the line to a list to dispose it more easily
            line=line.split('\t')
            # if °C in the ninth column, the tempreture must be seperated
            # due to a comma between them
            if('°C' in line[8]):
                line[7]=line[7]+'，'+line[8]
                line.remove(line[8])
                line='\t'.join(line)
            # if there is no °C in the ninth column, the tempreture must
            # be seperated due to a space between them
            else:
                line[7]=line[7]+line[8]
                line.remove(line[8])
                line='\t'.join(line)
        #write the changed line to the new file
        output_f.write(line)
        #read a new line
        line=input_f.readline()
        #count the number of tab in the new line again
        delimiters=line.count('\t')
        #the number of lines add one
        num_of_line+=1
    #close and save the two files
    input_f.close()
    output_f.close()
    #return the number of the lines
    return num_of_line
    

    

if __name__=='__main__':
    doctest.testmod()
    
