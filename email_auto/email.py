import win32com.client as win32
#importanto uma biblioteca que integra python e S.O

variavelx = "valor"
variavely = "valor"

#criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

#criar um email
email = outlook.CreateItem(0)

# configurar as informações do seu e-mail
email.To = "emailteste@gmail.com;emailteste2@gmail.com;emailteste3@gmail.com"
email.Subject = "assunto"
email.HTMLBody = f"""
<p>ola mundo, esse email é {variavelX}</p>

<p>loren pisen e {variavelY}</p>

<p>abs,</p>
<p>Eu</p>
"""

#anexo = "C://urser/eu/download/arquivo.xlsx"
#email.Attachments.add(anexo)

email.send()
print("email enviado")