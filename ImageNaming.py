import os 
  
# Function to rename multiple files 
def main(): 
    i = 1
      
    for filename in os.listdir('CyclingHelmets'): 
        dst = str(i) + ".jpg"
        src = 'CyclingHelmets/'+ filename 
        dst ='CyclingHelmets/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
