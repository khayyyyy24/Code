from Math_function import add, multiply, divide


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    result = None

    if operator == "+":
        result = add(data_1, data_2)
    elif operator == "-":
        result = data_1 - data_2
    elif operator == "*":
        result = multiply(data_1, data_2)
    elif operator == "/":
        if data_2 == 0:
            print("Tidak dapat dibagi oleh nol.")
            return
        result = divide(data_1, data_2)
    else:
        print("Operator tidak valid.")
        return

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))
