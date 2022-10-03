from user import Admin, User


def main():
    ad = Admin("Kosh","Goroshek228")
    ad.change_name("odn")
    ad.hi()
    print(ad.name,ad.password)

if __name__ == "__main__":
    main()