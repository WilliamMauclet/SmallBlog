from models import User, Post, About, ContactInfo

from app import db, app
import os, sys


def prefill(db):
    db.session.add_all((
        iliad_post(),
        kalevala_post(),
        goingon_post(),
        exampleimage_post(),
        aboutme(),
        email_contactinfo(),
        twitter_contactinfo(),
        phone_contactinfo()
    ))
    db.session.commit()

def admin():
    password = sys.argv[0]
    if password == "$password$":
        raise RuntimeError("Please set password in the Dockerfile!")

    username = 'admin'

    db.session.add(User(username=username, password=password))
    db.session.commit()

def iliad_post():
    intro = '''Sing, O goddess, the anger of Achilles son of Peleus, that brought countless ills upon the Achaeans.'''
    text = '''
	Many a brave soul did it send hurrying down to Hades, and many a hero did it yield a prey to dogs and vultures,
	for so were the counsels of Jove fulfilled from the day on which the son of Atreus, king of men, and great Achilles,
	first fell out with one another.

	And which of the gods was it that set them on to quarrel? It was the son of Jove and Leto; for he was angry with
	the king and sent a pestilence upon the host to plague the people, because the son of Atreus had dishonoured Chryses
	his priest. Now Chryses had come to the ships of the Achaeans to free his daughter, and had brought with him a
	great ransom: moreover he bore in his hand the sceptre of Apollo wreathed with a suppliant's wreath and he
	besought the Achaeans, but most of all the two sons of Atreus, who were their chiefs. '''

    return Post('Iliad', intro, text)


def kalevala_post():
    intro = '''MASTERED by desire impulsive,
	By a mighty inward urging,
	I am ready now for singing'''
    text = '''
	Ready to begin the chanting
	Of our nation's ancient folk-song
	Handed down from by-gone ages.
	In my mouth the words are melting,
	From my lips the tones are gliding,
	From my tongue they wish to hasten;
	When my willing teeth are parted,
	When my ready mouth is opened,
	Songs of ancient wit and wisdom
	Hasten from me not unwilling.'''

    image = 'AiguilleDuMidi.jpg'

    return Post('Kalevala', intro, text, image)


def goingon_post():
    intro = '''This post will feature a long text just going on.'''
    text = '''  It is important to remember that the PDF format is not HTML and knows nothing of HTML tags. When a document is converted to PDF, each piece of the document needs to be converted to its corresponding PDF entity. Therefore, when you introduce non-standard raw HTML into your document, the converter can easily be confused.

Of course, how the converter works under the hood could have some effect on the output as well. For example, if the tool you are using converts the Markdown to HTML and then converts that HTML to PDF, then the raw HTML may have a better chance of being mapped properly. However, if the tool goes straight from a parse tree (list of tokens) to the output format, then it may not know anything about the raw HTML (unless it is also an HTML).'''

    return Post('Going on', intro, text)


def exampleimage_post():
    intro = '''An example of how you can add an image anywhere in your post.'''
    text = '''
On olemassa monta eri versiota Lorem Ipsumin kappaleista, mutta suurin osa on kärsinyt muunnoksista joissain muodoissa, kuten huumorin tai sattumanvaraisesti asetetuin sanoin jotka eivät näytä edes vähän uskottavalta. Jos sinä aiot käyttää kappaletta Lorem Ipsumista, sinun pitää tarkistaa, ettei tekstin seassa ole mitään nolostuttavaa.

![Pluto](/static/added/pluto.jpg)

Kaikki Lorem Ipsum-generaattorit Internetissä tuntuvat toistavan ennalta määriteltyjä palasia tarpeen mukaan, tehden tästä ensimmäisen aidon generaattorin Internetissä. Se käyttää 200 latinalaisen sanan sanakirjaa, johon on yhdistetty kourallinen mallilauseiden rakenteita luoden Lorem Ipsumin, joka näyttää järjelliseltä. Generoitu Lorem Ipsum on siten aina vapaa toistoilta, huumorilta jne.'''

    return Post('Example image', intro, text)


def aboutme():
    text = '''It's very easy to make some words **bold** and other words
	*italic* with Markdown. You can even [link to Google!](http://google.com)

	*This text will be italic*
	_This will also be italic_

	**This text will be bold**
	__This will also be bold__

	_You **can** combine them_
	'''

    return About(text)


def email_contactinfo():
    return ContactInfo('email', 'admin@adminmail.com')


def twitter_contactinfo():
    return ContactInfo('twitter', '@admin')


def phone_contactinfo():
    return ContactInfo('phone', '+32 479 12 30 34')

    return email, twitter, phone


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        prefill(db)
