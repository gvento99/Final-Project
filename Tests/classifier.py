# File: classifier.py
import string

import Disorders
from Disorders import Anxiety
from Disorders import Depression
from Disorders import OCD
from Disorders import PTSD
from Disorders import BPD

# COPIED (A3) Function that will remove punctuation all punctuation
def remove_punctuation(input_string) :

    out_string = ''

    for character in input_string :
        if not character in string.punctuation :
            out_string = out_string + character
            
    return out_string

# COPIED (A3) Function that will take in input string and create a list of the strings
def prepare_text(input_string) :
    out_list = []

    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()

    return out_list

# ADDED
def altered_find_in_list(list_one, list_two):
    """Finds all of the words in list one that are also in list 2.
    
    Parameters
    ----------
    list_one : list of strings
        The input of the user to check.
    list_two : list of strings
        The list that is being check for overlap with the input.
    
    Returns
    ----------
    answer : list of strings
        The list of words found in both parameters.
    """
    
    myList = []
    
    for element in list_one:
        if element in list_two:
            myList.append(element)
            
    return myList

# ADDED, used to enter program created in other files
def enter_evaluater(input_list) :
    """Enters the program in the other files for diagnosis.
    
    Parameters
    ----------
    input_list : list of strings
        The input of the user to check.
        
    Returns
    ----------
    answer : True or False
        Returns true if input is 'evaluateme' otherwise, returns false.
    """
    
    if 'evaluateme' in input_list :
        return True
    else :
        return False

# ADDED Performs evaluation
def have_psychological_chat():
    # First prep a list of all possible Disorders
    disorder_list = [ Anxiety(), Depression(), OCD(), PTSD(), BPD() ]

    # Prompt user
    print("Hello, welcome to mental health help. \nPlease describe in first person how you've been feeling the past few days / weeks.  \nPlease attempt to use single-word describers and avoid NOT sentences.  \n(i.e instead of saying 'not happy', instead try 'unhappy')")

    # Get a message from the user and format
    msg = input('\nDESCRIPTION :\t')
    msg = prepare_text(msg)

    # Process results, create list of symptoms
    a_list = altered_find_in_list(msg, disorder_list[0].words)
    d_list = altered_find_in_list(msg, disorder_list[1].words)
    o_list = altered_find_in_list(msg, disorder_list[2].words)
    p_list = altered_find_in_list(msg, disorder_list[3].words)
    b_list = altered_find_in_list(msg, disorder_list[4].words)
    users_words = [ a_list, d_list, o_list, p_list, b_list ]

    # Create a list of disorders they qualify for
    users_disorders = []
    i = 0
    for element in disorder_list :
        if len(users_words[i]) >= element.word_cut_off :
            users_disorders.append(element)
        i = i + 1

    # Now for every disorder, ask approriate question and either remove or keep
    confirmed_disorders = []
    print("\nYou will now be prompted for various answers.  \nPlease answer as best as possible with either 'yes' or 'no'.  Any answer not fitting either of these will be interpretted as a no\n")
    for element in users_disorders :
        i = 1
        for sympt in element.symptoms :
            print(sympt)
            response = input('\tANSWER : ')
            response = prepare_text(response)
            print("\n")
            if 'yes' in response :
                element.num_symptoms = element.num_symptoms + 1
            if element.num_symptoms >= element.cut_off :
                confirmed_disorders.append( element )
                break
            elif (element.cut_off - element.num_symptoms) > (len(element.symptoms) - i) :
                break
            i = i + 1

    # At this point confirmed_disorders holds all disorders the user should
    # be notified about, so simply print out reaching
    if len(confirmed_disorders) > 0 :
        # Notify of results
        print("\nAccording to our algorithm, we have decided to notify you of the following...")
        print ( "\tWe have noticed you display some symptoms of: ", end = "" )
        i = 1
        for element in confirmed_disorders :
            if i == 1 and i == len(confirmed_disorders) :
                print( element.name )
            elif i == 1 :
                print( element.name, end = "" )
            elif i == len(confirmed_disorders):
                print( " and ", element.name)
            else :
                print ( ", ", element.name, end = "" )
            i = i + 1
        # Print out the resource they may find helpful
        print("\nRemeber it is always okay to ask for help or see a mental health professional. \nWe think you may find the following links useful...")
        for element in confirmed_disorders :
            print("\n", element.end_message )
    else :
        print("\nAccording to our algorithm, you display little symptoms of any disorder and seem to be in an somewhat healthy mindset.")