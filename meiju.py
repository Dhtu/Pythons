from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'mat', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


for name,member in Weekday.__members__.items():
    print(name,'=>',member)