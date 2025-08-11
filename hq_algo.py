#!/usr/bin/env python
# coding: utf-8

# In[6]:


def first_code(current_temp):
    #----TYPE D'ACCUMULATION
    
    if (current_temp >= -3) and (current_temp < 5):
        #-- VERGLAS
        new_code = 10
        
    elif (current_temp >= -6) and (current_temp < -3):
        #-- FORTE PROBABILITE DE VERGLAS
        new_code = 12
        
    elif (current_temp >= -9) and (current_temp < -6):
        #-- FORTE PROBABILITE DE GIVRE
        new_code = 21
        
    elif (current_temp >= -45) and (current_temp < -9):
        #-- GIVRE
        new_code = 20
    
    return new_code

def scenario1(current_temp):
    #---- SI LE DERNIER TYPE D'ACCUMULATION EST :
    #---- > DU VERGLAS
    
    if (current_temp >= -6) and (current_temp < 5):
        #-- VERGLAS
        new_code = 10
        
    elif (current_temp >= -9) and (current_temp < -6):
        #-- FORTE PROBABILITE DE GIVRE
        new_code = 21
        
    elif (current_temp >= -45) and (current_temp < -9):
        #-- GIVRE
        new_code = 20
    
    return new_code

def scenario2(current_temp):
    #---- SI LE DERNIER TYPE D'ACCUMULATION EST:
    #---- > FORT PROBABLEMENT DU VERGLAS
    
    if (current_temp >= -9) and (current_temp < 5):
        #-- FORTE PROBABILITE DE VERGLAS
        new_code = 12
        
    elif (current_temp >= -45) and (current_temp < -6):
        #-- GIVRE
        new_code = 20
        
    return new_code

def scenario3(current_temp):
    #---- SI LE DERNIER TYPE D'ACCUMULATION EST:
    #---- > FORT PROBABLEMENT DU GIVRE
    
    if (current_temp >= -6) and (current_temp < 5):
        #-- VERGLAS
        new_code = 10
        
    elif (current_temp >= -45) and (current_temp < -6):
        #-- FORTE PROBABILITE DE GIVRE
        new_code = 21
        
    return new_code

def scenario4(current_temp):
    #---- SI LE DERNIER TYPE D'ACCUMULATION EST:
    #---- > DU GIVRE
    
    if (current_temp >= -3) and (current_temp < 5):
        #-- VERGLAS
        new_code = 10
        
    elif (current_temp >= -6) and (current_temp < -3):
        #-- FORTE PROBABILITE DE VERGLAS
        new_code = 12
        
    elif (current_temp >= -45) and (current_temp < -6):
        #-- GIVRE
        new_code = 20
        
    return new_code

def raj(last_code, current_temp):
    masses = {10:23,12:20,21:13,20:9} #code : m [g/m]
    
    #scenario 1
    if last_code == 10:
        new_code = scenario1(current_temp)
        
    #scenario 2  
    elif last_code == 12:
        new_code = scenario2(current_temp)
    
    #scenario 3
    elif last_code == 21:
        new_code = scenario3(current_temp)
        
    #scenario 4  
    elif last_code == 20:
        new_code = scenario4(current_temp)
      
    
    return new_code, masses[new_code] /1000 #kg/m


    

