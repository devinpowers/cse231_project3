#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:28:46 2020

@author: devinpowers
"""




#variable contorl loop value,
starting = 0

while starting == 0:
    
    print("\n2019 MSU Undergraduate Tuition Calculator.\n")    
    
    resident = ''
    international_student = ''   
    non_resident = ''   
    grade_level = ''  #freshman, sophmore, junior or senior   
    college = '' #engineeron+ business + heath + ...
    credits_enrolled = 0   
    tuition = 0
    special_fees = 0 
    student_voted_taxes = 0
    
    
        
    resident = input("Are you a resident? (Yes or No): ").lower()

    if resident == 'yes':
        resident = True
        international_student = None
        non_resident = None
    
    else:
        international_question = input("Are you an International Student? (Yes or No): ").lower()
        
        if international_question == 'yes':   
            international_student = True 
            resident = None
            non_resident = None
        else: #must not be international so out-of-state resident
            non_resident = True
            resident = None
            international_student = None
            
    
    while True: #while True so it keeps looping asking for "correct grade level"
        
        grade_level = input("Enter Level as freshman, sophomore, junior, senior: ").lower()

        if grade_level == 'freshman' or grade_level == 'sophomore' or grade_level == 'junior' or grade_level == 'senior':
            break #exit loop since correct grade level value was entered
        else:
            print("invalid input. Try Again. ") #entered wrong grade level/ spelled wrong, will continue to loop
            
    
    # grade level junior or senior ask for college
    
    if grade_level == 'junior' or grade_level == 'senior':
        
        college = input("Enter college as business, engineering, health, science, or none: ").lower() 
        if college == 'none':
            college = None
        
        cmse = input("Is your major CMSE (Computational Mathematics and Engineering? (yes/no): ").lower()
        if cmse == 'yes':
            college = 'CMSE'
        
    #grade level freshman or sophmore
    if grade_level == 'freshman' or grade_level == 'sophomore':
        college_of_engineering = input("Are you admitted into the college of Engineering? (Yes or No) ").lower()
        if college_of_engineering == 'yes':
            college = 'engineering'
        else:
            college = None
    
    # James Madison 
    if college != 'business' and college != 'engineering' and college != 'health' and college != 'science':
        ask_james_madison = input("Are you in James Madison College? (yes/no) ").lower()
        
        if ask_james_madison == 'yes':
            college = "James Madison"
    
    #number of Credits with a while loop to make sure its a positive int!
    
    while True:
        credits_enrolled = input("How many credits are you taking? ")
        
        if credits_enrolled.isdigit() == True and credits_enrolled != '0':
            credits_enrolled = int(credits_enrolled)
            break # found correct input    
        else:
            print("Invalid input. Try again. ") # entered a non positive int, loop again!
        
    
    
    """ Tuition Calculation """
    
    """ Resident student tuition calculation """
    
    if resident == True:
    
    
        if grade_level == 'freshman':
            if credits_enrolled <= 11:
                tuition = 482*credits_enrolled
            elif 12 <= credits_enrolled < 18: #flat rate
                tuition = 7230
            else: #taking more than 18 credits
                tuition = 7230 + 482*(credits_enrolled-18)
    
        if grade_level == 'sophomore':
            if credits_enrolled <= 11:
                tuition = 494*credits_enrolled
            elif 12 <= credits_enrolled < 18: #flat rate
                tuition = 7410
            else: #taking more than 18 credits
                tuition = 7410 + 494*(credits_enrolled-18)
            
    
        if (grade_level == 'junior') or (grade_level == 'senior'):
        
            if (college == 'business') or (college == 'engineering'):
                if credits_enrolled <= 11:
                    tuition = 573*credits_enrolled   
                elif 12 <= credits_enrolled < 18: #flat rate
                    tuition = 8595
                else: #taking more than 18 credits
                    tuition = 8595 + 573*(credits_enrolled-18)
            
            # in any other college
            else:
                if credits_enrolled <= 11:
                    tuition = 555*credits_enrolled
                elif 12 <= credits_enrolled <18:
                    tuition = 8325
                else:
                    tuition = 8325 + 555*(credits_enrolled-18)
                
   # Must be international or non-resident
    else:
          
        if (grade_level == 'freshman') or (grade_level == 'sophomore'):
            
            if credits_enrolled <= 11:
                tuition = 1325.50*credits_enrolled
            elif 12 <= credits_enrolled < 18: #flat rate
                tuition = 19883
            else: #taking more than 18 credits
                tuition = 19883 + 1325.5*(credits_enrolled-18)
            
        if (grade_level == 'junior') or (grade_level == 'senior'):
        
            if (college == 'business') or (college == 'engineering'):
                if credits_enrolled <= 11:
                    tuition = 1385.75*credits_enrolled   
                elif 12 <= credits_enrolled < 18: #flat rate
                    tuition = 20786
                else: #taking more than 18 credits
                    tuition = 20786 + 1385.75*(credits_enrolled-18)
        
            else: # non-resident, junior or senior thats not in engineering or business colleges
                if credits_enrolled <= 11:
                    tuition = 1366.75*credits_enrolled
                elif 12 <= credits_enrolled <18:
                   tuition = 20501
                else:
                    tuition = 20501 + 1366.75*(credits_enrolled-18)
                
    
        
    """ Special Fees """
    
    #Part Time
    if credits_enrolled <= 4:
        
        if (grade_level == 'junior') or (grade_level == 'senior'):
            
            if college == 'business':
                special_fees += 133
            if college == 'health':
                special_fees += 50
            if college == 'science':
                special_fees += 50
            if college == 'CMSE':
                special_fees += 402
                
        if college == 'engineering':
            special_fees += 402
            
        if international_student == True:
            special_fees += 375
     
    if credits_enrolled > 4:
        
        
        if (grade_level == 'junior') or (grade_level == 'senior'):
            
            if college == 'business':
                special_fees += 226
            if college == 'health':
                special_fees += 100
            if college == 'science':
                special_fees += 100
            if college == 'CMSE':
                special_fees += 670
                
        if college == 'engineering':
            special_fees += 670
            
        if international_student == True:
            special_fees += 750
    
        
    """ Student- Voted Taxes """
    # ASMSU Tax
    student_voted_taxes += 21
    #FM radio tax
    student_voted_taxes += 3
    
    #State News Taxes
    
    if credits_enrolled >= 6:
        student_voted_taxes += 5
    
    #James Madison taxes
    if college == 'James Madison':
        student_voted_taxes += 7.50
        
    total_tuition_cost = (tuition + special_fees + student_voted_taxes)
        

    
    print('Resident', resident)
    print('international student', international_student)
    print('non resident', non_resident)
    print("grade level", grade_level)
    print("college", college)
    print("credits:", credits_enrolled)
    print("Tuition is: $", format(total_tuition_cost, ",.2f"))
    
    
    
    
    another_calc = input("Would you like to perform another calculation? (yes/no) ").lower()
    
    if another_calc == 'yes':   
        starting = 0
    else:
        print("Thank You.... Exiting")
        starting = 1
    
    
            
        
      
    
        
        
       
    
    
    