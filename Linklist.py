class Node:
    def __init__(self,data=None, next=None): 
    #__init__ fucntion is used to intialzie/assign value to the class object instance created ,
    #just like methods in java 
        self.data=data
        self.next=next

class linklist: # Linklists class is created, in which we will initilaize head, and all the neceassasry functions.

    ################################################
    ##intialization like java constructors
    def __init__(self):
        self.head=None

    ################################################
    ####nserting at the begning of the linklist
    def insert_beg(self,data):
        node_variable=Node(data,self.head)
        self.head=node_variable


    ################################################
    ####inserting at the end:
    def insert_end(self,data):
        ##checking if head is empty/None
        if self.head is None:
            self.head=Node(data, None)
            return

        ###Linklist is not empty
        ### we have to iterate through the list and find the last element and add the New Node
        temp=self.head
        while(temp.next):
            temp=temp.next

        temp.next=Node(data,None)   
    ################################################
    ### This function is used to insert a List data elements in the linklist

    def insert_elements(self,list_of_data):
        #First we make the head of the previous linklist made NUll/None
        self.head=None

        ### Then we loop through each element in the list and then add using insert_at_end function
        for i in list_of_data:
            self.insert_end(i)
        
    ################################################
    ### Finding lenght of the linklist
    def lenght(self):
        if self.head is None:
            print("List is empty")

        temp=self.head    
        count=0
        while(temp):
            count=count+1
            temp=temp.next

        print("Length of the List is ",count)
        print("")
         
     ## deleting/removing element from specified index
     ################################################
    def remove_at_index(self,index):


        ## check index is out of bounds or not
        if index<0:
            raise Exception(" Ivalid Input")
        

        ## check we are removing the head/first element
        if index==0:
            self.head=self.head.next 
            return 
            
        count=0
        temp=self.head
        pre_temp=None
        while(count<index):
            count=count+1
            pre_temp=temp
            temp=temp.next

        pre_temp.next=temp.next
        print("element removed is ",temp.data,"at index ",index)  

    ###############################################
    ## inserting at a specific index
    def insert_at_index(self,data,index):
        #check if we are inserting at first element 
        if index==0:
            node=Node(data,self.head)
            self.head=node
        else:
        ####inserting at any other positon  
            count=0
            temp=self.head
            while(count<index-1):
                count=count+1
                temp=temp.next

            print("element inserted at index", index)
            node=Node(data,None)
            node.next=temp.next
            temp.next=node   

  
    ################################################
    ## deleting element by call by value by first occurance in the list 
    def remove_element(self,data):
        ###Finding the element at the head 
        if self.head.data==data:
            print("element deleted is ",self.head.data)  
            self.head=self.head.next
        #### Finding element other than head 
        temp=self.head
        prev=None

        while(temp.data!=data):
            prev=temp
            temp=temp.next 

        prev.next=temp.next
        print("element removed by value is ",temp.data)
               






    ################################################
    def printing(self):

            ### For Empty list
            if self.head==None:
                print("Linklist is empty")
        
            temp=self.head
            empty_string=""
            while(temp):
                # This loop print elements till the last node till none is not found unline in "C" Langauge.
                #print(temp.data,"--->")
                empty_string=empty_string+temp.data+"-->"
                #print(" --->")
                #print("\|/")
                #print(" .")
                temp=temp.next
            #after while loop if we print temp it will get an error of object not found
            print(empty_string)  


Single_linklist=linklist()
#Firstlinklist.head=Node(1)
#second=Node(2)
#third=Node(3)
#Firstlinklist.head.next=second
#second.next=third

##nserting functions
Single_linklist.insert_beg(10)
Single_linklist.insert_beg(11)
Single_linklist.insert_end(13)
Single_linklist.insert_end(100)

 

#mtaking a list and making it a linklist 
dd=["pumpkins","oranges","mangoes","apples","Niti","Mohit","Patil","perfect","will be together"]
Single_linklist.insert_elements(dd)
print()
Single_linklist.lenght()
### Printing
Single_linklist.printing()
print()
print("######################")

##inserting at index 
print("inserting at the index : ")
Single_linklist.insert_at_index("world",2)
### Printing
Single_linklist.printing()
print()
print("######################")


## removing element at given index
Single_linklist.remove_at_index(3)
### Printing
Single_linklist.printing()
print()
print("######################")


##removing element by given value
Single_linklist.remove_element("perfect")
### Printing
Single_linklist.printing()

















