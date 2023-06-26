def feet2meters(feet):
    foot_to_meter =3.281
    return round(feet/foot_to_meter, 2)


def main():
    input_data = input("Сколько футов:")
    feet = float(input_data[0:-2])
    meters = feet2meters(feet)
    print(f'Это будет {meters} метров.')


if __name__ == '__main__':
    main()