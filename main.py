from user import Admin, User


def main():
    u = User("Lisa","QWERTY123")
    ad = Admin("Kosh","Goroshek228")
    ad.change_name("odn")
    ad.hi()

    print(u.name,u.password)
    print(ad.name,ad.password)

if __name__ == "__main__":
    main()