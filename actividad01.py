
def leap_year(year):
    if type(year) != int:
        error = 'por favor ingresar un numero'
        return error
    else :
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            result = 'el año es bisiesto'
            return result
        else:
            result = 'el año no es bisiesto'
            return result
    

print(leap_year(2012))
