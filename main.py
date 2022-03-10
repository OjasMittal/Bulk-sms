import requests
import pandas
num=""
df=pandas.read_excel('people.xlsx')
for index,row in df.iterrows():
        a= str(row['number'])
        num+=a+','
l=len(num)
num=num[:l-1]
url= "https://www.fast2sms.com/dev/bulkV2"
message="Hello, How are you?"
payload=f'sender_id=Cghpet&message={message}&route=v3&language=english&numbers={num}'
headers={
  'authorization':"ENTER YOUR AUTHORIZATION KEY HERE",
'Content-Type':'application/x-www-form-urlencoded'
  
}
response=requests.request("POST",url=url,data=payload,headers=headers)
print(response.text)
