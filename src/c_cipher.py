'''
    c_cipher.py = encrypts/decrypts a given email by shifting up/down 3
    Class: CSC138-EG
    Created by: Tristan McDevitt
    Created on: 20240926
    Changes:
        20240926 - Added framing comment
        20240917 - Added Documentation comments, Formatted comments
        20241001 - Got rid of literals throughout the code so it would accept any argument.
                   Added more comments and altered docstrings
'''
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email):
    """
    Objective:
        The encrypt method: should receive a String argument and shift each element up 3 ASCII
        if the conditions are met

    Args:
        String email: text String (should be six characters, 3 letters followed by 3 numbers)

    Returns:
        output: input validation message letting the user know the argument was invalid
        retVal: a String with each element shifted up 3 ASCII from the argument   
    """
    output = "" 
    
    #input validation to make sure the email String has a length of 6
    len_flag = len(email) != 6
    
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = not email[:3].isalpha() or not email[3:].isdecimal() 

    if len_flag:                         # NOTE: here we provide input validation on length 
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output     
        
    # TODO: fix line below, process our string into a list
    # Turns the email String into a list where each element is a String of each character
    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]
        
    # TODO: complete line(s) below, convert EACH new element into a string
    # Converts each element into a string of ASCII 3 above what the current element is
    new_ascii = ord(email_lst[0]) + 3    # NOTE: here we extract and update element at 0 
    email_lst[0] = chr(new_ascii)        # NOTE: here we convert our ASCII into string

    new_ascii = ord(email_lst[1]) + 3
    email_lst[1] = chr(new_ascii)

    new_ascii = ord(email_lst[2]) + 3
    email_lst[2] = chr(new_ascii)

    new_ascii = ord(email_lst[3]) + 3
    email_lst[3] = chr(new_ascii)

    new_ascii = ord(email_lst[4]) + 3
    email_lst[4] = chr(new_ascii)

    new_ascii = ord(email_lst[5]) + 3
    email_lst[5] = chr(new_ascii)

    # TODO: fix line below, convert list into a string
    #uses the join function to form a String of all the elements in the email_lst list
    email_str = ''.join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    
    #Declares and initializes the retVal variable with the String within the email_str variable
    retVal = email_str

    #returns the String stored within the retVal variable
    return retVal 

def decrypt(email):
    """
    Objective:
        The decrypt method: Should receive a String argument and shift each element down 3 ASCII
        if the conditions are met 

    Args:
        String email: text String (should be six characters, 3 letters followed by 3 numbers)

    Returns:
        output: input validation message letting the user know the argument was invalid
        retVal: a String with each element shifted up 3 ASCII from the argument 
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 

    # Turns the email String into a list where each element is a String of each character
    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]

    # Converts each element into a string of ASCII 3 below what the current element is
    old_ascii = ord(email_lst[0]) - 3
    email_lst[0] = chr(old_ascii)
    
    old_ascii = ord(email_lst[1]) - 3
    email_lst[0] = chr(old_ascii)
    
    old_ascii = ord(email_lst[2]) - 3
    email_lst[0] = chr(old_ascii)
    
    old_ascii = ord(email_lst[3]) - 3
    email_lst[0] = chr(old_ascii)
    
    old_ascii = ord(email_lst[4]) - 3
    email_lst[0] = chr(old_ascii)
    
    old_ascii = ord(email_lst[5]) - 3
    email_lst[0] = chr(old_ascii)

    email = ''.join(email_lst)
    #     A = email[:3] (check first half)
    #     B = email[3:] (check second half)
    #     enum_flag = A or B
    anum_flag = not email[:3].isalpha() or not email[3:].isdecimal()

    if len_flag:                         # NOTE: here we provide input validation on length
        output = "Length check failed\n"
        output += "Email must be 6 characters long."
        logging.info(output)
        return output        
    if anum_flag:                        # NOTE: here we provide input validation on alpha/num
        output = "alpha num check failed\n"
        output += "Email must have 3 letters followed by 3 digits."
        logging.info(output)
        return output   

    # TODO: apply the encrypt pseudocode but shift down 3
    
    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = email
    #    email_1 = email_str.strip()
    #    retVal = email_1

    #Declares and initializes the retVal variable with the String within the email variable
    retVal = email
    
    #returns the String stored within the retVal variable
    return retVal
