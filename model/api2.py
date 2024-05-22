from requests import get
island = input('island (Biscoe - 0, Dream - 1, Torgersen - 2) = ')
bill_length_mm = input('bill length (mm) = ')
bill_depth_mm = input('bill depth (mm) = ')
flipper_length_mm = input('flipper length (mm) = ')
body_mass_g = input('body mass (g) = ')
year = input('year (2007-2009) = ')
print(get(f'http://127.0.0.1:5000/api2', json={'island': island, 'bill_length_mm': bill_length_mm,
                                               'bill_depth_mm': bill_depth_mm, 'flipper_length_mm': flipper_length_mm,
                                               'body_mass_g': body_mass_g, 'year': year
                                               }).json())

# 2
# 39.1
# 18.7
# 181.0
# 3750.0
# 2007