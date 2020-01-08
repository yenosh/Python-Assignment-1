#!/usr/bin/env python
# coding: utf-8

# # Task 1:
# ## 1.1 Write a Python Program to implement your own myreduce() function which works exactly like
# ## Python's built-in function reduce()¶

# In[1]:


def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result


# In[2]:


lst =[1,2,3,4,5,6]
print(myreduce(lambda x,y: x+y, lst))


# In[ ]:





# # # 1.2
# ### Write a Python program to implement your own myfilter() function which works exactly like
# ### Python's built-in function filter()

# In[3]:



# Custom filter function 
def myfilter(anyfunc, sequence):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in sequence:
  if anyfunc(item):
   result.append(item)

 # return funal output
 return result


# In[4]:



seq = [0, 1, 2, 3, 5, 8, 13]
result = myfilter(lambda x: x % 2, seq)
print(list(result))


# In[ ]:





# ### 2. Implement List comprehensions to produce the following lists.
# ### Write List comprehensions to produce the following Lists
# ####  ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# #### ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# #### ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# #### [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# #### [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# #### [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[5]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))


# In[6]:


input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


# In[7]:


input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))


# In[8]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


# In[9]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


# In[10]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# In[ ]:





# ### 3. Implement a function longestWord() that takes a list of words and returns the longest one.¶

# In[11]:


def longestWord(words_list):  
    word_len = []  
    for n in words_list:  
        word_len.append((len(n), n))  
    word_len.sort()  
    return word_len[-1][1]  
  
print(longestWord(["Mani", "Rajesh", "Bapi","Ashutosh","YenoshKumar"]))


# In[ ]:





# ## Task 2:
# ### 1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.¶
# ### area = (s(s-a)(s-b)*(s-c)) ** 0.5
# ### Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass

# In[12]:


class triangle(object):
    #a = input('Enter the first side of a triangle: ')
    #b = input('Enter the second side of a triangle: ')
    #c = input('Enter the third side of a triangle: ')
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
class get_area(triangle):
    def area(self):
        s = (self.a + self.b + self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return 'The area is : %s'%area
    
obj = get_area(3,6,8)
obj.area()


# In[ ]:





# ## 1.2
# ### Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[13]:


def filter_long_words(words,n):
    lst = []
    for word in words:
        if len(word)>n:
            lst.append(word)
    return lst           
   # return filter(lambda word:len(word)>n, words)


# In[14]:


words = ['a', 'Yenosh', 'Yenoshkumar', 'TK']
print(filter_long_words(words, 3))


# In[ ]:





# ### 2.1
# #### Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words .

# In[15]:


def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


# In[16]:


words = ['Mani', 'Hello Mani', 'How is your test']
print(map_to_lengths_for(words))


# In[ ]:





# ## 2.2
# Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise

# In[17]:


def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E','I','O','U')
    if char not in vowels:
        return False
    return True


# In[18]:


is_vowel('b')


# In[19]:


is_vowel('a')


# In[20]:


is_vowel('i')


# In[21]:


is_vowel('z')


# In[22]:


is_vowel('U')


# In[ ]:





# In[ ]:




