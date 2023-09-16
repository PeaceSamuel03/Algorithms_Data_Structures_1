#Student No.: 121376141
#Student name: Peace Samuel
from random import randint, shuffle, choice
import time, copy

###########SORTING FUNCTIONS##########################
#INSERTION SORT:(from lecture notes)
def insertion_sort(mylist: list,*args):
    n = len(mylist)
    i = 1
    while i < n:
        j = i-1
        while mylist[i] < mylist[j] and j > -1:
            j -= 1
         #insert i in the cell after j
        temp = mylist[i]
        k = i-1
        while k > j:
            mylist[k+1] = mylist[k]
            k -= 1
        mylist[k+1] = temp
        i += 1
    #return the sorted list in order to check
    return mylist


#MERGE SORT: (from lecture notes)
def merge(list1, list2, mylist):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(mylist):
        if f1 == len(list1):
            mylist[f1+f2] = list2[f2]
            f2 += 1
        elif f2 == len(list2):
            mylist[f1+f2] = list1[f1]
            f1 += 1
        elif list2[f2] < list1[f1]:
            mylist[f1+f2] = list2[f2]
            f2 += 1
        else:
            mylist[f1+f2] = list1[f1]
            f1 += 1

def mergesort(mylist,*args):
    n = len(mylist)
    if n > 1:
        list1 = mylist[:n//2]
        list2 = mylist[n//2:]
        mergesort(list1)
        mergesort(list2)
        merge(list1, list2, mylist)
    #return sorted list in order to check
    return mylist

#HEAP SORT:(https://www.programiz.com/dsa/heap-sort)
def heapify(arr: list, n: int, i: int):
      # Find largest among root and children
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
      if l < n and arr[i] < arr[l]:
          largest = l
      if r < n and arr[largest] < arr[r]:
          largest = r
      # If root is not largest, swap with largest and continue heapifying
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def heapSort(arr: list,*args):
    n = len(arr)
    # Build max heap
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify root element
        heapify(arr, i, 0)
    return arr

#QUICK SORT:(https://www.programiz.com/dsa/quick-sort)
def partition(array, low, high):
  #choose last item as pivot
  pivot = array[high]
  #pointer for greater element
  i = low - 1
  #compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high,*args):
  if low < high:
    # find pivot element such that: smaller elements are on the left and greater on the right
    pi = partition(array, low, high)
    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)
    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)
    return array


###########TEST RUNTIME ON SORTING FUNCTIONS############
#RANDOM LIST GENERATOR:
def create_random_list(num:int, k:int) -> list:
    """Creates a list of size num with random integers from 1 to (num-k)"""
    #generate list from 1 to (num-k)
    test_list = []
    for j in range(1,(num-k)+1):
        test_list.append(j)
    #randomly select an int from that list and append it on, k times
    i = 0
    while i < k:
        test_list.append(test_list[randint(0,len(test_list)-1)])
        i += 1
    #shuffle the list
    shuffle(test_list)
    return test_list

#RUNTIME TEST:
def runtime_test(test_list:list, f) -> int:
    """Tests the runtime of a single function, Returns elapsed time"""
    clocktime0 = time.perf_counter()
    size = len(test_list)#needed for calling the quick sort function
    ans = f(test_list,0,size-1)
    clocktime1 = time.perf_counter()
    check_sorted(test_list,f)
    elapsed_time = clocktime1 - clocktime0
    return  elapsed_time

#CHECK IF LIST IS SORTED:
def check_sorted(inlist:list,f):
    """Checks if first parameter is sorted"""
    for i in range(0, len(inlist)):
        #if a list is sorted all numbers will be bigger than all previous numbers, opposite true for unsorted list.
        #index of -1 is the last numer in a python list!
        if inlist[i] < inlist[i-1] and (i-1)!= -1:
            print("list not sorted")
            print("number:",inlist[i], "index:",i,"number:",inlist[i-1], "index:",i-1)
            print("function:",f.__name__)
            break

#EVALUATING ON MULTIPLE LISTS:
def evaluate(n:int, k:int, num:int, f):
    """Evaluates sorting algorithms using multiples of the input list"""
    #create a random list using the function
    test_list = create_random_list(n, k)
    #create a list with multiples of the same shuffled list
    evaluation = []
    for i in range(1, num):
        i = copy.deepcopy(test_list)
        shuffle(i)
        evaluation.append(i)
    #find the average runtime
    sum = 0
    for list in evaluation:
        time = runtime_test(list,f)
        sum += time
    average = sum / len(evaluation)
    print("average runtime:", average,"function:",f.__name__,n,k)


#EVALUATING MULTIPLE FUNCTIONS:
def evaluateall(n:int, k:int, num:int, funcs:list):
    #create a random list
    test_list = create_random_list(n, k)
    #create a list that contains multiples of the same shuffled list
    evaluation = []
    for i in range(0, num):
        i = copy.deepcopy(test_list)
        shuffle(i)
        evaluation.append(i)
    #test each function and find the average
    for f in funcs:
        copy_list = copy.deepcopy(evaluation)
        if (f == insertion_sort) and n >= 5000:
               print("list too long for insertion sort")
               break
        sum = 0
        for list in copy_list:
            time = runtime_test(list,f)
            sum += time
        average = sum / len(copy_list)
        print("Sorting Function:",f.__name__,"\nAverage runtime:", average, "n:",n ,"k:", k,"\n")


#EVALUATING USING PARTIALLY SORTED LISTS:
def evaluateallpartial(n:int,k:int,d:int,num:int,funcs):
    """Evaluates sorting algorithms on partially sorted lists"""
    #generate a random list
    test_list = create_random_list(n, k)
    #sort the generated list
    test_list.sort()
    #create a list of  multiples of the list, partially sorted
    evaluation = []
    for i in range(0, num):
        i = copy.deepcopy(test_list)
        for p in range(1, n//d):
            index1 =  choice(range(0,len(i)))
            index2 = choice(range(0, len(i)))
            i[index1], i[index2] = i[index2], i[index1]
        evaluation.append(i)
    #test these partially sorted lists on each sorting function
    for f in funcs:
        copy_list = copy.deepcopy(evaluation)
        if (f == insertion_sort) and n >= 5000:
            print("List too long to run insertion sort")
            continue
        #find the average runtime for each function
        sum = 0
        for list in copy_list:
            time = runtime_test(list, f)
            sum += time
        average = sum / len(copy_list)
        print("Sorting Function:",f.__name__,"\nAverage runtime:", average, "n:",n ,"k:", k,"\n") 

#EVALUATE SCALE
def evalautescale():
    parameters = [(100, 20),
                  (1000, 200),
                  (10000, 2000)]
    functions = [quickSort, mergesort, heapSort, insertion_sort]
    for (n,k) in parameters:
        #UNCOMMENT TO RUN!!!!!(regular and unsorted)
        evaluateall(n,k,20,functions)
        #evaluateallpartial(n,k,50,20,functions)

#evalautescale()

                         

