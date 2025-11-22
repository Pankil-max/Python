# s1={1,2,3,6,4}
# s2={3,4,5,6}
# print(s1.union(s2))
# s1.update(s2)
# print(s1.intersection(s2))
# print(s1,s2)

cities1={"tokyo","ktm","delhi"}
cities2={"tokyo","delhi","new york","dharan"}
cities1.intersection_update(cities2)
print(cities1)
#symmetric_difference means those values which are not common

cities1={"tokyo","ktm","delhi"}
cities2={"tokyo","delhi","new york","dharan"}
cities1.symmetric_difference_update(cities2)
cities3={"tokyo","ktm","delhi"}
del cities3
print(cities3)
print(cities1)