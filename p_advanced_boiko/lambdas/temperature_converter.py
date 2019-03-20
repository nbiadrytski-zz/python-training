temps = [39.2, 36.5, 37.3, 38, 37.8]

farenh_temp = list(map(lambda x: (float(9)/5)*x + 32, temps))

cels_temp = list(map(lambda x: (float(9)/5) * (x-32), farenh_temp))

print(f'Temperature in F: {farenh_temp}')
print(f'Temperature in C: {cels_temp}')