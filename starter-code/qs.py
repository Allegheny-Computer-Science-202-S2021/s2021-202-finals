import random
def generate(patients,size):
	'''
        Data is prepared by inserting random values 
        between 1 and 100. Data items may be assumed to 
        be repeated. 
        Please refer to lab spec for the problem definiton.
    '''
	maximum = 100; # maximum patient id of 300
	for i in range(0,size):
		patients.insert(i,random.randint(1,maximum))


def start_sort(data):
	# Add your logic below to sort the list 
	# and store the final output in data.
	# Create a separate method for Partition 
	# use this method for main sorting procedure. 
	pass


data = []
size = int(input("Enter the no of patients:")) # number of patients provided by the user.
generate(data,size)
print(f"unsorted:\t{data}")
# Implement the Quick Sort methods, so as to get the correct results.
start_sort(data)
print(f"sorted:\t\t{data}")

data = []