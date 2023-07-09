import requests
from bs4 import BeautifulSoup
'''This function is used to operate the links part of the project,i.e. accessing links of a particular website.'''
def links():
    '''this function is used to find all links on webpage of iit with similar webaddress'''
    def all_links(url,url1): 
        linkst=[]        #list containing all the links 

        #boundary condition as we found that this website does not allow us to access it.
        if(url.find("www.cga.iitrpr.ac.in")!=-1):
            return []

        

        if(str(url).find("https")!=0):  #we check if it has https at the beginning or not otherwise request and beautifulSoup may not work
            return []
        
        web=requests.get(url)       # request is sent to website 
        web_text=web.text         #it returns content of webpage in string format
        soup_text=BeautifulSoup(web_text,"html.parser")   #it parser the website using beautifulSoup
        links=soup_text.find_all('a')       #we find all the anchor tags 
        links2=soup_text.find_all('img')    #we find all the image tags 
        links3=soup_text.find_all('video') #we find all the video tag 
        
        x=url[url1.find("iit"):url1.find(".in")+4]      # we check if we have website in iitabc.ac.in form or not,so we slice iitabc.ac.in part from link
        for link in links:                              #we check all the links 
                
            j=link
            j=str(j)      #we convert link to string 
            if(j.find(x)!=-1):       #we find x in j and if it is not returning -1, we apppend it to linkst 
                        linkst.append(link.get("href"))
        
        for link in links2:
            j=link
            j=str(j)    #we convert link to string 
            if(j.find(x)!=-1):#we find x in j and if it is not returning -1, we apppend it to linkst 
                        linkst.append(link.get("src"))
        
        for link in links3:
                
            j=link
            j=str(j) #we convert link to string 
            if(j.find(x)!=-1):#we find x in j and if it is not returning -1, we apppend it to linkst 
                        linkst.append(link.get("src"))
        return linkst  #linkst is returned 


    '''we use this function to find all links in links '''
    def all_links_in_links(url,n):
        if (n==1):       #condition to check all the links in terminal
            print ('please wait for a few seconds')
        l=all_links(url,url)       #all links function is called on l

        for x in l:            #we access each link in l
            j=all_links(x,url)     #we call all_links function on x 
            l=l+j      # we append list j to l
        
        l=set(l)     #list is converted into set as we want unique links 
        l=list(l)      #list is again converted into list so that we can use it again 
        if (n==1):      #condition to  print 
            print ('all the links in the iit ropar site are')    
            for i in l:
                print (i)     #all links are printed 
            print ()
            print ('the total no. of the links extracted are')
            print ()
            print (len(l))  #number of all links are updated 
        else:
            return l        #l is returned 
    '''this function is used to segregate all links found into image docx an pdf links''' 
    def segregator(url):
        print ('please wait for a few seconds')
        f=open('all_links.txt','a')
        o=open('all_links_pdf.txt','a')
        p=open('all_links_img.txt','a')
        z=open('all_links_docx.txt','a')

        l=all_links_in_links(url,2)      #all links_in links  is called using option 

        for x in l:        #accessing all links in l
            x=str(x)        #we convert all links to str
            
            f.write(x+'\n')   #we write x to f containing all links
            if(x.find('pdf')==len(x)-3): # we check if link has ending pdf and append to o if present
                o.write(x+'\n')
            if(x.find('jpg')==len(x)-3 or x.find('png')==len(x)-3 or x.find('jpeg')==len(x)-3): #we check link has png or jpg or jpeg
                p.write(x+'\n')
            if(x.find('docx')==len(x)-4 or x.find('doc')==len(x)-3):  #we find if it end with docx or doc and write it to z
                z.write(x+'\n')
                
        f.close() #closing all the files
        o.close()
        p.close()
        z.close()
        print ('all the links are now present in your computer in text files')
        print ('for all links refer all_links.txt')
        print ('for all pdf links refer all_links_pdf.txt')
        print ('for all images links refer all_links_img.txt')
        print ('for all documents links refer all_links_docx.txt')
            

    print ('enter 1 if you want to see all the links extracted on the terminal')
    print ('enter 2 if you want all the links to be stored in your computer as text files separately for pdf,images and documents')
    n=int (input())
    if (n==1):
        all_links_in_links("https://www.iitrpr.ac.in/",1)
    elif(n==2):
        segregator("https://www.iitrpr.ac.in/")
    else:
        print('invalid input')
        
'''the following function placements picks out the placement data of some colleges and displays it.
the function can alco compare the placement stats of two colleges with any branches'''
def placements():
    '''the function placements_iit_bhubaneswar picks out the placement data from the official site of iit bhubaneswar.
    #n shows the choice of user whether to display the placemnet data(n=2) or to compare it with any college(n=1).'''
    def placements_iit_bhubaneswar(n):
        #url contains the url of the official page of iit bhubaneswar that displays the placement data of the college.
        url="https://www.iitbbs.ac.in/highlights-of-placement.php#:~:text=Undergraduate%20placement%20is%20over%2087,Lakh%20Per%20Annum%20for%20M."
        #the http request is sent to the web to get the response data in the variable web.
        web=requests.get(url)
        #we convert the contents of web into text to move the process further.
        web_text=web.text
        #beautifulsoup parses the data we got using the html parser.
        soup_text=BeautifulSoup(web_text,"html.parser")
        #we find all the occureneces of tr(row in table). so now trs contains all the rows in the table that contains the placement data.
        trs=soup_text.find_all('tr')
        #highest is a list that contains the highest packages each branch got, in form of tuples with branch and respective highest package as tuple elements.
        highest=[]
        #average is a list that contains the average packages each branch got, in form of tuples with branch and respective average package as tuple elements.
        average=[]
        #percentage is a list that contains the percentage of the students placed from each branch.
        percentage=[]
        branches=['CSE','ECE','EE','MECH','CIVIL','MME']
        #we found that the highest packages are writen in the row with index 2 in trs 
        for tr in trs[2]:   
            #we take out each block's content from the row
            for td in tr:
                #we found that the required data is in the p tag of the blocks.
                    for p in td:
                        #if there is something in the p tag we append the data next to the branch name in form of tuple to the list.
                        if(p!='\n' ):
                            highest.append((branches[len(highest)-1],p))
            if(len(highest)==7):
                break
        #we found that the average packages are writen in the row with index 4 in trs 
        for tr in trs[4]:
            #we take out each block's content from the row
            for td in tr:        
                #we found that the required data is in the p tag of the blocks.
                    for p in td:
                        #if there is something in the p tag we append the data next to the branch name in form of tuple to the list.
                        if(p!='\n'):
                            average.append((branches[len(average)-1],p)) 
            if(len(average)==7):
                break
            
        #we found that the percent placements are writen in the row with index 1 in trs 
        for tr in trs[1]:
            #we take out each block's content from the row
            for td in tr:    
                #we found that the required data is in the p tag of the blocks.
                    for p in td:
                        #further inside the p tag percentages are in the strong tag.
                        for strong in p:
                            #if there is something in the strong tag we append the data next to the branch name in form of tuple to the list.
                            if(strong!='\n'):
                                percentage.append((branches[len(percentage)-1],strong)) 
            if(len(percentage)==7):
                break
        
        #we remove the first element of each list as that is empty.
        highest.remove(highest[0])
        average.remove(average[0])
        percentage.remove(percentage[0])
        #now taking the user's choice into account,we print tha data if the enetered choice is 2.
        if (n==2):
            print ('PLACEMENT STATISTICS OF IIT bhubaneswar')
            print()
            print ('highest ctc (in lakhs per annum)')
            print(highest)
            print()
            print ('average ctc (in lakhs per annum)')
            print(average)
            print()
            print ('percent of students placed')
            print(percentage)
        #if the choice is 1.
        elif (n==1):
            #taking the input of the branch to be considered.
            print ('enter the branch you want to analyse')
            print ('enter cse for computer science')
            print ('enter ece for electronics and communication engineering')
            print ('enter ee for electrical engineering')
            print ('enter mech for mechanical engineering')
            print ('enter civil for civil engineering')
            print ('enter mme for metallurgical engineering')
            branch=input()
            #checking if the college has the enetered branch
            for i in percentage:
                #if we found the entered branch we return the respective percent of the students placed
                if (i[0]==branch.upper()):
                    return (float(i[1][0:5]))
            #otherwise we return -1.
            return -1
        else:
            #we return -1 if the value of n is not 1 or 2 as asked.
            return -1
                    
    #------------------------------------------------------------------------------
    #the function placements_mnnit_allahabad picks out the placement data from the official site of mnnit allahabad.
    #n shows the choice of user whether to display the placemnet data(n=2) or to compare it with any college(n=1).
    def placements_mnnit_allahabad(n):
        #url contains the url of the official page of mnnit allahabad that displays the placement data of the college.
        url="https://tpo.mnnit.ac.in/tnp/placement/placementarchive.php"
        #the http request is sent to the web to get the response data in the variable web.
        web=requests.get(url)
        #we convert the contents of web into text to move the process further.
        web_text=web.text
        #beautifulsoup parses the data we got using the html parser.
        soup_text=BeautifulSoup(web_text,"html.parser")
        #we find all the occureneces of tr(row in table). so now trs contains all the rows in the table that contains the placement data.
        trs=soup_text.find_all('tr')
        #highest contains the highest packages of different branches of thhe college.
        highest=[]
        #average contains the average packages of different branches of thhe college.
        average=[]
        #percentage contains the percentage placements in every branch in the college.
        percentage=[]
        #stats contains all the data in single list that we will segregate later into highest, average, and percentage.
        stats=[]
        #i is used to keep track of the branch
        i=0
        #we notice the branches we consider are in the rows with indexes from 3 to 8.
        for tr in trs[3:9]:
            #we check that the row should not be empty.
            if(tr!='\n'):
                #we see that the highest, average and percentage starts from the fourth index so we keep this counter to add only relevent data.
                k=0
                #taking out data in each block of the row.
                for  td in tr:
                        if(td!='\n'):
                            #we add only if the value of k is past 4
                            if (k>=4):
                                #converting the block data into string to later segregate into haighest, average and percent data.
                                x=str(td)
                                #we note the starting and ending index that contains the required nos., and slice the text accordingly.
                                m=x[x.find('>')+1:x.find('/')-1]
                                #the conditions to pair the required data with the respective branch.
                                if(i==0):
                                            stats.append(('CIVIL',m))
                                elif(i==1):
                                            stats.append(('CSE',m)) 
                                elif(i==2):
                                            stats.append(('EE',m))
                                elif(i==3):
                                            stats.append(('ECE',m))
                                elif(i==4):
                                            stats.append(('IT',m))
                                elif(i==5):
                                            stats.append(('MECH',m))      
                            k=k+1
                i=i+1
        #the code to segregate the data into different lists namely highest, average and percentage.
        for i in range (len(stats)):
            #since the average packages are there at the positions right next to every index of multiple of 3., we append that to average.
            if ((i+2)%3==0):
                average.append(stats[i])
            #since the highest packages are there at the positions 2 units next to every index of multiple of 3., we append that to highest.    
            elif((i+1)%3==0):
                highest.append(stats[i])
            #the percentage placemenets are there ar every index of multiple of 3.
            else:
                percentage.append(stats[i])
        #if the user chose for all the data to be displayed, we do so.
        if (n==2):
            print ('PLACEMENT STATISTICS OF MNNIT ALLAHABAD') 
            print ()
            print ('highest ctc (in lakhs per annum)')
            print (highest)
            print ()
            print ('average ctc (in lakhs per annum)')
            print(average)
            print ()
            print ('percent of students placed')
            print (percentage)
        #if the user chose to compare the placement stats of two colleges we return the relevent data if the college has the enetered branch.
        if (n==1):
            #taking the input of the branch.
            print ('enter the branch you want to analyse')
            print ('enter cse for computer science')
            print ('enter ece for electronics and communication engineering')
            print ('enter ee for electrical engineering')
            print ('enter mech for mechanical engineering')
            print ('enter civil for civil engineering')
            print ('enter it for information technology')
            branch=input()
            #returning the relevent sliced data.
            for i in percentage:
                if (i[0]==branch.upper()):
                    return (float(i[1][0:4]))
            #returning -1 if the enetered branch is not present in the college.
            return -1

    #------------------------------------------------------------------
    #the function placements_iit_ropar picks out the placement data from the official site of iit ropar.
    #n shows the choice of user whether to display the placemnet data(n=2) or to compare it with any college(n=1).
    def placements_iit_ropar(n):
        #the url of the webpage that contains the placement data of iit ropar.
        url="https://cdcrc.iitrpr.ac.in/info/placement-statistics/"
        #requesting the url from web. and storing the response data in the variable called web.
        web=requests.get(url)
        #converting the response data into text for further operations.
        web_text=web.text
        #beautifulsoup parses the data we got using the html parser.
        soup_text=BeautifulSoup(web_text,"html.parser")
        #we find all the occureneces of tr(row in table). so now trs contains all the rows in the table that contains the placement data.
        trs=soup_text.find_all('tr')
        #percentage will contain all the percentage placements of respesctive branches in the college.
        percentage=[]
        #branches contains the branches that the college has.
        branches=[0,'CSE','EE','MECH','CEB','OVERALL']
        #we take out the tr tag of index 3 as we notice that the required data is present there.
        for tr in trs[3]:
            #taking out each block of data in every tr tag
            for td in tr:
                #if the block is not blank we slice out the relevent data ab=nd store it into the list.
                if(td!='\n'):
                        percentage.append((branches[len(percentage)],td))
        #l contains the overall averrage ctc of the college.
        l=[]
        #the average ctc is there in the index 4 of trs.
        for  tr in trs[4]:
            #taking out each block's data
                for td in tr:
                    #if the block is not blank we append the data to the list l.
                        if(td!='\n'):
                            l.append(td)
                            
        percentage.remove(percentage[0])
        #displaying all the data if user chose that.
        if (n==2):
            print ('PLACEMENT STATISTICS OF IIT ROPAR')
            print ()
            print ('average ctc (in lakhs per annum)')
            print (l)
            print ()
            print ('percent placements')
            print(percentage)
        #returning the requested branch's placement data if the user chose that.
        if (n==1):
            #taking the input of the branch.
            print ('enter the branch you want to analyse')
            print ('enter cse for computer science')
            print ('enter ceb for electronics and chemical engineering')
            print ('enter ee for electrical engineering')
            print ('enter mech for mechanical engineering')
            branch=input()
            #checking if the college has the enetered branch and appending it to our list if so.
            for i in percentage:
                if (i[0]==branch.upper()):
                    return (float(i[1][0:4]))
            #returning -1 if we did not find the requested branch.
            return -1
             
    #-----------------------------------------------------------------
    #the function placements_nit_duragapur picks out the placement data from the official site of nit durgapur.
    #n shows the choice of user whether to display the placemnet data(n=2) or to compare it with any college(n=1).
    def placements_nit_durgapur(n):
        #url now contains the url of the webpage that contains the placement data.
        url="https://nitdgp.ac.in/p/placementnitd"
        #requesting the url from web. and storing the response data in the variable called web.
        web=requests.get(url)
        #converting the response data into text for further operations.
        web_text=web.text
        #beautifulsoup parses the data we got using the html parser.
        soup_text=BeautifulSoup(web_text,"html.parser")
        #we find that the required data is there in the class with the following name.
        divs=soup_text.find_all(class_="progress-bar bg-warning progress-bar-striped progress-bar-animated")
        ans=[]
        branches=['CIVIL','CHEM','CSE','ECE','EE','MECH','MME']
        i=0
        #we take out each element from the list divs 
        for div in divs:
            #extracting out the text part of the elements.
            div=div.text
            #converting the text part into string.
            div=str(div)
            #we append the required data to final list.
            if(i>=1 and i<=7):
                m=div[len(div)-6:len(div)]
                ans.append((branches[i-1],m))
            i=i+1
        
        #displaying all the data if the user chose so.
        if (n==2):
            print ('PLACEMENT STATISTICS OF NIT DURGAPUR')
            print ()
            print(ans)
        #returning the stats of requested branch if the user chose so.
        if (n==1):
            #taking the branch as input.
            print ('enter the branch you want to analyse')
            print ('enter cse for computer science')
            print ('enter ece for electronics and communication engineering')
            print ('enter ee for electrical engineering')
            print ('enter mech for mechanical engineering')
            print ('enter civil for civil engineering')
            print ('enter mme for metallurgical engineering')
            branch=input()
            #returning the data of the requested branch if it is present in the college.
            for i in ans:
                if (i[0]==branch.upper()):
                    return (float(i[1][0:4]))
            #returning -1 otherwise.
            return -1
    
    #the function control controls the progress of the operation the user chooses.
    def control():
        #displaying the choices the user may have.
        print ('input 1 if you want to compare two college placements for a branch')
        print ('input 2 if you want to see a college placement stats')
        #taking the choice input.
        n=int(input ())
        #if the user choooses to have the stats of a prticular college to be displayed we do so here.
        if (n==2):
            #displaying the choices the user may have.
            print ('input 1 for iit bhubaneswar')
            print ('input 2 for iit ropar')
            print ('input 3 for mnnit allahabad')
            print ('input 4 for nit durgapur')
            a=int (input ())
            if (a==1):
                placements_iit_bhubaneswar(2)
            elif (a==2):
                placements_iit_ropar(2)
            elif(a==3):
                placements_mnnit_allahabad(2)
            elif (a==4):
                placements_nit_durgapur(2)
            else:
                print ('invalid input')
        #if user chooses to compare any two colleges with any branch we do so here.    
        if (n==1):
            #taking input of any two colleges
            print ('input any two of the following options')
            print ('input 1 for iit bhubaneswar')
            print ('input 2 for iit ropar')
            print ('input 3 for mnnit allahabad')
            print ('input 4 for nit durgapur')
            a=int (input())
            b=int (input())
            #college1 and college2 store the colleges name chosen.
            college1=''
            college2=''
            #c,d store the percentage placements in the asked branch in the colleges.
            c=0
            d=0
            #placing the name of college1 and the returned placement stats in the relevent variables.
            if (a==1):
               c=placements_iit_bhubaneswar(1)
               college1='iit bhubaneswar'
            elif (a==2):
               c=placements_iit_ropar(1)
               college1='iit ropar'
            elif (a==3):
               c=placements_mnnit_allahabad(1)
               college1='mnnit allahabad'
            elif (a==4):
               c=placements_nit_durgapur(1)
               college1='nit duragapur'
            else:
                print ('invalid input')
                
            #placing the name of college2 and the returned placement stats in the relevent variables.
            if (b==1):
               d=placements_iit_bhubaneswar(1)
               college2='iit bhubaneswar'
            elif (b==2):
               d=placements_iit_ropar(1)
               college2='iit ropar'
            elif (b==3):
               d=placements_mnnit_allahabad(1)
               college2='mnnit allahabad'
            elif (b==4):
               d=placements_nit_durgapur(1) 
               college2='nit duragapur'
            else:
                print ('invalid input')
            
            #in case user enters any wrong choice or the branch is not present we print the following statement.
            if (c==0 or c==-1 or d==0 or d==-1):
                print ('we did not get any data')
            #if we found the data we print it.
            else:
                print (college1,'placement statistics for the entered branch =',c,'% students were placed')
                print (college2,'placement statistics for the entered branch =',d,'% students were placed')
    #calling the function control  
    control()
    

'''This function is used to find all review and rating of a few mentioned colleges from website'''
def ratings_reviews():
    '''All links are stored '''
    career_360_links_stars=['https://www.careers360.com/university/international-institute-of-information-technology-bhubaneswar','https://www.careers360.com/university/motilal-nehru-national-institute-of-technology-allahabad-prayagraj','https://www.careers360.com/university/national-institute-of-technology-durgapur','https://www.careers360.com/university/indian-institute-of-technology-ropar/reviews']

    shiksha_link_stars=['https://www.shiksha.com/college/indian-institute-of-technology-bhubaneswar-32717','https://www.shiksha.com/university/mnnit-allahabad-motilal-nehru-national-institute-of-technology-24357/reviews','https://www.shiksha.com/university/nit-durgapur-national-institute-of-technology-54019','https://www.shiksha.com/college/indian-institute-of-technology-ropar-32693']
    getmyuni_link_stars=['https://www.getmyuni.com/college/indian-institute-of-technology-iit-bhubaneswar','https://www.getmyuni.com/college/motilal-nehru-national-institute-of-technology-mnnit-allahabad','https://www.getmyuni.com/college/national-institute-of-technology-nit-durgapur','https://www.getmyuni.com/college/indian-institute-of-technology-iit-ropar']

    shiksha_review_links=['https://www.shiksha.com/college/indian-institute-of-technology-bhubaneswar-32717/reviews','https://www.shiksha.com/university/mnnit-allahabad-motilal-nehru-national-institute-of-technology-24357/reviews','https://www.shiksha.com/university/nit-durgapur-national-institute-of-technology-54019/reviews','https://www.shiksha.com/college/indian-institute-of-technology-ropar-32693/reviews']
    career_360_review_links=['https://www.careers360.com/university/indian-institute-of-technology-bhubaneswar','https://www.careers360.com/university/motilal-nehru-national-institute-of-technology-allahabad-prayagraj/reviews','https://www.careers360.com/university/national-institute-of-technology-durgapur/reviews','https://www.careers360.com/university/indian-institute-of-technology-ropar/reviews']


    #this function is used to find reviews from a shiksha website
    def shiksha(url):  
        web=requests.get(url)    #request is sent to url 
        web_text=web.text         #content is converted to text 
        soup_text=BeautifulSoup(web_text,"html.parser")  #html is parsed 
        div=soup_text.find_all(class_='desc-sp')    #all div tags with class=desc-p are found 
        j=0
        for i in div:   # for accessing element  every tag in div  list
            if (j<3):     #condition for j
                print (i.text) #printing text in i
            j=j+1
    #this function is used to find reviews from a shiksha website
    def careers360(url):
        web=requests.get(url)   #request is sent to url 
        web_text=web.text       #content is converted to text 
        soup_text=BeautifulSoup(web_text,"html.parser") #html is parsed 
        div=soup_text.find_all(class_='ratingOuter')   #all div tags with ratingOuter are found 
        a=div[1].text.split('\n')    #text is split about '\n' and converted to list 
        for i in range (7):
            print (a[i])    #every element of a is printed
    #this function is used to get career360 rating 
    def rating_careers360(url):
    
        web=requests.get(url) #request is sent to url 
        web_text=web.text    #content is converted to text
        soup_text=BeautifulSoup(web_text,"html.parser")  #html is parsed 
        
        div=soup_text.find_all(class_='iconRow ratingIcon') #all div tags with iconRow ratingIcon are found 
        a=div[0].text.split(' ')  #text is split about '\n' and converted to list 
        b=a[1].split('/')         #all a is split about '/'

        print (float(b[0]),'out of 5') #printing first element of b 
    
    #this function is used to get Shiksha rating of MNNIT
    def rating_shiksha_mnnit():
        url='https://www.shiksha.com/university/mnnit-allahabad-motilal-nehru-national-institute-of-technology-24357/reviews'
        web=requests.get(url)  #request is sent to url 
        web_text=web.text      #content is converted to text
        soup_text=BeautifulSoup(web_text,"html.parser") #html is parsed 
        div=soup_text.find_all(class_='rvwScore')  #all div tags with class rvwScore are found 
        
        print (float(div[0].text.split(' ')[0]),'out of 5') #div[0] is  split and it's zero index element is obtained
    
    #this function is used to get rating from Shiksa website 
    def rating_shiksha(url):
    
        web=requests.get(url)  #request is sent to url 
        web_text=web.text      #content is converted to text
        soup_text=BeautifulSoup(web_text,"html.parser") #html is parsed
        div=soup_text.find_all(class_='ctpv2-rating')  #all div tags with class  are found tpv2-rating
        
        print (float(div[0].text),'out of 5')   #text of div[0] is returned 
    
    #this function is used to get rating from getmyuni website
    def getmyuni(url):
    
        web=requests.get(url)     #request is sent to url 
        web_text=web.text          #content is converted to text
        soup_text=BeautifulSoup(web_text,"html.parser") #html is parsed
        div=soup_text.find_all(class_='mobileOnly pl') #all div tags with class  are found tpv2-rating
        a=div[0].text.split('\n') #div[0] is split about '\n'  
        b=float(a[1].strip())  #a[1] is stripped 
        print (b) # b is print
    
    #control function which provides instruction
    def control2():
        print('If you want the reviews of IIT Ropar,IIT bhubaneswar,MNNIT and NIT Durgarpur enter 1')
        print('If you want the ratings of IIT Ropar,IIT bhubaneswar,MNNIT and NIT Durgarpur enter 2')
        
        #input is taken 
        a=int(input())
        #conditions for different input are given 
        if(a==1):                          
            print("Which college's  review you want ") #instructions to get desired output are given
            print("Enter 1 for IIT bhubaneswar")
            print("Enter 2 for MNNIT")
            print("Enter 3 for NIT Durgapur")
            print("Enter 4 for IIT Ropar")
            
            m=int(input())     #input in taken 
            print("Which website's review you want ,Enter 1 for Shiksha and 2 for careers 360") #instructions to get desired output are given
            w=int(input()) #input in taken 

            if(w==1):  #if w==1 shiksha review is given 
                shiksha(shiksha_review_links[m-1])
            
            elif(w==2): #else career review is given 
                careers360(career_360_review_links[m-1])
            
            else:
                print("Invalid Input")#condition for invalid input
            

        
        #conditions for different input are given 
        elif(a==2):
            print("Which college's  rating you want ") #instructions to get desired output are given
            print("Enter 1 for IIT bhubaneswar")  
            print("Enter 2 for MNNIT")
            print("Enter 3 for NIT Durgapur")
            print("Enter 4 for IIT Ropar")
            #conditions for different input are given 

            m=int(input())
            print("Which website's rating  you want")
            print ('Enter 1 for Shiksha')
            print ('2 for careers360')
            print ('3 for getmyuni') #instructions to get desired output
            w=int(input())  #input in taken 

            if(w==1): #if w==1 shiksha rating is given 
                if(m==2): #if m==2 we give MNNIT is given
                    print("The rating is ",end='')
                    rating_shiksha_mnnit()
                else: 
                    print("The rating is ",end='')
                    rating_shiksha(shiksha_link_stars[m-1]) # rating is given 
              
            elif(w==2): #if w is 2 career rating is given 
                 print("The rating is ",end='')
                 rating_careers360(career_360_links_stars[m-1])
            
            elif(w==3): #if w is 3 getmyuni rating is given 
                print("The rating is ",end='')
                getmyuni(getmyuni_link_stars[m-1]) 
            
            else:
                print("Invaild input")  #conditon for invalid input
            
        
        else:
            print("Invalid Input") #condtion for invalid input
            
    control2() #contorl2 is called 
    
print ('input 1 if you want to work with the links extracted from iit ropar site')
print ('input 2 if you want to work with and compare the placement statistics of some colleges')
print ('input 3 if you want to see the ratings and reviews of these colleges on some websites')
n=int(input())
if (n==1):
    links()
elif(n==2):
    placements()
elif (n==3):
    ratings_reviews()
else:
    print ('invalid entry')


        
        
        
        

            
        
                            
                        
                    
                   
                    

        

            



        

        
        
                    

            
            
        
        


            
         

            

        
        
            

            
                
                





                
            
        
        

        
        

        

        
            
                


        
        







        
        



        









        














































