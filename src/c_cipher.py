'''
    c_cipher.py = encrypts/decrypts a given email by shifting up/down 3
    Class: CSC138-EG
    Created by: Tristan McDevitt
    Created on: 20240926
    Changes:
        20240926 - Added framing comment
        20240917 - Added Documentation comments, Formatted comments
'''
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def encrypt(email):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    output = "" 
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
    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]
        
    # TODO: complete line(s) below, convert EACH new element into a string
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
    email_str = ''.join(email_lst)

    # keep all updates in the retVal (str) variablei
    # i.e.,
    #    email_str = " some string updates here "
    #    email_1 = email_str.strip()
    #    retVal = email_1
    retVal = email_str
    return retVal 

def decrypt(email="def345"):
    """
    TODO: What is the objective? 

    Args:
        TODO: what arguments and data types are expected? (i.e., email)

    Returns:
        TODO: what varibale and data types are being returned?   
    """
    # input validation
    output = "" 
    len_flag = len(email) != 6
    # TODO: fix line below and, implement functionality rather than literals
    # keep all updates in the anum_flag (bool) variable
    # i.e., 

    email_lst = [email[0], email[1], email[2], email[3], email[4], email[5]]
    
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
    retVal = "aef345"
    return retVal
