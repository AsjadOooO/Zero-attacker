# importing module
import requests
 
def domain_scanner(domain_name,sub_domnames):
    print('URLS FOUND: ')
     
    
    for subdomain in sub_domnames:
       
       
        url = f"https://{subdomain}.{domain_name}"
         
        
        try:
            
            requests.get(url)
             
            
            print(f'[+] {url}')
             
            
        except requests.ConnectionError:
            pass
 
#DEV7 THE  GOAT 
if __name__ == '__main__':
   
    print("please dont be dumb and put the url just domain name")
    domain = input("Enter the Domain Name: ")
 
    
    with open('basiclist.txt','r') as file:
       
        
        name = file.read()
         
       
        sub_dom = name.splitlines()
         

    domain_scanner(domain,sub_dom)