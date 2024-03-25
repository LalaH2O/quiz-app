import random
import time
import requests
import functs
import settings

if __name__ == "__main__":
    filename = 'data.txt'

    #if input('Do you want to search for a name (write 1) or do you already know an id (write 2):') == '1':
    #    print(functs.namesearch_for_ids(input('Search request:')))

    #fuck searching. Just distribute the id!
    
    functs.downloadandload()

    if settings.debug == 1:
        # Print the arrays to verify
        functs.do_things_with_variables()
        print("First parts:", functs.first_send())
        print("Second parts:", functs.second_send())
        print("Third parts:", functs.third_send())
        print("Fourth parts:", functs.fourth_send())

    functs.main(input('Please select a Mode(1:Type the word out, 2:Multiple choice)'))