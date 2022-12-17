# from capsuling import open_form, writ_data, email, male, number, hobbi
from module.capsuling import *

def test_form():
    open_form()
    writ_data(name='test', lastname='selene')
    email(email='sobaka@mail.com')
    male(Male="Male")
    number(phone='1234567891')
    hobbies(hobbi='sports')
    subjects(subject='Computer Science')
    birthInput(date='11 May 1999')
    resurse(photo='photo.jpg')
    address(Address='street house ')
    state_city(state='NCR', city='Delhi')



'''    browser.all('.table td:nth-of-type(2)').should(
        have.texts(
            name,
            lastname,
            email,
            Male,
            number,
            date,
            subjects,
            photo,
            Address,
            state,
            city,
        )
    )'''
