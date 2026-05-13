const tours = [
    {
        id: 1,
        link: '../tour-components/tours/bishkek-city-tour.html',
        imageUrl: 'img/png/1.png',
        price: 'From 35 USD per person',
        title: 'Private Bishkek City Tour: Soviet to Modern',
        description: 'Discover Bishkek on a half-day tour with an English-speaking guide. Visit iconic spots like Ala-Too Square and Osh Bazaar. Dive into Kyrgyz history, admire Soviet-era architecture, and savor a local lunch at a national restaurant. Ideal for first-time visitors.'
    },
    {
        id: 2,
        link: './link/linl/index.html',
        imageUrl: 'img/png/2.png',
        price: 'From 40 USD per person',
        title: '4 Hours Private Bishkek Food Tasting Tour',
        description: 'Embark on a flavorful journey through Bishkek, visiting three authentic restaurants known for their excellent Kyrgyz cuisine. Discover the true taste of the nations culinary heritage, and immerse yourself in the vibrant culture and history of the city.'
    },
    {
        id: 3,
        link: './link/linl/index.html',
        imageUrl: 'img/png/3.png',
        price: 'From 35 USD per person',
        title: 'Kyrgyz Family Dinner: Meet, Eat, and Talk',
        description: 'Experience genuine Kyrgyz hospitality with a local family dinner. Help prepare traditional dishes, including boorsok, and delve into daily life and culture. A memorable dive into authentic living, perfect for cultural explorers.'
    },
    {
        id: 4,
        link: './link/linl/index.html',
        imageUrl: 'img/png/4.png',
        price: 'From 50 USD per person',
        title: 'Wildlife hiking adventure in Ala Archa National Park',
        description: 'There are numerous hiking options, from gentle strolls along the Ala-Archa valley floor to serious mountaineering. In addition to the mountains, rivers and waterfalls are is the unique and rich fauna and flora.'
    },
    {
        id: 5,
        link: './link/linl/index.html',
        imageUrl: 'img/png/5.png',
        price: 'From 60 USD per person',
        title: 'All in one-day: Bishkek city tour and Ala-Archa National Park',
        description: 'Within a one-day tour, we will introduce you to the history of Bishkek, the colorful streets of Osh Bazaar, and the amazing landscape of Ala-Archa National Park.'
    },
    {
        id: 6,
        link: './link/linl/index.html',
        imageUrl: 'img/png/6.png',
        price: 'From 60 USD per person',
        title: 'Full Day in Nature: Chunkurchak and Ala Archa National Park',
        description: 'Join this day-long adventure to explore two of the most renowned natural spots near Bishkek. Discover majestic mountains, enjoy serene river walks, witness breathtaking waterfalls, and savor the flavors of traditional Kyrgyz cuisine!'
    },
    {
        id: 7,
        link: './link/linl/index.html',
        imageUrl: 'img/png/7.png',
        price: 'From 55 USD per person',
        title: 'Medieval Burana Tower and Bishkek city tour',
        description: 'It’s the perfect day-trip from Bishkek and can be visited at any time of year. It combines a guided tour through Bishkek’s top attractions, colorful streets of Osh bazaar market with a trip to the most famous archaeological sites - Burana Tower.'
    },
    {
        id: 8,
        link: './link/linl/index.html',
        imageUrl: 'img/png/8.png',
        price: 'From 60 USD per person',
        title: 'Day Trip to Burana Tower and Konorchek Canyons',
        description: 'The most amazing sights of the Chui valley in one day! The ancient and impressive Burana Tower is one of Kyrgyzstan’s most outstanding historical sites, and the famous Konorchek Canyons, formed by red sandy rocks eroded by rain and wind, are equally breathtaking.'
    },
    {
        id: 9,
        link: './link/linl/index.html',
        imageUrl: 'img/png/9.png',
        price: 'From 70 USD per person',
        title: 'Scenic Kol Tor Lake Hike & Burana Tower in 1 Day',
        description: 'Journey from Bishkek to the historic Burana Tower, then hike to tranquil Kol Tor Lake in the Tien-Shan Mountains. A day of discovery and natural beauty awaits adventurers and history enthusiasts.'
    },
    {
        id: 10,
        link: './link/linl/index.html',
        imageUrl: 'img/png/10.png',
        price: 'From 60 USD per person',
        title: 'Full day tour to Kegeti waterfall and Medieval Burana tower',
        description: 'This one-day tour is a great combination of most famous archaeological sites - Burana Tower and no less famous Kegeti Gorge with its natural reserve, alpine forests, river and easily accessible Kegeti waterfall.'
    },
    {
        id: 11,
        link: './link/linl/index.html',
        imageUrl: 'img/png/11.png',
        price: 'From 80 USD per person',
        title: 'Horseback riding on the mountains of Chon Kemin National Park',
        description: 'During this tour, the guide will introduce you to the history of Silk-Road-era Burana Tower, with a horseback ride through scenic Chon-Kemin National Park. It is suitable for both horseback riding enthusiasts and beginners.'
    },
    {
        id: 12,
        link: './link/linl/index.html',
        imageUrl: 'img/png/12.png',
        price: 'From 90 USD per person',
        title: 'One nomad day tour: Horseback riding, archery at Chunkurchak',
        description: 'One of our favorite trips in which we will visit the Pigeon waterfall, suspension bridge, do horseback riding, archery masterclass and have a picnic with a view of the beautiful landscapes of the Chunkurchak gorge.'
    },
    {
        id: 13,
        link: './link/linl/index.html',
        imageUrl: 'img/png/13.png',
        price: 'From 250 USD per person',
        title: '2-Days in Song-Kul Lake as Nomad - horseback riding and yurt stay',
        description: 'Discover the stunning azure waters of Son-Kul Lake with lush green meadows, go horseback riding, witness breathtaking sunsets, and sleep in a cozy yurt for a truly unique cultural experience.'
    },
    {
        id: 14,
        link: './link/linl/index.html',
        imageUrl: 'img/png/14.png',
        price: 'From 230 USD per person',
        title: 'Year-Round Adventure: 2 Days Horse Trek to Song Kul Lake',
        description: 'his tour caters to adventurers short on time but eager for an immersive experience at Song Kul Lake. Navigate grand mountains, engage with local traditions, and spend nights in authentic yurts.'
    },
    {
        id: 15,
        link: './link/linl/index.html',
        imageUrl: 'img/png/15.png',
        price: 'From 250 USD per person',
        title: 'Year-Round Adventure: 3 Days Horse Trek to Song Kul Lake',
        description: 'Embark on an adventurous horse trek to Song Kul Lake, traversing majestic mountains, immersing in local culture, and staying in traditional yurts. All riding levels welcome for a lifetime journey.'
    },
    {
        id: 16,
        link: './link/linl/index.html',
        imageUrl: 'img/png/16.png',
        price: 'From 100 USD per person',
        title: 'One-day adventure to the stunning Issyk Kul Lake',
        description: 'Discover the cultural and historical highlights of Kyrgyzstan on a one-day tour to Issyk-Kul Lake. Visit the Rukh Ordo cultural complex, ancient petroglyphs, the Hippodrome, and the iconic Burana Tower. Take a boat ride on the waters of Issyk-Kul Lake for a memorable experience.'
    },
    {
        id: 17,
        link: './link/linl/index.html',
        imageUrl: 'img/png/17.png',
        price: 'From 250 USD per person',
        title: '2 Days Issyk Kul Lake Canyons Horse Riding and Yurt Stay',
        description: "Explore Kyrgyzstan's Issyk-Kul area on a 2-day adventure. Discover Burana Tower, hike Konorchek & Skazka Canyons, enjoy horseback rides by the lake, and sleep in a traditional yurt. A journey packed with culture and nature."
    },
    {
        id: 18,
        link: './link/linl/index.html',
        imageUrl: 'img/png/18.png',
        price: 'From 500 USD per person',
        title: '3-days around Issyk-Kul lake with Yurt stay and Eagle hunting show',
        description: 'TDuring this 3-day tour, you will be trying the national cuisine, riding a horse, witnessing an eagle hunting show, sailing the endless lake on the boat, sleeping in a yurt, visiting museums with parks, roaming the canyons with gorges, rivers, waterfalls and so much more!'
    },
    {
        id: 19,
        link: './link/linl/index.html',
        imageUrl: 'img/png/19.png',
        price: 'From 700 USD per person',
        title: 'Issyk Kul Lake and Altyn Arashan Highlights in 4 days',
        description: 'Discover the Hidden Gems of Issyk Kul Lake and Altyn Arashan, reveling in activities that immerse you in local traditions and breathtaking landscapes. A unique journey blending adventure, culture, and history.'
    },
    {
        id: 20,
        link: './link/linl/index.html',
        imageUrl: 'img/png/20.png',
        price: 'From 600 USD per person',
        title: 'Best of Song Kul and Issyk Kul Lakes Tour in 4 Days',
        description: "Explore Song Kul & Issyk Kul Lakes, each offering its own unique experience. Discover nomadic life and untouched nature at Song Kul, and embrace adventure among Issyk Kul's mountains and valleys. A journey of stunning landscapes, rich culture, and unforgettable memories."
    },
    {
        id: 21,
        link: './link/linl/index.html',
        imageUrl: 'img/png/21.png',
        price: 'From 650 USD per person',
        title: '5-days around the hidden gems of Issyk-Kul lake',
        description: "This 5-day adventure is crafted to be the trip of a lifetime. You'll visit +10 destinations and enjoy numerous authentic experiences unique to Kyrgyzstan. Despite not being the longest tour, it offers a complete package of cultural immersion and adventure."
    }
];

document.addEventListener('DOMContentLoaded', () => {
    const toursList = document.getElementById('tours-list');
    
    tours.forEach(tour => {
        const tourElement = document.createElement('a');
        tourElement.className = 'justify__content__center';
        tourElement.href = tour.link;
        tourElement.innerHTML = `
            <div class="loader" style="--clr: #01e100;--i:1">
                <div class="card__tour__content">
                    <div class="img__card">
                        <div class="img__tour" style="--imgg: url('${tour.imageUrl}');"></div>
                    </div>
                    <div class="text__card">
                        <span class="price">${tour.price}</span>
                        <h3 class="descriptions">${tour.title}</h3>
                        <p class="descriptions__text">${tour.description}</p>
                    </div>
                </div>
            </div>
        `;
        toursList.appendChild(tourElement);
    });
})
