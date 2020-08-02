#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error_list = []
    for ii in range(len(predictions)):
        error = abs(net_worths[ii] - predictions[ii])
        error_list.append(error)
        
    error_list.sort()
    reduced_error_list = error_list[:int(len(error_list)*0.9)]
    
    for ii in range(len(predictions)):
        error = abs(net_worths[ii] - predictions[ii])
        if error in reduced_error_list:
            cleaned_data.append((ages[ii], net_worths[ii], error))

    
    return cleaned_data

