from message import Emoji, Message
from user import Admin, User


def main():
    ad = Admin("Kosh","Goroshek228")
    ad.change_name("odn")
    ad.hi()
    print(ad.name,ad.password)
    m = Message('Kit', 'I love you, baby!')
    m.change_text('lol')
    print(m.username, m.text)
    e = Emoji('Lis', 'Me too!')
    e.smile()
    print(e.username, e.text)


if __name__ == "__main__":
    main()