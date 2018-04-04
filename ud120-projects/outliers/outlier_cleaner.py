#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    error=[]
    cleaned_data = []
    for i in range(0,len(predictions)):
        error.append(net_worths[i]-predictions[i])
        cleaned_data.append((ages[i],net_worths[i],error[i]))
    errabs=map(abs,error)
    for _ in range(0,int(0.1*len(error))):
        pop_index=errabs.index(max(errabs))
        errabs.pop(pop_index)
        cleaned_data.pop(pop_index)


    ### your code goes here

    
    return cleaned_data

