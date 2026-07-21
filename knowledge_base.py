# =============================================== RESTAURANT BAISC INFO =============================================== #

info = {
    "restaurant_name": "Big Plate",
    "about_restaurant": "🍽️ We're Big Plate! A popular, multi-cuisine restaurant with multiple locations in Sri Lanka (including Kollupitiya, Rajagiriya, and Port City). We're well-known for our large, generous portions and diverse menu that covers everything from Sri Lankan staples like Biryani and Kottu to Arabic Shawarmas, Chinese dishes, and American fast food.",
    "hotline": "+94 77 035 9400",
    "email": "marketing@bigplate.lk",
    "website": "bigplate.lk",
    "app": "Big Plate",
    
    "branches": [
        {
            "colombo3": {
                "name": "Big Plate - Colombo 3",
                "address": "No 32, Marine Drive, Kollupitiya, Colombo 03",
                "contact": "+94 77 779 9400"
            }
        },

        {
            "rajagiriya": {
                "name": "Big Plate - Rajagiriya",
                "address": "493/1, Sri Jayawardhanepura Mawatha, Kotte",
                "contact": "+94 77 744 9222"
            }
        },

        {
            "portcity": {
                "name": "Big Plate - Port City",
                "address": "Port City Beach Plaza",
                "contact": "+94 77 795 7795"
            }
        }
    ],

    "socials": {
        "facebook": "facebook.com/Bigplatelk",
        "instagram": "instagram.com/bigplate.lk",
        "website": "bigplate.lk"
    },

    "working_hours": {
        "open": "11:30 AM",
        "close": "12:30 AM"
    },
}

# =============================================== RESTAURANT MENU INFO =============================================== #

# 54 Food Items
menu = {
    # =========== VEGETARIAN (9) =========== #

    "chilli paneer": {
        "price": 1550,
        "description": "A popular vegetarian Indo-Chinese dish made with crispy paneer cubes tossed in spicy chili sauce with vegetables. This flavorful dish is rich, spicy, and satisfying.",
        "ingredients": ["Paneer", "onion", "capsicum", "garlic", "ginger", "green chili", "soy sauce", "chili sauce", "corn flour", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "paneer 65": {
        "price": 1800,
        "description": "A vegetarian version of the famous 65 dish made with crispy paneer cubes coated in flavorful spices and curry leaves. This dish is crispy, spicy, and delicious.",
        "ingredients": ["Paneer", "garlic", "ginger", "curry leaves", "green chili", "chili powder", "corn flour", "wheat flour", "vegetable oil", "black pepper", "salt"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "paneer tikka 6 pcs": {
        "price": 1800,
        "description": "A popular vegetarian grilled dish made with paneer cubes marinated in spices and yogurt, then cooked until smoky and flavorful. This dish is rich, aromatic, and satisfying.",
        "ingredients": ["Paneer", "yogurt", "capsicum", "onion", "garlic", "ginger", "chili powder", "garam masala", "lemon juice", "vegetable oil", "black pepper", "salt"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "paneer butter masala": {
        "price": 1800,
        "description": "A rich and creamy vegetarian curry made with soft paneer cubes cooked in buttery tomato gravy with mild spices.",
        "ingredients": ["Paneer", "butter", "tomato", "fresh cream", "garlic", "ginger", "garam masala", "chili powder", "sugar", "vegetable oil", "black pepper", "salt", "coriander leaves"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "paneer tikka masala": {
        "price": 1850,
        "description": "A flavorful vegetarian curry made with grilled paneer cubes cooked in rich tomato-based masala sauce.",
        "ingredients": ["Paneer", "onion", "tomato", "yogurt", "garlic", "ginger", "garam masala", "chili powder", "turmeric", "vegetable oil", "black pepper", "salt", "coriander leaves"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "mushroom masala": {
        "price": 1550,
        "description": "A delicious vegetarian curry made with fresh mushrooms cooked in rich onion and tomato-based masala gravy.",
        "ingredients": ["Mushroom", "onion", "tomato", "garlic", "ginger", "garam masala", "chili powder", "turmeric", "vegetable oil", "black pepper", "salt", "coriander leaves"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "kadai paneer": {
        "price": 1950,
        "description": "A popular North Indian vegetarian dish made with paneer cooked with capsicum, tomatoes, and aromatic kadai spices.",
        "ingredients": ["Paneer", "onion", "tomato", "capsicum", "garlic", "ginger", "garam masala", "chili powder", "coriander powder", "vegetable oil", "black pepper", "salt", "coriander leaves"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "paneer makhani": {
        "price": 1650,
        "description": "A creamy and rich North Indian vegetarian dish made with soft paneer cubes cooked in a buttery tomato-based gravy with mild spices. This dish is smooth, flavorful, and satisfying.",
        "ingredients": ["Paneer", "butter", "tomato", "fresh cream", "garlic", "ginger", "garam masala", "chili powder", "sugar", "vegetable oil", "black pepper", "salt", "coriander leaves"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    "channa masala": {
        "price": 1099,
        "description": "A popular North Indian vegetarian curry made with chickpeas cooked in a rich tomato and spice-based gravy. This dish is hearty, flavorful, and full of aromatic spices.",
        "ingredients": ["Chickpeas", "onion", "tomato", "garlic", "ginger", "green chili", "garam masala", "chili powder", "turmeric", "coriander powder", "vegetable oil", "black pepper", "salt"],
        "time": 20,
        "vegetarian": True,
        "category": "vegetarian"
    },

    # =========== STARTER (5) =========== #

    "french fries": {
        "price": 999,
        "description": "Crispy on the outside, soft on the inside, these golden potato sticks are the ultimate snack or side, perfect for dipping in your favorite sauces.",
        "ingredients": ["potato", "salt"],
        "time": 15,
        "vegetarian": True,
        "category": "starter"
    },

    "hot garlic wings": {
        "price": 1299,
        "description": "Juicy chicken wings tossed in a fiery garlic sauce, delivering the perfect balance of heat and flavor in every bite.",
        "ingredients": ["Chicken wings", "garlic", "chili sauce", "soy sauce", "black pepper", "salt"],
        "time": 20,
        "vegetarian": False,
        "category": "starter"
    },

    "calamari": {
        "price": 1850,
        "description": "Golden, crunchy seafood strips fried to perfection and served with a creamy spicy dipping sauce. Light, crispy coating with tender, juicy seafood inside — perfect as a starter or sharing snack.",
        "ingredients": ["Calamari (squid)", "seafood strips (likely prawns or squid)", "batter coating", "oil for deep frying", "mayo", "chili", "spices"],
        "time": 20,
        "vegetarian": False,
        "category": "starter"
    },

    "coleslaw salad": {
        "price": 900,
        "description": "A refreshing mix of crisp cabbage, carrots, and tangy dressing, perfectly creamy and crunchy with every bite.",
        "ingredients": ["finely shredded raw cabbage (green, purple, or a mix)", "grated carrots", "mayonnaise", "vinegar (apple cider or white)", "sugar", "Dijon mustard"],
        "time": 20,
        "vegetarian": True,
        "category": "starter"
    },

    "chicken lollipop": {
        "price": 1650,
        "description": "A popular appetizer made with juicy chicken wings shaped into lollipops, marinated with spices and deep-fried until crispy. This halal-friendly dish is crunchy on the outside and tender inside, perfect as a starter or snack.",
        "ingredients": ["Chicken wings", "garlic", "ginger", "chili powder", "soy sauce", "corn flour", "wheat flour", "egg", "vegetable oil", "black pepper", "salt"],
        "time": 20,
        "vegetarian": False,
        "category": "starter"
    },

    # =========== SOUP (2) =========== #

    "sweet corn seafood soup": {
        "price": 899,
        "description": "Delight in the rich and comforting taste of our Sweet Corn Seafood Soup. This flavorful soup combines sweet corn kernels with a mix of tender seafood, gently simmered in a light, savory broth. Smooth, comforting, and full of umami flavor.",
        "ingredients": ["Mixed seafood", "sweet corn kernels", "seafood stock", "egg", "cornflour", "garlic", "ginger", "spring onions", "soy sauce", "salt", "white pepper", "sesame oil"],
        "time": 20,
        "vegetarian": False,
        "category": "soup"
    },

    "sweet corn chicken soup": {
        "price": 899,
        "description": "Warm, comforting, and full of flavor, our Sweet Corn Chicken Soup is a classic favorite made with tender shredded chicken and naturally sweet corn kernels simmered in a light, savory broth. Smooth, hearty, and deliciously satisfying, this comforting soup is perfect as a starter or a light meal, delivering a perfect balance of sweetness and savory goodness in every spoonful.",
        "ingredients": ["Chicken breast", "sweet corn kernels", "chicken stock", "egg", "cornflour", "garlic", "ginger", "spring onions", "salt", "white pepper"],
        "time": 20,
        "vegetarian": False,
        "category": "soup"
    },

    # =========== SANDWITCHES (3) =========== #

    "vegetable sandwich": {
        "price": 950,
        "description": "Enjoy a fresh and satisfying bite with our Vegetable Sandwich, served as 4 delicious pieces alongside crispy French fries. Made with toasted bread layered with fresh vegetables and creamy spread, this sandwich delivers a perfect balance of crunch, flavor, and freshness. Paired with golden, crispy fries, it’s a light yet filling meal ideal for any time of the day.",
        "ingredients": ["Sandwich bread (toasted)", "lettuce", "tomato slices", "cucumber slices", "onion slices", "carrot (grated)", "mayonnaise or butter spread", "cheese slice (optional)", "black pepper", "salt", "french fries"],
        "time": 20,
        "vegetarian": True,
        "category": "sandwich"
    },

    "chicken club sandwich": {
        "price": 1250,
        "description": "Enjoy a hearty and satisfying meal with our Chicken Club Sandwich, served as 4 delicious pieces with a side of crispy French fries. Made with toasted sandwich bread layered with tender chicken, fresh vegetables, and creamy mayo, this classic sandwich offers the perfect combination of flavor, crunch, and freshness. Paired with golden, crispy fries, it’s an ideal choice for a filling lunch or snack.",
        "ingredients": ["Sandwich bread (toasted)", "cooked chicken breast (shredded)", "lettuce", "tomato slices", "cucumber slices"],
        "time": 20,
        "vegetarian": False,
        "category": "sandwich"
    },

    "tuna club sandwich": {
        "price": 1250,
        "description": "Enjoy a delicious and satisfying meal with our Tuna Club Sandwich, served as 4 tasty pieces with a side of crispy French fries. Made with toasted sandwich bread layered with flavorful tuna filling, fresh vegetables, and creamy mayo, this sandwich offers a perfect balance of freshness and savory taste. Paired with golden, crispy fries, it’s a great choice for a light yet filling meal any time of the day.",
        "ingredients": ["Sandwich bread (toasted)", "tuna flakes", "lettuce", "tomato slices", "cucumber slices", "onion slices", "mayonnaise", "cheese slice (optional)", "black pepper", "salt", "french fries"],
        "time": 20,
        "vegetarian": False,
        "category": "sandwich"
    },

    # =========== RICE (6) =========== #

    "vegetable fried rice": {
        "price": 1199,
        "description": "Fragrant long-grain rice stir-fried in a hot wok with a colorful mix of fresh vegetables and savory sauces. This classic Asian favorite is cooked with aromatic garlic and perfectly seasoned to deliver a rich, satisfying flavor in every bite. Light yet filling, our Vegetable Fried Rice is a delicious halal-friendly option, perfect as a main dish or as a side with your favorite meals.",
        "ingredients": ["Rice", "Carrot", "Green beans", "Cabbage", "Leeks", "Onion", "Garlic", "Green chili", "Spring onion", "Soy sauce", "Vegetable oil", "Salt", "Pepper", "Sesame oil", "Egg"],
        "time": 20,
        "vegetarian": True,
        "category": "rice"
    },

    "egg fried rice": {
        "price": 799,
        "description": "A flavorful and satisfying rice dish made with fluffy rice stir-fried in a hot wok with scrambled eggs and fresh vegetables. Seasoned with aromatic garlic and savory sauces, this halal-friendly Egg Fried Rice delivers a perfect balance of taste and texture. Light, fragrant, and delicious, it is an ideal choice for a quick meal or a tasty side dish.",
        "ingredients": ["Rice", "Egg", "Carrot", "Green beans", "Cabbage", "Leeks", "Onion", "Garlic", "Green chili", "Spring onion", "Soy sauce", "Vegetable oil", "Salt", "Pepper", "Sesame oil"],
        "time": 20,
        "vegetarian": False,
        "category": "rice"
    },

    "beef fried rice": {
        "price": 1699,
        "description": "A rich and flavorful rice dish made with fluffy rice stir-fried in a hot wok with tender halal beef, scrambled egg, and fresh vegetables. Infused with aromatic garlic and savory sauces, this hearty fried rice delivers a delicious balance of taste and texture in every bite. A satisfying meal perfect for beef lovers.",
        "ingredients": ["Rice", "Beef", "Egg", "Carrot", "Green beans", "Cabbage", "Leeks", "Onion", "Garlic", "Green chili", "Spring onion", "Soy sauce", "Vegetable oil", "Salt", "Pepper", "Sesame oil"],
        "time": 20,
        "vegetarian": False,
        "category": "rice"
    },

    "chicken nasi goreng rice": {
        "price": 1890,
        "description": "A classic Indonesian-style fried rice cooked in a hot wok with tender halal chicken, savory sausages, and sweet pineapple for a delicious balance of flavors. Stir-fried with aromatic garlic, spices, and rich sauces, this dish offers a slightly sweet and savory taste with a fragrant finish. A flavorful and satisfying meal perfect for any time of the day.",
        "ingredients": ["Rice", "Chicken", "Sausages", "Pineapple", "Egg", "Carrot", "Leeks", "Onion", "Garlic", "Green chili", "Spring onion", "Soy sauce", "Chili sauce", "Tomato sauce", "Vegetable oil", "Salt", "Pepper", "Sesame oil"],
        "time": 20,
        "vegetarian": False,
        "category": "rice"
    },

    "mongolian seafood rice": {
        "price": 4250,
        "description": "A rich and flavorful rice dish served with delicious Mongolian-style seafood cooked in a savory and slightly spicy sauce. Made with a mix of fresh seafood and vegetables, this dish is perfectly seasoned with garlic, sauces, and spices to create a bold and satisfying taste. Served over fluffy rice, it is a perfect choice for seafood lovers looking for a hearty and flavorful meal.",
        "ingredients": ["Rice", "Kang kung", "Prawns", "Cuttlefish", "Fish", "Carrot", "Cabbage", "Leeks", "Onion", "Garlic", "Green chili", "Spring onion", "Soy sauce", "Oyster sauce", "Chili sauce", "Corn flour", "Vegetable oil", "Salt", "Pepper", "Sesame oil"],
        "time": 20,
        "vegetarian": False,
        "category": "rice"
    },

    "mongolian mixed rice": {
        "price": 4250,
        "description": "A hearty and flavorful rice dish served with Mongolian-style stir-fry made from a rich mix of meats and seafood. Tender chicken, beef, fish, prawns, and savory sausages are cooked with fresh vegetables in a bold, savory, and slightly spicy Mongolian sauce. Served over fluffy rice, this dish offers a delicious variety of flavors and textures in every bite.",
        "ingredients": ["Rice", "Kang kung", "Chicken", "Beef", "Fish", "Prawns", "Sausages", "Carrot", "Cabbage", "Leeks", "Onion", "Garlic", "Green chili", "Spring onion", "Soy sauce", "Oyster sauce", "Chili sauce", "Corn flour", "Vegetable oil", "Salt", "Pepper", "Sesame oil"],
        "time": 20,
        "vegetarian": False,
        "category": "rice"
    },

    # =========== NOODLES (4) =========== #

    "mixed fried noodles": {
        "price": 1950,
        "description": "A hearty and flavorful noodle dish loaded with a variety of meats and seafood. Our Mixed Fried Noodles are stir-fried on high heat with tender chicken, beef, fish, prawns, and sausages, combined with fresh vegetables and savory sauces. This halal-friendly dish delivers a rich, satisfying taste with every bite, making it perfect for those who enjoy a generous mix of flavors and textures.",
        "ingredients": ["Egg noodles", "Fish", "Prawns", "Chicken", "Beef", "Sausage", "Cabbage", "Carrot", "Leeks", "Green beans", "Capsicum", "Onion", "Garlic", "Ginger", "Soy sauce", "Chili sauce", "Vegetable oil", "Black pepper", "Salt", "Spring onion"],
        "time": 20,
        "vegetarian": False,
        "category": "noodles"
    },

    "thai chicken noodles": {
        "price": 1999,
        "description": "A fragrant and flavorful noodle dish inspired by Thai-style cooking. Our Thai Chicken Noodles are stir-fried with tender chicken, fresh vegetables, and a blend of aromatic sauces that deliver a slightly sweet, savory, and mildly spicy taste. Cooked on high heat, the noodles absorb the rich flavors perfectly, creating a delicious and satisfying halal-friendly meal.",
        "ingredients": ["Egg noodles", "chicken", "cabbage", "carrot", "leeks", "capsicum", "onion", "garlic", "ginger", "soy sauce", "chili sauce", "oyster sauce", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": False,
        "category": "noodles"
    },

    "egg fried noodles": {
        "price": 1199,
        "description": "A classic and flavorful noodle dish stir-fried with fresh vegetables and scrambled eggs. Our Egg Fried Noodles are cooked on high heat to create a perfect balance of soft noodles and lightly crisp vegetables, combined with savory sauces and aromatic seasonings. This halal-friendly dish offers a rich taste and satisfying texture, making it a popular choice for a quick and delicious meal.",
        "ingredients": ["Egg noodles", "egg", "cabbage", "carrot", "leeks", "green beans", "capsicum", "onion", "garlic", "ginger", "soy sauce", "chili sauce", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": True,
        "category": "noodles"
    },

    "chop-suey mixed noodles": {
        "price": 4499,
        "description": "A delicious noodle dish inspired by classic chop suey flavors, featuring a generous mix of meats and fresh vegetables. Our Chopsuey Mixed Noodles are stir-fried with tender chicken, beef, and prawns, combined with crunchy vegetables and savory sauces. Cooked over high heat, this halal-friendly dish delivers a rich taste and satisfying texture in every bite.",
        "ingredients": ["Egg noodles", "chicken", "beef", "prawns", "cabbage", "carrot", "leeks", "green beans", "capsicum", "onion", "garlic", "ginger", "soy sauce", "chili sauce", "oyster sauce", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": False,
        "category": "noodles"
    },

    # =========== KOTTU (5) =========== #

    "vegetable kottu": {
        "price": 999,
        "description": "A popular Sri Lankan street food made with chopped godamba roti stir-fried with fresh vegetables and flavorful spices. Our Vegetable Kottu is cooked on a hot griddle, mixing soft roti pieces with crunchy vegetables and aromatic seasonings to create a delicious and satisfying halal-friendly meal full of texture and taste.",
        "ingredients": ["Godamba roti", "cabbage", "carrot", "leeks", "green beans", "capsicum", "onion", "garlic", "ginger", "egg", "soy sauce", "curry powder", "chili flakes", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": True,
        "category": "kottu"
    },

    "egg kottu": {
        "price": 1199,
        "description": "A classic Sri Lankan street food made with chopped godamba roti stir-fried with eggs, fresh vegetables, and flavorful spices. Our Egg Kottu is cooked on a hot griddle, blending soft roti pieces with scrambled eggs and aromatic seasonings to create a rich and satisfying halal-friendly dish with delicious taste and texture.",
        "ingredients": ["Godamba roti", "egg", "cabbage", "carrot", "leeks", "green beans", "capsicum", "onion", "garlic", "ginger", "soy sauce", "curry powder", "chili flakes", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": False,
        "category": "kottu"
    },

    "chicken kottu": {
        "price": 1499,
        "description": "A famous Sri Lankan street food made with chopped godamba roti stir-fried with tender pieces of chicken, fresh vegetables, and aromatic spices. Our Chicken Kottu is prepared on a hot griddle, mixing soft roti pieces with juicy chicken and flavorful seasonings to create a rich and satisfying halal-friendly dish with bold taste and texture.",
        "ingredients": ["Godamba roti", "chicken", "egg", "cabbage", "carrot", "leeks", "green beans", "capsicum", "onion", "garlic", "ginger", "soy sauce", "curry powder", "chili flakes", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": False,
        "category": "kottu"
    },

    "beef kottu": {
        "price": 1699,
        "description": "A hearty Sri Lankan street food made with chopped godamba roti stir-fried with tender pieces of beef, fresh vegetables, and aromatic spices. Our Beef Kottu is prepared on a hot griddle, combining soft roti pieces with flavorful beef and savory seasonings to create a rich and satisfying halal-friendly dish with bold taste and texture.",
        "ingredients": ["Godamba roti", "beef", "egg", "cabbage", "carrot", "leeks", "green beans", "capsicum", "onion", "garlic", "ginger", "soy sauce", "curry powder", "chili flakes", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": False,
        "category": "kottu"
    },

    "seafood kottu": {
        "price": 1799,
        "description": "A flavorful Sri Lankan street food made with chopped godamba roti stir-fried with a delicious mix of seafood, fresh vegetables, and aromatic spices. Our Seafood Kottu is cooked on a hot griddle, combining soft roti pieces with prawns and cuttlefish, creating a rich and satisfying halal-friendly dish full of bold flavors and texture.",
        "ingredients": ["Godamba roti", "prawns", "cuttlefish", "egg", "cabbage", "carrot", "leeks", "green beans", "capsicum", "onion", "garlic", "ginger", "soy sauce", "curry powder", "chili flakes", "vegetable oil", "black pepper", "salt", "spring onion"],
        "time": 20,
        "vegetarian": False,
        "category": "kottu"
    },

    # =========== BURGER (4) =========== #

    "crispy chicken burger": {
        "price": 1599,
        "description": "Enjoy the perfect comfort meal with our Crispy Chicken Burger served with a side of golden French fries. A juicy, crispy-fried chicken fillet is tucked inside a soft, toasted bun with fresh lettuce, juicy tomato slices, and creamy mayo for the perfect balance of crunch and flavor. Paired with hot, crispy French fries, this satisfying combo is ideal for lunch, dinner, or anytime cravings.",
        "ingredients": ["crispy fried chicken fillet", "toasted bun", "lettuce", "tomato slices", "creamy mayo", "french fries"],
        "time": 20,
        "vegetarian": False,
        "category": "burger"
    },

    "tower burger": {
        "price": 3100,
        "description": "A bold, satisfying feast for serious burger lovers. This towering triple-layer crispy chicken burger is stacked with perfectly golden fried chicken, melted cheese, fresh lettuce, and savory deli slices, all tucked inside soft toasted brioche buns. Finished with rich house sauces for the perfect balance of flavor and texture in every bite. Served as a Big Plate Special with a generous portion of crispy golden French fries, making it a complete and indulgent meal that’s perfect for lunch, dinner, or anytime you crave something big and delicious.",
        "ingredients": ["toasted brioche burger buns", "crispy fried chicken pieces", "cheddar cheese slices", "deli ham / smoked chicken slice", "fresh lettuce", "burger sauce / mayonnaise", "tomato ketchup or BBQ sauce", "wooden skewer with olive", "chicken pieces (boneless)", "flour / crispy coating mix", "salt", "black pepper", "paprika or chili powder", "garlic powder", "eggs / buttermilk", "french fries"],
        "time": 20,
        "vegetarian": False,
        "category": "burger"
    },

    "classic chicken burger": {
        "price": 1350,
        "description": "A delicious and satisfying burger made with our in-house chicken patty served in a soft toasted bun. Layered with fresh vegetables and flavorful sauces, this burger offers a juicy, savory taste with a perfect balance of texture and flavor. For an extra treat, you can add egg and crispy beef bacon to enhance the taste. This halal-friendly burger is a great choice for a hearty and tasty meal.",
        "ingredients": ["burger bun", "in house chicken patty", "lettuce", "tomato", "onion", "cheese", "mayonnaise", "tomato sauce", "mustard sauce", "black pepper", "salt", "vegetable oil"],
        "time": 20,
        "vegetarian": False,
        "category": "burger"
    },

    "classic beef burger": {
        "price": 1450,
        "description": "A juicy and satisfying burger made with our in-house beef patty served in a soft toasted bun. Layered with fresh vegetables and flavorful sauces, this burger delivers a rich, savory taste with every bite. You can upgrade your burger by adding egg and crispy beef bacon for an extra boost of flavor. This halal-friendly burger is a perfect choice for a hearty and delicious meal.",
        "ingredients": ["burger bun", "in house beef patty", "lettuce", "tomato", "onion", "cheese", "mayonnaise", "tomato sauce", "mustard sauce", "black pepper", "salt", "vegetable oil"],
        "time": 20,
        "vegetarian": False,
        "category": "burger"
    },

    # =========== SUBMARINE (3) =========== #

    "chicken submarine": {
        "price": 1440,
        "description": "A delicious and filling submarine sandwich made with tender chicken and fresh vegetables served in a soft toasted sub roll. Our Chicken Submarine is layered with flavorful sauces and perfectly seasoned chicken, creating a satisfying and tasty halal-friendly meal with every bite.",
        "ingredients": ["submarine bread", "chicken", "lettuce", "tomato", "onion", "cheese", "mayonnaise", "tomato sauce", "black pepper", "salt", "vegetable oil"],
        "time": 20,
        "vegetarian": False,
        "category": "submarine"
    },

    "chilli chicken submarine": {
        "price": 1640,
        "description": "A spicy and flavorful submarine made with tender chilli chicken served in a soft toasted sub roll. Our Chilli Chicken Submarine is layered with fresh vegetables and savory sauces, creating a perfect balance of heat and flavor. This halal-friendly dish is a delicious choice for those who enjoy a bold and satisfying meal.",
        "ingredients": ["submarine bread", "chicken", "onion", "capsicum", "tomato", "lettuce", "garlic", "chili sauce", "soy sauce", "mayonnaise", "tomato sauce", "black pepper", "salt", "vegetable oil"],
        "time": 20,
        "vegetarian": False,
        "category": "submarine"
    },

    "shawarma chicken submarine": {
        "price": 1799,
        "description": "A flavorful submarine made with tender shawarma-style chicken served in a soft toasted sub roll. Our Shawarma Chicken Submarine is layered with fresh vegetables and creamy sauces, creating a rich and aromatic taste inspired by Middle Eastern flavors. This halal-friendly dish offers a delicious and satisfying combination of juicy chicken and bold seasoning.",
        "ingredients": ["submarine bread", "shawarma chicken", "lettuce", "tomato", "onion", "cucumber", "garlic sauce", "mayonnaise", "chili sauce", "black pepper", "salt", "vegetable oil"],
        "time": 20,
        "vegetarian": False,
        "category": "submarine"
    },

    # =========== BIRIYANI (5) =========== #

    "chicken biriyani": {
        "price": 1200,
        "description": "A classic and flavorful biriyani made with tender chicken cooked with aromatic basmati rice and traditional spices. This halal-friendly dish offers a rich, savory taste with perfectly balanced flavors, making it a popular choice for any occasion.",
        "ingredients": ["Basmati rice", "chicken", "onion", "tomato", "yogurt", "garlic", "ginger", "biriyani spices", "chili powder", "turmeric", "vegetable oil", "coriander leaves", "mint leaves", "salt"],
        "time": 20,
        "vegetarian": False,
        "category": "biriyani"
    },

    "beef biriyani": {
        "price": 1899,
        "description": "A hearty and rich biriyani prepared with tender beef slow-cooked with fragrant basmati rice and bold spices. This halal-friendly dish delivers deep, robust flavor and a satisfying experience in every bite.",
        "ingredients": ["Basmati rice", "beef", "onion", "tomato", "yogurt", "garlic", "ginger", "biriyani spices", "chili powder", "turmeric", "vegetable oil", "coriander leaves", "mint leaves", "salt"],
        "time": 20,
        "vegetarian": False,
        "category": "biriyani"
    },

    "egg biriyani": {
        "price": 899,
        "description": "A simple yet delicious biriyani made with boiled eggs cooked with aromatic basmati rice and spices. This halal-friendly dish is flavorful, satisfying, and perfect for a lighter option.",
        "ingredients": ["Basmati rice", "egg", "onion", "tomato", "yogurt", "garlic", "ginger", "biriyani spices", "chili powder", "turmeric", "vegetable oil", "coriander leaves", "mint leaves", "salt"],
        "time": 20,
        "vegetarian": True,
        "category": "biriyani"
    },

    "fish biriyani": {
        "price": 0,
        "description": "A flavorful biriyani prepared with tender fish and fragrant basmati rice cooked with traditional spices. This halal-friendly dish offers a light yet rich taste with perfectly blended flavors.",
        "ingredients": ["Basmati rice", "fish", "onion", "tomato", "yogurt", "garlic", "ginger", "biriyani spices", "chili powder", "turmeric", "vegetable oil", "coriander leaves", "mint leaves", "salt"],
        "time": 20,
        "vegetarian": False,
        "category": "biriyani"
    },

    "prawns biriyani": {
        "price": 0,
        "description": "A delicious seafood biriyani made with juicy prawns cooked with aromatic basmati rice and flavorful spices. This halal-friendly dish offers a rich and slightly tangy taste, perfect for seafood lovers.",
        "ingredients": ["Basmati rice", "prawns", "onion", "tomato", "yogurt", "garlic", "ginger", "biriyani spices", "chili powder", "turmeric", "vegetable oil", "coriander leaves", "mint leaves", "salt"],
        "time": 20,
        "vegetarian": False,
        "category": "biriyani"
    },

    # =========== DRINKS (5) =========== #

    "water bottle": {
        "price": 70,
        "description": "Pure and refreshing drinking water to keep you hydrated.",
        "ingredients": ["Mineral water"],
        "time": 5,
        "vegetarian": False,
        "category": "drinks"
    },

    "ginger beer": {
        "price": 340,
        "description": "A refreshing and mildly spicy non-alcoholic drink with a bold ginger flavor.",
        "ingredients": ["Carbonated water", "ginger flavor", "sugar"],
        "time": 5,
        "vegetarian": False,
        "category": "drinks"
    },

    "pepsi": {
        "price": 365,
        "description": "A classic carbonated soft drink with a sweet and refreshing cola taste.",
        "ingredients": ["Carbonated water", "sugar", "caffeine", "flavoring"],
        "time": 5,
        "vegetarian": False,
        "category": "drinks"
    },

    "seven up": {
        "price": 350,
        "description": "A crisp and refreshing lemon-lime flavored soft drink.",
        "ingredients": ["Carbonated water", "lemon flavor", "sugar"],
        "time": 5,
        "vegetarian": False,
        "category": "drinks"
    },

    "mountain dew": {
        "price": 340,
        "description": "A citrus-flavored soft drink with a bold and refreshing taste.",
        "ingredients": ["Carbonated water", "citrus flavor", "sugar", "caffeine"],
        "time": 5,
        "vegetarian": False,
        "category": "drinks"
    },

    # =========== DESERTS (3) =========== #

    "brownie": {
        "price": 499,
        "description": "A rich and moist chocolate brownie with a soft center and slightly crisp edges, perfect for chocolate lovers.",
        "ingredients": ["Chocolate", "cocoa powder", "flour", "egg", "sugar"],
        "time": 2,
        "vegetarian": False,
        "category": "dessert"
    },

    "caramel pudding": {
        "price": 490,
        "description": "A smooth and creamy dessert topped with rich caramel sauce, offering a soft texture and sweet flavor.",
        "ingredients": ["Milk", "egg", "sugar", "caramel syrup"],
        "time": 2,
        "vegetarian": False,
        "category": "dessert"
    },

    "chocolate lava cake": {
        "price": 650,
        "description": "A soft chocolate cake with a gooey molten chocolate center, delivering a rich and indulgent experience.",
        "ingredients": ["Chocolate", "flour", "egg", "sugar"],
        "time": 5,
        "vegetarian": False,
        "category": "dessert"
    },  
}