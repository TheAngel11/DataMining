from section1 import Section1
from section2 import Section2
from section3 import Section3
from section4 import Section4

if __name__ == '__main__':
    section1 = Section1()
    section1.run_all()
    section2 = Section2(section1)
    section2.run_all()
    section3 = Section3(section2)
    section3.run_all()
    section4 = Section4(section2)
    section4.run_all()
