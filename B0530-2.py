class person :
    def __init__ (self, name, age) :
        self.name = name
        self.age = age
        
    def __repr__ (self) : # 객체를 문자열로 변환하여 반환
        return "<name : %s, age : %s>" %(self.name, self.age)
    
def kage (person) : # class를 instance한 함수 만들기
    return person.age

people = [person('lim', 20), person('daramji', 3)]

print (sorted(people, key = kage))