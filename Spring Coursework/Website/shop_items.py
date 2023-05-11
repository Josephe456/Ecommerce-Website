from flask_sqlalchemy import SQLAlchemy
from .models import Item
from . import db

def get_products(product):
    #Runs all the get_watch functions to which ensure all items are in the database
    if product == "":
        return [get_watch1(), get_watch2(), get_watch3(), get_watch4()]

    if product == "1":
          return get_watch1()
    if product == "2":
          return get_watch2()
    if product == "3":
          return get_watch3()
    if product == "4":
          return get_watch4()

def get_watch1():
    #with app.app_context():
        #Countdown Watch
        countdown_watch = Item.query.filter_by(id=1).first()  #Checks the item is not already in the database
        if not countdown_watch:
            countdown_watch = Item(id=1,
                                name='Countdown Watch',
                                price='150',
                                description='Introducing the "Countdown Mystery Watch" - a sleek and stylish timepiece with a unique and intriguing feature that sets it apart from other watches. At the heart of this watch is a mysterious countdown that ticks away relentlessly, leaving you wondering what its counting down to. The countdown timer is fully adjustable and can be set for any duration, from a few minutes to several hours or even days. The timers purpose and endpoint are left entirely up to the wearers imagination, making it a truly personal and enigmatic experience. The watchs design is minimalist and modern, featuring a sleek black stainless steel case and a matching mesh strap that is both comfortable and durable. The watch face is uncluttered, with a small digital display for the countdown timer. If you enjoy the thrill of anticipation, the Countdown Mystery Watch is the perfect accessory for anyone who loves a little mystery and excitement in their lives.',
                                envImpact='Environmental Impact: Uses lithium batteries, which have negative impacts on the ecosystems in the countries where lithium is mined.',
                                image='Countdown Watch'
                                )
            db.session.add(countdown_watch)
            db.session.commit()
        return countdown_watch
def get_watch2():
    #with app.app_context():
        #Forgetful Watch
        forgetful_watch = Item.query.filter_by(id=2).first() 
        if not forgetful_watch: 
            forgetful_watch = Item(id=2,
                                name='Memory Watch',
                                price='200',
                                description='Introducing the Memory Watch - a bold and unique timepiece that turns the traditional watch face on its head. This watch features a completely inverted design, with the numbers and markers placed in a reversed order. At first glance, the Memory Watch may seem confusing or even disorienting, but its unconventional layout offers a refreshing and thought-provoking way of telling time. Rather than simply glancing down at your wrist and quickly noting the time, the Upside-Down Watch requires a moment of contemplation and a shift in perspective, making you more mindful of the present moment. The watchs design is classic and timeless, with a brushed stainless steel case and a comfortable brown leather strap. The watch face is uncluttered, with bold, easy-to-read numbers and markers that are sure to turn heads and spark conversation wherever you go. Warning: the watch possesses a powerful amnestic and may cause the wearer to forget the watch immediately after looking at it for the time.',
                                envImpact='Environmental Impact: Manufacturing this watch uses up to 1000 tonnes of CO2, which is linked to global warming.',
                                image='Forgetful Watch'
                                )
            db.session.add(forgetful_watch)
            db.session.commit()
        return forgetful_watch
def get_watch3():
    #with app.app_context():
        #Madness Watch
        madness_watch = Item.query.filter_by(id=3).first() 
        if not madness_watch:
            madness_watch = Item(id=3,
                                name='Galaxy Space Watch',
                                price='1000',
                                description='Introducing the Galaxy Space Watch - a stunning timepiece that captures the beauty and wonder of the cosmos. This watch features a mesmerizing window into the universe on its watch face, showcasing stunning images of galaxies, nebulae, and stars. The Galaxy Space Watch is not only a stunning accessory, but it also offers precise and reliable timekeeping with its high-quality quartz movement. The watch is designed with a sleek black stainless steel case and matching band, making it a versatile and stylish addition to any outfit. The Galaxy Space Watch is the perfect accessory for astronomy enthusiasts, science fiction fans, or anyone who appreciates the beauty and vastness of the universe. Whether youre gazing up at the night sky or simply going about your day, the Galaxy Explorer Watch is sure to capture your imagination and spark conversations wherever you go. Warning: Staring into the watch for long periods of time may cause: psychosis, insanity or even brain-death.',
                                envImpact='Environmental Impact: This watch is constructed from materials only obtained through a manufacturing process that released huge quantities of ionizing radiation, which is linked to increased genetic mutations in wildlife within 100km of the manufacturing location.',
                                image='Madness Watch'
                                )
            db.session.add(madness_watch)
            db.session.commit()
        return madness_watch
def get_watch4():
    #with app.app_context():
        # Time-Travel Watch
        time_travel_watch = Item.query.filter_by(id=4).first() 
        if not time_travel_watch:
            time_travel_watch = Item(id=4,
                                name='Time-Travel Watch',
                                price='500',
                                description='Introducing the Time Travel Watch - a sleek and practical timepiece that allows you to easily adjust the time and date with the push of a button. This watch features user-friendly buttons located on the side of the case, making it simple to adjust the time and date to your preferred settings. At any given time the watch displays a random time and date on its display. A simple press of a button allows the wearer to alter the time and date within a set limit of roughly one year. A glance at this watch by the wearer will transport the user through time to the time listed on the watch. Warning: As the earth is moving through space around the milky way galaxy, being transported backwards or forwards through time does not guarantee that the wearer will also end up on Earth.',
                                envImpact='Environmental Impact: Time-space anomolies may occur through repeated use, increasing the instability of the fabric of reality, also causes damage to the ozone layer through emissions from the watch.',
                                image='Time-Travel Watch'
                                )
            db.session.add(time_travel_watch)
            db.session.commit()
        return time_travel_watch
      