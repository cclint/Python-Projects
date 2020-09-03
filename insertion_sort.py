"""
Clinton Campbell
9/02/2020
Algorithms & Data Structures
Lab 02: Insertion Sort

"""
# ===================== imports ======================
import time
from operator import itemgetter
# ====================================================


def fileReader(text):
    file = open(text) 
    content = file.read() # returns file content as a string and stores in 'content'
    array = content.split()
    array = list(map(int, array)) # converts the list of strings to a list of ints
    file.close()
    return array


def insertionSort(array):
    for j in range(2,len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i] # element array[i] essentially moves up one
            i -= 1
        array[i + 1] = key
    return array


def run(): # run() will return "output", a list that contains the runtime floasts for each test. The elements are in order of the tests (ascending order)   
    sort = []
    test1 = (insertionSort(fileReader("input_1000.txt")), time.time() - start_time)
    test2 = (insertionSort(fileReader("input_5000.txt")), time.time() - start_time)
    test3 = (insertionSort(fileReader("input_10000.txt")), time.time() - start_time)
    test4 = (insertionSort(fileReader("input_50000.txt")), time.time() - start_time)
    test5 = (insertionSort(fileReader("input_100000.txt")), time.time() - start_time)
    test6 = (insertionSort(fileReader("input_500000.txt")), time.time() - start_time) # WARNING: THIS COMPUTATION WILL TAKE ABOUT 2.5 HOURS. PLEASE COMMENT THIS OUT AND REMOVE "test6" FROM THE ARRAY IF YOU WISH TO SEE A PROOF OF CONCEPT
    sort.extend([test1,test2,test3,test4,test5,test6]) # extend() appends multiple items to a list, in this case I'm appending each test case as tuples. First value holding the array and second holding the runtime for the analogous array
    output = list(map(itemgetter(1), sort)) # map() maps all the elements and itemgetter() returns the desired element, in this case it's the second element (index 1) in the tuple
    return output


def main():
    print(run())
   
    
if __name__ == "__main__":
    start_time = time.time()
    main()  
    #print(time.time() - start_time)

    # 1,000: 0.0246860980988
    # 5,000: 0.546637058258
    # 10,000: 2.49005117416
    # 50,000: 56.1582579613
    # 100,000: 253.512299061
    # 500,000 @: 7810.55437112
    
    # Time complexity 
    # worse case is n^2 (quadratic)
    # best case is n (linear) 