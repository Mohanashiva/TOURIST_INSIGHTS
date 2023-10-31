import json

# Your input JSON data
input_json_data = [{
        "_id": "63230b666ba1ea059ceb6923",
        "name": "Hyderabad",
        "summary": "Hyderabad is the fifth largest metropolis of India and the capital of the states of Telangana and Andhra Pradesh. It is known for its rich history and culture with monuments, mosques, temples, a rich and varied heritage in arts, crafts and dance. Also known as The City of Nizams and The City of Pearls, Hyderabad is today one of the fast developing cities in the country and a modern hub of IT, ITES, and Biotechnology. Hyderabad is often referred to the twin cities of Hyderabad and Secunderabad together which are commonly referred as a single city.Muhammad Quli Qutb Shah, a ruler of the Qutb Shahi dynasty (the ruling family of the Golconda - previously a feudatory of Bahmani sultanate that declared independence in 1512) founded the city of Hyderabad on the banks of the Musi River in 1591. The Mughal emperor Aurangzeb captured Hyderabad in 1687, but the Mughal-appointed governors of the city soon gained autonomy. In 1724, Asaf Jah I, who was granted the title Nizam-ul-Mulk ('Governor of the country') by the Mughal emperor, defeated a rival official to establish control over Hyderabad. Asaf Jah's successors ruled as the Nizams of Hyderabad. The rule of the seven Nizams saw the growth of Hyderabad both culturally and economically.Hyderabad is the financial and economic capital of the state of Andhra Pradesh. Hyderabad is known as the city of pearls, lakes and, lately, for its IT companies.",
        "type": "Historical",
        "description": "Bhagya Nagaram",
        "state": "Hyderabad",
        "location": [17.360589, 78.4740613],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 5,
        "price": 125
    },
    {
        "_id": "63230b666ba1ea059ceb6923",
        "name": "Shimla",
        "summary": "Shimla is a mesmerizing hill station in Himachal Pradesh. It is one of the top hill stations in India, and among the top Himachal tourist places. Among the top hill stations in Himachal, Shimla derives its name from 'Goddess Shyamala', an incarnation of Goddess Kali. Kali Bari Temple, Annandale, Vice Regal Lodge, Jakhu Temple / Jakhu Hill, The Mall, Tara Devi Temple, Christ Church, and Kalka - Shimla Railway are some of the best tourist places in Shimla. Tourists can go in for the various treks to the Kullu valley, indulge in trout fishing at the Pabbar River, try skiing at the Narkanda and Kufri, and play golf at Naldehra as part of Shimla holiday packages. It is regarded as one of the most beautiful places to visit near Chandigarh.",
        "type": "Hill Station",
        "description": "Queen of Hills",
        "state": "Himachal Pradesh",
        "location": [31.1041526, 77.1709729],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 4,
        "price": 100
    },
    {
        "_id": "63230b666ba1ea059ceb6924",
        "name": "Ooty",
        "summary": "Ooty is one of the best hill stations in India and among the top places to visit in Tamilnadu. Ooty is situated at a distance of 265 km from Bangalore.At an altitude of 7,440 feet, Ooty was a popular summer retreat for the British during colonial days. The rolling hills, lush green vegetation, and misty landscapes attract a large number of tourists to this hill station. Ooty Lake, Botanical Garden, Wenlock Downs, and Rose Garden are among the must include places in Ooty tour packages. The toy train, known as Nilgiri Mountain Railway that runs from Mettupalayam to Ooty is a UNESCO World Heritage Site and a must be experienced. The establishment of numerous tea estates made Ooty famous. Lofty mountains, dense forest, sprawling grasslands, and miles and miles of tea gardens greet the visitors on most routes. The annual Tea and Tourism Festival (Jan) and Summer Festival (May) attract crowds in huge numbers. Ooty can also be visited along with Wayanad tour packages.",
        "type": "Hill Station",
        "description": "Queen of hill stations",
        "state": "Tamil Nadu",
        "location": [11.4126769, 76.7030504],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3,
        "price": 75
    },
    {
        "_id": "63230b666ba1ea059ceb6925",

        "name": "Munnar",
        "summary": "Situated at an altitude ranging from 5000 to 8000 feet on the Kannan Devan Hills, the fascinating hill station of Munnar is one of the best tourist places in Kerala and among the must include places in honeymoon tour packages. It is about 120 km from Kochi, and 284 km from Trivandrum.Often referred to as the Swiss of South India, Munnar is one of the famous weekend getaways from Kochi, Coimbatore & Madurai. Mattupetty Dam, Echo point, Kundala Lake, Devikulam, Pothamedu Viewpoint, Nyayamkad falls, Thoovanam falls, Eravikulam National Park and Attukal Waterfalls are among the must include places in Munnar packages. Munnar is a trekker's paradise too, which offers both soft and mountain trekking. Munnar is home to some of the world's best tea estates. The tea plants covering Munnar hills make the feeling of seeing a wide green carpet. Munnar is also known for Neelakurinji flowers, which blooms once in 12 years. It is also known for being the spice center of Kerala. Over twelve varieties of spices including ginger, garlic, cardamom, vanilla, pepper, cinnamon, coffee, tea, clove, and nutmeg are cultivated in Munnar and its neighboring villages.",
        "type": "Hill Station",
        "description": "Fascinating hill station of Kerala",
        "state": "Kerala",
        "location": [10.0869959, 77.0600915],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 5
    },
    {
        "_id": "63230b666ba1ea059ceb695b",

        "name": "Kedarnath",
        "summary": "Kedarnath is a town and a famous center of pilgrimage in Uttarakhand situated in Rudraprayag district.Kedarnath is a popular pilgrimage destination for Hindus and is one of the four major Places to visit in Uttarakhand known as Chota Char Dham pilgrimage that also includes Badrinath, Gangotri and Yamunotri. It lies at an altitude of 3584 m near Chorabari Glacier, the head of river Mandakini. It is the most remote of the four Char Dham sites and is flanked by breathtaking snow-clad peaks. Kedarnath is named after King Kedar. It is believed that the temple existed even during the time of Mahabharata. It is the place where Lord Shiva absolved Pandavas from the sin of killing their own cousins Kauravas in the battle of Kurukshetra. The famous Kedarnath temple is one of the twelve Jyotirlingas and is thronged by thousands of tourists each year. Other than Kedarnath temple, Bhairavnath temple, Chorabari Tal, Shankaracharya Samadhi and Hans Kund are the some other religious places near Kedarnath.Kedarnath temple is a major tourist attraction and pilgrims book their hotels way in advance. Rooms in budget hotels and dharamshalas are available under Rs 500 ...",
        "type": "Pilgrimage",
        "description": "Kedarnath Attractions",
        "state": "Uttarakhand",
        "location": [30.7345609, 79.0673204],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 4
    },
    {
        "_id": "63230b666ba1ea059ceb6926",
        "name": "Manali",
        "summary": "Manali is a breathtakingly beautiful hill station nestled in the mountains of Himachal Pradesh near the northern end of the Kullu Valley. About 295 km from Chandigarh, and 545 km from Delhi, it is one of the top hill stations in Himachal, and among the top places to visit near Chandigarh.Renowned for its snow-covered mountains, scenic beauty, history, and culture, Manali is located at an altitude of 2050 m and is spread along the banks of the river Beas. Manali is named after the Hindu lawgiver Manu. Naggar Castle, Hidimbi Devi Temple, and Rohtang Pass are among the must include places in Manali holiday packages. Manali also has many Buddhist monasteries that are worth visiting. Enfield point, Manali Gompa, Manu Temple, Naggar Castle, Nehru Kund and Zana Waterfalls are the other famous tourist places in Manali. Manali is also famous for adventure sports like skiing, hiking, mountaineering, Paragliding, rafting, kayaking, and mountain biking. Paragliding in Manali is an unforgettable experience.",
        "type": "Hill Station",
        "description": "Valley of the Gods",
        "state": "Himachal Pradesh",
        "location": [32.26309405, 77.18812183241408],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 4
    },
    {
        "_id": "63230b666ba1ea059ceb6965",

        "name": "Amritsar",
        "summary": "Amritsar is an ancient pilgrimage town and headquarters of Amritsar district in Punjab state. It is the most popular Sikh shrine in Punjab and also one of the top places of pilgrimage in India.. The name Amritsar is derived from Amrit Sarovar, the holy tank that surrounds the marvelous Golden Temple. The town of Amritsar was founded in 1577 CE by Guru Ram Das, the 4th Sikh guru and the village was named as Ram Das Pura after him. Amritsar is the place where the tragic episode of the Jallianwala Bagh Massacre took place under the British rule. It also witnessed Operation Blue Star in 1984 under the late prime minister of India, Smt. Indira Gandhi.Amritsar is world famous for its Golden Temple, the seat of Sikh religion. Also known as Harmandir Sahib, the Golden Temple in Amritsar is famous for its full golden dome and is one of the most popular places of pilgrimage in Punjab. Jallianwallah Bagh, Durgiana Temple, Gobindgarh Fort, Central Sikh Museum, Maharaja Ranjith Singh Museum, and Wagah Border are the other popular places to visit in Amritsar.There are many fairs and festivals celebrated in Amritsar. One of the most famous festivals of Amritsar is Guru Nanak Jayanti held in the month of October/November. Lohri ...",
        "type": "Historical & Heritage",
        "description": "The Pool of Nectar",
        "state": "Punjab",
        "location": [31.6343083, 74.8736788],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },

    {
        "_id": "63230b666ba1ea059ceb692c",
        "name": "Kodaikanal",
        "summary": "Kodaikanal or Kodai is one of the top tourist destinations in Tamilnadu tour packages and among the best hill stations in South India. It is located at a distance of about 469 km from Bangalore & 528 km from Chennai.At an altitude of about 7000 feet (2133 m) amidst the rolling slopes of the Palani Hills, Kodai has several scenic places that are enjoyed by its visitors as part of Kodaikanal tour packages. Kodaikanal is not extensively commercialized like Ooty and it offers a pleasant experience to tourists with relatively less crowd. Kodai Lake, Bryant Park, Coaker's Walk, Bear Shola Falls, Silver Cascade, and Pillar Rocks are the top tourist places in Kodaikanal.Kodaikanal is a place you can go to take a break from the rigours of daily city life, and this hill station lets you sit back and connect with nature as you head out on biking or trekking trails or take a stroll through the vast forests surrounding the town. Dolphin's Nose, and Vattakanal are some of the top trekking places in Kodaikanal.",
        "type": "Hill Station",
        "description": "Princess of Hill stations",
        "state": "Tamilnadu",
        "location": [10.273275349999999, 77.51160822153315],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb693a",
        "name": "Andaman Islands",
        "summary": "The Andaman & Nicobar Islands form an archipelago in the Bay of Bengal between India and Myanmar. Most part of the Andaman & Nicobar Islands is a Union Territory of India, while a small part in the north of the archipelago, including the Coco Islands, belongs to Myanmar. Port Blair is the capital town and the tourist hub in Andaman Islands. Andamans are one of the popular destinations for honeymoon tours.The archipelago is divided into two groups of islands - the Andaman Islands and the Nicobar Islands. Andaman & Nicobar Islands stretch over a length of more than 800 km from North to South. It consists of about 572 islands out of which only around 36 islands are inhabited. Of these, only 9 islands in the Andaman Islands are open for tourists while the Nicobar Islands are inaccessible to tourists. Non-Indian nationals need special permit to visit Andaman Islands.",
        "type": "Beach",
        "description": "Andaman Islands Attractions",
        "state": "Andaman & Nicobar Islands",
        "duration": 8,
        "location": [12.61123865, 92.83165406414926],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 6,
        "price": 200
    },
    {
        "_id": "63230b666ba1ea059ceb693c",

        "name": "Pondicherry",
        "summary": "Pondicherry or Puducherry is a city and capital of the Union Territory of Pondicherry and is one of the most popular tourist destinations you must include in honeymoon packages. It is among top 2 day trip from Bangalore and Chennai. Pondicherry is located along the Coromandel Coast of Bay of Bengal.The Union Territory of Puducherry comprises of four coastal regions namely Puducherry, Karaikal, Mahe and Yanam. Puducherry and Karaikal are situated on the East Coast of Tamil Nadu, Yanam in Andhra Pradesh and Mahe on the West Coast in Kerala. According to legend, Pondicherry was known by the name Vedapuri and this place is also believed to be the abode of the revered sage, Saint Agasthya. Pondicherry had trade relations with Rome during 1st century AD. Roman pottery excavated from Arikamedu near Pondicherry dates back to 1st century AD. Pondicherry was ruled by the Pallava dynasty in 4th century AD followed by different southern dynasties ...",
        "type": "Beach",
        "description": "Pondicherry Attractions",
        "state": "Pondicherry",
        "location": [11.9340568, 79.8306447],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb6927",

        "name": "Nainital",
        "summary": "Situated at the Kumaon foothills of Himalayas, Nainital is a beautiful hill station in Uttarakhand. It is one of the most popular hill stations in India and among the must-include places in Uttarakhand tour packages. It is about 278 km from Dehradun, and 294 km from Delhi.Nainital is famous for its scenic mountain views and is commonly known as the Lake District of India. Situated at an altitude of 1938 m, Nainital derives its name from Naini Lake, among the must include places in your Nainital holiday packages. Nainital is a famous tourist destination of India, attracting large number of domestic and foreign tourists every year.Nainital is one of the popular hill stations near Delhi. Naina Peak, Nainital Lake, Naina Devi Temple, Mall, Raj Bhavan, High Altitude Zoo, Bhimtal and Sattal are some of the prominent tourist places in Nainital.",
        "type": "Hill Station",
        "description": "Foothills of Himalayas",
        "state": "Uttarakhand",
        "location": [29.29478295, 79.41548093726253],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 4
    },
    {
        "_id": "63230b666ba1ea059ceb6928",

        "name": "Darjeeling",
        "summary": "Darjeeling is a charming hill station located in the Shivalik hills of the lower Himalayas in West Bengal, India. Situated at an altitude of 6,700 feet, Darjeeling is one of the most popular tourist places in West Bengal and among the must include places in your honeymoon tour packages.Nepal yielded one-third of their lands to the British, who established Darjeeling as the summer capital of Bengal Presidency. During 19th century AD, they set up a sanatorium and a military depot in Darjeeling. Later, extensive tea plantations were established in the region by the British. After independence, in 1947, Darjeeling was merged with West Bengal.Amidst the backdrop of the mighty snow-clad Himalayan peaks, Darjeeling is famous for its tea plantations, spectacular views of snow-capped peaks and Darjeeling Himalayan Railway. The majestic Kanchenjunga, third highest mountain in ...",
        "type": "Hill Station",
        "description": "Darjeeling Attractions",
        "state": "West Bengal",
        "location": [27.0377554, 88.263176],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb6929",

        "name": "Coorg",
        "summary": "Coorg is one of the top hill stations in South India and among the most popular attraction not to miss in your Karnataka holiday packages. Coorg (or Kodagu) is about 265 km from Bangalore city and takes about 6 hrs drive. Coorg is the largest producer of Coffee in India. Also, it is one of the places with the highest rainfall in India. Places like Raja's Seat, Abbey Falls, Iruppu Falls, Omkareshwara Temple, Bylakuppe, Talacauvery and Dubare are the major attractions to be included in Coorg Holiday Packages. The famous Cauvery River is originated in the hills of Coorg at Talacauvery.Explore our Coorg Travel Guide for complete details on the hill station of Coorg. Being a part of the Western Ghats, Coorg is home to three wildlife sanctuaries - the Talacauvery, Pushpagiri, and Brahmagiri Sanctuaries, and one national park, the Nagarhole National Park. Coorg is also famous for trekking activities with peaks like Thandiyandamole, Brahmagiri, and Pushpagiri. Besides, Coorg can also be visited along with Ooty tour packages.",
        "type": "Hill Station",
        "description": "Fondly called the Scotland of India",
        "state": "Karnataka",
        "location": [12.3225856, 75.8900616],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 4
    },
    {
        "_id": "63230b666ba1ea059ceb696f",

        "name": "Ellora Caves",
        "summary": "An UNESCO World Heritage Site, Ellora Caves are the most visited places of heritage in Maharashtra, and among the must include places in Maharashtra tour packages. Situated about 28 km from Aurangabad, 253 km from Pune, and 344 km from Mumbai. Ellora Caves is an impressive complex of Buddhist, Hindu, and Jain Cave temples carved out of the vertical face of the Charanandri hills between the 6th and 10th centuries AD. Ellora is one of the prominent heritage places to visit near Mumbai. The caves have a slightly less dramatic setting than those at Ajanta, but more exquisite sculptures. The cave complex comprises 34 caves includes 12 Buddhist, 17 Hindu, and 5 Jain Caves. The central attraction at Ellora is Kailash Temple (Cave 16), which is the most remarkable. Every year Ajanta-Ellora Festival is organized in Aurangabad to pay tribute to the legendary caves of Ellora, Ajanta, and other historical monuments in the region. Earlier the venue for this festival was Kailasa Temple of Ellora Caves but it has now been shifted to Soneri Mahal, among the must include places in Aurangabad tour packages.",
        "type": "Historical & Heritage",
        "description": "Ellora Caves Attractions",
        "state": "Maharashtra",
        "location": [20.026752549999998, 75.17751524179019],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb693f",

        "name": "Kochi",
        "summary": "Kochi or Cochin is the financial capital of Kerala. It is situated about 190 km from Coimbatore, and 204 km from Trivandrum. Kochi is one of the prime places to visit as part of Kerala tour packages. Kochi packages are admired for its scenic beauty, traditional architecture, churches, and beaches. Fort Kochi, Bolghatty Palace, Marine Drive, Mangalavanam Bird Sanctuary, St. George Ferona Church - Edappally, Matancherry Palace, Chinese Fishing Nets, and Fort Kochi Beach are some of the prominent Kochi tourist places.Kochi is one of the finest natural harbors in the world. This city is home to Cochin Jewish Synagogue, the oldest synagogue in the Commonwealth, as well as numerous old churches and temples.",
        "type": "Beach",
        "description": "The Queen of the Arabian Sea",
        "state": "Kerala",
        "location": [9.931308, 76.2674136],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 5
    },
    {
        "_id": "63230b666ba1ea059ceb6948",
        "name": "Agra",
        "summary": "Agra, the land of the Taj Mahal, which is one of the Seven Wonders of the World, is situated on the banks of River Yamuna in the state of Uttar Pradesh. Agra is also among best weekend getaways near Delhi & Noida for a two day trip. Agra is included on the Golden Triangle tourist circuit, along with Delhi and Jaipur.Agra is one of the most popular tourist destinations of the World with three UNESCO World Heritage monuments - Taj Mahal, Fatehpur Sikri & Red Fort. Agra was first mentioned in the epic Mahabharata, where it was called Agrevana meaning the border of the forest. Agra famously became the capital of the Mughal Emperors from 1526 to 1658. It was known then as Akbarabad and remained the capital of the Mughal Empire under the Emperors Akbar, Jahangir ...",
        "type": "City",
        "description": "Agra Attractions",
        "state": "Uttarakhand",
        "location": [27.1752554, 78.0098161],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 2
    },
    {
        "_id": "63230b666ba1ea059ceb692a",

        "name": "Mussoorie",
        "summary": "Mussoorie is a popular hill station in Dehradun district of Uttarakhand state. Mussoorie is one of the well known tourist destination not to miss in your honeymoon trip.Kempty Falls, Camel's Back Road and Dhanaulti are among the must include places in your Mussoorie tour packages. Mussoorie is situated atop a horseshoe crest on the mountains of Garhwal at an average altitude of 1880 m. Mussoorie offers commanding views of the underlying Doon Valley and the magnificent Himalayas. The highest in the region is Lal Tibba in Landour, with a height of over 2,275 m. Mussoorie is called the gateway to the Yamunotri and Gangotri, two sacred destinations known to be the origin of rivers Ganga and Yamuna respectively.Mussoorie gets its name from the Mansoor plant that grows in abundance in this region. It was founded in 1820 by Captain Young from the British army. The British officials visited it as a getaway from the heat during summer. During the 1959 Tibetan Rebellion, ...",
        "type": "Hill Station",
        "description": "Gateway to the Yamunotri and Gangotri",
        "state": "Uttarakhand",
        "location": [30.4569012, 78.0782906],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 2
    },
    {
        "_id": "63230b666ba1ea059ceb692b",

        "name": "Mahabaleshwar",
        "summary": "Perched at an altitude of 1,353 m in the Western Ghats of Maharashtra, Mahabaleshwar is one of the popular hill stations in Maharashtra, and among the best places to visit near Pune & Mumbai.It is one of the must include places in Maharashtra tour packages.Known for its lovely views, beautiful landscapes, and pleasant weather. It boasts of many tourist attractions including Pratapgarh Fort, Venna Lake, Mahabaleshwar Mandir, Krishnabai Temple, Lingamala Falls, and Panchgani. Several viewpoints are strategically located here to capture the panoramic views created by the majestic Sahyadri Mountains and deep valleys. Arthur's Seat, Wilson Point, Kate's Point, Elephant Head Point, and Bombay Point are some popular viewpoints you must include in Mahabaleshwar packages.Mahabaleshwar is the source of the Krishna River. Four other rivers also flow from here, before they merge into the Krishna; these are Koyana, Venna, Savitri, and Gayatri. Also, it is famous for the cultivation of strawberries and mulberries.",
        "type": "Hill Station",
        "description": "Queen of hill stations in Maharashtra",
        "state": "Maharashtra",
        "location": [17.893641000000002, 73.61316885788803],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb692d",

        "name": "Thekkady",
        "summary": "Periyar Wildlife Sanctuary is one of the top wildlife sanctuaries in Kerala, especially for wildlife enthusiasts.Established in the year 1950, the sanctuary is spread across 777 sq. km, of which 360 sq. km is a thick evergreen forest. The splendid artificial lake formed by the Mullaperiyar Dam across the Periyar River adds to the charm of the park. Among the top tourist places in Kerala, Thekkady is famous for Asian Elephants, Tigers, Gaurs, Sambars, Lion-tailed Macaques, Nilgiri Langurs, Wild Boars, Spotted Deer, Nilgiri Tahr, etc. This is the only sanctuary in India where you can watch wildlife at close quarters from the safety of a boat from the lake. The main attraction of the sanctuary is a group of wild elephants that come to play in the lake. Thekkady offers elephant rides, jeep safari, boating in the lake, tiger trails, and forest treks. Murikkady, Chellar Kovil, Anakkara, Mangala Devi Temple, Suruli Falls, and Pullumedu are the popular places to visit as part of Thekkady packages.",
        "type": "Hill Station",
        "description": "Kerala Attractions",
        "state": "Kerala",
        "location": [9.5804995, 77.181142],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 2
    },
    {
        "_id": "63230b666ba1ea059ceb692e",
        "name": "Chikmagalur",
        "summary": "Chikmagalur or Chikkamagaluru situated at the foothills of Mulliyangiri range with an altitude of 3,400 feet. It is one of the best hill stations in Karnataka and among the most famous tourist places near Bangalore.Chikmagalur is famous for its serene environment, lush green forests and tall mountains. Baba Budangiri, Hirekolale Lake, Mulliyangiri, Ayyanakere Lake, Manikyadhara Falls, Horanadu and Kemmanagundi are among the must include places in Chikmagalur Holiday Packages.Chikkamagaluru is also famous for coffee and is known as the Coffee Land of Karnataka. It is the place where coffee was cultivated for the first time in India. The climate of Chikmagalur is pleasant all year round but the best time to visit the place is from the months of September till March. Explore our Chikmagalur Travel Guide for complete details on the mighty hill station. Chikmagalur can also be visited along with Coorg packages.",
        "type": "Hill Station",
        "description": "Scenic hill town",
        "state": "Karnataka",
        "location": [13.318014, 75.7738743],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 2
    },
    {
        "_id": "63230b666ba1ea059ceb692f",

        "name": "Gangtok",
        "summary": "The capital of north-eastern state of Sikkim, India. Known for its cleanliness and breathtaking beauty, it is one of the popular places to visit in Sikkim and is one of the popular attraction not to miss in your honeymoon trip.Situated at an altitude of 5410 feet, Gangtok is the largest city and the main business and tourist hub of Sikkim. The name meaning hill-top, Gangtok is known for its scenic beauty and striking views of Mount Kanchenjunga, the third highest mountain in the world. It is also known as the land of monasteries, as it has maximum number of monasteries in the world. Located right in the middle of the Himalayan range and having mild temperate climate year-round, Gangtok is the most important center for Sikkim Tourism.According to history, Gangtok rose to prominence as a popular Buddhist pilgrimage site after the construction of the Enchey Monastery in 1840 CE. In 1894, the ruling Sikkimese Chogyal, Thutob Namgyal, transferred the capital from Tumlong to Gangtok, increasing the city's importance. In the early 20th century, Gangtok became a major stopover on the trade route between Tibet and India. After India's independence ...",
        "type": "Hill Station",
        "description": "Fascinating hill town",
        "state": "Sikkim",
        "location": [27.325756900000002, 88.69827694810172],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6930",

        "name": "Wayanad",
        "summary": "Wayanad is one of the popular hill stations in Kerala, and among the best places to visit near Kozhikode. It is about 118 km from Ooty, 246 km from Kochi, and 442 km from Trivandrum. Wayanad is among the mountains of the Western Ghats on the borders of Tamil Nadu and Karnataka. This hill district is home to several lakes, caves, sanctuaries, and waterfalls which are the main attractions of Wayanad Packages. Banasura Sagar Dam, Edakkal Caves, Meenmutty Falls, Soochipara Waterfalls, Wayanad Wildlife Sanctuary are some of the prominent tourist places in Wayanad.Wayanad is one of the biggest foreign exchange earners of the State with its production of cash crops like pepper, cardamom, coffee, tea, spices, and other condiments. Wayanad can be visited along with Ooty tour packages.",
        "type": "Hill Station",
        "description": "Picturesque plateau nestled",
        "state": "Kerala",
        "location": [11.715219000000001, 76.12690294658198],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6931",
        "name": "Dharamshala",
        "summary": "At an average altitude of 1,475 m above sea level, Dharamshala is a pristine hill station situated in the Kangra district of Himachal Pradesh. It is one of the best hill stations in Himachal Pradesh, and among the most famous places to visit near Delhi.Dharamshala is the headquarters of Kangra district and among the must-include places in Himachal tour packages. In the year 1960, Dharamshala became a temporary headquarters to His Holiness Dalai Lama. The hill station of Dharamshala is covered by thick woods of oak and coniferous trees and it is enfolded on its three sides by the Dhauladhar ranges. Dharamshala packages have a lot to offer ranging from ancient temples, churches, and monasteries to museums and beautiful trekking trails. The ancient Chamunda Temple, Dalailama Temple, Namgyalma Stupa, Bhagsunath Temple, Triund Hill, Norbulingka Institute, Gyuto Monastery, and Indru Nag are some of the prime tourist places in Dharamshala.",
        "type": "Hill Station",
        "description": "Little Lhasa or Dhasa",
        "state": "Himachal Pradesh",
        "location": [32.2143039, 76.3196717],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6932",

        "name": "Shillong",
        "summary": "Shillong is a mesmerizing hill station in East Khasi Hills district of Meghalaya in India. Perched at an attitude of 1496 m, Shillong is situated on a plateau bounded by the Umiam gorge on the north, Diengiei Hills on the northwest, and the hills of the Assam valley on the northeast. Shillong Peak is the highest point in Shillong with an altitude of 6449 feet. The city gets its name from the deity Shyllong or Lei Shyllong, who is worshipped at the Shillong Peak. The British fondly called Shillong the 'Scotland of the East' as the rolling hills around the town reminded the European settlers of Scotland. Earlier a small village, Shillong became the new civil station of the Khasi and Jaintia hills in 1864 CE. In 1874, it became the capital of composite Assam under British rule due to its favorable location between the Brahmaputra and Surma valleys. Shillong remained the capital of Assam till 1969 when the autonomous state of Meghalaya was formed.In 1972 CE,Meghalaya turn out to be a full - fledged state...",
        "type": "Hill Station",
        "description": "Picturesque hill stations",
        "state": "Meghalaya",
        "location": [25.5760446, 91.8825282],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6933",

        "name": "Cherrapunji",
        "summary": "Cherrapunji or Cherrapunjee is a small sub divisional town in the East Khasi Hills district of Meghalaya. It is one of the wettest places on the earth and among the must visit places. This name eventually evolved into the current name, Cherrapunji. Receiving an annual rainfall of about 11,777 mm, Cherrapunji happens to be the second wettest place on the planet after Mawsynram. The town receives both south-west and north-east monsoons. Despite receiving an abundant rainfall, Cherrapunji faces an acute water shortage and the inhabitants have to trek very long distances to obtain potable water. The excessive rain causes soil erosion which has deprived the land of Cherrapunji and the surrounding valleys.Located in Meghalaya, Cherrapunji is a paradise ...",
        "type": "Hill Station",
        "description": "Land of oranges",
        "state": "Meghalaya",
        "location": [25.2837969, 91.7193603],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6934",

        "name": "Kullu",
        "summary": "It is located on the banks of the Beas River in Kullu Valley at an altitude of 1230 meters. Kullu Manali is one of the top summer resorts to visit as part of Himachal tour packages. Kullu is a broad open valley formed by the Beas River between Manali and Larji. This valley is famous for its temples, beauty and its majestic hills covered with Pine and Deodar Forest and sprawling Apple Orchards. The beautiful valley is also mentioned in epics like Ramayana, Mahabharata and Vishnu Purana. Chinese traveler Huien Tsang visited Kullu in 634 or 635 AD and described it as a region completely surrounded by mountains. The place had a stupa built by Asoka. In ancient days Kullu had several Buddhist monasteries. There were Hindu temples too and people of both faiths lived peacefully together.Kullu valley is the largest valley in Kullu district. The Beas River runs through the middle of the valley. It is also called the 'Valley of the Gods' or 'Dev Bhumi'. It connects with the Lahaul and Spiti valleys ...",
        "type": "Hill Station",
        "description": "The ending point of inhabitable world",
        "state": "Himachal Pradesh",
        "location": [32.00186325, 77.37899639741332],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6935",

        "name": "Lonavala",
        "summary": "Situated at an altitude of 622 m in the Sahyadri Range, Lonavala is a beautiful hill station in the Pune district of Maharashtra. It is one of the top hill stations you must include in Maharashtra tour packages and among the best tourist places to visit near Mumbai & Pune. Lonavala has several tourist places in the form of caves, lakes, forts and waterfalls. Lohagad Fort, Rajmachi Point, Bhushi Dam, Kune Waterfalls, Karla Caves, Tikona Fort, Visapur Fort, Bedsa Caves and Tung Fort are some of the best places to include in Lonavala tour packages. The twin hill stations of Lonavala and Khandala are the most popular monsoon getaways in India. The best time to visit Lonavala and Khandala is during the monsoon, between July - September when the scenic spots become lush green and the waterfalls are in full flow.",
        "type": "Hill Station",
        "description": "Lonavala Attractions",
        "state": "Maharashtra",
        "location": [18.7548563, 73.4016729],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6936",

        "name": "Pelling",
        "summary": "Pelling is a wonderful hill station located in the West Sikkim district of north Indian state of Sikkim. Situated at an altitude of 6,800 feet, Pelling is the second biggest tourist destination in Sikkim after Gangtok. Pelling was initially a land filled with jungle which was home to a lot of wildlife. The area developed into a full-fledged village after the construction of two Buddhist monasteries Pemayangtse and Sangacholing. Pelling offers good view of entire Kanchenjunga mountain range including Koktang, Kumbhakaran (Jannu), Rathong, Kabru, Kabru Dome, Kanchenjunga, Pandim, and Siniolchu. Pelling is mostly known for its mesmerizing views of the snow-capped Kanchenjunga range, several historical sites and monasteries. Kanchenjunga Waterfalls, Pemayangtse Monastery, Khecheopalri Lake, Singshore Bridge, Sanga Choeling Monastery, Tashiding Monastery, Rimbi Falls and Changey Waterfalls are the top places to visit in Pelling. In the months of winter, the town is covered in a blanket of snow and is a perfect holiday destination for all nature ...",
        "type": "Hill Station",
        "description": "The seat of the religious body",
        "state": "Sikkim",
        "location": [27.3003722, 88.2356503],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6937",

        "name": "Dalhousie",
        "summary": "Located at an altitude of 1,970 m, Dalhousie is one of the famous hill stations in Himachal, and among the popular places to visit near Chandigarh. Surrounded by snow-capped mountains, Dalhousie is located on the western edge of the Dhauladhar mountain range of the Himalayas. It is hill stations near Delhi, and among the best places to visit in Himachal. It was named after Lord Dalhousie, the then Viceroy of India, who established this town as a summer retreat in 1854. The beautiful and picturesque Dalhousie is spread around five hills, known as Katalagh, Potreyn, Bakrota, Terah, and Bhangora. Ganji Pahadi, Dainkund Peak, Khajjiar, Noorwood Paramdham, Rang Mahal, Bara Pathar Temple, Hariraya Temple, St. Patrick Church, Bakrota Hills, Satdhara Falls, Village Lohali, Kalatop, and Kalatop Forest, Panchpula, Subhash Baoli, and Salooni are the top tourist places in Dalhousie. Dalhousie also offers a lot of activities for nature lovers and adventurers as part of Dalhousie holiday packages.",
        "type": "Hill Station",
        "description": "Dalhousie Attractions",
        "state": "Himachal Pradesh",
        "location": [32.54357545, 75.94484088677805],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6938",

        "name": "Almora",
        "summary": "Almora, a scenic hill station in the Almora district is a famous hill resorts in Uttarakhand. It lies at an altitude of 1,651 m, amidst the southern part of the Kumaon Hills. It is a one of the popular hill stations near Delhi and also of one of the top Tourist places in Uttarakhand.Almora is located on a 5 km long horse shoe shaped ridge, the eastern portion of which is called the Talifat and the western one is known as Selifat. The Kosi and Suyal rivers run alongside the town adding to the beauty of the place. Almora is considered the cultural heart of the Kumaon region of Uttarakhand. The town got its name from kilmora, a short plant found in nearby region, which was used for washing the utensils of Katarmal Temple. The people bringing kilmora were called Kilmori and later Almori and the place came to be known as Almora. Almora is one of the top attractions you must include in Nainital packages.Almora was founded in 1568 by Kalyan Chand during the rule of the Chand dynasty. Prior to that the region was under the control of Katyuri King Bhaichaldeo and he has donated part of this land to a Gujrati Brahmin Sri Chand Tiwari. In the days of the Chand Kings it was called Rajapur and was also mentioned ...",
        "type": "Hill Station",
        "description": "Scenic hill station",
        "state": "Uttarakhand",
        "location": [29.703094999999998, 79.43317023326716],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6939",

        "name": "Lachung",
        "summary": "Lachung is a small hill station located in North Sikkim district of Indian state of Sikkim. Situated near the border with Tibet, it is one of the beautiful places to visit in Sikkim. At an altitude of 9,600 feet, Lachung is located at the confluence of River Lachen and River Lachung, the tributaries of Teesta River. The word Lachung means 'small pass'. The Indian Army has a forward base in the town. The town's economy has been boosted by tourism in recent years as the region has been opened up by the Indian government. The town is majorly inhabited by Lepchas and Bhutias who are prime followers of Buddhism.With its stunning fruit orchards, sparkling streams and gushing rivers flowing against the mesmerizing backdrop of snow-capped Himalayas, Lachung has been described as the 'most picturesque village of Sikkim' by British explorer Joseph Dalton Hooker in his definitive, The Himalayan Journal (1855). Lachung Monastery, Shingba Rhododendron Sanctuary, Yume Samdong (Zero Point), Yumthang Valley, Bhim Nala Falls and Naga Falls are the top places to visit in Lachung. Also, it acts as the base camp for Rhododendron ...",
        "type": "Hill Station",
        "description": "Picturesque hill stations",
        "state": "Sikkim",
        "location": [27.6897097, 88.7425876],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },

    {
        "_id": "63230b666ba1ea059ceb693b",

        "name": "Alleppey",
        "summary": "Alappuzha or Alleppey is one of the best places to visit near Kochi, and among the must-include places in Kerala tour packages. It is about 63 km from Kochi, and 152 km from Trivandrum.Along with Kumarakom, Alappuzha is among the most famous destination of Backwaters in Kerala. A houseboat cruise in these backwaters is a delightful experience. The never-ending panorama of lush green paddy fields, towering coconut trees, shimmering water, and long canals around Alappuzha make it a delightful destination. Alappuzha Beach, Ambalappuzha Sri Krishna Temple, Arthunkal Church, Mannarasala Temple, Chettikulangara Devi Temple, Mullakkal Temple, Champakulam, Kuttanad, and Krishnapuram Palace are some of the famous tourist places in Alleppey.Alappuzha is also known for the annual Nehru Trophy Boat Race held on the Punnamada Lake on the second Saturday of August every year. This is the most popular of the boat races in India, and among the must-experience things to do as part of Alleppey tour.",
        "type": "Beach",
        "description": "Venice of the East",
        "state": "Kerala",
        "location": [9.1988871, 76.4860494754194],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb693d",

        "name": "Puri",
        "summary": "Puri is an ancient temple town situated along the coast of Bay of Bengal in Odisha. Puri is one of the places of original holy Char Dham Yatra of Hinduism and also one of the top places to experience Odisha Tourism.Earlier called as ShriKhetra, Purushottama Khetra, and Jagannath Puri, Puri is home to the world famous Sri Jagannath Temple. Often referred as the spiritual capital of Odisha, Puri forms the Golden Triangle of Orissa along with Konark and Bhubaneswar. Puri became an important center of pilgrimage with the arrival of Gangas in the 12th century and emerged as one of the centers of Vaishnavism.Dedicated Lord Vishnu, Lord Jagannath Temple is one of the prime places to visit in Puri and is a ...",
        "type": "Beach",
        "description": "Puri Attractions",
        "state": "Odisha",
        "location": [19.8076083, 85.8252538],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb693e",

        "name": "Kovalam",
        "summary": "Kovalam is a coastal town on the shores of the Arabian Sea in Kerala. About13 km from Trivandrum, and 212 km from Kochi, it is one of the most famous places to visit in Kerala. It can be visited along with Trivandrum tour packages.Kovalam means 'A grove of coconut trees' and the whole area beyond the shores around Kovalam is filled with the endless sight of coconut trees offering magnificent views while approaching the beach. Often called the 'Paradise of the South', Kovalam is one of the wonderful places to visit near Trivandrum.Light House Beach, Vizhinjam Mosque, Samudra Beach, Eve's Beach are the must include places in Kovalam packages. There are several activities for tourists like sunbathing, swimming, catamaran cruising, herbal body massage, and cultural programs. Kovalam is also famous for its Ayurvedic massages and many yoga resorts.",
        "type": "Beach",
        "description": "Kovalam Attractions",
        "state": "Kerala",
        "location": [8.4004698, 76.9788156],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6940",

        "name": "Vizag",
        "summary": "Visakhapatnam (also called Vizag) is a coastal & port city in the state of Andhra Pradesh, located on the shores of Bay of Bengal. It is the headquarters of Visakhapatnam district and is the base for Eastern Naval Command of the Indian Navy. Vizag is also one of the top places to experience Andhra Pradesh tourism.The city of Vizag, as Visakhapatnam is popularly called, derives its name from the Hindu God of valour, Visakha. The city is located beautifully among the hills of the Eastern Ghats with facing towards the Bay of Bengal. According to the Archaeological records. Kailasagiri, Rama Krishna Beach and Rishikonda Beach are among the must include places in your Vizag tour packages. The relics found in the area also prove the existence of a Buddhist empire in the region. Kalinga later lost the territory to King Ashoka in the bloodiest battle of the time which prompted him to embrace Buddhism. The city was also under the rulers of Chalukya, Pallava,Vengi, ...",
        "type": "Beach",
        "description": "Vizag Attractions",
        "state": "Andhra Pradesh",
        "location": [17.7231276, 83.3012842],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6941",

        "name": "Kumarakom",
        "summary": "Kumarakom is a cluster of little islands on the Vembanad Lake in Kerala. Kumarakom is the most famous places to visit near Trivandrum for Kerala backwaters, and among the must include places in Kerala tour packages. Kumarakom is a special tourism zone in Kerala due to the special ecology of the place. Kumarakom Bird Sanctuary, Kumaramangalam Temple, Vaikom, Pathiramanal Island, Aranmula, and Erumeli are the popular tourist places in Kumarakom. The major sightseeing option at Kumarakom is a boat cruise in the backwaters of Vembanad and is an amazing experience for every traveler to Kumarakom.Kumarakom Bird Sanctuary is a noted bird sanctuary where one can see many species of migratory birds as part of Kumarakom packages. It is an unbelievably beautiful paradise of mangrove forests, emerald green paddy fields, and coconut groves. It is also famous for Ayurvedic massage, yoga, meditation, boating, fishing, and swimming. Kumarakom is the venue for Sree Narayana Jayanthi Boat Race held in September during Onam festival.",
        "type": "Lake & Backwater",
        "description": "The Queen of Vembanad",
        "state": "Kerala",
        "location": [9.5967759, 76.4311258],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6942",

        "name": "Srisailam",
        "summary": "Srisailam is one of the twelve Jyotirlingas of Lord Shiva situated on the banks of River Krishna in Kurnool district of Andhra Pradesh. It is one of the most important pilgrimage centers of Lord Shiva in India and also one of the top Places to visit in Andhra. Srisailam is also one of the most popular weekend getaways from Hyderabad.Srisailam is famous for Srisailam Dam & Bhramaramba Mallikarjuna Temple which is dedicated to Lord Shiva. The sanctum enshrines Lord Mallikarjuna in the form of a linga protected by a three-hooded cobra. This ancient temple built in the Dravidian style with lofty towers and sprawling courtyards is one of the finest specimens of Vijayanagara architecture. The unique feature of this kshetram is the combination of Jyothirlingam and Mahasakthi (in the form of Bhramarambika) in one campus, which is very rare and only one of its kind. The great religious leader Aadi Sankara is said to have visited this shrine and composed his immortal Sivananda Lahiri here.",
        "type": "Lake & Backwater",
        "description": "Srisailam Attractions",
        "state": "Andhra Pradesh",
        "location": [16.090979400000002, 78.8656307623982],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6943",

        "name": "Athirapally Waterfalls",
        "summary": "Athirapally Waterfall is one of the best waterfalls in India and among the must include places in Kerala tour packages. Formed over Chalakudy River, Athirapally is one of the scenic waterfalls in Kerala that drops down from a height of 80 feet through several parallel streams offering a great scenic beauty. In the monsoon season, the water gets strength and all the streams join together and appear like Niagara Falls. The Vazhachal Waterfalls, Charpa Falls, Anakkayam, Sholayar Dam, Valparai, and Malayattur Wildlife Sanctuary are the nearby places to visit during your Athirapally trip. It also offers adventure activities like river rafting, trekking, etc. It is one of the best waterfalls near Kochi.The forest that surrounds Athirapally Falls is also the natural habitat of different species like the great hornbill, Malabar pied hornbill, Malabar grey hornbill, Indian grey hornbill, Asiatic elephant, tiger, leopard, and bison. The falls can be visited as part of Kochi tour packages.",
        "type": "Waterfall",
        "description": "Athirapally Waterfalls Attractions",
        "state": "Kerala",
        "location": [10.2847989, 76.5691181],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6944",

        "name": "Hogenakkal",
        "summary": "Hogenakkal Falls is one of the best waterfalls in India, and among the best places to visit in Tamil Nadu. It is about 146 km from Bangalore and 345 km from Chennai. Also, it is one of the major waterfalls near Bangalore.Hogenakkal is one of the wonderful places to visit near Bangalore & Chennai. When the River Kaveri enters the Tamil Nadu border after winding its way through the state of Karnataka, it descends down the lofty landscape forming the Hogenakkal Waterfalls. The Carbonatite rocks found near the waterfall are one of the oldest in the world. The falls has about 14 channels with drops varying between 15 & 65 ft. It can be visited as part of Yercaud tour packages.Coracle riding is one of the main attractions here which is allowed during the monsoon and winter season. Boating is usually stopped in peak monsoons. Hogenakkal is also the good place to try out your swimming skills. Tourists can also go for trekking on the nearby surrounding hills. The water from the fall flows towards the Mettur Dam which is also known as the Stanley Reservoir. Yercaud, MM Hills, and Yelagiri Hills are some of the major tourist destinations near Hogenakkal Falls.",
        "type": "Waterfall",
        "description": "Niagara of India",
        "state": "Tamil Nadu",
        "location": [12.1200274, 77.7778683],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6945",

        "name": "Shivanasamudra Falls",
        "summary": "Shivanasamudra is one of the best waterfalls near Bangalore and also among popular one day trip from Bangalore. Shivanasamudra is a segmented waterfall with several parallel stream formed adjacent to each other. Situated on River Kaveri, Shivanasamudra is among the popular Tourist places in Karnataka. The island of Shivanasamudra divides Kaveri River into two parts that form two waterfalls, one is Gaganachukki and the other is Bharachukki. Gaganachukki includes a huge horsetail shaped waterfall dropping from a height of 90 m and two large parallel streams that cascade down through a rocky bed from a height of over 320 feet. Asia's first hydroelectric power station was set up in the downstream of the falls in the year 1905. Barachukki is a cascading fall with a height of 70 m forming several streams through the wide rocky formations establishing superb natural beauty. This place offers breathtaking sight in the peak monsoons. Shivanasamudra is among the must include place in your Mysore tour packages. An interesting way to watch the beauty of the waterfall is to take a coracle ride to the mouth of the magnificent waterfall.",
        "type": "Waterfall",
        "description": "Shivanasamudra Falls Attractions",
        "state": "Karnataka",
        "location": [12.3035074, 77.1611196],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6946",

        "name": "Valley Of Flowers",
        "summary": "Valley of Flowers National Park is one of the most popular tourist destinations in India located in Western Himalayas in Chamoli district of Uttarakhand. It is perched at an altitude of 3600 m and is known for its meadows of endemic alpine flowers and the variety of flora. Valley of Flowers is one of the best national parks in India and also among the best Tourist places in Uttarakhand for trekking enthuasists.Stretching over a vast expanse of 87.50 sq. km, the park is about 5 km long and 2 km wide. The gentle landscape of the Valley of Flowers complements the rugged mountain of Nanda Devi National Park to the east. Together, they encompass a unique transition zone between the mountain ranges of the Zanskar and Great Himalayas. Valley of Flowers and Nanda Devi National Park, together, constitute the Nanda Devi Biosphere Reserve.",
        "type": "Nature & Scenic",
        "description": "Valley Of Flowers Attractions",
        "state": "Uttarakhand",
        "location": [30.7430879, 79.6177253430334],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb6947",

        "name": "Dandeli",
        "summary": "Situated on the banks of the River Kali, the picturesque town of Dandeli is one of the top Karnataka tourist places. It is located about 130 km from Goa, and 462 km from Bangalore. Dandeli is quite famous for its gorgeous natural backdrop, wildlife, and adventure activities, that can be experienced as part of Dandeli tour packages.Dandeli Wildlife Sanctuary is the second largest wildlife sanctuary in Karnataka. Dandeli is one of the top white Water Rafting destinations in India. Kayaking, water rafting, and canoeing trips on the Kali River are some of the things one can indulge in Dandeli. Sathodi Falls, Syntheri Rocks, and Kavala Caves are the other important places to visit in Dandeli.Explore our Dandeli Travel Guide for complete details on the stunning scenic place. Dandeli can also be visited along with Goa tour packages and Gokarna Packages.",
        "type": "Adventure / Trekking",
        "description": "Dandeli Attractions",
        "state": "Karnataka",
        "location": [15.2490284, 74.6236037],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6949",
        "name": "Panjim",
        "summary": "Goa is India's smallest state by area and the fourth smallest by population. Located in West India in the region known as the Konkan, it is one of the most popular tourist destinations of India with beautiful beaches and historical sites.Goa is a strip of land 110 km long and 60 km wide between the Sahyadri range of the Western Ghats and the Arabian Sea on the west coast of India. Panaji is the state's capital while Vasco Da Gama is the largest city. Renowned for its beaches, places of worship and world heritage architecture. Goa is visited by large numbers of international and domestic tourists each year. It also has rich flora and fauna.The festival of Shigmo Mel or the Holi, Goa carnival and Ganesh Chaturthi are the main festivals in Goa.",
        "type": "City",
        "description": "Panjim Attractions",
        "state": "Goa",
        "location": [15.4989946, 73.8282141],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb694a",

        "name": "Bangalore",
        "summary": "Bangalore, the capital city of Karnataka, is the 5th largest city in India, and among the top places to visit in Karnataka. It is one of the fastest growing industrial and commercial centers in India. It is often referred as Silicon Valley of India due to large number of software companies established in the city.Bangalore is one of the ideal places for those planning to visit south India with many attractions in the form of heritage palaces, gardens, museums, temples, etc. Lalbagh Garden, Cubbon Park, Tipu Sultan's Palace, Bangalore Palace, Bannerghatta National Park, and Vishveswaraiah Museum, are the some of the must include places in Bangalore tour packages. Explore our Bangalore Travel Guide for complete details on the capital city of Karnataka.Bangalore is the perfect stopover point, because this city is the gateway to a plethora of South Indian tourist destinations - you can choose from ancient temples, jungles, historic sites to even scenic countrysides for a quick weekend getaways. Coorg, Mysore, Chikmagalur, Wayanad and Ooty are the top weekend getaways from Bangalore.",
        "type": "City",
        "description": "Garden City of India",
        "state": "Karnataka",
        "location": [12.9767936, 77.590082],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb694b",

        "name": "Bhubaneswar",
        "summary": "Bhubaneswar or Bhubaneshwar is an ancient city situated in Khordha district of Odisha, India. It is the capital city of Odisha and also one of the best places to experience Odisha Tourism.It is a thriving center of art and culture. Literally, Bhubaneswar means Lord of the Universe and is known for its architecture and temples. Bhubaneswar is one of the 3 cities designed by the German Architect Otto. H. Koeingsberges along with Chandigarh and Jamshedpur and is one of the first planned cities in Modern India. The origin of the city dates back to more than 2,000 years while the modern city came into existence in 1948. Bhubaneshwar was the capital of the Kalinga dynasty. Later Emperor Kharavela established his capital in Sisupalgarh which is on the outskirts of the city. After that the area was subsequently ruled by several dynasties, including Satavahanas, Guptas, Matharas and Mughals. In 1803, the area came under the British and was part of the Bengal Presidency until 1912, and Bihar - Orissa Province till 1936. In 1936, Odisha became a separate province in British India with Cuttack as its capital. In 1947, when India got independence, Orissa became ...",
        "type": "City",
        "description": "The City of Temples",
        "state": "Odisha",
        "location": [20.2602964, 85.8394521],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb694c",

        "name": "Guwahati",
        "summary": "Guwahati is the largest city in the Indian state of Assam. Situated on the banks of Brahmaputra River, Guwahati is one of the fastest growing cities in India and among the popular places to experience Assam Tourism.Considered to be the gateway to north east India, Guwahati is situated between the southern bank of Brahmaputra River and the foothills of the Shillong plateau. Dispur, a part of Guwahati, serves as the capital of Assam. The city derives its name from two Assamese words 'Guwa' meaning betel nut and 'Haat' meaning market. The city is regarded as the cultural hub of North Eastern India and is also the second largest metropolis in eastern India after Kolkata.There have been a lot of mythological references regarding the city of Guwahati which clearly states that it has been the capital of mythological kings such as Bhagadatta and Narakasura. According to Ambari excavations, the city was under the Hindu kingdoms of Shunga-Kushana, between the 2nd century BC and the 1st century AD. Earlier called as Pragjyotishpura, it served as the capital city for the Varman and Pala dynasties and it remained the capital of Assam till the 10th - 11th Century AD. Under the Ahom kings, ...",
        "type": "City",
        "description": "City of Eastern Light",
        "state": "Assam",
        "location": [26.1805978, 91.753943],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb694d",

        "name": "Trivandrum",
        "summary": "Also known as Trivandrum, Thiruvananthapuram is the capital city of Kerala. About 85 km from Kanyakumari, and 204 km from Kochi, it is one of the most popular places to visit in Kerala.The city derives its name from the deity of Anantha Padmanabha Swamy Temple, among the must include places in Trivandrum packages. Located on the west coast of India, Trivandrum is famous for its enchanting tourist spots including internationally renowned beaches like Kovalam, historic monuments with Gothic architecture, lakes/backwaters, unexplored mountain ranges, etc. Sri Padmanabha Swamy Temple, Napier Museum, Kanakakkunnu Palace, Science, and Technology Museum, Kowdiar Palace, St. Joseph's Cathedral, Thiruvananthapuram Zoo, Happyland Amusement Park, etc. are some of the prominent tourist places in Trivandrum.Trivandrum is a popular medical tourism destination as there are more than a hundred recognized Ayurveda centers in and around the city. It is also considered as one of the cleanest cities in India, and among the most popular tourist places to visit near Kochi.",
        "type": "City",
        "description": "Trivandrum Attractions",
        "state": "Kerala",
        "location": [8.4882267, 76.947551],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb694e",
        "name": "Varanasi",
        "summary": "Varanasi is an ancient city located on the banks of river Ganga in Uttar Pradesh, India. It is one among the most revered places of Pilgrimage in India and also one of the best places to visit in Uttar Pradesh.Also known as Kashi and Banaras, the city gets its name from two rivers Varuna and Assi. Nicknamed as the cultural capital of India, Varanasi was the seat of learning in the past. Legend has it that Lord Shiva himself established this holy city as his abode. It is one of the twelve Jyotirlinga sites in India and also one of the Shakti Peethas. Varanasi is an important destination among Hindus as they believe those who die in Varanasi will attain salvation. Varanasi is also a preferred site for immersing ashes of the dead in river Ganga. Performing funeral rites and cremation in the pyres are the common sights here.The holy city of Varanasi",
        "type": "Pilgrimage",
        "description": "The holy city of Varanasi",
        "state": "Uttar Pradesh",
        "location": [25.3356491, 83.0076292],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb694f",
        "name": "Haridwar",
        "summary": "Haridwar is one of the must include places in Uttarakhand tour packages, and among the prominent pilgrimage sites near Delhi.Situated on the banks of the River Ganges, Haridwar, literally translated as Gateway to God, is one of the seven holiest places for Hindus. It is the place where the river Ganga descends to the plains. It serves as a gateway to the Char Dham destinations of Uttarakhand which are Badrinath, Kedarnath, Gangotri, and Yamunotri. Haridwar is also one of the well known places to visit near Chandigarh.Har-ki-Pauri is one of the most important Haridwar places to visit where thousands of people take a dip in the holy waters of the Ganges. Chandi Devi Temple, Mansa Devi Temple at Bilwa Parvat, Vaishno Devi Temple, Bharat Mata Temple, Maya Devi Temple, Bhimgoda, Shanti Kunj, Sapt Sarovar, Triveni Ghat, Kanva Rishi Ashram, Chila Wildlife Sanctuary are the other placesto visit as part of Haridwar packages. Haridwar is one of the venues for the famous Kumbh Mela which takes place once every 12 years.",
        "type": "Pilgrimage",
        "description": "Haridwar Attractions",
        "state": "Uttarakhand",
        "location": [29.91235135, 78.00871782398349],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6950",
        "name": "Tirupati",
        "summary": "Tirupati is a pilgrimage city in the extreme southeast of Andhra Pradesh in Chittoor district. It is often referred as a synonym to Tirumala (called as Tirumala Tirupati), which is a sacred temple town famous for Sri Venkateswara Temple also known as Tirumala Tirupati Balaji Temple. Tirupati along with Chandragiri is an ideal Chennai getaways for a two day trip and also one of the top Andhra Pradesh tourist places.Tirupati is one of the most ancient and sacred pilgrimage sites in India. Tirumala, the home of Lord Venkateswara is at a distance of 22 km from Tirupati. However, Tirupati is the town and transport hub to Tirumala at the bottom of the hill. The initial temple at Tirumala was built by the Tamil king Thondaimaan.",
        "type": "Pilgrimage",
        "description": "Tirupati Attractions",
        "state": "Andhra Pradesh",
        "location": [13.77928955, 79.83512262283737],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6951",

        "name": "Shirdi",
        "summary": "Shirdi is a pilgrimage town located in the Ahmednagar district of Maharashtra.It is among the best places to visit near Aurangabad.Shirdi is home to the shrine of Shirdi Sai Baba, the star attractions of Shirdi Tour. Sai Baba, who belonged to the 20th century, is known as one of the greatest saints of India. Sai Baba visited Shirdi when he was 16 years old and stayed there until he died in 1918. Shirdi is the place where he attained his 'Samadhi' or final abode. This is one of the must include places in Maharashtra holiday packages. The Shirdi temple complex covers an area of about 200 square meters. It includes Gurusthan, Samadhi Mandir, Dwarkamai, Chavadi, and Lendi Baug. Shirdi Temple is one of the richest temples in India with estimated donations of INR 4 billion per annum. Maruti Temple, Khandoba Mandir, Sai Heritage Village, Shanisinghnapur, and Nashik are the other Shirdi places to visit.",
        "type": "Pilgrimage",
        "description": "Shirdi Attractions",
        "state": "Maharashtra",
        "location": [19.7668121, 74.4754386],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6952",
        "name": "Somnath",
        "summary": "Somnath is a temple town situated in the Gir Somnath district of Gujarat. Also known as Prabhas Patan, it is one of the most important places of pilgrimage in India, and among the prominent places to visit in Gujarat. The town of Somnath is famous for the Somnath Temple, among the must include places in Somnath packages. Dedicated to Lord Shiva, the temple is one among the twelve prominent Jyotirlinga shrines and also one of the oldest pilgrimage sites in Gujarat. Somnath Beach, Gita Mandir, Bhalka Tirtha, Rudreshwara Temple, Triveni Sangam Temple, Suraj Mandir, Parshuram Temple, Kamnath Mahadev Temple, Junagadh Gate, Somnath Museum, Panch Pandav Gufa are some other  tourist places in Somnath.Somnath Mahadev Fair which is held on Kartik Purnima and Maha Shivaratri are the two major festivals celebrated in Somnath with great pomp and fervor. The temple town witnesses a huge number of tourists from various parts of the country during these festivals.",
        "type": "Pilgrimage",
        "description": "Somnath Attractions",
        "state": "Gujarat",
        "location": [20.8907001, 70.4025266],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6953",

        "name": "Rameshwaram",
        "summary": "Rameshwaram is one of the popular places of pilgrimage in Tamilnadu as well as in India. Situated at a distance of 562 km from Chennai, the town is home to the famous Rameshwaram Temple, among the must include places in Tamilnadu Tour Packages. Dedicated to Lord Shiva, Rameshwaram Temple is one of the Jyotirlinga temples in India, and is one of the top attractions you must visit as part of Rameshwaram tour packages. It is significant for Hindus as a pilgrimage to Banaras is incomplete without a Pilgrimage to Rameswaram. This is also the place where Rama worshipped Lord Shiva to cleanse away the sin of killing Ravana. Rameswaram along with Dwarka, Puri and Badrinath form the four Char Dhams. Sri Ramanathaswamy Temple, Agnitheertham, Gandamadana Parvatham, Dhanushkodi, Kothandaraswamy Temple and Erwadi are some of the most visited attractions of Rameshwaram. Sri Ramanatha Swamy Temple is renowned for its magnificent corridors and massive sculptured pillars. The third corridor of Ramanathaswamy temple is the longest one in the world.",
        "type": "Pilgrimage",
        "description": "Rameshwaram Attractions",
        "state": "Tamil Nadu",
        "location": [9.2844657, 79.3125553],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb6954",

        "name": "Rishikesh",
        "summary": "Located at the foothills of the Himalayas, Rishikesh is a holy city on the banks of the River Ganges in Uttarakhand. It is one of the top pilgrimage sites near Delhi, and among the prominent places to visit in Uttarakhand. Rishikesh is the gateway to the upper Garhwal region and the starting point for the Char Dham pilgrimage (Gangotri, Yamunotri, Badrinath, and Kedarnath). Rishikesh is one of the the best places to visit near Chandigarh. Rishikesh has several famous ashrams and temples. Triveni Ghat, Neel Kanth Mahadev Temple, Swarganiwas Temple, and Bharat Mandir are the important Rishikesh places to visit. Rishikesh is now famous as the Yoga Capital of the World. Every year during the February month one-week-long International Yoga Festival is hosted here. One can also try several activities like mountain biking, bungee jumping, and white water rafting as part of Rishikesh packages. It is also the base for several trekking trails in Uttarakhand state. Rishikesh can also be visited along with Haridwar tour packages.",
        "type": "Pilgrimage",
        "description": "Rishikesh Attractions",
        "state": "Uttarakhand",
        "location": [30.1086537, 78.2916193],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6955",

        "name": "Sabarimala",
        "summary": "Sabarimala is one of the most famous places of pilgrimage in Kerala. Situated about 70 km from Pathanamthitta, this temple is one of the oldest temples in India, with a history of more than 5000 years old.Regarded as one of the popular places to visit in Kerala, Sabarimala temple is dedicated to Lord Ayyappan, and is believed that Lord Parasurama installed the idol of Ayyappa here. The pilgrimage season begins in the month of November and ends in January (the temple remains closed during the rest of the year except for the first five days of each Malayalam month). The devotees following Ayyappa Vratam (Ayyappa Maala - a 41 days Vratam with strict restrictions) carry Irumudi Kettu containing traditional offerings to the Lord. Mandalapooja (Nov17th) and Makaravilakku (Jan 14th) are the important events of the temple. Makara Jyothi (a celestial star) appeared on Jan 14th is the most crowded occasion of this temple that one must witness as part of Sabarimala packages.Sabarimala temple has no restrictions on caste and religion. The temple is open to males of all age groups, but women between 10-50 years of age are NOT allowed into the temple. Pamba, Erumeli, and Malikappurathu Amma Temple are some other Sabarimala places to visit.",
        "type": "Pilgrimage",
        "description": "Sabarimala Attractions",
        "state": "Kerala",
        "location": [9.434588600000001, 77.08138690374139],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6956",

        "name": "Kanyakumari",
        "summary": "Located at the southernmost tip of the Indian Peninsula, Kanyakumari is one of the famous pilgrimage places to visit as part of Tamilnadu tour. It is about 242 km from Madurai and 707 km from Chennai.Tamilnadu Tourist Places. Swami Vivekananda is said to have been lived here for a while and meditated. Situated at the confluence of the Bay of Bengal, the Arabian Sea, and the Indian Ocean, this is the only place in India where one can enjoy the unique spectacle of Sunset and Moonrise simultaneously on full moon days. One of the main attractions in Kanyakumari is the Kumariamman Temple. Thiruvalluvar Statue, Vivekananda Rock Memorial, Gandhi Memorial, Padmanabhapuram Palace, Suchindram, Pechiparai Reservoir, Vattakottai Fort, St Xavier's Church and Udayagiri Fort are some of the top places to visit as part of Kanyakumari tour packages. Kanyakumari is also known for its spectacular beaches. Thengapattinam Beach, Sanguthurai Beach, and Chothavilai Beach are the important beaches near Kanyakumari.",
        "type": "Pilgrimage",
        "description": "A place of great natural beauty",
        "state": "Tamil Nadu",
        "location": [8.079252, 77.5499338],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6957",

        "name": "Ganpatipule",
        "summary": "Ganpatipule is a small pilgrimage & beach town on the Konkan coast of Maharashtra in India.It is one of the top places to visit near Kolhapur, and among the must include places in Maharashtra packages.Ganpatipule is mainly known for its 400 years old Ganapati Temple which is the prime attraction in Ganpatipule holiday packages. The idol of Ganesha is believed to be a monolith that was self-incarnated and discovered over 1600 years ago. It is one of the Ashta Ganapati Temples of India and is known as 'Paschim Dwar Devata'. The temple is at the base of a hill, and pilgrims walk around (pradakshina) the hill as a mark of respect. Ganpatipule can be visited as a day trip along with Mahabaleshwar tour packages. Besides, Ganpatipule has some of the most spectacular beaches that can be visited along with Konkan packages. It is an ideal getaway that attracts peace-seekers, beach lovers, and pilgrims alike. Jaigad Fort, Prachin Konkan Museum, Arey Ware Beach, Guhagar Beach, and Velneshwar are the other prominent places to visit in Ganpatipule.",
        "type": "Pilgrimage",
        "description": "Ganpatipule Attractions",
        "state": "Maharashtra",
        "location": [17.1466952, 73.2697524],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6958",

        "name": "Dwarka",
        "summary": "Dwarka is one of the most significant pilgrimage sites near Rajkot, and among the best places to visit in Gujarat. It is about 224 km from Rajkot, and 442 km from Ahmedabad.Located on the western tip of the Saurashtra peninsula in Gujarat, Dwarka is popularly known as the 'home of Lord Krishna' and is believed to have been the first capital of Gujarat. Also, Dwarka is one of the foremost Char Dhams for Hindus and among the seven most ancient religious cities (sapta puris) in India. For this reason, the town attracts thousands of pilgrims throughout the year as part of Dwarka packages.The present-day Dwarka is a prominent pilgrimage site that boasts of several shrines. Among the temples, the 2000-year-old Dwarkadhish temple is the most notable one. Nageshwar Jyotirlinga Temple, Gomti Ghat, Rukmani Devi Temple, Beyt Dwarka, Gopi Talav, Bhadkeshwar Mahadev Mandir, Swaminarayan Temple, Dwarka Beach, Shivrajpur Beach, and Okhamadhi Beach are some of the important tourist places in Dwarka. If you specifically want to participate in the grand festivities of the Janmashtami festival, visiting the town during August and September will be eventful.",
        "type": "Pilgrimage",
        "description": "Dwarka Attractions",
        "state": "Gujarat",
        "location": [22.2471009, 68.9742446],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6959",
        "name": "Mathura",
        "summary": "Mathura is one of the popular tourist places near Agra and also one of the best places to visit near Delhi.Mathura is one of the seven cities (Sapta Puri) considered holy by Hindus, the other six are Ayodhya, Haridwar, Varanasi, Kanchipuram, Ujjain and Dwarka. Mathura has been chosen as one of the heritage cities for HRIDAY - Heritage City Development and Augmentation Yojana scheme of Government of India. Mathura is also one of the popular Delhi weekend getaways for 2 day trip. Mathura is located at the banks of river Yamuna and is popularly known as the Brajbhoomi, the sacred land of Lord Krishna. The Sri Krishna Janmabhoomi temple is home to a prison cell called Garbha Griha that is believed to be the exact birthplace of Krishna. Large number of devotees visit this temple every year on Janmashtami. The city of Mathura has a rich history. In the traditional times, Mathura was an important point of culture and civilization. According to the Archaeological Survey of India, the city is mentioned in the epic, Ramayana. In the epic, the Ikshwaku prince Shatrughna slays a demon called Lavanasura and claims the land. Afterwards, the ...",
        "type": "Pilgrimage",
        "description": "Mathura Attractions",
        "state": "Uttar Pradesh",
        "location": [27.633333, 77.583333],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb695a",

        "name": "Gokarna",
        "summary": "Gokarna is one of the famous places of pilgrimage in Karnataka, and among the top places to visit as part of Karnataka tour packages. It is about 514 km from Bangalore.Sri Mahabaleshwar Temple which houses the Atmalinga is one of the must-visit places as part of Gokarna holiday packages. Gokarna is considered to be the Mukti Stala, where Hindus perform funeral rites. Gokarna is also home to some of the best beaches in Karnataka including Om Beach, Kudle Beach, Gokarna Beach. Among the beaches in Gokarna, the Om Beach is extremely popular among surfers. The beach gets its name due to the natural formation of the holy Om symbol. Explore our Gokarna Travel Guide for complete details on Gokarna. Gokarna can also be visited along with Dandeli tour packages.",
        "type": "Pilgrimage",
        "description": "Gokarna Attractions",
        "state": "Karnataka",
        "location": [14.5439629, 74.3184418],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb695c",

        "name": "Badrinath",
        "summary": "Badrinath is an ancient holy town in Chamoli district of Uttarakhand. It lies at an altitude of 3133 m in the Garhwal Himalayan ranges along the banks of River Alaknanda near India - Tibet border. It is one of the most famous centers of pilgrimage in India and also one of the most popular Uttarakhand places to visit as part of Char Dham.Badrinath is the most important of the four sites of famous Char Dham pilgrimage; the other three being Puri, Dwarka and Rameshwaram. It is also visited as part of Chota Char Dham Pilgrimage along with Kedarnath, Yamunotri and Gangotri in Himalayan region of Uttarakhand. Surrounded by Nar and Narayana mountain ranges and the Nilkantha peak, Badrinath has great mythical significance. This holy town is mentioned as Badari or Badarikashram in many ancient texts and scriptures. According to the epic Mahabharata, Badrinath is the site where Nara and Narayana, the dual forms of Vishnu, did meditation. It is also believed that the Pandavas passed through Badrinath on their way to heaven. Legend has it that Sage Vyasa authored Mahabharata at a cave in Mana, which is about 4 km from Badrinath.Badrinath is ...",
        "type": "Pilgrimage",
        "description": "Badrinath Attractions",
        "state": "Uttarakhand",
        "location": [30.7423302, 79.4930256],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb695d",

        "name": "Vrindavan",
        "summary": "Vrindavan is a holy town situated on the banks of Yamuna River in Mathura district of Uttar Pradesh. It is also among the sacred places to visit near Delhi for a 2 day weekend trip and also one of the popular places to visit near Agra.Vrindavan is a major pilgrimage center for the Hindus and one of the oldest cities in the country. The holy town of Vrindavan has a very rich history associated with the Hindu god Lord Krishna. It is said to be the place where Lord Krishna spent his childhood. Chaitanya Mahaprabhu, a great devotee of Lord Krishna is credited with rediscovering of Vrindavan. The place was later developed by various kings of the region. The name Vrindavan is derived from the words vrinda meaning tulsi (or basil) and van meaning grove and most likely refers to the two small groves at Nidhivan and Seva Kunj. While Seva Kunj is believed to be the place where Krishna performed Raaslila with Radha and the Gopikas, Nidhivan is said to be the place where the divine couple rested. The place is also one of the Shaktipeeths, named Bhuteshwar Mahadev. The place is believed to have been the site where the hair of Devi Sati fell.Vrindavan is also one of the most prominent sites for ISKCON, the association ...",
        "type": "Pilgrimage",
        "description": "Vrindavan Attractions",
        "state": "Uttar Pradesh",
        "location": [27.5753726, 77.6938045],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb695e",

        "name": "Murudeshwar",
        "summary": "Murudeshwar is one of the most famous places to visit in Karnataka and among the popular places of pilgrimage in Karnataka. It is about 162 km from Mangalore & 497 km from Bangalore. Murudeshwar is the abode of Lord Shiva. The temple town is famous for the world's second tallest Shiva statue (123 ft) & tallest temple tower (249 feet). The sea on three sides surrounds the Murudeshwar Temple towering on the small hill called Kanduka Giri. This is a great place to watch the sunset. Murdeshwar Beach, Kollur Temple are popular sites to visit as part of Murudeshwar holiday packages. Gokarna, Karwar, Kollur, Udupi, Jog Falls, Sirsi & Sringeri are the nearby attractions.Maha Shivaratri during February is the important festival celebrated here with much devotion and religious rituals. The best time to visit Murudeshwar is from November to February. Murudeshwar can also be visited along with Gokarna packages.Explore our Murudeshwar Travel Guide for complete details on the beautiful and sacred placce.",
        "type": "Pilgrimage",
        "description": "Murudeshwar Attractions",
        "state": "Karnataka",
        "location": [14.0959549, 74.4883354],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb695f",

        "name": "Udupi",
        "summary": "Udupi is one of the most famous pilgrimage sites in Karnataka, and among the top places to visit near Mangalore. Located between the verdant mountains of the Western Ghats and the Arabian Sea, Udupi is the land of breathtaking beauty. It is about 59 km from Mangalore, and 403 km from the city of Bangalore.Udupi is famous for Sri Krishna Temple which attracts pilgrims from all over India. This temple has a fascinating idol of Lord Krishna that is richly adorned with jewels. Apart from the temple, Malpe Beach, Kaup Beach & St Mary's Island are the top places to visit as part of Udupi holiday packages.Udupi can also be visited along with Murudeshwar packages. It is also the source of renowned Udupi cuisine, which is served all over India in the efficiently-run Udupi restaurants, famous for dosas, idlis and other snacks. The tradition of this cuisine started in the great kitchens of the Krishna Temple which serve meals in the form of prasad to the thousands of devotees who come to pray at the holy shrine. Explore our Udupi Travel Guide for complete details on the holy shrine.",
        "type": "Pilgrimage",
        "description": "Udupi Attractions",
        "state": "Karnataka",
        "location": [13.3419169, 74.7473232],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6960",

        "name": "Nashik",
        "summary": "Nashik or Nasik is the third-largest city by population in Maharashtra. Situated about 182 km from Mumbai, and 211 km from Pune, it is one of the popular places of pilgrimage in Maharashtra, and among the famous places to visit near Mumbai.Situated at an altitude of 700 m, Nashik is famous for its numerous temples that can be visited as part of Nashik Tour Packages. Panchavati, Someshwar, Ram Kund, Muktidham Temple, Coin Museum, Pandavleni Caves, Sinnar, Anjaneri, and Trimbakeshwar are some of the popular places to visit in Nashik.Nashik also holds Kumbha Mela, the largest religious gathering held once every 12 years. A large number of pilgrims, sadhus, and holy men attend this magnificent fair and take bath in the holy river Godavari. Apart from its religious importance, Nashik has numerous vineyards that dot the countryside and is known as the wine capital of India. Nashik can be visited along with Shirdi Tour Packages.",
        "type": "Pilgrimage",
        "description": "Nashik Attractions",
        "state": "Maharashtra",
        "location": [20.0112475, 73.7902364],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6961",

        "name": "Kumbakonam",
        "summary": "Kumbakonam is an ancient temple town located amidst the two rivers Cauvery and Arasalar in the Thanjavur district of Tamil Nadu. About 235 km from Madurai, and 282 km from Chennai, it is one of the famous places of pilgrimage in Tamilnadu, and among the popular places to visit near Chennai. Kumbakonam is known for its temples and mutts (monasteries). There are around 188 Hindu temples within the municipal limits of Kumbakonam. Adi Kumbeswarar Temple, Nageswaraswamy temple and Kasi Viswanathar temple are the prominent temples to visit as part of Kumbakonam tour packages. Sarangapani temple is the largest Vaishnava shrine present in Kumbakonam. Patteeswaram, the Oppiliappan Kovil, the Swamimalai Murugan temple and the Airavateeswarar Temple are the other temples located in the vicinity of Kumbakonam.The town is well - known for its prestigious educational institutions and carved Panchaloha idols, silk products, brass, and metal wares. The important festival of Kumbakonam is the Mahamaham festival. It takes place once in 12 years during the Tamil Month of Masi (February/March) and lakhs of pilgrims visit Kumbakonam and takes a holy bath in the sacred Mahamaham Tank.",
        "type": "Pilgrimage",
        "description": "Kumbakonam Attractions",
        "state": "Tamil Nadu",
        "location": [10.9645549, 79.37173036154906],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6962",
        "name": "Delhi City",
        "summary": "Delhi, also known as Dilli. New Delhi, the national capital of India, is one of the nine districts of the NCT of Delhi.Located in northern part of India, Delhi is situated on the banks of River Yamuna at an elevation of 293 meters. It is bound by the states of Haryana, Punjab, Uttar Pradesh and Rajasthan. Delhi is India's second most populous city after Mumbai. With an area of 47.2 sq. km, it is one of the fastest growing cities in the world. The IT sector, handloom, fashion, textile and electronic industry contribute a lot to Delhi's economy.Historically, the city was known as Indraprastha or Hastinapura, the renowned capital of the legendary Pandavas, which has overwhelming history and rich cultural heritage.",
        "type": "Historical & Heritage",
        "description": "The National Capital Territory (NCT)",
        "state": "Delhi",
        "location": [28.6559519, 77.2811441],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb6963",
        "name": "Jaipur",
        "summary": "Jaipur is the capital city of Rajasthan in Northern India. It is one of the famous places to visit in India, and among the must include places in Rajasthan tour packages. It is situated about 268 km from Delhi. Along with Delhi and Agra, Jaipur forms the Golden Triangle of Indian tourism. Jaipur attracts numerous visitors from all over the world due to its rich heritage and culture. Amber Fort, Sheesh Mahal, Ganesh Pol, Hawa Mahal, Jal Mahal, Nahargarh Fort, etc. are the important places to visit in Jaipur as part of Jaipur holiday packages.Jaipur is also famous for its beautiful jewellery, fabrics, shoes, and spacious gardens. The city is also well known for its fairs and fests that are held on a grand scale. The major festivals include Kite Festival, Camel Festival, Teej, Gangaur, and Elephant Festival. The city witnesses a large number of tourists during these festivals.",
        "type": "Historical & Heritage",
        "description": "The Pink City",
        "state": "Rajasthan",
        "location": [26.9154576, 75.8189817],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6964",
        "name": "Ajanta Caves",
        "summary": "Ajanta Caves are one of the oldest UNESCO World heritage sites in Maharashtra, and among the most prominent Maharashtra tourist places. One of the most visited ancient monuments in India, Ajanta Caves are excavated in a horseshoe-shaped bend of rock surface nearly 76 m in height overlooking the Waghur River. The complex consists of 29 rock-cut cave monuments built during the Satavahana period and the Vakataka period. The caves at Ajanta are famous for beautiful mural paintings and sculptures that depict tales of Jatakas. The world-famous paintings at Ajanta also fall into two broad phases. The earliest is noticed in the form of fragmentary specimens in Cave 9 & 10, which are among the must-visit places as part of Ajanta holiday packages. The second phase of paintings started around the 5th - 6th centuries and the specimen of these exemplary paintings could be noticed in Cave 1, 2, 16, and 17. Various incidents from the life of Gautama Buddha and the Jataka Tales are represented and recreated on the walls of these caves. It can be visited along with Aurangabad tour packages.",
        "type": "Historical & Heritage",
        "description": "Ajanta Caves Attractions",
        "state": "Maharashtra",
        "location": [20.552449699999997, 75.6995312210475],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6966",

        "name": "Mysore",
        "summary": "Mysore, the erstwhile capital of the Mysore Maharajas, is one of the popular destinations in Karnataka and among the must-visit places as part of 2 day trip near Bangalore. It is about 139 km from Bangalore. With its dazzling royal heritage, intricate architecture, its famed silk sarees, yoga, and sandalwood, Mysore is one of the top heritage sites in India. Mysore still retains its old-world charm with its palaces, heritage buildings, traditions, and temples. Mysore Palace is among the must include places in your Mysore tour packages. Apart from the Mysore Palace, Chamundi Hill Temple, Mysore Zoo, Srirangapatna, and Brindavan Gardens are the most famous places to visit in Mysore. The royal city of Mysore Dussehra is known for its grand Dussehra celebrations. The month-long Dussehra celebrations, with its colorful processions, fireworks, and the beautifully lighted palace, give an enchanting look to the city. Explore our Mysore Travel Guide for complete details on the heritage city. Mysore can also be visited as part of Coorg tour packages.",
        "type": "Historical & Heritage",
        "description": "City of Palaces",
        "state": "Karnataka",
        "location": [12.3051828, 76.6553609],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"],
        "duration": 3
    },
    {
        "_id": "63230b666ba1ea059ceb6967",

        "name": "Mumbai",
        "summary": "Mumbai is the capital city of the Indian state of Maharashtra. It is city with highest number of billionaires and is also one of the must include places in Maharashtra tour packages.Mumbai is more affectionately known as the city of dreams. The city is a collection of 7 islands and was named after the goddess Mumbadevi. Gateway of India, Chhatrapati Shivaji Terminus (Victoria Terminus), Elephanta Caves, Kanheri Caves, Haji Ali Darga, Siddivinayaka Temple, Juhu Beach, Marve Beach, Marine Drive, Chowpatty, Film City, Mani Bhavan Gandhi Sangrahalaya, Babulnath Temple and Mount Mary Church are some of the popular places to visit in Mumbai as part of Mumbai tour packages. Mumbai is the entertainment capital as well as financial powerhouse of India. The city is also famous for fashionable clothes and imitation jewellery. Mumbai is the perfect stopover point because this city is the gateway to a plethora of tourist destinations - you can choose from ancient temples, hill stations, and historic forts for a quick weekend getaway. Alibaug, Lonavala, Mahabaleshwar, and Panchgani.",
        "type": "Historical & Heritage",
        "description": "Wealthiest City in India",
        "state": "Maharashtra",
        "location": [19.0785451, 72.878176],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6968",

        "name": "Hampi",
        "summary": "Hampi is a renowned UNESCO World Heritage Site situated on the banks of Tungabhadra River in northern Karnataka. Situated about 340 km from Bangalore & 377 km from Hyderabad, Hampi is one of the best heritage sites in India and among the must include places in your Karnataka tour packages. Hampi is an extremely significant place in terms of history and architecture as it stands within the ruins of the city of Vijayanagara, the former capital of the Vijayanagara Empire. It is an open-museum of architecture, religion, and history dotted with innumerable gems that were hewed from stones. Virupaksha Temple, Vittala Temple, and Hampi Bazaar are among the must include places in your Hampi tour packages. The ruins of Vijayanagara Empire in and around the village of Hampi are spread over an area of more than 26 Sq.km. The famous Vittala Temple is located 2 km east of the Hampi Bazaar. Explore our Hampi Travel Guide for complete details on the stunning heritage city. Hampi can also be visited along with Badami tour packages.",
        "type": "Historical & Heritage",
        "description": "Hampi Attractions",
        "state": "Andhra Pradesh",
        "location": [15.3358, 76.4610201],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6969",

        "name": "Madurai",
        "summary": "Situated on the banks of the River Vaigai, Madurai is the third-largest city in Tamilnadu and one of the most famous places of pilgrimage in India. The city is situated about 209 km from Coimbatore and 464 km from Chennai. Also referred to as Athens of the East, Madhurai is the oldest continually inhabited city in the Indian peninsula, with a history dating back to the Sangam period of the pre-Christian era. Madurai was the seat of power of the Pandyan Empire. Often considered the cultural capital of Tamilnadu, Madurai is one of the top places to visit in tamilnadu. The city is very well known for Madurai Meenakshi Temple, among the most visited temple in South India tour packages.Meenakshi Temple, also known as Madurai Meenakshi, is the biggest landmark of Madurai and is one of the largest temples in India. The temple has stunning architecture and a significant testimony for Vishwakarma Brahmins for their master architecture in sculpting this temple. Along with Meenakshi Temple, Thirumalai Nayak Mahal & Koodal Alagar Temple are other important places to visit as part of Madurai tour packages.",
        "type": "Historical & Heritage",
        "description": "Madurai Attractions",
        "state": "Tamil Nadu",
        "location": [9.9261153, 78.1140983],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },

    {
        "_id": "63230b666ba1ea059ceb696a",

        "name": "Udaipur",
        "summary": "Udaipur is a historical city and also the administrative headquarters of the Udaipur district in the Indian state of Rajasthan. About 399 km from Jaipur, & 656 km from Delhi, it is one of the top heritage sites near Delhi, and among the must include places in Rajasthan tour packages. The city has an abundance of natural beauty, mesmerizing temples, and breathtaking architecture which are the prime attractions of Udaipur packages. The City Palace, Lake Palace, Bagore Ki Haveli, Pichola Lake, Fateh Sagar Lake, Lake Palace, Jag Mandir Palace, Jagdish Temple, Sajjan Garh, Saheliyon Ki Bari, and Eklingji Temple are some prominent Udaipur places to visit. Kumbhalgarh Fort, Chittorgarh Fort, Nathdwara, Sas-Bahu Temple, Ahar, and Ranakpur are the nearest attractions.Mewar festival and Gangaur festival are the popular festivals celebrated in Udaipur and have a unique charm. The festival of Gangaur is very significant for the women of Rajasthan. This festival is a visual feast with Rajasthani songs, dances, processions, devotional music, and firework displays.",
        "type": "Historical & Heritage",
        "description": "Venice of the East & City of Lakes",
        "state": "Rajasthan",
        "location": [24.578721, 73.6862571],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb696b",

        "name": "Kanchipuram",
        "summary": "Kanchipuram or Kanchi is one of the most famous places of pilgrimage in Tamilnadu. It is situated at a distance of 75 km from Chennai. It is one of the most popular places to visit near Chennai.Located on the bank of the Palar River, Kanchipuram is one of the oldest cities in India and was served as the capital of the Pallava Dynasty. Kanchi is known for its temples and silk sarees which are woven manually. Kamakshi Amman Temple is the landmark of Kanchipuram, and among the most popular places to visit in Kanchipuram. Varadharaja Perumal Temple, Kailasanathar Temple, Karchapeshwarar Temple, Sri Ekambarnathar Temple are the other prominent temples to visit as part of Kanchipuram tour packages. The temples of Kanchipuram are known for their grandeur and great architecture.Kanchipuram is a traditional center of silk weaving and handloom industries for producing Kanchipuram Sarees. In 2005, 'Kanchipuram Silk Sarees' received the Geographical Indication tag, the first product in India to carry this label.",
        "type": "Historical & Heritage",
        "description": "Kanchipuram Attractions",
        "state": "Tamil Nadu",
        "location": [12.9647163, 79.9839686],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb696d",
        "name": "Jodhpur",
        "summary": "Jodhpur is the second-largest city in the Indian state of Rajasthan. About 562 km from Delhi, it is one of the top tourist places in India, and among the must include places in Rajasthan packages.Jodhpur is featuring many palaces, forts, and temples, set in the stark landscape of the Thar Desert. The landscape is scenic and mesmerizing that one can experience as part of Jodhpur packages. Jodhpur was founded by Rao Jodha, the Chief of Rathore Clan in 1459 CE. Jodhpur is divided into the old city and the new city. The old city circles the fort and is bounded by a wall with several gates. The new city is located outside the structure. It is also known as 'Blue City' because of the houses around Mehrangarh Fort that are painted in blue. Mehrangarh Fort, Umaid Bhawan Palace, Jaswant Thada, Mandore, Kaylana Lake and Garden, Balsamand Lake, Sardar Samand Lake and Palace, Siddhnath Shiva Temple, and Naini Bai ka Temple are some of the prominent places to visit in Jodhpur. The bazaars of Jodhpur are a treasure trove of tie-and-dye textiles, embroidered leather shoes, lacquer-ware, antiques, carpets, and puppets.",
        "type": "Historical & Heritage",
        "description": "The Sun City",
        "state": "Rajasthan",
        "location": [26.2967719, 73.0351433],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb696e",

        "name": "Ahmedabad",
        "summary": "Ahmedabad is the largest city and also the former capital of Gujarat. Situated on the banks of the River Sabarmati, it is one of the popular places of places to visit in Gujarat.Ahmedabad is India's first UNESCO World Heritage City and is also regarded as one of the fastest-growing cities in India. Also known as Amdavad, the city of Ahmedabad is the commercial hub and also the living symbol of the rich cultural heritage of Gujarat state. Splendid monuments, wonderful museums, and gorgeous lakes are the prime attractions of Ahmedabad holiday packages. Popularly called the Land of Gandhi, Ahmedabad is closely associated with Mohandas Karamchand Gandhi, the father of the nation. Sabarmati Ashram, Kankarai Lake, Jama Masjid, Akshardham Temple, Adalaj Stepwell, Huthee Singh Jain Temple, ISKCON Temple, Vintage Car Museum, Nalsarovar Bird Sanctuary, Swaminarayan Mandir, and Sardar Patel National Memorial are some of the well-known tourist places in Ahmedabad.",
        "type": "Historical & Heritage",
        "description": "Ahmedabad Attractions",
        "state": "Gujarat",
        "location": [23.0216238, 72.5797068],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6970",

        "name": "Khajuraho",
        "summary": "Khajuraho is a historical town located in Chhatarpur district of Madhya Pradesh. Khajuraho is one of the top places to visit in Madhya Pradesh and among the must include places in your Madhya Pradesh tour packages. Earlier, Khajuraho was the cultural capital of Chandela Rajputs who ruled this part of India during 10th to 12th centuries AD. Khajuraho Temples were built by the Chandela monarchs over a span of 200 years, from 950 to 1150 AD. After the fall of Chandela rulers, these temples were abandoned and long-forgotten until rediscovered by British Captain T.S. Burt, in 1838 AD. Known around the world for its stunning temples adorned by erotic carvings, the Khajuraho group of monuments has been listed as a UNESCO World Heritage Site, and is considered to be one of the seven wonders of India.The marvelous architecture and erotic carvings are the best and most notable aspects of Khajuraho temples. There were originally over 80 Hindu temples, of which only 25 now stand in a reasonable state of preservation, scattered over an area of about 8 square miles. The temples also have numerous other sculptures depicting the life of a common man in that era. Khajuraho ...",
        "type": "Historical & Heritage",
        "description": "Khajuraho Attractions",
        "state": "Madhya Pradesh",
        "location": [24.8515132, 79.9259786],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6971",
        "name": "Konark",
        "summary": "Konark is a small town in Puri district of Odisha along the coast of Bay of Bengal. Renowned world over for the Sun Temple, Konark is one of the top tourist destinations in Odisha and also one of the popular places of heritage in India.The name Konark is derived from two Sanskrit words - Kona meaning angle and Arka meaning sun, in reference to the temple which was dedicated to the Sun God. Also known as the Black Pagoda, the Sun Temple was built in black granite during the reign of Narasimhadeva-I. The temple resembles the mythical chariot of the Sun God and is a UNESCO World Heritage Site since 1984. The temple is now mostly in ruins, and a collection of its sculptures is housed in the Sun Temple Museum, which is run by the Archaeological Survey of India.Konark Tourism presents a multitude of attractions that fascinate tourists from all over the world. Konark Beach, Ramachandi Temple, Kuruma, Astranga Beach, Varahi Devi Temple at Chaurasi and Maa Mangala Devi Temple at Kakatapur are some popular places to visit in Konark apart from Sun Temple. Konark was also one of the few places in India to experience a total solar eclipse.Besides the magnificent Sun Temple, Konark is also famous for Konark Dance Festival. This five day long cultural extravaganza is one of the most ...",
        "type": "Historical & Heritage",
        "description": "Konark Attractions",
        "state": "Odisha",
        "location": [19.90742915, 86.14201945385827],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6972",

        "name": "Mahabalipuram",
        "summary": "Mahabalipuram, also called Mamallapuram is one of the must-visit weekend getaways from Chennai for one day trip. About 57 km from Chennai, it is one of the UNESCO heritage site in Tamil Nadu and one of the best places to experience Tamilnadu Tourism. Famous for its Shore Temple built in 7th century, Mahabalipuram was the second capital of the Pallava kings of Kanchipuram. It is known for its historical monuments, sculptures, scenic beauty, culture and tradition. The famous Arjuna's Penance, the Krishna Mandapa, Thirukadalmallai temple, Cholamadal Artist's Village, Mahabalipuram Beach, Tiger Cave and Crocodile Bank are the must include places in Mahabalipuram tour packages. One of the prominent festivals celebrated here is the Mamallapuram Dance Festival, which is organized by the Department of Tourism every year from December - January. Mahabalipuram is one of the best places to include in your Pondicherry tour packages.",
        "type": "Historical & Heritage",
        "description": "Mahabalipuram Attractions",
        "state": "Tamil Nadu",
        "location": [12.6195981, 80.1936497],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6973",

        "name": "Jaisalmer",
        "summary": "Jaisalmer is one of the must include places in Rajasthan tour packages, and among the prominent heritage sites in India. It is situated about 278 km from Jodhpur, and 762 km from Delhi.Jaisalmer is popularly called the 'Golden City of India' because the yellow sand and the yellow sandstone used in the architecture of the city provide a golden glow to the city. Jaisalmer is also quite famous for royal forts, havelis, palaces, museums, and temples that can be visited as part of Jaisalmer packages. Jaisalmer Fort, Nathmalji ki Haveli, Salim Singh ki Haveli, Patwon ki Haveli, Manak Chowk, Jaisalmer Folklore Museum, Tazia Tower, Gadisagar Lake, Bada Bagh, Khuri Sand Dunes, Sam Sand Dunes, and Kuldhara are some of the popular tourist places in Jaisalmer. Jaisalmer attracts a lot of tourists for its desert camel safari. A bumpy ride on a camel in the Thar Desert is one of the exciting things to do in Jaisalmer. Sam Sand Dunes and Khuri Sand Dunes are the popular dunes in Jaisalmer. Jaisalmer Desert Festival, a music festival held in the 2nd week of February is also hosted near Sam Sand Dunes. Jaisalmer can be visited along with Jodhpur tour packages.",
        "type": "Historical & Heritage",
        "description": "The Heart of Thar Desert",
        "state": "Rajasthan",
        "location": [27.02801615, 70.7785056232077],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6974",

        "name": "Thanjavur",
        "summary": "Thanjavur, also known as Tanjore, is one of the popular places of heritage in Tamilnadu as it has a rich historical heritage and is a prism of ancient as well as the modern south Indian civilizations.Situated on the banks of River Cauvery, it is one of the top places to visit as part of Madurai tour packages. The city was once the stronghold of the historic Cholas. Since then, Thanjavur has been one of the chief political, cultural and religious centers of South India. Thanjavur is famous for the Brihadeeswarar Temple built by Rajaraja Chola in the year 1010 AD. Also known as the Big Temple, Brihadeeswarar Temple is one of UNESCO World Heritage Sites and among the most important heritage sites in India. The temple is considered to be one of the best specimens of South Indian temple architecture and among the must-visit places as part of Thanjavur tour packages.Apart from Brihadeeswarar Temple, Thanjavur and the surrounding areas have several important tourist attractions like Thanjavur Palace, Kumbakonam, Darasuram, Gangaikonda Cholapuram, Thiruvaiyaru, Thirubuvanam, etc.",
        "type": "Historical & Heritage",
        "description": "Thanjavur Attractions",
        "state": "Tamil Nadu",
        "location": [10.7860267, 79.1381497],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6975",

        "name": "Rann Of Kutch",
        "summary": "With the Thar Desert on one side and the Arabian Sea on the other side, Rann of Kutch is a spellbinding marvel of sand and salt. About 80 km from Bhuj, and 413 km from Ahmedabad, it is one of the top places to visit in India, and among the must include places in Gujarat packages.It lies between the Gulf of Kutch and the Indus River in Pakistan and comprises flatlands of salty clay located about 15 meters above sea level. A large part of the Kutch, commonly known as the Great Rann of Kutch, submerges in water during the rainy season and becomes dry during the winter season. Spread over an area of 7500 sq. km, the Great Rann of Kutch, formed of salt marshes, is considered one of the largest salt deserts in the world and among the most popular tourist places in Kutch.Besides, one can also visit Kutch Desert Wildlife Sanctuary, Narayan Sarovar & Sanctuary, Kalo Dungar, Siyot Caves, Chhari Dandh Bird Sanctuary, Kutch Bustard Sanctuary, etc. as part of Kutch tour packages. It can be visited along with Bhuj tour packages.",
        "type": "Historical & Heritage",
        "description": "Rann Of Kutch Attractions",
        "state": "Gujarat",
        "location": [23.790559350000002, 70.49681598808152],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6976",

        "name": "Tiruchirappalli",
        "summary": "Situated on the banks of the Cauvery River, Tiruchirappalli or Trichy is the 4th largest city in Tamilnadu and among the must include places in Tamilnadu tour packages. It is located about 133 km from Madurai and 334 km from Chennai. Tiruchirappalli is home to numerous historical monuments and temples that attract tourists and pilgrims from all parts of the country throughout the year. The city played a critical role in the Carnatic Wars (1746-1763) between the British and the French East India companies. Ranganathaswamy Temple at Srirangam, one of the most famous pilgrimage centers in South India is situated near Trichy. Rockfort Temple, Jambukeshwar Temple, Uraiyur, Mariamman Temple, Government Museum and the St John's Church are some of the top places to visit as part of Trichy tour packages.Tiruchirappalli is internationally known for a brand of cheroot known as the Trichinopoly cigar. The city is very popular for its cigars, handloom saris and stone-studded jewelry, Pith models, and cheroots. According to the National Urban Sanitation Policy (2010), Tiruchirappalli was one of the ten cleanest cities in India.",
        "type": "Historical & Heritage",
        "description": "Tiruchirappalli Attractions",
        "state": "Tamil Nadu",
        "location": [10.804973, 78.6870296],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6977",

        "name": "Alibaug",
        "summary": "Alibaug, or Alibag is a coastal town in the Raigad district of Maharashtra. About 75 km from Lonavala, & 102 km from Mumbai, it is one of the popular places for beaches in Maharashtra, and among the must include places in Konkan Tour Packages.Located in the Konkan region of Maharashtra, Alibaug is well known for its beautiful beaches and ancient forts that are the most visited places as part of Alibaug packages. Alibaug Beach, Kihim Beach, Akshi Beach, Mandwa Beach, Kashid Beach, Varsoli Beach, Nagaon Beach, Murud Beach, Kolaba Fort, and Murud -Janjira Fort are the most popular places to visit in Alibaug.It can also be visited along with Mahabaleshwar tour packages. Alibag is one of the must include places in Maharashtra Tour Packages, especially for beach lovers.",
        "type": "Historical & Heritage",
        "description": "Alibaug Attractions",
        "state": "Maharashtra",
        "location": [18.6627281, 72.8787677],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6978",

        "name": "Ajmer",
        "summary": "Ajmer or Ajmere is one of the popular pilgrimage sites near Delhi, and among the most important religious places to visit in Rajasthan. It is situated about 132 km from Jaipur, and 390 km from Delhi. Ajmer is can be visited along with Jaipur tour packages. The city of Ajmer gets its name from 'Ajay Meru'. Ajmer is home to the famous Dargah Sharif, which houses the Tomb of Garib Nawaz, also known as Moinuddin Chishti, the founder of the Chishti order of Sufism. Considered to be one of the holiest cities in India, it attracts hordes of Hindu and Muslim devotees every year as part of Ajmer packages. Anasagar, Taragarh Fort, Akbar Palace & Museum, Adhai Din Ka Jhonpra, the Nasiyan Temple, Nareli Jain temple, and Kishangarh are other popular tourist places in Ajmer. Urs of Khwaja Moinuddin Chishti is the popular fair celebrated with great pomp and fervor in Ajmer. It is held every year in the month of May to mark the death anniversary of the Sufi saint.",
        "type": "Historical & Heritage",
        "description": "Invincible Hills",
        "state": "Rajasthan",
        "location": [26.4691, 74.639],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb6979",

        "name": "Bikaner",
        "summary": "Bikaner is a vibrant desert town in the middle of the Thar Desert in Rajasthan, India. About 333 km from Jaipur, and 435 km from Delhi, it is one of the famous places of heritage in India, and among the must include places in Rajasthan tour packages.Formerly the capital of the princely state of Bikaner, the city was founded by Rao Bika in 1486 CE. The Junagarh Fort, built during the reign of Raja Rai Singh, is the most famous fort in Bikaner and is one of the must include places in Bikaner packages. The Laxmi Niwas Palace, Lalgarh Palace, Gajner Palace are some of the other palaces in Bikaner which add to the beauty of the town and gives it a feel of the Rajput heritage. Karni Mata Temple, Rampuria Haveli, National Research Centre on Camel, Shri Laxminath Temple, and Shiv Bari Temple are the other popular tourist places in Bikaner.Bikaner is one of the most frequented desert cities of the state of Rajasthan along with Jodhpur and Jaisalmer packages. Bikaner is famous for its savory Bikaneri Bhujia and Bikaner Camel Festival.",
        "type": "Historical & Heritage",
        "description": "Bikaner Attractions",
        "state": "Rajasthan",
        "location": [28.0159286, 73.3171367],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb697a",

        "name": "Chidambaram",
        "summary": "Chidambaram is a pilgrimage town in Tamil Nadu. Well known for Nataraja Temple, Chidambaram temple is one of the most celebrated shrines in South India and also one of the famous Tamilnadu places to visit. The town is known for the Thillai Nataraja Temple which is dedicated to Lord Shiva. Built during the 11th century, Chidambaram Nataraja Temple has a great religious as well as historic and cultural significance. This is one of the Panchabhoota Stalas signifying the five elements of wind (Kalahasti), water (Tiruvanaikka), fire (Tiruvannamalai), earth (Kanchipuram) and space (Chidambaram). Thillai Kaali Amman Temple, Pichavaram, Sattanathar Temple, Bhuvanagiri, Parangipettai, Annamalai University, Kollidam (river) and Poompuhar are the other prominent places to visit as part of Chidambaram tour packages.Brahmotsavam, Ani Thirumanjanam, Thai Poosam and Arudra Dharshan are some of the Nataraja Temple festivals that attract large crowds from far and nearby places. Natyanjali Dance Festival is a major festival held in February. Many eminent dancers give their performances during this festival.",
        "type": "Historical & Heritage",
        "description": "Thillai",
        "state": "Tamil Nadu",
        "location": [11.41018075, 79.67222017841891],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb697b",

        "name": "Shravanabelagola",
        "summary": "Shravanabelagola is one of the most popular Jain places of pilgrimage in Karnataka.It is one of the popular places to visit near Bangalore. Shravanabelagola is famous for the Bahubali Statue, among the must include places in Shravanabelagola tour packages. With a height of 58 feet carved out of a single block of granite, the statue is supposed to be the tallest monolithic stone statue in the world. Gomateswara temple, Odegal Basadi, Tyagada Kamba, Siddhara Basadi, Chennanna Basadi, Akhanda Bagilu, Chamundaraya Basadi, Chandragupta Basadi, Chandraprabha Basadi, Kattale Basadi, and Parshwanatha Basadi are importantplaces to visit in Shravanabelagola.Once in 12 years, Shravanabelagola celebrates the Mahamastakabhisheka festival which attracts thousands of devotees and tourists from all over India. Shravanabelagola can also be visited along with Mysore tour packages.",
        "type": "Historical & Heritage",
        "description": "Shravanabelagola Attractions",
        "state": "Karnataka",
        "location": [12.858127, 76.4870114],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb697c",

        "name": "Pune",
        "summary": "Situated at the confluence of Mula and Mutha Rivers, Pune is one of the most popular cities in India and the second-largest city in Maharashtra. Pune is one of the must include places in Maharashtra tour packages.Pune boasts of several historical monuments from the Maratha period and many places of tourist interest. Shaniwar Wada, Osho Ashram, Dagdusheth Ganapathi, Pataleshwar Cave Temple, Rajiv Gandhi Zoological Park, Shinde Chhatri, Raja Dinkar Kelkar Museum, National War Museum, Bund Garden, Saras Baug, Parvati Hill, Aga Khan Palace, Rajgad Fort, and Darshan Museum are the some of the prominent attractions one must visit as part of Pune tour packages.Also, Pune is considered as the cultural capital of Maharashtra and is renowned for its cultural activities such as classical music, spirituality, theater, sports, and literature. The city is also known for its IT, manufacturing and automobile industries, and prestigious educational institutions. Pune is also one of the fastest-growing cities in the Asia-Pacific region. The 'Mercer 2015 Quality of Living' rankings evaluated local living conditions in more than 440 cities around the world where Pune ranked at 145, second in India after Hyderabad (138).",
        "type": "Historical & Heritage",
        "description": "Pune Attractions",
        "state": "Maharashtra",
        "location": [18.521428, 73.8544541],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb697d",

        "name": "Gwalior",
        "summary": "Gwalior is a historical city situated in the central Indian state of Madhya Pradesh. It is one of the important tourist places near Agra and also one of the top tourist destinations in Madhya Pradesh.One of the most beautiful cities of Madhya Pradesh, Gwalior is very famous for its glorious history and rich cultural heritage. After being founded by Maharaja Suraj Sen in 8th century AD, Gwalior Fort was described as the pearl amongst fortresses in India. The city and its fortress have been ruled by several historic northern Indian kingdoms. From the Tomars in the 13th century, it was passed on to the Mughal Empire, then to the Maratha in 1754, followed by the Scindias in 18th century AD.Well-known for its ancient temples, marvelous palaces and alluring monuments, Gwalior is the tourist capital of Madhya Pradesh. Gwalior is best known for being the birthplace of the great musician, Tansen. And apart from all this, Gwalior was also one among the five princely states that got the honor of 21 gun salute during the British rule. Gwalior Fort, Jai Vilas Mahal, Teli ka Mandir, Sun Temple, Gujari Mahal, Sas Bahu Temple, Man Mandir Palace are some of the popular places to visit in Gwalior. Gwalior ...",
        "type": "Historical & Heritage",
        "description": "Gwalior Attractions",
        "state": "Madhya Pradesh",
        "location": [26.2037247, 78.1573628],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    },
    {
        "_id": "63230b666ba1ea059ceb697e",

        "name": "Chittorgarh",
        "summary": "Chittorgarh or Chittaurgarh is a historical city and municipality located on the banks of river Gambhiri and Berach in Rajasthan, India. About 117 km from Udaipur, and 620 km from Delhi, it is one of the top heritage places in Rajasthan, and among the must include places in Rajasthan tour packages.Chittorgarh is the former capital of the Sisodia dynasty of Mewar, and this fascinating destination can be visited along with Udaipur packages. Chittorgarh is mainly known for its beautiful forts and temples. The Chittorgarh Fort is one of the largest forts in India and among the prime places to visit as part of Chittorgarh packages. Kirti Stambh, Padmini's Palace, Rana Kumbha Palace, Vijaya Stambh, Gaumukh Reservoir, Kalika Mata Temple, Meera Temple, Shyam Temple are some of the prominent tourist places in Chittorgarh. Gangur and Jauhar are the popular festivals celebrated in Chittorgarh, followed by other festivals like Diwali and Holi.",
        "type": "Historical & Heritage",
        "description": "Chittorgarh Attractions",
        "state": "Rajasthan",
        "location": [24.71779695, 74.47210311178024],
        "guides": ["63255ce17a4c80b378fd469a", "63255d0e7a4c80b378fd469d"]
    }
]

# Create a new list to store modified JSON objects
output_json_data = []

# Iterate through each input JSON object
for obj in input_json_data:
   # Remove the "_id", "summary", and "guides" attributes
    obj.pop("_id", None)
    obj.pop("summary", None)
    obj.pop("guides", None)
    
    # Separate the "location" array into "latitude" and "longitude" attributes
    latitude, longitude = obj["location"]
    obj["latitude"] = latitude
    obj["longitude"] = longitude
    obj.pop("location", None)
    
    #Append the modified object to the output list
    output_json_data.append(obj)

    print(type(obj))

# Define the output JSON file path
output_file_path = "modified_data.json"

# Write the modified JSON data to a file
with open(output_file_path, "w") as output_file:
    json.dump(output_json_data, output_file, indent=4)

print(f"Modified data saved to {output_file_path}")
