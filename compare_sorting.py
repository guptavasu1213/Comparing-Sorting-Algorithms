'''
->The main purpose of this program is to test the different sorting algorithms. They are tested by determining the time taken for 
      each algorithm to sort the given array, the number of array accesses made and the use of extra memory by creating more arrays.
->We DO NOT use lists in this lab. We use ctype arrays to implement the algorithms.
->This program prompts the user to choose the sorting algorithm from the menu they want to use to sort the numbers. 
->The user is also prompted to enter the number upto which the values will be sorted. Eg: If the user inputs n,
      then we will have values from 1...n in the array to be sorted. 
'''
import ctypes
import random
import time
        
#This class sorts the given array using Selection sort algorithm; also counts the number of recursive calls and array accesses
class SelectionSort:
        #Constructor for the class
        def __init__(this, array):
                this.array = array
                this.array_accesses = 0 
                this.extra_memory = 0    #No extra memory consumed      
                this.recursive_calls = 0 #No recursive calls made
                this.selectionsort() #Method in the class is called
        #In this method, the sorting algorithm is implemented   
        def selectionsort(this):
                for i in range(len(this.array)-1,0,-1):
                        max_position = 0
                        for location in range(1,i+1):
                                this.array_accesses += 2 #For the if statement
                                if this.array[location] > this.array[max_position]:
                                        max_position  = location
                        #Swapping
                        temp = this.array[i]
                        this.array[i] = this.array[max_position]
                        this.array[max_position] = temp
                        this.array_accesses += 4 #For the previous 3 lines 
                return this.array

#This class sorts the given array using Quick sort algorithm; also counts the number of recursive calls and array accesses
class QuickSort():
        #Constructor of the class instantiates the member variables
        def __init__(this,array, start, end):
                this.array = array
                this.extra_memory = 0                  #This sorting mechanism does not use extra memory for arrays
                this.array_accesses = 0                #Counts the array accesses
                this.recursive_calls = -1               #Counts the recursive calls             
                this.quick_sort(array,start, end)    
        #Sorting happens within this method
        def quick_sort(this, array, start, end):
                this.recursive_calls += 1
                if start < end:
                        pivot = this.partition(array,start,end)
                        this.quick_sort(array ,start   ,pivot-1)
                        this.quick_sort(array ,pivot+1 ,end    )
        #Making partition using the this method
        def partition(this, array, first, last):
                big = first + 1 
                small = last
                pivot = array[first] ; this.array_accesses += 1
                while (big <= small) :
                        while (big <= last and array[big] <= pivot) :
                                this.array_accesses += 1
                                big += 1
                        while array[small] > pivot :
                                this.array_accesses += 1
                                small -= 1
                        if big < small :
                                #Swapping
                                temp1 = array[small]
                                array[small] = array[big]
                                array[big] = temp1
                                this.array_accesses += 4                                
                #Swapping 
                temp2 = array[first]
                array[first] = array[small]
                array[small] = temp2
                this.array_accesses += 4                
                return small

#This class sorts the given array using Merge sort algorithm; also calculates the extra memory used, the number of recursive calls and array accesses
class MergeSort():
        #Constructor of the class
        def __init__(this, array, array_accesses=0):
                this.array = array
                this.extra_memory = 0
                this.array_accesses = 0
                this.recursive_calls = -1 #Starting from -1 to zero the variable out when we go through mergesort()
                this.array = MergeSort.mergesort(this, array) #The array gets modified after sorting
                
        #Sorting mechanism happens within this method
        def mergesort(this, array):
                this.recursive_calls += 1
                n = len(array)
                #One element left, return back
                if n <= 1:
                        return array
                
                #Temporary left
                #Creating Ctype array for the elements on the left half
                left_array = (n//2 * ctypes.py_object)()
                this.extra_memory += n//2  
                for index in range(n//2):
                        left_array[index] = array[index] 
                        this.array_accesses += 2
                        
                #Temporary Right
                #Creating Ctype array for the elements on the right half                
                this.extra_memory += n-(n//2)                
                right_array = ((n-(n//2)) * ctypes.py_object)()
                for index in range(n//2, n):
                        right_array[index-(n//2)] = array[index]       
                        this.array_accesses += 2
                        
                list1 = MergeSort.mergesort(this, left_array)
                list2 = MergeSort.mergesort(this, right_array)
                array = MergeSort.merge(this, list1, list2)
                return array
        
        #The arrays get combined in this method
        def merge(this, l1,l2):
                #Creating a final array to display all the values
                this.extra_memory += len(l1)+len(l2)
                final_array = ((len(l1)+len(l2) ) * ctypes.py_object)()
                
                ind=0
                i=0
                j=0
                while i<len(l1)  and j<len(l2):
                        this.array_accesses += 2 #For the if statement
                        if l1[i] < l2[j]:
                                final_array[ind]=l1[i] 
                                this.array_accesses += 2 #For the previous statement
                                i+=1
                                ind+=1
                        else: 
                                final_array[ind]=l2[j]
                                this.array_accesses += 2 #For the previous statement                                
                                j+=1
                                ind+=1         
                while( i < len(l1)):  
                        final_array[ind]=l1[i] 
                        this.array_accesses += 2 #For the previous statement                        
                        i+=1
                        ind+=1        
                while (j < len(l2)): 
                        final_array[ind]=l2[j] 
                        this.array_accesses += 2 #For the previous statement                        
                        j+=1
                        ind+=1	
                return final_array
        
#This class sorts the given array using Heap sort algorithm; also counts the number of recursive calls and array accesses
class HeapSort:
        def __init__(this, array):
                this.array = array 
                this.extra_memory = 0 #This sorting mechanism does not use extra memory
                this.recursive_calls = 0              
                this.array_accesses = 0 
                this._size=len(this.array)
                
                #Creating a heap
                i=(this._size-2)//2
                while i>=0:
                        this.max_heap(i)
                        i-=1
                this.heapSort() #Method in the class is called
        
                        
        # Inserts the largest element 
        def max_heap(this,index):
                largest=index
                left=2*index+1
                right=2*index+2
                
                this.array_accesses += 2 #For the if statement
                if left < this._size and this.array[left] > this.array[largest]:
                        largest=left
                this.array_accesses += 2 #For the if statement
                if right < this._size and this.array[right] >this.array[largest]:
                        largest=right
                if not largest==index:
                        #Swapping
                        temp = this.array[largest]
                        this.array[largest] = this.array[index]
                        this.array[index] = temp
                        this.array_accesses += 4 #For the above 3 steps
                        
                        this.recursive_calls += 1     #Keeps track of the recursive calls                                
                        this.max_heap(largest)
        #Performs the sorting mechanism
        def heapSort(this):
                while this._size >1:
                        #Swapping
                        temp = this.array[0]
                        this.array[0] = this.array[this._size-1]
                        this.array[this._size-1] = temp
                        #For the above 3 steps
                        this.array_accesses += 4
                        
                        this._size-=1
                        this.max_heap(0)
                return this.array

#This function creates a cType array using the given number of elements by the user
def create_array(given_array_size):
        numbers_in_array = (given_array_size * ctypes.py_object)() # Defining the size of array
        for value in range(1, given_array_size+1):                 # Not including Zero
                numbers_in_array[value-1] = value                  # Adding the Values in the array
        return numbers_in_array

#This function shuffles the elements in the array (random.shuffle() not used)  
def shuffle_array(array):
        for element in range(len(array)-1,0,-1):
                random_index = random.randint(0, element)
                #Swapping the element at that position with the random value index element
                temp = array[element]
                
                array[element] = array[random_index] 
                array[random_index] = temp 
        return array

#Prompts the user for the sorting algorithm they want to perform
#Prompts the user for a value upto which you want the numbers to be
#Creates a ctype array from 1...n and then shuffles it
#Performs the sorting mechanism by the user requested algorithm
#Displays the unsorted and the sorted array, time taken to perform the algorithm, the number of array accesses and the extra memory taken for the algorithm
def main():
        while True:
                print("1: Merge Sort\n"
                      "2: Heap Sort\n"
                      "3: Quick Sort\n"
                      "4: Selection Sort\n"
                      "5: Exit\n")
                try:
                        user_input = int(input("Enter your choice:\t"))
                        if user_input < 1 or user_input > 5: #For choosing the algorithm
                                print("\nInvalid input. Try Again!\n\n") 
                                continue                        
                        array_size = int(input("Enter the number of elements in the Array:\t")) #For creating the ctype array                       
                except:
                        print("\nInvalid input. Try again!\n\n")
                        continue
                
                unsorted_array = create_array(array_size) #Creating a ctype array of the given size
                shuffle_array(unsorted_array) #Shuffling the created array

                print("Array Before Sorting:")
                for i in range(0, array_size):
                        print(unsorted_array[i], end = ", " if i != array_size-1 else "\n\n")                    
                                
                starting_time = time.time() #Capturing the time before performing the algorithm
                #Merge sort
                if user_input == 1:
                        print("***Merge Sort***")
                        recursive_calls = 0 
                        sorted_array = MergeSort(unsorted_array, 0)
                        #sorted_array.mergesort()
                #Heap sort
                elif user_input == 2:
                        print("***Heap Sort***")                        
                        sorted_array = HeapSort(unsorted_array)                        
                #Quick sort        
                elif user_input == 3:
                        print("***Quick Sort***")                  
                        sorted_array = QuickSort(unsorted_array,0,len(unsorted_array)-1)
                #Selection sort        
                elif user_input == 4: 
                        sorted_array = SelectionSort(unsorted_array)
                #Exit
                elif user_input == 5:
                        print("\nExiting program...\n")
                        exit()
                #Elapsed     = End - Start
                elapsed_time = time.time() - starting_time  #The time elapsed in performing the algorithm
                
                print("Array After Sorting:")
                for i in range(0, array_size):
                        print(sorted_array.array[i], end = ", " if i != array_size-1 else "\n\n")                                    
                print("Elapsed Time:\t\t\t\t\t\t\t", elapsed_time, "seconds")
                print("Numbers of array accesses:\t\t\t\t\t"+str(sorted_array.array_accesses))
                print("Number of extra memory space occupied:\t\t"+str(sorted_array.extra_memory))
                print("Number of recursive calls:\t\t\t\t\t"+str(sorted_array.recursive_calls),end="\n\n\n")
                
main()
