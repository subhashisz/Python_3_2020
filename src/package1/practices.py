

# 
# 
# dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
# countries = ["Italy", "Germany", "Spain", "USA"]
# country_specialities_iterator = zip(countries, dishes)
# print(country_specialities_iterator)
# 
# country_specialities = list(country_specialities_iterator)
# print(country_specialities) 
# 
# # Python3 program to convert a 
# # list into a tuple 
# def convert(lis): 
#     return tuple(lis) 
# 
# # Driver function 
# lis = [1, 2, 3, 4] 
# print(convert(lis)) 

# 
# 
# l1 = ["a","b","c"]
# l2 = [1,2,3]
# c = zip(l1, l2)
# for i in c:
#     print(i)
# 
# 
# 
# l1 = ["a","b","c"]
# l2 = [1,2,3]
# c = zip(l1,l2)
# z1 = list(c)
# z2 = list(c)
# print(z1)
# 
# print(z2)



dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
country_specialities_zip = zip(dishes,countries)
print(list(country_specialities_zip))

country_specialities_dict = dict(country_specialities_zip)
print(country_specialities_dict)







