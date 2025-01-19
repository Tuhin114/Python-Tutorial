def f_to_c(f):
    return (5 / 9) * (f - 32)

f = int(input("Enter the temperature in Fahrenheit: "))

print(f"{round(f_to_c(f), 2)} degrees Celsius")