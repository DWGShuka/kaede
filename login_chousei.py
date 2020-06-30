from robobrowser import robobrowser
import sqlite3

browser = RoboBrowser(parser='html.parser')
browser.open('https://chouseisan.com/schedule/newEvent/create')

form = browser.get_form(attrs={'id':'newEventForm'})
form['name']='絶アレキサンダー'
form['comment']='今週もよろしくお願いします'
form['kouho']= a '\n' b '\n' c '\n' d '\n' e '\n' f '\n' g
browser.submit_form(form,headers={'Referer':browser.url,'Accept-Language':'ja,en-US;q=0.7,en;q=0.3',})
