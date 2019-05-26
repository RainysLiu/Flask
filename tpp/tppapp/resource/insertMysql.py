from tppapp.models import *
import json


def insertMysql():
    with open('city.json', 'rb') as f:
        citys = json.load(f)
    info = citys['returnValue']
    print(info)
    letters = info.keys()
    for letter in letters:
        print(letter)
        addletter = Letter(letter=letter)
        db.session.add(addletter)
        db.session.commit()
        citys = info[letter]
        for city in citys:
            print(city)
            addcity = City(id=city['id'],regionName=city['regionName'],cityCode=city['cityCode'],pinYin=city['pinYin'],letter_id=Letter.query.filter_by(letter=letter)[0].id)
            db.session.add(addcity)
            db.session.commit()
if __name__ == '__main__':
    insertMysql()
