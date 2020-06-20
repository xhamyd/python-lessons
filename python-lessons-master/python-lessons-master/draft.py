def second_element_sort(tuple_list):
    
    return(sorted(tuple_list, key= lambda x: x[1]))   

print(second_element_sort(((3,2),(4,1))))
