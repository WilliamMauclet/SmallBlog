from models import User, Post, About, ContactInfo


def prefill(db):
    prefill_admin(db)

    prefill_iliad_post(db)
    prefill_kalevala_post(db)
    prefill_goingon_post(db)
    prefill_exampleimage_post(db)

    prefill_aboutme(db)

    prefill_contactinfo(db)

    db.session.commit()


def prefill_admin(db):
    admin = User(username='admin', password='admin')

    db.session.add(admin)


def prefill_iliad_post(db):
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

    db.session.add(Post('Iliad', intro, text))


def prefill_kalevala_post(db):
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

    db.session.add(Post('Kalevala', intro, text, image))


def prefill_goingon_post(db):
    intro = '''This post will feature a long text just going on.'''
    text = '''  It is important to remember that the PDF format is not HTML and knows nothing of HTML tags. When a document is converted to PDF, each piece of the document needs to be converted to its corresponding PDF entity. Therefore, when you introduce non-standard raw HTML into your document, the converter can easily be confused.

Of course, how the converter works under the hood could have some effect on the output as well. For example, if the tool you are using converts the Markdown to HTML and then converts that HTML to PDF, then the raw HTML may have a better chance of being mapped properly. However, if the tool goes straight from a parse tree (list of tokens) to the output format, then it may not know anything about the raw HTML (unless it is also an HTML).'''

    db.session.add(Post('Going on', intro, text))


def prefill_exampleimage_post(db):
    intro = '''An example of how you can add an image anywhere in your post.'''
    text = '''
On olemassa monta eri versiota Lorem Ipsumin kappaleista, mutta suurin osa on kärsinyt muunnoksista joissain muodoissa, kuten huumorin tai sattumanvaraisesti asetetuin sanoin jotka eivät näytä edes vähän uskottavalta. Jos sinä aiot käyttää kappaletta Lorem Ipsumista, sinun pitää tarkistaa, ettei tekstin seassa ole mitään nolostuttavaa.

![Pluto](/static/added/pluto.jpg)

Kaikki Lorem Ipsum-generaattorit Internetissä tuntuvat toistavan ennalta määriteltyjä palasia tarpeen mukaan, tehden tästä ensimmäisen aidon generaattorin Internetissä. Se käyttää 200 latinalaisen sanan sanakirjaa, johon on yhdistetty kourallinen mallilauseiden rakenteita luoden Lorem Ipsumin, joka näyttää järjelliseltä. Generoitu Lorem Ipsum on siten aina vapaa toistoilta, huumorilta jne.'''

    db.session.add(Post('Example image', intro, text))


def prefill_aboutme(db):
    text = '''It's very easy to make some words **bold** and other words 
	*italic* with Markdown. You can even [link to Google!](http://google.com)

	*This text will be italic*
	_This will also be italic_

	**This text will be bold**
	__This will also be bold__

	_You **can** combine them_
	'''

    db.session.add(About(text))


def prefill_contactinfo(db):
    email = ContactInfo('email', 'admin@adminmail.com')
    twitter = ContactInfo('twitter', '@admin')
    phone = ContactInfo('phone', '+32 479 12 30 34')

    db.session.add(email)
    db.session.add(twitter)
    db.session.add(phone)
