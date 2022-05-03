import math

class Pi_Day:
    def pi_to_number_of_digits(self):
        N = int(input('How many decimal places of Pi do you want : '))
        return f'{math.pi:.{N}}'  # here is how it should look


if __name__ == '__main__':
    p = Pi_Day()
    print(p.pi_to_number_of_digits())