# taskthree


We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you. Example Inputs object = {“a”:{“b”:{“c”:”d”}}} key = a/b/c object = {“x”:{“y”:{“z”:”a”}}} key = x/y/z value = a


Define a function that takes two parameters named

  object : the full JSON object keys : an Array of keys in the order
  
Written a python code to pass in the object which is in the form of full JSON object, keys with list of values to get back the value as per the object that is passed 

Please find the code in the file named code.py

Code implementation logic : 

As for this this code it is specified to get the value for the object and key we passed,

let's say here obj is dict - {"a":{"b":{"c":"3"}}}
key is the form of a/b/c
to get the value we must have keys in the form of list to iterate in the loop
so we used a splic function here to split at /
now we will pass that key to this loop 
if we give a/b it must return {"c":3}
if we give a/b/c it must return 3
if we give a key which is not there then it will return none


