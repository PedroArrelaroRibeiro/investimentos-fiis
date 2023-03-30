import urllib.request

open_adress = urllib.request.urlopen('https://www.google.com/finance/quote/MXRF11:BVMF?sa=X&ved=2ahUKEwizjc384oz9AhXRFbkGHZLfCCUQ3ecFegQIMBAg')
codigo_html = str(open_adress.read())
index_cotacao=(codigo_html.index("data-last-price="))
cte0=0
while True:
            try:
                0+int(codigo_html[index_cotacao+17+cte0])
            except:
                if codigo_html[index_cotacao+17+cte0] != ".":
                    break
                cte0=cte0+2
                break
            else:
                cte0=cte0+1 
cotacao=(codigo_html[index_cotacao+17:index_cotacao+17+cte0])
print(cotacao)