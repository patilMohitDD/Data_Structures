class Node:
    def __init__(self,data=None,prev=None,next=None): 
    #__init__ fucntion is used to intialzie/assign value to the class object instance created ,
    #just like methods in java 
        self.prev=prev
        self.data=data
        self.next=next


class Double_Linklist: # Linklists class is created, in which we will initilaize head, and all the neceassasry functions.   
    def __init__(self):
        self.head=None


    #####inserting element at the start 
    def insert_at_start(self,data):
        ### if the list is empty 
        if self.head is None:
            head=Node(data,None,None)
        else:
            node=Node(data,None,None)
            #self.head.prev=node
            node.next=self.head
            self.head=node
    ##### inserting element at the end 
    def insert_at_end(self,data):
        ### if the list is empty 
        if self.head is None:
            head=Node(data,None,None)
        else:
            temp=self.head
            while temp.next is not  None :
                temp=temp.next
            node=Node(data,temp,None)
            temp.next=node


    ###### inserting elements of the list in linklist
    def inserting_values(self,list_of_data):
        ####making head null which was used earlier
        for i in list_of_data:
            self.insert_at_end(i)

    
    ##### deleting element at given index 
    def deleting_at_index(self,index):
        if index<0:
            print("Index out of bounds")

        temp=self.head
        prev=None
        count=0
        while(count<index-1):
            count=count+1
            prev=temp
            temp=temp.next

        prev.next=temp.next
        print("element deleted is ",temp.data,"at index ",index)      

    
    ##### deleting element of given value 
    def deleting_by_value(self,value):
        #### check for empty list
        if self.head is None:
            print("Linklist is empty")

        temp=self.head
        prev=None

        while(temp.data!=value):
            prev=temp
            temp=temp.next

        prev.next=temp.next 
        print("element deleted is ",temp.data," by value ")       


    ##### getting the length of the list
    def lenght(self):
        if self.head is None:
            print("List is empty")

        temp=self.head    
        count=0
        while(temp):
            count=count+1
            temp=temp.next

        print("Length of the List is ",count)
        print()



    #### Printing the linklist by it in a string variable
    def printing(self):

            ### For Empty list
            if self.head==None:
                print("Linklist is empty")
            ##############
            temp=self.head
            empty_string=""

            while(temp):
                # This loop print elements till the last node till none is not found unline in "C" Langauge.
                #print(temp.data,"--->")
                empty_string=empty_string+str(temp.data)+"-->"
                temp=temp.next

            #after while loop if we print temp it will get an error of object not found
            print(empty_string) 

       # print(Empty_string)    


    
    #### Printing the linklist in reverse order without using another list data type for it 
    def printing_reverse(self):
        print("entered the function ")

        ### For Empty list
        if self.head==None:
            print("Linklist is empty")

        temp=self.head
        previous=None
        empty_string=""
        while(temp):
            previous=temp
            temp=temp.next

       # print(previous.data)
    

        while(previous):
            print(previous.data)
            #empty_string=empty_string+str(previous.data)+"-->"
            previous=previous.prev 

        #print(empty_string,"-->",self.head.data)     

          



###### simple implementation 
double_linklist=Double_Linklist()
double_linklist.head=Node(1)


dd=["apples","Niti","Mohit","Patil","perfect","will be together"]


####insert at the start 
double_linklist.insert_at_start("start")
double_linklist.insert_at_start("right")
double_linklist.printing()
print()
######insert at the end 
double_linklist.insert_at_end("end")
double_linklist.insert_at_end("end_2")
double_linklist.printing()
print()
#####inserting the list values
double_linklist.inserting_values(dd)
double_linklist.printing()
double_linklist.lenght()

#### removing element at given index
double_linklist.deleting_at_index(3)
double_linklist.printing()
print()

#### removing element at given value
double_linklist.deleting_by_value("end")
double_linklist.printing()
print()

#### printing list in forward direction 
double_linklist.printing_reverse()
print()








#####printing the list 
#double_linklist.printing()




