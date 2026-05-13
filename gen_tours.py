import os

BASE = r'c:/Users/Argen/Downloads/Telegram Desktop/DatkaTravel-main/DatkaTravel-main/tours_pages'

tours = [
    {
        'id': 5, 'slug': 'Bishkek City Tour and Ala-Archa',
        'cat_icon': '🏙️🏔️', 'cat': 'City + Nature Combo', 'cat_data': 'nature',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(30,90,140,0.18) 0%,transparent 60%),linear-gradient(160deg,#060c14 0%,#040809 50%,#04040b 100%)',
        'title': 'All in One-Day: Bishkek City Tour<br>and <em>Ala-Archa National Park</em>',
        'duration': 'Full Day', 'duration_sub': '8-9 Hours', 'difficulty': 'Moderate', 'price': 'From $60',
        'about': 'Within a single day, we introduce you to the history of Bishkek, the colourful streets of Osh Bazaar, and the breathtaking alpine landscape of Ala-Archa National Park. Morning for the city, afternoon for the mountains — the ultimate Kyrgyzstan day.',
        'highlights': ['Morning city tour of Bishkek', 'Osh Bazaar — Central Asia\'s great market', 'Ala-Too Square with Manas statue', 'Traditional Kyrgyz lunch', 'Afternoon hike in Ala-Archa National Park', 'Tian Shan mountain scenery'],
        'itinerary': [('Osh Bazaar & City Walk', 'Start at 9 AM with Bishkek\'s iconic Osh Bazaar, then explore Soviet-era monuments, leafy parks and Ala-Too Square with your expert guide.'), ('Traditional Kyrgyz Lunch', 'Enjoy a sit-down lunch of beshbarmak and samsa at a national restaurant — fuel for the afternoon mountain adventure.'), ('Drive to Ala-Archa (40 min)', 'Leave the city behind as the road climbs through the Chuy Valley foothills. The transformation from urban to wilderness is dramatic.'), ('Afternoon Hike in Ala-Archa', 'A 2-3 hour trail through alpine meadows along the glacial Ala-Archa River. Reach the Ak-Say waterfall and stunning panoramic views.'), ('Return to Bishkek', 'Back at your hotel around 6-7 PM — city and mountain, history and wilderness, all in one perfect day.')],
        'included': ['Private transport all day', 'English-speaking guide', 'National park entrance fee', 'Traditional Kyrgyz lunch', 'Bottled water throughout'],
        'excluded': ['Hiking footwear', 'Souvenirs', 'Tips (appreciated)'],
        'prices': [('$110', 'Solo 1 person'), ('$75', 'Couple 2 people'), ('$60', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(6, '6', 'Nature', 'From $60', 'Chunkurchak & Ala Archa Full Day'), (1, '1', 'City', 'From $35', 'Bishkek City Tour'), (4, '4', 'Nature', 'From $50', 'Wildlife Hiking Ala Archa')],
    },
    {
        'id': 6, 'slug': 'Chunkurchak and Ala Archa National Park',
        'cat_icon': '🏔️🌊', 'cat': 'Nature · Full Day', 'cat_data': 'nature',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(20,110,50,0.18) 0%,transparent 60%),linear-gradient(160deg,#040d07 0%,#040805 50%,#04040b 100%)',
        'title': 'Full Day in Nature: Chunkurchak<br>and <em>Ala Archa National Park</em>',
        'duration': 'Full Day', 'duration_sub': '8-9 Hours', 'difficulty': 'Moderate', 'price': 'From $60',
        'about': 'Join this day-long adventure to explore two of the most renowned natural spots near Bishkek. Discover majestic mountains, enjoy serene river walks, witness breathtaking waterfalls, and savour the flavours of traditional Kyrgyz cuisine.',
        'highlights': ['Chunkurchak gorge — dramatic ravine', 'Pigeon waterfall & suspension bridge', 'Serene Chunkurchak river valley', 'Ala-Archa National Park alpine trails', 'Tian Shan panoramic mountain views', 'Traditional Kyrgyz picnic lunch'],
        'itinerary': [('Departure for Chunkurchak Gorge', 'Leave Bishkek at 9 AM for the dramatic Chunkurchak gorge. Steep cliffs and a river create a breathtaking natural corridor.'), ('Pigeon Waterfall & Suspension Bridge', 'Hike to the Pigeon waterfall and cross the thrilling suspension bridge over the rushing mountain stream.'), ('Kyrgyz Lunch in the Gorge', 'Enjoy a traditional meal in nature — fresh air, mountain views, and hearty Kyrgyz cooking.'), ('Drive to Ala-Archa National Park', 'Transition from gorge to park — both beautiful, both wild, both quintessentially Kyrgyz.'), ('Ala-Archa Valley Trail', 'A gentle to moderate hike through the glacial Ala-Archa valley, surrounded by Tian Shan peaks.'), ('Return to Bishkek', 'Arrive back at your hotel in the evening, refreshed by nature and full of mountain memories.')],
        'included': ['Private 4x4 transport', 'English-speaking nature guide', 'Park entrance fees', 'Traditional Kyrgyz lunch', 'Bottled water & snacks'],
        'excluded': ['Hiking footwear', 'Personal purchases', 'Tips (appreciated)'],
        'prices': [('$110', 'Solo 1 person'), ('$75', 'Couple 2 people'), ('$60', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(4, '4', 'Nature', 'From $50', 'Wildlife Hiking Ala Archa'), (5, '5', 'City+Nature', 'From $60', 'Bishkek City Tour & Ala-Archa'), (12, '12', 'Adventure', 'From $90', 'Nomad Day: Horseback & Archery')],
    },
    {
        'id': 7, 'slug': 'Medieval Burana Tower and Bishkek City Tour',
        'cat_icon': '🏛️', 'cat': 'History · Full Day', 'cat_data': 'history',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(160,110,30,0.18) 0%,transparent 60%),linear-gradient(160deg,#140e04 0%,#0a0803 50%,#04040b 100%)',
        'title': 'Medieval Burana Tower<br>and <em>Bishkek City Tour</em>',
        'duration': 'Full Day', 'duration_sub': '8 Hours', 'difficulty': 'Easy', 'price': 'From $55',
        'about': 'It is the perfect day-trip from Bishkek. Combine a guided tour through Bishkek\'s top attractions and the colourful Osh Bazaar with a visit to the most famous archaeological site in Kyrgyzstan — the 11th-century Burana Tower.',
        'highlights': ['11th-century Burana Tower minaret', 'Ancient balbals (stone warriors) field', 'Osh Bazaar & Soviet-era Bishkek', 'Ala-Too Square & historic monuments', 'Chuy Valley panoramas', 'Traditional Kyrgyz lunch'],
        'itinerary': [('Morning — Bishkek City Tour', 'Begin in Bishkek with Osh Bazaar, Ala-Too Square, the Philharmonic and Victory Square. Your guide weaves the story of Kyrgyzstan from nomadic origins to present day.'), ('Traditional Kyrgyz Lunch', 'Enjoy a hearty lunch at a national restaurant before the afternoon drive into history.'), ('Drive to Burana Tower (1 hr)', 'Head east through the fertile Chuy Valley toward the distant glint of a medieval minaret.'), ('Burana Tower & Balbals', 'Climb the 11th-century minaret for panoramic Chuy Valley views. Explore the open-air museum of balbals — ancient stone warriors.'), ('Archaeological Museum', 'View the collection of Karakhanid artefacts, coins, and ceramics discovered at this Silk Road crossroads.'), ('Return to Bishkek', 'Drive back through the golden valley. Arrive at your hotel around 6 PM.')],
        'included': ['Private transport', 'English-speaking guide', 'Burana Tower entrance fee', 'Traditional Kyrgyz lunch', 'Bottled water'],
        'excluded': ['Souvenir purchases', 'Tips (appreciated)'],
        'prices': [('$100', 'Solo 1 person'), ('$70', 'Couple 2 people'), ('$55', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(8, '8', 'History+Nature', 'From $60', 'Burana Tower & Konorchek Canyons'), (1, '1', 'City', 'From $35', 'Bishkek City Tour'), (9, '9', 'Hiking+History', 'From $70', 'Kol Tor Lake & Burana Tower')],
    },
    {
        'id': 8, 'slug': 'Burana Tower and Konorchek Canyons',
        'cat_icon': '🏛️🏜️', 'cat': 'History + Nature', 'cat_data': 'history',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(160,80,30,0.18) 0%,transparent 60%),linear-gradient(160deg,#140804 0%,#0a0503 50%,#04040b 100%)',
        'title': 'Day Trip to Burana Tower<br>and <em>Konorchek Canyons</em>',
        'duration': 'Full Day', 'duration_sub': '9 Hours', 'difficulty': 'Moderate', 'price': 'From $60',
        'about': 'The most amazing sights of the Chui valley in one day! The ancient Burana Tower is one of Kyrgyzstan\'s most outstanding historical sites, and the famous Konorchek Canyons — formed by red sandy rocks eroded by rain and wind — are equally breathtaking.',
        'highlights': ['11th-century Burana Tower & balbals', 'Red sandstone Konorchek Canyons', 'Chui Valley panoramic landscapes', 'Ancient Silk Road history', 'Labyrinth canyon hike', 'Picnic lunch among the red rocks'],
        'itinerary': [('Burana Tower & Archaeological Site', 'Begin at the iconic Burana Tower — climb the 11th-century minaret, walk the balbal field and explore the on-site museum.'), ('Picnic Lunch', 'A picnic-style lunch with homemade dishes, enjoyed in the Chuy Valley countryside.'), ('Drive to Konorchek Canyons', 'Continue into the rugged landscape of the Konorchek Canyon system — a geological wonder of red sandstone formations.'), ('Canyon Hike', 'Navigate the canyon labyrinth on foot — narrow passages, towering walls of ancient rock, views like another planet.'), ('Summit Viewpoint', 'Climb to the canyon rim for sweeping views across the Chuy Valley to the mountains above Bishkek.'), ('Return to Bishkek', 'Drive back as the sun paints the red rocks golden. Hotel drop-off around 7 PM.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Burana Tower entry fee', 'Picnic lunch & water', 'Canyon trail guidance'],
        'excluded': ['Hiking boots (recommended)', 'Personal purchases', 'Tips (appreciated)'],
        'prices': [('$110', 'Solo 1 person'), ('$75', 'Couple 2 people'), ('$60', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(7, '7', 'History', 'From $55', 'Burana Tower & Bishkek City Tour'), (9, '9', 'Hiking+History', 'From $70', 'Kol Tor Lake & Burana Tower'), (10, '10', 'Nature+History', 'From $60', 'Kegeti Waterfall & Burana Tower')],
    },
    {
        'id': 9, 'slug': 'Kol Tor Lake Hike and Burana Tower',
        'cat_icon': '🥾💧', 'cat': 'Hiking + History', 'cat_data': 'history',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(30,80,150,0.18) 0%,transparent 60%),linear-gradient(160deg,#060c18 0%,#040810 50%,#04040b 100%)',
        'title': 'Scenic Kol Tor Lake Hike &amp;<br><em>Burana Tower</em> in 1 Day',
        'duration': 'Full Day', 'duration_sub': '9-10 Hours', 'difficulty': 'Moderate+', 'price': 'From $70',
        'about': 'Journey from Bishkek to the historic Burana Tower, then hike to the tranquil Kol Tor Lake in the Tien-Shan Mountains. A day of discovery and natural beauty awaits adventurers and history enthusiasts alike.',
        'highlights': ['11th-century Burana Tower minaret', 'Kol Tor glacial mountain lake (2100m)', 'Tien-Shan alpine panoramas', 'River and waterfall landscapes', 'Off-the-beaten-path hiking trail', 'History and nature combined'],
        'itinerary': [('Burana Tower, Tokmok', 'Morning visit to the historic Burana Tower — ascend the minaret, explore the balbal field and the on-site museum.'), ('Drive to Kol Tor Trailhead', 'Continue east along the Chuy Valley and turn into the mountains toward the Kol Tor trailhead.'), ('Kol Tor Trail — Ascent', 'A 3-4 hour hike through juniper forest and mountain meadows, following a river upstream toward the hidden alpine lake.'), ('Kol Tor Lake (2,100 m)', 'Arrive at the emerald-green glacial lake surrounded by grey granite peaks. A moment of perfect mountain serenity.'), ('Picnic & Descent', 'Enjoy a prepared picnic lunch by the lake before descending in golden afternoon light.'), ('Return to Bishkek', 'Hotel drop-off around 7-8 PM. Ancient civilisation meets raw mountain wilderness.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Burana Tower entry', 'Picnic lunch & water', 'Trail safety briefing'],
        'excluded': ['Hiking boots (required)', 'Personal items', 'Tips (appreciated)'],
        'prices': [('$120', 'Solo 1 person'), ('$85', 'Couple 2 people'), ('$70', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(8, '8', 'History+Nature', 'From $60', 'Burana Tower & Konorchek Canyons'), (4, '4', 'Nature', 'From $50', 'Wildlife Hiking Ala Archa'), (11, '11', 'Adventure', 'From $80', 'Horseback Riding Chon Kemin')],
    },
    {
        'id': 10, 'slug': 'Kegeti Waterfall and Burana Tower',
        'cat_icon': '🌊🏛️', 'cat': 'Nature + History', 'cat_data': 'history',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(20,90,40,0.18) 0%,transparent 60%),linear-gradient(160deg,#060c06 0%,#040806 50%,#04040b 100%)',
        'title': 'Full Day Tour to <em>Kegeti Waterfall</em><br>and Medieval Burana Tower',
        'duration': 'Full Day', 'duration_sub': '9 Hours', 'difficulty': 'Moderate', 'price': 'From $60',
        'about': 'A great combination of Kyrgyzstan\'s most famous archaeological site — Burana Tower — and the equally renowned Kegeti Gorge with its natural reserve, alpine forests, river and easily accessible Kegeti waterfall.',
        'highlights': ['11th-century Burana Tower & balbals', 'Kegeti Gorge nature reserve', 'Kegeti waterfall', 'Alpine forest & mountain streams', 'Rich flora and fauna', 'Traditional lunch by the river'],
        'itinerary': [('Burana Tower, Tokmok', 'Ascend the medieval Burana Tower minaret, explore the balbal (stone warrior) field and the archaeological museum showcasing Silk Road history.'), ('Drive to Kegeti Gorge', 'Head northwest into the Kyrgyz mountains toward the Kegeti Gorge — a pristine alpine valley barely touched by tourism.'), ('Kegeti Gorge Trail', 'Walk through the gorge along a mountain river through dense spruce and fir forest. Your guide identifies local medicinal herbs.'), ('Kegeti Waterfall', 'Reach the beautiful Kegeti waterfall — a curtain of white water over granite rocks, surrounded by alpine vegetation.'), ('Lunch by the River', 'Enjoy a prepared Kyrgyz lunch beside the mountain stream — the sound of rushing water, the scent of pine, the taste of home cooking.'), ('Return to Bishkek', 'Drive back through the valley as the afternoon fades to golden evening light. Hotel drop-off around 7 PM.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Burana Tower entry fee', 'Lunch & water', 'Trail guidance'],
        'excluded': ['Hiking boots (recommended)', 'Personal purchases', 'Tips (appreciated)'],
        'prices': [('$110', 'Solo 1 person'), ('$75', 'Couple 2 people'), ('$60', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(7, '7', 'History', 'From $55', 'Burana Tower & Bishkek City Tour'), (6, '6', 'Nature', 'From $60', 'Chunkurchak & Ala Archa'), (4, '4', 'Nature', 'From $50', 'Wildlife Hiking Ala Archa')],
    },
    {
        'id': 11, 'slug': 'Horseback Riding in Chon Kemin National Park',
        'cat_icon': '🐎', 'cat': 'Adventure · Horseback', 'cat_data': 'adventure',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(180,80,20,0.18) 0%,transparent 60%),linear-gradient(160deg,#180a04 0%,#0e0603 50%,#04040b 100%)',
        'title': 'Horseback Riding on the Mountains<br>of <em>Chon Kemin National Park</em>',
        'duration': 'Full Day', 'duration_sub': '8-9 Hours', 'difficulty': 'Moderate', 'price': 'From $80',
        'about': 'The guide will introduce you to the history of the Silk-Road-era Burana Tower, then take you on a horseback ride through the scenic Chon-Kemin National Park — a pristine alpine valley that feels worlds away from any city. Suitable for all riding levels.',
        'highlights': ['11th-century Burana Tower & balbals', 'Horseback riding in Chon Kemin valley', 'River crossings & mountain meadows', 'Alpine forest trails on horseback', 'Nomadic culture & riding traditions', 'Traditional lunch with local family'],
        'itinerary': [('Burana Tower Visit', 'Morning at the archaeological Burana Tower — ascend the minaret, explore the balbal field, and hear about the ancient Karakhanid dynasty.'), ('Drive to Chon Kemin Valley (1 hr)', 'Head east into the pristine Chon Kemin valley — a long, green corridor between forested mountains, almost completely free of tourism.'), ('Meet Your Horse', 'Introduction to your horse, saddle fitting and a brief riding lesson for beginners. Experienced riders join the longer trail directly.'), ('Horseback Trail Ride (3 hrs)', 'Ride through meadows, along mountain rivers and through alpine forest. Your guide shares nomadic horse culture — the heart of Kyrgyz identity.'), ('Traditional Lunch', 'A hearty meal with a local family — beshbarmak, dairy products, and fresh bread.'), ('Return to Bishkek', 'Drive back through the golden Chon Kemin valley. Hotel drop-off around 7 PM.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Burana Tower entry fee', 'Horse, saddle & riding lesson', 'Traditional lunch & water'],
        'excluded': ['Riding gloves', 'Personal insurance', 'Tips (appreciated)'],
        'prices': [('$140', 'Solo 1 person'), ('$100', 'Couple 2 people'), ('$80', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(12, '12', 'Adventure', 'From $90', 'Nomad Day: Horseback & Archery'), (13, '13', 'Song-Kul', 'From $250', '2 Days Song-Kul Lake Nomad'), (7, '7', 'History', 'From $55', 'Burana Tower & Bishkek City Tour')],
    },
    {
        'id': 12, 'slug': 'One Nomad Day: Horseback Riding and Archery',
        'cat_icon': '🐎🏹', 'cat': 'Adventure · Nomadic', 'cat_data': 'adventure',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(200,60,20,0.18) 0%,transparent 60%),linear-gradient(160deg,#1a0604 0%,#0e0403 50%,#04040b 100%)',
        'title': 'One Nomad Day Tour:<br>Horseback Riding, <em>Archery</em> at Chunkurchak',
        'duration': 'Full Day', 'duration_sub': '8-9 Hours', 'difficulty': 'Easy-Moderate', 'price': 'From $90',
        'about': 'One of our favourite trips — a full nomadic adventure in the Chunkurchak gorge. Visit the Pigeon waterfall, cross the suspension bridge, do horseback riding, complete an archery masterclass and enjoy a scenic picnic. The quintessential Kyrgyz nomad experience.',
        'highlights': ['Pigeon waterfall — Chunkurchak gorge', 'Thrilling suspension bridge crossing', 'Horseback riding through the gorge', 'Traditional archery masterclass', 'Nomadic games & activities', 'Mountain picnic with Kyrgyz cuisine'],
        'itinerary': [('Pigeon Waterfall', 'Hike to the beautiful Pigeon waterfall in the Chunkurchak gorge — a dramatic cascade fed by mountain streams.'), ('Suspension Bridge', 'Cross the heart-pumping suspension bridge over the gorge river — a highlight that gets the blood pumping.'), ('Horseback Riding', 'Mount your horse for a scenic ride through the gorge — meadows, river crossings and forest trails. Beginners are fully guided.'), ('Archery Masterclass', 'Learn the ancient nomadic art of archery with a traditional Kyrgyz bow. Surprisingly challenging and deeply satisfying.'), ('Nomadic Games & Activities', 'Try traditional nomadic games — kok-boru polo demonstration, kurash wrestling, and the traditional eagle whistle.'), ('Picnic Lunch with Mountain Views', 'A beautifully arranged Kyrgyz picnic with views across the gorge — fresh bread, cheese, meat dishes and mountain spring water.')],
        'included': ['Private transport', 'English-speaking guide', 'Horse, saddle & instruction', 'Archery lesson & equipment', 'Picnic lunch & water'],
        'excluded': ['Personal insurance', 'Souvenirs', 'Tips (appreciated)'],
        'prices': [('$150', 'Solo 1 person'), ('$110', 'Couple 2 people'), ('$90', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(11, '11', 'Adventure', 'From $80', 'Horseback Riding Chon Kemin'), (6, '6', 'Nature', 'From $60', 'Chunkurchak & Ala Archa'), (3, '3', 'Cultural', 'From $35', 'Kyrgyz Family Dinner')],
    },
    {
        'id': 13, 'slug': '2 Days in Song-Kul Lake as a Nomad',
        'cat_icon': '🏕️💙', 'cat': 'Song-Kul · 2 Days', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(60,80,180,0.18) 0%,transparent 60%),linear-gradient(160deg,#060818 0%,#040510 50%,#04040b 100%)',
        'title': '2 Days in Song-Kul Lake<br>as a <em>Nomad</em>',
        'duration': '2 Days', 'duration_sub': '1 Night in Yurt', 'difficulty': 'Moderate', 'price': 'From $250',
        'about': 'Discover the stunning azure waters of Son-Kul Lake with lush green meadows, go horseback riding, witness breathtaking sunsets, and sleep in a cozy yurt for a truly unique cultural experience at 3,016 metres above sea level.',
        'highlights': ['Song-Kul alpine lake at 3,016 m altitude', 'Overnight stay in traditional yurt', 'Horseback riding along the lakeshore', 'Spectacular mountain sunset & sunrise', 'Nomadic family life and culture', 'Star-gazing at high altitude'],
        'itinerary': [('Day 1 Morning — Departure from Bishkek', 'Early morning departure for the 5-hour drive to Song-Kul, passing through the Suusamyr Valley and over the Kalmak-Ashu Pass (3,447 m).'), ('Day 1 Afternoon — Arrival at Song-Kul', 'Arrive at the sacred lake. Meet your nomadic host family and settle into your traditional yurt. First horseback ride along the lakeshore.'), ('Day 1 Evening — Sunset & Yurt Dinner', 'Watch the sun set over Song-Kul — colours that must be seen to be believed. Dinner with the nomadic family: traditional dishes cooked over an open fire.'), ('Night — Star Gazing', 'With no light pollution at 3,000 m, the night sky is extraordinary. Your guide shares Kyrgyz star lore and nomadic navigation techniques.'), ('Day 2 Morning — Sunrise & Breakfast', 'Wake to a mountain sunrise over the lake. Breakfast of fresh dairy products, bread and tea with the host family.'), ('Day 2 — Return to Bishkek', 'Morning horseback ride, then pack and begin the descent back to Bishkek, arriving in the evening.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Traditional yurt accommodation', 'All meals (dinner, breakfast, lunch)', 'Horseback riding', 'Bottled water throughout'],
        'excluded': ['Alcoholic beverages', 'Personal insurance for altitude', 'Tips (appreciated)'],
        'prices': [('$450', 'Solo 1 person'), ('$320', 'Couple 2 people'), ('$250', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(14, '14', 'Song-Kul', 'From $230', '2-Day Horse Trek to Song Kul'), (15, '15', 'Song-Kul', 'From $250', '3-Day Horse Trek to Song Kul'), (16, '16', 'Issyk-Kul', 'From $100', 'Issyk-Kul Lake Day Tour')],
    },
    {
        'id': 14, 'slug': '2-Day Horse Trek to Song Kul Lake',
        'cat_icon': '🐎💙', 'cat': 'Song-Kul · 2 Days', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(70,50,160,0.18) 0%,transparent 60%),linear-gradient(160deg,#070618 0%,#050410 50%,#04040b 100%)',
        'title': 'Year-Round Adventure:<br>2-Day <em>Horse Trek</em> to Song Kul Lake',
        'duration': '2 Days', 'duration_sub': '1 Night in Yurt', 'difficulty': 'Moderate+', 'price': 'From $230',
        'about': 'This tour caters to adventurers short on time but eager for an immersive experience at Song Kul Lake. Navigate grand mountains, engage with local traditions, and spend nights in authentic yurts beside the sacred lake.',
        'highlights': ['Multi-hour horseback trek to Song-Kul', 'Mountain pass crossings on horseback', 'Song-Kul Lake at 3,016 m altitude', 'Nomadic yurt overnight stay', 'Encounter with nomadic herder families', 'Pristine alpine wilderness'],
        'itinerary': [('Day 1 — Trek Begins', 'Depart early from the trailhead. Mount your horse and begin the ascent through the Naryn mountain system toward Song-Kul. Cross alpine meadows and high passes with spectacular views.'), ('Day 1 Afternoon — Arrival at Song-Kul', 'Arrive at the lake after a 5-6 hour trek. The sight of the sacred azure lake surrounded by green mountains is unforgettable. Settle into your yurt.'), ('Day 1 Evening — Nomadic Life', 'Participate in evening nomadic activities — milking mares, making kumiss, tending the horses. Dinner around the fire.'), ('Day 2 Morning — Lake & Mountains', 'Morning ride along the lakeshore as the mist rises off the water. A moment of extraordinary peace.'), ('Day 2 — Descent & Return', 'Trek back down the mountain on horseback, with different views on the return route. Drive back to Bishkek.')],
        'included': ['Private transport to/from trailhead', 'English-speaking guide', 'Horses for the full trek', 'Traditional yurt accommodation', 'All meals', 'Safety gear'],
        'excluded': ['Riding insurance', 'Personal items', 'Tips (appreciated)'],
        'prices': [('$420', 'Solo 1 person'), ('$300', 'Couple 2 people'), ('$230', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(13, '13', 'Song-Kul', 'From $250', '2 Days Song-Kul Nomad'), (15, '15', 'Song-Kul', 'From $250', '3-Day Horse Trek to Song Kul'), (11, '11', 'Adventure', 'From $80', 'Horseback Riding Chon Kemin')],
    },
    {
        'id': 15, 'slug': '3-Day Horse Trek to Song Kul Lake',
        'cat_icon': '🐎🏔️', 'cat': 'Song-Kul · 3 Days', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(50,40,150,0.18) 0%,transparent 60%),linear-gradient(160deg,#060520 0%,#040415 50%,#04040b 100%)',
        'title': 'Year-Round Adventure:<br>3-Day <em>Horse Trek</em> to Song Kul Lake',
        'duration': '3 Days', 'duration_sub': '2 Nights in Yurt', 'difficulty': 'Hard', 'price': 'From $250',
        'about': 'Embark on an adventurous horse trek to Song Kul Lake, traversing majestic mountains, immersing in local culture, and staying in traditional yurts. All riding levels are welcome for this lifetime journey through the Kyrgyz highlands.',
        'highlights': ['3-day horseback expedition', 'Multiple mountain pass crossings', 'Song-Kul Lake at 3,016 m', '2 nights in traditional yurts', 'Deep nomadic cultural immersion', 'Astronomy & night sky at altitude'],
        'itinerary': [('Day 1 — Bishkek to Kochkor Valley', 'Drive to the Kochkor Valley and begin the first day\'s ride through rolling steppe and foothills toward the mountain approaches.'), ('Day 1 Evening — First Camp', 'Night in a yurt at a nomadic camp. Dinner, kumiss and star-gazing by the fire.'), ('Day 2 — Mountain Passes', 'The most dramatic day: ride over high mountain passes with sweeping views. Reach Song-Kul Lake by afternoon.'), ('Day 2 Evening — Song-Kul Sunset', 'Watch the sunset over the sacred lake from horseback. Dinner with a nomadic family in their lakeside yurt.'), ('Day 3 Morning — Lake & Departure', 'Final sunrise by the lake, morning ride, then the long descent and drive back to Bishkek.')],
        'included': ['Private transport', 'English-speaking guide', 'Horses for all 3 days', '2 nights yurt accommodation', 'All meals throughout', 'Safety equipment'],
        'excluded': ['Riding insurance', 'Personal medication', 'Tips (appreciated)'],
        'prices': [('$500', 'Solo 1 person'), ('$360', 'Couple 2 people'), ('$250', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(14, '14', 'Song-Kul', 'From $230', '2-Day Horse Trek to Song Kul'), (20, '20', 'Lakes', 'From $600', 'Song Kul & Issyk Kul 4 Days'), (13, '13', 'Song-Kul', 'From $250', '2 Days Song-Kul Nomad')],
    },
    {
        'id': 16, 'slug': 'One-Day Adventure to Issyk-Kul Lake',
        'cat_icon': '🌊☀️', 'cat': 'Issyk-Kul · Day Tour', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(20,80,160,0.18) 0%,transparent 60%),linear-gradient(160deg,#040d1e 0%,#030910 50%,#04040b 100%)',
        'title': 'One-Day Adventure to<br>Stunning <em>Issyk-Kul Lake</em>',
        'duration': 'Full Day', 'duration_sub': '10-11 Hours', 'difficulty': 'Easy', 'price': 'From $100',
        'about': 'Discover the cultural and historical highlights of Kyrgyzstan on a one-day tour to Issyk-Kul Lake. Visit the Rukh Ordo cultural complex, ancient petroglyphs, the Hippodrome and the iconic Burana Tower. Take a boat ride on the legendary blue waters.',
        'highlights': ['Rukh Ordo cultural complex', 'Ancient petroglyphs & rock art', 'Hippodrome — traditional Kyrgyz games', 'Burana Tower & balbals', 'Boat ride on Issyk-Kul Lake', 'The "Warm Lake" — never freezes'],
        'itinerary': [('Early Departure from Bishkek', 'Depart at 7 AM for the 3-hour drive east to Issyk-Kul along the scenic Northern Chuy Valley.'), ('Burana Tower Stop', 'A brief visit to the medieval Burana Tower before continuing to the lake.'), ('Rukh Ordo Cultural Complex', 'Visit this extraordinary lakeside complex with chapels dedicated to all major world religions and sculptures by Chingiz Aitmatov.'), ('Ancient Petroglyphs', 'Explore the fascinating collection of ancient rock carvings — some dating back 3,000 years — depicting animals and hunting scenes.'), ('Boat Ride on Issyk-Kul', 'A peaceful boat excursion on the deep blue "Warm Lake" — the world\'s second largest mountain lake — with panoramic views.'), ('Return to Bishkek', 'Drive home through the valley as the evening sky turns the lake to gold.')],
        'included': ['Private transport', 'English-speaking guide', 'Burana Tower entry', 'Rukh Ordo entry', 'Boat ride', 'Lunch & water'],
        'excluded': ['Swimming gear (optional)', 'Personal purchases', 'Tips (appreciated)'],
        'prices': [('$170', 'Solo 1 person'), ('$125', 'Couple 2 people'), ('$100', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(17, '17', 'Issyk-Kul', 'From $250', '2 Days Issyk-Kul Canyons & Horses'), (18, '18', 'Issyk-Kul', 'From $500', '3 Days Issyk-Kul & Eagle Hunting'), (13, '13', 'Song-Kul', 'From $250', '2 Days Song-Kul Nomad')],
    },
    {
        'id': 17, 'slug': '2 Days Issyk Kul Lake Canyons Horse Riding and Yurt Stay',
        'cat_icon': '🌊🐎', 'cat': 'Issyk-Kul · 2 Days', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(10,100,130,0.18) 0%,transparent 60%),linear-gradient(160deg,#040f18 0%,#030b10 50%,#04040b 100%)',
        'title': '2 Days Issyk Kul Lake, Canyons,<br><em>Horse Riding</em> &amp; Yurt Stay',
        'duration': '2 Days', 'duration_sub': '1 Night in Yurt', 'difficulty': 'Moderate', 'price': 'From $250',
        'about': "Explore Kyrgyzstan's Issyk-Kul area on a 2-day adventure. Discover Burana Tower, hike Konorchek & Skazka Canyons, enjoy horseback rides by the lake, and sleep in a traditional yurt. A journey packed with culture and nature.",
        'highlights': ['Burana Tower & archaeological site', 'Konorchek red sandstone canyons', 'Skazka (Fairytale) Canyon', 'Horseback riding by Issyk-Kul lakeshore', 'Traditional yurt overnight', 'Sunrise over the lake'],
        'itinerary': [('Day 1 Morning — Burana Tower & Konorchek Canyon', 'Begin at the historic Burana Tower, then explore the dramatic red sandstone labyrinth of Konorchek Canyon.'), ('Day 1 Afternoon — Issyk-Kul Arrival', 'Arrive at the southern shore of Issyk-Kul. Settle into your lakeside yurt camp.'), ('Day 1 Evening — Horseback Ride & Sunset', 'Evening horseback ride along the Issyk-Kul lakeshore as the sun sets behind the Tian Shan peaks. Dinner in the yurt.'), ('Day 2 Morning — Skazka Canyon', 'Morning visit to the otherworldly Skazka (Fairytale) Canyon — terracotta formations sculpted by wind and rain into shapes that resemble dragons and castles.'), ('Day 2 — Return to Bishkek', 'Drive back through the Chuy Valley with panoramic mountain views. Hotel drop-off in the evening.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Burana Tower & canyon entries', 'Yurt accommodation', 'Horse riding', 'All meals throughout'],
        'excluded': ['Swimming gear', 'Personal insurance', 'Tips (appreciated)'],
        'prices': [('$450', 'Solo 1 person'), ('$330', 'Couple 2 people'), ('$250', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(16, '16', 'Issyk-Kul', 'From $100', 'Issyk-Kul Lake Day Tour'), (18, '18', 'Issyk-Kul', 'From $500', '3 Days Issyk-Kul & Eagle Hunting'), (13, '13', 'Song-Kul', 'From $250', '2 Days Song-Kul Nomad')],
    },
    {
        'id': 18, 'slug': '3 Days Around Issyk-Kul with Eagle Hunting Show',
        'cat_icon': '🦅🌊', 'cat': 'Issyk-Kul · 3 Days', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(10,60,130,0.18) 0%,transparent 60%),linear-gradient(160deg,#030a1e 0%,#020814 50%,#04040b 100%)',
        'title': '3 Days Around Issyk-Kul<br>with <em>Eagle Hunting Show</em>',
        'duration': '3 Days', 'duration_sub': '2 Nights', 'difficulty': 'Moderate', 'price': 'From $500',
        'about': 'During this 3-day tour, you will be trying the national cuisine, riding a horse, witnessing an eagle hunting show, sailing the endless lake on a boat, sleeping in a yurt, visiting museums and parks, roaming canyons with gorges, rivers, waterfalls and so much more!',
        'highlights': ['Traditional eagle hunting show', 'Boat sailing on Issyk-Kul', 'Skazka & Konorchek Canyons', 'Horseback riding by the lake', 'National cuisine tasting', '2 nights accommodation (yurt + hotel)'],
        'itinerary': [('Day 1 — Bishkek to Issyk-Kul North Shore', 'Drive to Cholpon-Ata. Visit the open-air petroglyphs museum and the Rukh Ordo complex. Afternoon boat ride. Overnight in a comfortable hotel.'), ('Day 2 — Eagle Hunting & Canyons', 'Morning eagle hunting show with a traditional berkutchi (eagle hunter). Afternoon exploration of Skazka Canyon. Yurt overnight on the southern shore.'), ('Day 3 — Horse Riding & Return', 'Morning horseback ride along the lakeshore. Visit the Karakol Hippodrome. Afternoon drive back to Bishkek.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Hotel 1 night + Yurt 1 night', 'Eagle hunting show', 'Boat ride', 'Horse riding', 'All meals', 'All entry fees'],
        'excluded': ['International flights', 'Personal insurance', 'Tips (appreciated)'],
        'prices': [('$900', 'Solo 1 person'), ('$680', 'Couple 2 people'), ('$500', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(17, '17', 'Issyk-Kul', 'From $250', '2 Days Issyk-Kul Canyons & Horses'), (19, '19', 'Issyk-Kul', 'From $700', '4 Days Issyk-Kul & Altyn Arashan'), (20, '20', 'Lakes', 'From $600', 'Song Kul & Issyk Kul 4 Days')],
    },
    {
        'id': 19, 'slug': 'Issyk Kul Lake and Altyn Arashan Highlights in 4 Days',
        'cat_icon': '♨️🌊', 'cat': 'Issyk-Kul · 4 Days Premium', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(10,50,120,0.18) 0%,transparent 60%),linear-gradient(160deg,#02081e 0%,#020610 50%,#04040b 100%)',
        'title': 'Issyk Kul Lake and <em>Altyn Arashan</em><br>Highlights in 4 Days',
        'duration': '4 Days', 'duration_sub': '3 Nights', 'difficulty': 'Moderate+', 'price': 'From $700',
        'about': "Discover the Hidden Gems of Issyk Kul Lake and Altyn Arashan, revelling in activities that immerse you in local traditions and breathtaking landscapes. A unique journey blending adventure, culture, and history.",
        'highlights': ['Altyn Arashan thermal hot springs', 'Karakol valley hiking', 'Issyk-Kul lake & canyons', 'Ancient petroglyphs & Dungan mosque', 'Eagle hunting demonstration', 'Horse trekking in alpine valleys'],
        'itinerary': [('Day 1 — Bishkek to Karakol', 'Drive to Karakol via the northern shore of Issyk-Kul. Visit Cholpon-Ata petroglyphs, Rukh Ordo, and arrive at the charming town of Karakol.'), ('Day 2 — Altyn Arashan Valley', 'The highlight: trek or ride by horse into the stunning Altyn Arashan valley. Bathe in the natural thermal hot springs surrounded by Tian Shan peaks.'), ('Day 3 — Karakol & Southern Shore', 'Explore Karakol\'s Orthodox church and unique Dungan mosque. Drive the southern shore visiting Skazka Canyon.'), ('Day 4 — Return via Northern Shore', 'Morning at the lake. Visit the Hippodrome, then the scenic drive back to Bishkek along the Boom Gorge.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', '3 nights accommodation (hotels)', 'All meals', 'Hot spring access', 'All entry fees & activities'],
        'excluded': ['International flights', 'Personal insurance', 'Tips (appreciated)'],
        'prices': [('$1300', 'Solo 1 person'), ('$950', 'Couple 2 people'), ('$700', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(18, '18', 'Issyk-Kul', 'From $500', '3 Days Issyk-Kul & Eagle Hunting'), (21, '21', 'Issyk-Kul', 'From $650', '5 Days Issyk-Kul Hidden Gems'), (20, '20', 'Lakes', 'From $600', 'Song Kul & Issyk Kul 4 Days')],
    },
    {
        'id': 20, 'slug': 'Best of Song Kul and Issyk Kul Lakes Tour in 4 Days',
        'cat_icon': '💙🌊', 'cat': 'Two Lakes · 4 Days', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(40,40,140,0.18) 0%,transparent 60%),linear-gradient(160deg,#050518 0%,#030410 50%,#04040b 100%)',
        'title': 'Best of Song Kul and Issyk Kul<br><em>Lakes Tour</em> in 4 Days',
        'duration': '4 Days', 'duration_sub': '3 Nights', 'difficulty': 'Moderate+', 'price': 'From $600',
        'about': "Explore Song Kul & Issyk Kul Lakes, each offering its own unique experience. Discover nomadic life and untouched nature at Song Kul, and embrace adventure among Issyk Kul's mountains and valleys.",
        'highlights': ['Song-Kul alpine lake (3,016 m)', 'Yurt night at Song-Kul', 'Issyk-Kul lake adventures', 'Skazka Canyon & petroglyphs', 'Horseback riding at both lakes', 'Cultural immersion with nomads'],
        'itinerary': [('Day 1 — Bishkek to Song-Kul', 'Drive via the Kalmak-Ashu Pass to the sacred Song-Kul Lake. Horseback ride, yurt accommodation, sunset over the steppe.'), ('Day 2 — Song-Kul to Issyk-Kul', 'Morning at Song-Kul before the drive east and descent to the Issyk-Kul basin. Check into lakeside accommodation.'), ('Day 3 — Issyk-Kul Exploration', 'Skazka Canyon, Konorchek Canyon, and Rukh Ordo cultural complex. Evening boat ride on the lake.'), ('Day 4 — Return to Bishkek', 'Morning at the lake, then the scenic Boom Gorge drive back to Bishkek.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Yurt 1 night + Hotel 2 nights', 'Horse riding at both lakes', 'All meals', 'All entry fees'],
        'excluded': ['International flights', 'Personal insurance', 'Tips (appreciated)'],
        'prices': [('$1100', 'Solo 1 person'), ('$820', 'Couple 2 people'), ('$600', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(13, '13', 'Song-Kul', 'From $250', '2 Days Song-Kul Nomad'), (19, '19', 'Issyk-Kul', 'From $700', '4 Days Issyk-Kul & Altyn Arashan'), (21, '21', 'Issyk-Kul', 'From $650', '5 Days Issyk-Kul Hidden Gems')],
    },
    {
        'id': 21, 'slug': '5 Days Around the Hidden Gems of Issyk-Kul',
        'cat_icon': '🌟🌊', 'cat': 'Issyk-Kul · 5 Days Premium', 'cat_data': 'lake',
        'gradient': 'radial-gradient(ellipse 80% 60% at 70% 30%,rgba(20,30,120,0.2) 0%,transparent 60%),radial-gradient(ellipse 60% 50% at 20% 80%,rgba(0,100,120,0.12) 0%,transparent 60%),linear-gradient(160deg,#030415 0%,#02030e 50%,#04040b 100%)',
        'title': '5 Days Around the Hidden Gems<br>of <em>Issyk-Kul Lake</em>',
        'duration': '5 Days', 'duration_sub': '4 Nights', 'difficulty': 'Moderate', 'price': 'From $650',
        'about': "This 5-day adventure is crafted to be the trip of a lifetime. You'll visit 10+ destinations and enjoy numerous authentic experiences unique to Kyrgyzstan. The complete package of cultural immersion and adventure.",
        'highlights': ['10+ unique destinations', 'Eagle hunting show', 'Altyn Arashan hot springs', 'Skazka & Konorchek Canyons', 'Horseback riding', 'Yurt stay & hotel nights', 'Ancient petroglyphs & monuments', 'Boat ride on Issyk-Kul'],
        'itinerary': [('Day 1 — Bishkek to Northern Shore', 'Depart for Issyk-Kul. Visit Burana Tower and Cholpon-Ata petroglyphs. Check into lakeside hotel.'), ('Day 2 — Rukh Ordo & Boat Ride', 'Morning at the Rukh Ordo cultural complex. Afternoon boat excursion on Issyk-Kul. Eagle hunting show demonstration.'), ('Day 3 — Karakol & Altyn Arashan', 'Drive east to Karakol. Trek into the Altyn Arashan valley and soak in natural thermal hot springs.'), ('Day 4 — Southern Shore Canyons', 'Explore Skazka Canyon and Konorchek Canyon. Horseback riding along the lakeshore. Yurt overnight.'), ('Day 5 — Return to Bishkek', 'Final morning by the lake, then the scenic drive home via the spectacular Boom Gorge.')],
        'included': ['Private 4x4 transport', 'English-speaking guide', 'Hotels 3 nights + Yurt 1 night', 'Eagle hunting show', 'Boat ride', 'Horse riding', 'Hot spring access', 'All meals', 'All entry fees'],
        'excluded': ['International flights', 'Personal insurance', 'Tips (appreciated)'],
        'prices': [('$1200', 'Solo 1 person'), ('$880', 'Couple 2 people'), ('$650', 'Group 3-4 people'), ('REQUEST', 'Large group 5+')],
        'related': [(18, '18', 'Issyk-Kul', 'From $500', '3 Days Issyk-Kul & Eagle Hunting'), (19, '19', 'Issyk-Kul', 'From $700', '4 Days Issyk-Kul & Altyn Arashan'), (20, '20', 'Lakes', 'From $600', 'Song Kul & Issyk Kul 4 Days')],
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{slug} — Datka Travel</title>
  <link rel="stylesheet" href="../assets/css/luxury.css">
  <style>.tour-hero-bg{{background:{gradient}}}</style>
</head>
<body>
<nav class="lux-nav"><div class="container"><div class="nav-inner">
  <a href="../index_second.html" class="nav-logo">Datka <span>Travel</span></a>
  <ul class="nav-links"><li><a href="../index_second.html#tours">All Tours</a></li><li><a href="#book">Book Now</a></li><li><a href="../index_second.html#contact">Contact</a></li></ul>
  <a href="#book" class="btn btn-gold nav-cta" style="padding:11px 26px;font-size:10.5px;">Book Now</a>
  <div class="burger" id="burger"><span></span><span></span><span></span></div>
</div></div></nav>
<div class="mobile-menu" id="mobileMenu"><a href="../index_second.html">Home</a><a href="../index_second.html#tours">All Tours</a><a href="#book">Book Tour</a></div>

<section class="tour-hero">
  <div class="tour-hero-bg"></div><div class="tour-hero-overlay"></div>
  <img class="tour-hero-icon" src="../img/png/{id}.png" alt="">
  <div class="tour-hero-content"><div class="container">
    <div class="breadcrumb"><a href="../index_second.html">Home</a><span>/</span><a href="../index_second.html#tours">Tours</a><span>/</span><span style="color:var(--gold);">{slug}</span></div>
    <span class="tour-hero-category">{cat_icon} {cat}</span>
    <h1 class="tour-hero-title">{title}</h1>
    <div class="tour-hero-actions"><a href="#book" class="btn btn-gold">Book This Tour</a><a href="#itinerary" class="btn btn-outline-gold">See Itinerary</a></div>
  </div></div>
</section>

<div class="tour-stats"><div class="container"><div class="tour-stats-grid">
  <div class="tour-stat"><div class="tour-stat-icon">⏱️</div><div class="tour-stat-value">{duration}</div><div class="tour-stat-label">{duration_sub}</div></div>
  <div class="tour-stat"><div class="tour-stat-icon">🎯</div><div class="tour-stat-value">{difficulty}</div><div class="tour-stat-label">Difficulty</div></div>
  <div class="tour-stat"><div class="tour-stat-icon">👥</div><div class="tour-stat-value">Private</div><div class="tour-stat-label">Group Type</div></div>
  <div class="tour-stat"><div class="tour-stat-icon">🌍</div><div class="tour-stat-value">English</div><div class="tour-stat-label">Guide Language</div></div>
  <div class="tour-stat"><div class="tour-stat-icon">💰</div><div class="tour-stat-value">{price}</div><div class="tour-stat-label">Per Person</div></div>
</div></div></div>

<section class="section"><div class="container"><div class="tour-about">
  <div class="tour-about-text reveal-left">
    <div class="label">About This Tour</div>
    <h2 class="h-display h3" style="margin-bottom:22px;">Discover <em>{slug}</em></h2>
    <p>{about}</p>
    <p>With Datka Travel you travel privately — your own guide, your own vehicle, your own pace. We've pre-tested every tour and only work with the finest local guides who know these landscapes deeply.</p>
  </div>
  <div class="tour-highlights reveal-right">
    <div class="tour-highlights-title">Tour Highlights</div>
    {highlights_html}
  </div>
</div></div></section>

<section class="section" id="itinerary"><div class="container">
  <div class="section-head reveal"><div class="label">Step by Step</div><h2 class="h-display h2" style="margin-bottom:60px;">What to <em>Expect</em></h2></div>
  <div style="max-width:760px;"><div class="itinerary">{itinerary_html}</div></div>
</div></section>

<section class="section-sm"><div class="container">
  <div class="section-head reveal"><div class="label">What's Covered</div><h2 class="h-display h3" style="margin-bottom:48px;">Included &amp; <em>Excluded</em></h2></div>
  <div class="incl-grid">
    <div class="incl-card reveal d1"><div class="incl-card-title gold">What's Included</div>{included_html}</div>
    <div class="incl-card reveal d2"><div class="incl-card-title red">Not Included</div>{excluded_html}</div>
  </div>
</div></section>

<section class="section-sm"><div class="container">
  <div class="section-head center reveal"><div class="label">Pricing</div><h2 class="h-display h3" style="margin-bottom:48px;">Tour <em>Prices</em></h2></div>
  <div class="prices-grid">{prices_html}</div>
</div></section>

<section class="section-sm" id="book"><div class="container"><div class="booking-wrap reveal">
  <div class="booking-title">Book This <em style="font-style:italic;color:var(--gold);">Tour</em></div>
  <p class="booking-sub">Fill out the form and we'll confirm within 24 hours</p>
  <form class="lux-form">
    <div class="lux-input-wrap"><label>Full Name</label><input type="text" class="lux-input" placeholder="Your full name" required></div>
    <div class="lux-input-wrap"><label>Phone Number</label><input type="tel" class="lux-input" placeholder="+1 234 567 890" required></div>
    <div class="lux-input-wrap"><label>Email Address</label><input type="email" class="lux-input" placeholder="your@email.com" required></div>
    <div class="lux-input-wrap"><label>Preferred Date</label><input type="date" class="lux-input"></div>
    <div class="lux-input-wrap"><label>Number of Guests</label><input type="number" class="lux-input" placeholder="e.g. 2" min="1"></div>
    <div class="lux-input-wrap"><label>Special Requests</label><textarea class="lux-input lux-textarea" placeholder="Any notes, fitness level, dietary requirements, or questions..."></textarea></div>
    <button type="submit" class="btn btn-gold" style="width:100%;justify-content:center;">Confirm Booking</button>
    <p class="form-agree">By submitting you agree to the processing of personal data. Payment is made upon meeting our guide.</p>
  </form>
</div></div></section>

<section class="section-sm"><div class="container">
  <div class="section-head center reveal"><div class="label">You Might Also Like</div><h2 class="h-display h3" style="margin-bottom:48px;">Other <em>Tours</em></h2></div>
  <div class="related-grid">{related_html}</div>
</div></section>

<footer class="lux-footer"><div class="container"><div class="footer-bottom">
  <a href="../index_second.html" class="nav-logo">Datka <span>Travel</span></a>
  <span class="footer-copy">© 2016–2024 Datka Travel. All Rights Reserved.</span>
</div></div></footer>
<script src="../assets/js/luxury.js"></script>
</body></html>'''

def gen_page(t):
    highlights_html = ''.join(
        f'<div class="tour-highlight-item"><div class="tour-highlight-dot"></div><div class="tour-highlight-text">{h}</div></div>'
        for h in t['highlights']
    )
    itinerary_html = ''.join(
        f'<div class="itinerary-item reveal d{min(i+1,6)}"><div class="itinerary-num">{i+1}</div><div class="itinerary-body"><div class="itinerary-place">{place}</div><div class="itinerary-desc">{desc}</div></div></div>'
        for i, (place, desc) in enumerate(t['itinerary'])
    )
    included_html = ''.join(f'<div class="incl-item"><span class="incl-icon">✅</span>{item}</div>' for item in t['included'])
    excluded_html = ''.join(f'<div class="incl-item"><span class="incl-icon">❌</span>{item}</div>' for item in t['excluded'])
    prices_html = ''
    for i, (amt, grp) in enumerate(t['prices']):
        featured = 'featured' if i in [1, 2] else ''
        size_style = 'font-size:28px;' if amt == 'REQUEST' else ''
        prices_html += f'<div class="price-card {featured} reveal"><div class="price-amount" style="{size_style}">{amt}</div><div class="price-unit">per person</div><div class="price-group">{grp}</div></div>'
    related_html = ''.join(
        f'<a href="tour-{rid}.html" class="tour-card reveal d{i+1}"><div class="tour-card-img"><div class="tour-card-img-inner" style="--img:url(\'../img/png/{rimg}.png\')"></div><div class="tour-card-img-overlay"></div><span class="tour-card-category">{rcat}</span><span class="tour-card-price">{rprice}</span></div><div class="tour-card-body"><h3 class="tour-card-title">{rtitle}</h3><div class="tour-card-meta"><span class="tour-card-link">Explore →</span></div></div></a>'
        for i, (rid, rimg, rcat, rprice, rtitle) in enumerate(t['related'])
    )
    return TEMPLATE.format(
        slug=t['slug'], gradient=t['gradient'], id=t['id'],
        cat_icon=t['cat_icon'], cat=t['cat'],
        title=t['title'], duration=t['duration'], duration_sub=t['duration_sub'],
        difficulty=t['difficulty'], price=t['price'], about=t['about'],
        highlights_html=highlights_html, itinerary_html=itinerary_html,
        included_html=included_html, excluded_html=excluded_html,
        prices_html=prices_html, related_html=related_html
    )

created = []
for t in tours:
    path = os.path.join(BASE, f'tour-{t["id"]}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(gen_page(t))
    created.append(f'tour-{t["id"]}.html')

print('Created:', ', '.join(created))
