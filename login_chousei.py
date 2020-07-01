from robobrowser import RoboBrowser
import datetime

def chousei():
    thisweek=[datetime.date.today()+datetime.timedelta(days = i) for i in range(7)]
    strweek=[i.strftime('%Y/%m/%d') for i in thisweek]
    browser = RoboBrowser(parser='html.parser')
    browser.open('https://chouseisan.com/schedule/newEvent/create')
    form = browser.get_form(attrs={'id':'newEventForm'})
    form['name']='絶アレキサンダー'
    form['comment']='今週もよろしくお願いします'
    form['kouho']= strweek[0] +'\n'+ strweek[1]+ '\n'+ strweek[2]+ '\n'+ strweek[3]+ '\n'+ strweek[4]+ '\n'+ strweek[5] +'\n'+ strweek[6]
    browser.submit_form(form,headers={'Referer':browser.url,'Accept-Language':'ja,en-US;q=0.7,en;q=0.3',})
    print('on processing')
    print(browser.find(attrs={'id':'listUrl'}))
    return browser.find(attrs={'id':'listUrl'})
