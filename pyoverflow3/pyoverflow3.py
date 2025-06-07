#importing the libraries
import sys
import webbrowser
from googlesearch import search

#defining a search array
search_result = []

class pyoverflow3:
#passing error as args
    @staticmethod
    def submit_error(err_msg,no_solution):
        print('''Please wait......
             PyOverflow3 is searching the top solutions for your code problems
        ''')
        try:
            #performing a google search
            search_word = "python"+" "+str(err_msg)
            for url in search(search_word,stop=2):
                search_result.append(url)
        #handling exception
        except Exception as e:
            print(e)
            sys.exit(0)
        #handling no of solutions
        try:
            if(int(no_solution)>0):
                for i in range(0,int(no_solution)):
                    print ("opening"+"\t"+str(i)+"solution in browser")
                    webbrowser.open_new_tab(search_result[i])
            else:
                print("Number of solutions should be > 0")
        except Exception as e:
            print(e)
            sys.exit(0)
