import smtplib
from datetime import datetime
def Firstperson():
    '''covert current to string and add to text'''

    current_time = datetime.now()
    ct=str(current_time)


       
    smtpUser = 'your_account@gmail.com'
    smtpPass = 'your_password'

    toAdd = 'Firstperson_cell_phone#@Firstperson_provider.com'
    fromAdd = smtpUser

    subject = 'python test'
    header = 'To: '+ toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Sub: ' + subject
    body = 'power on at ' + ct

    print (header + '\n' + body)

    s = smtplib.SMTP('smtp.gmail.com',587)

    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(smtpUser, smtpPass)
    s.sendmail(fromAdd, toAdd, header +'\n\n' + body)

    s.quit()
    
def Secondperson():
    '''covert current to string and add to text'''

    current_time = datetime.now()
    ct=str(current_time)


       
    smtpUser = 'your_account@gmail.com'
    smtpPass = 'your_password'

    toAdd = 'Secondperson@Secondperson_provider.com'
    fromAdd = smtpUser

    subject = 'python test'
    header = 'To: '+ toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Sub: ' + subject
    body = 'power on at ' + ct

    print (header + '\n' + body)

    s = smtplib.SMTP('smtp.gmail.com',587)

    s.ehlo()
    s.starttls()
    s.ehlo()

    s.login(smtpUser, smtpPass)
    s.sendmail(fromAdd, toAdd, header +'\n\n' + body)

    s.quit() 
    
if __name__ == '__main__':
    Firstperson()
    Secondperson()
    exit()

