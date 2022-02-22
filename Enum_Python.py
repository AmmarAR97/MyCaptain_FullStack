from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('Member name: {}'.format(Country.Albania.name),'Member value: {}'.format(Country.Albania.value))
print()

'''
output:
D:\Python\Course\MyCaptain\FullStack Dev\New folder\python_project.py
Member name: Albania Member value: 355
'''