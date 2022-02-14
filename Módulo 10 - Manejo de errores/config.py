def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except PermissionError:
        print('Has no permissions to access config.txt')


if __name__ == '__main__':
    main()
