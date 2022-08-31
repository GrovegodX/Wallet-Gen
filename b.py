from discord import Webhook, RequestsWebhookAdapter
import os
import random

os.system("cls")

hee = input(" Webhook >>> : ")
amount = input(" Amount Url >>> : ")

url = "https://gift.truemoney.com/campaign/?v="

for i in range(int(amount)):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    string = lower + upper + numbers
    length = 18
    code = "".join(random.sample(string,length))

    webhook = Webhook.from_url(f"{hee}", adapter=RequestsWebhookAdapter())
    webhook.send(content=f"{url}{code}")
    print(f" Truemoney Gen Code : {code}")