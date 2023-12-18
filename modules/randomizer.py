#load dependencies
import random


# amount_start_range=float(input("Starting range for amount: "))
# amount_end_range=float(input("Ending range for amount: "))
#generate random amounts
def random_amount(start:float, end:float) -> float:
    return random.randint(start,end)

#get list of companies
with open("./contents/company.txt","r")as company_file:
    company_list=company_file.readlines()
    company_list=[company.strip("\n") for company in company_list]

# call market 
def random_company(company_list:list)->str:
    lenght=len(company_list)-1
    return company_list[random.randint(0,lenght)]


#list of charge vocubalaries
with open("./contents/words.txt","r")as words_file:
    word_list=words_file.readlines()
    word_list=[word.strip("\n") for word in word_list]

# call word
def random_word(word_list:list)->str:
    lenght=len(word_list)-1
    return word_list[random.randint(0,lenght)]



#get list of links
with open("./contents/link.txt","r")as links_file:
    link_list=links_file.readlines()
    link_list=[link.strip("\n") for link in link_list]

# call word
def random_link(word_list:list)->str:
    lenght=len(word_list)-1
    return word_list[random.randint(0,lenght)]



#merge text
def randomize(text:str, start:float, end:float)->str:
    #replace [company], ['word'], ['amount'], ['link'] keywords
    global company_list, word_list, link_list
    text = text.replace("[company]",random_company(company_list))
    text = text.replace("[word]",random_word(word_list))
    text = text.replace("[link]",random_link(link_list))
    text = text.replace("[amount]",str(random_amount(start,end)))

    return text

amount_of_text=int(input("Enter amount: "))

with open("./contents/spam_text.txt","a") as file:
    for i in range(0,amount_of_text):
        file.write(randomize("you have been [word] [amount], by [company] to cancel visit [link]\n"))

