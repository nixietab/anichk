import os
import hashlib

ANIMAL_LIST = [
    "Aardvark", "Agouti", "Albatross", "Alpaca", "Anaconda", "Andean Condor", "Andean Mountain Cat", "Angelfish", "Ant", "Anteater", "Antelope", "Ape", "Armadillo", "Donkey", "Baboon", "Badger", "Barracuda", "Bass", "Bat", "Bear", "Beaver", "Bee", "Beluga Sturgeon", "Bird", "Bison", "Black Drum", "Black Marlin", "Black Sea Turbot", "Blackbird", "Bluefish", "Boar", "Bobcat", "Bonefish", "Bowfin", "Buffalo", "Bullhead", "Butterfly", "Caiman", "Camel", "Canary", "Capybara", "Caracara", "Carp", "Cat", "Caterpillar", "Catfish", "Cattle", "Chinchilla", "Chimpanzee", "Chipmunk", "Cobia", "Cobra", "Cockroach", "Cod", "Condor", "Conger Eel", "Cougar", "Cow", "Coyote", "Crab", "Crane", "Croaker", "Crocodile", "Crow", "Cusk", "Dab", "Deer", "Dinosaur", "Dog", "Dolphin", "Donkey", "Dove", "Dragonfish", "Duck", "Eagle", "Eel", "Elephant", "Elk", "Emu", "Anchovy", "Falcon", "Filefish", "Finch", "Fish", "Flounder", "Fly", "Flying Fish", "Fox", "Frog", "Galapagos Giant Tortoise", "Galapagos Penguin", "Gar", "Gazelle", "Gerbil", "Giant Grouper", "Giant Otter", "Gilt-head Bream", "Giraffe", "Goat", "Goblin Shark", "Golden Lion Tamarin", "Goldfish", "Goose", "Gorilla", "Grasshopper", "Guanaco", "Guppy", "Guinea pig", "Haddock", "Hagfish", "Hamster", "Hare", "Hawk", "Hedgehog", "Heron", "Herring", "Hippocampus", "Hippopotamus", "Horse", "Houndshark", "Hummingbird", "Hyena", "Iguana", "Insect", "Jack Mackerel", "Jackfish", "Jaguar", "Jellyfish", "John Dory", "Kangaroo", "Kelp Perch", "Kinkajou", "Koala", "Koi", "Komodo dragon", "Kookaburra", "Lama", "Lamprey", "Leafcutter Ant", "Lemur", "Leopard", "Lion", "Lizard", "Llama", "Lobster", "Locust", "Loris", "Louse", "Lungfish", "Lyrebird", "Macaw", "Mackerel", "Magpie", "Mammal", "Manatee", "Mantis", "Marmot", "Meerkat", "Mink", "Mole", "Monkfish", "Monkey", "Moose", "Moray Eel", "Mosquito", "Mouse", "Mule", "Mullet", "Newt", "Nightingale", "Ocelot", "Octopus", "Opossum", "Ostrich", "Otter", "Owl", "Ox", "Oyster", "Paca", "Panda", "Parrot", "Partridge", "Peacock", "Pelican", "Penguin", "Perch", "Pickerel", "Pig", "Pike", "Piranha", "Plaice", "Pigeon", "Pony", "Porcupine", "Porpoise", "Prairie dog", "Pufferfish", "Puma", "Quail", "Queen Angelfish", "Quetzal", "Rabbit", "Raccoon", "Rat", "Raven", "Ray", "Red Snapper", "Reindeer", "Reptile", "Rhea", "Rhinoceros", "Ribbonfish", "Robin", "Rodent", "Rooster", "Sablefish", "Sailfish", "Salamander", "Salmon", "Sardine", "Scallop", "Scorpion", "Seahorse", "Seal", "Sea Robin", "Sea Trout", "Shark", "Sheep", "Shrimp", "Skate", "Skunk", "Sloth", "Snail", "Snake", "Snapper", "Sole", "Spectacled Bear", "Spider", "Spotted Catfish", "Squirrel", "Starfish", "Stingray", "Stork", "Sturgeon", "Sucker", "Sunfish", "Swallow", "Swan", "Swordfish", "Tapir", "Tarantula", "Tarpon", "Tench", "Termite", "Thornback Ray", "Tiger", "Tilefish", "Toad", "Tomcod", "Toucan", "Trout", "Tuna", "Turbot", "Turkey", "Turtle", "Vampire Bat", "Vicuna", "Viperfish", "Vulture", "Wallaby", "Walleye", "Walrus", "Wasp", "Weasel", "Whale", "Whitefish", "Wolf", "Wolverine", "Woodpecker", "Worm", "Wrasse", "Yak", "Yellow Perch", "Yellowfin Tuna", "Zebra"
]

ADJECTIVE_LIST = [
    "Aggressive", "Agile", "Agitated", "Alert", "Alien", "Alive", "Alluring", "Alone", "Aloof", "Amazing", "Ambitious", "Ample", "Amused", "Ancient", "Angry", "Anguished", "Animated", "Annual", "Another", "Antique", "Anxious", "Appealing", "Appetizing", "Applicable", "Appropriate", "Arbitrary", "Archaic", "Architectural", "Arctic", "Ardent", "Arid", "Aristocratic", "Aromatic", "Artistic", "Ashamed", "Astonishing", "Athletic", "Atomic", "Attentive", "Attractive", "Audacious", "Auspicious", "Authentic", "Automatic", "Available", "Average", "Awake", "Aware", "Awful", "Azure", "Babyish", "Back", "Bad", "Balanced", "Balmy", "Barbaric", "Bare", "Barren", "Basic", "Beautiful", "Believable", "Belligerent", "Beneficial", "Benevolent", "Best", "Better", "Bewildered", "Big", "Biological", "Bizarre", "Black", "Bleak", "Blessed", "Blind", "Blissful", "Bloody", "Blue", "Blunt", "Blurred", "Boastful", "Bold", "Bombastic", "Bored", "Boring", "Bottom", "Boundless", "Bountiful", "Brave", "Breakable", "Brief", "Bright", "Brilliant", "Brisk", "Broken", "Brutal", "Bubbly", "Bulky", "Burning", "Businesslike", "Busy", "Calm", "Camouflaged", "Capable", "Capricious", "Captivating", "Careful", "Careless", "Caring", "Casual", "Cautious", "Celestial", "Central", "Certain", "Challenging", "Chaotic", "Charming", "Cheap", "Cheerful", "Chemical", "Chief", "Childish", "Chilly", "Chronic", "Circular", "Civil", "Classic", "Clean", "Clear", "Clever", "Clinical", "Cloudy", "Clumsy", "Coarse", "Cold", "Collective", "Colossal", "Colorful", "Comfortable", "Common", "Compact", "Comparable", "Compassionate", "Competent", "Competitive", "Complex", "Compliant", "Complicated", "Comprehensive", "Compulsory", "Conceited", "Concerned", "Concrete", "Condensed", "Confident", "Confidential", "Confused", "Congested", "Conscious", "Conservative", "Considerable", "Consistent", "Constant", "Constructive", "Contemporary", "Content", "Continuous", "Contradictory", "Contrary", "Controversial", "Convenient", "Conventional", "Convincing", "Cool", "Cooperative", "Coordinated", "Cordial", "Corporate", "Correct", "Corrupt", "Costly", "Courageous", "Courteous", "Covered", "Cowardly", "Cozy", "Cracked", "Crafty", "Crazy", "Creative", "Credible", "Creepy", "Criminal", "Critical", "Crooked", "Crowded", "Crucial", "Crude", "Cruel", "Crumbling", "Cryptic", "Cultural", "Cunning", "Curious", "Curly", "Current", "Curved", "Cute", "Daily", "Damp", "Dangerous", "Daring", "Dark", "Dashing", "Dazzling", "Dead", "Deadly", "Deafening", "Dear", "Decayed", "Deceitful", "Decent", "Decisive", "Decorative", "Deep", "Defeated", "Defensive", "Defiant", "Delicate", "Delicious", "Delightful", "Delirious", "Demanding", "Democratic", "Dense", "Dependent", "Depressed", "Descriptive", "Deserted", "Desirable", "Desolate", "Desperate", "Detailed", "Determined", "Devastating", "Devoted", "Different", "Difficult", "Digital", "Diligent", "Dim", "Diminutive", "Direct", "Dirty", "Disabled", "Disastrous", "Discreet", "Disgusting", "Distant", "Distinct", "Distinguished", "Disturbed", "Dizzy", "Domestic", "Dominant", "Doubtful", "Down", "Drab", "Dramatic", "Drastic", "Dreadful", "Dreamy", "Dry", "Dual", "Dull", "Durable", "Dynamic", "Eager", "Early", "Earthly", "Easy", "Eccentric", "Ecological", "Economic", "Educated", "Educational", "Effective", "Efficient", "Effortless", "Elastic", "Elderly", "Electric", "Electrical", "Electronic", "Elegant", "Elementary", "Eligible", "Elite", "Embarrassed", "Emergency", "Emotional", "Empty", "Enchanting", "Encouraging", "Endangered", "Endless", "Energetic", "Enormous", "Enough", "Entertaining", "Enthusiastic", "Entire", "Environmental", "Envious", "Equal", "Equatorial", "Essential", "Established", "Eternal", "Ethical", "Ethnic", "Even", "Eventual", "Every", "Evil", "Exact", "Excellent", "Exceptional", "Excessive", "Excited", "Exclusive", "Exotic", "Expensive", "Experienced", "Experimental", "Expert", "Explicit", "Explosive", "Extensive", "External", "Extra", "Extraordinary", "Extravagant", "Extreme", "Fabulous", "Faint", "Fair", "Faithful", "Fake", "Fallen", "False", "Familiar", "Famous", "Fancy", "Fantastic", "Far", "Fascinating", "Fast", "Fat", "Fatal", "Favorable", "Favorite", "Fearful", "Fearless", "Feeble", "Female", "Feminine", "Ferocious", "Fertile", "Feverish", "Few", "Fierce", "Filthy", "Final", "Fine", "Finicky", "Firm", "First", "Fit", "Fixed", "Flaming", "Flashy", "Flat", "Flexible", "Flighty", "Floating", "Floral", "Flowing", "Fluent", "Fluffy", "Flying", "Focused", "Fond", "Foolish", "Forced", "Foreign", "Formal", "Former", "Formidable", "Fortunate", "Forward", "Foul", "Fragile", "Fragrant", "Frank", "Frantic", "Free", "Frequent", "Fresh", "Friendly", "Frightened", "Frightening", "Frigid", "Front", "Frozen", "Fruitful", "Frustrating", "Full", "Fun", "Functional", "Fundamental", "Funny", "Furious", "Future", "Fuzzy", "Galactic", "Gallant", "Game", "Generous", "Gentle", "Genuine", "Geographic", "Giant", "Gifted", "Gigantic", "Glamorous", "Glaring", "Glassy", "Gleaming", "Gleeful", "Glorious", "Glowing", "Golden", "Good", "Gorgeous", "Graceful", "Grand", "Grandiose", "Graphic", "Grateful", "Grave", "Great", "Greedy", "Green", "Gregarious", "Grim", "Gritty", "Gross", "Grotesque", "Growing", "Grumpy", "Guilty", "Gullible", "Gummy", "Hairy", "Half", "Hallucinatory", "Handmade", "Handsome", "Handy", "Happy", "Hard", "Harmful", "Harmonious", "Harsh", "Hateful", "Haunting", "Healthy", "Heartbreaking", "Heartfelt", "Hearty", "Heavenly", "Heavy", "Hefty", "Helpful", "Helpless", "Heroic", "Hidden", "Hideous", "High", "Hilarious", "Historical", "Holistic", "Holy", "Homeless", "Homely", "Honest", "Honorable", "Horrible", "Horrific", "Hot", "Huge", "Human", "Humble", "Humorous", "Hungry", "Hurt", "Hushed", "Hydraulic", "Hypnotic", "Icy", "Ideal", "Identical", "Ideological", "Idiotic", "Idle", "Ignorant", "Ill", "Illegal", "Illegitimate", "Illogical", "Illustrious", "Imaginary", "Immaculate", "Immense", "Imminent", "Immortal", "Impartial", "Impatient", "Important", "Impossible", "Impractical", "Impressive", "Improbable", "Impure", "Inadequate", "Inappropriate", "Incredible", "Independent", "Indestructible", "Indian", "Indifferent", "Indirect", "Individual", "Industrial", "Industrious", "Inevitable", "Infamous", "Infinite", "Informal", "Inherent", "Initial", "Innocent", "Innovative", "Innumerable", "Inquisitive", "Insane", "Insecure", "Inside", "Insignificant", "Instant", "Instinctive", "Institutional", "Insufficient", "Intact", "Intellectual", "Intelligent", "Intense", "Interactive", "Interested", "Interesting", "Interior", "Intermediate", "Internal", "International", "Intimate", "Intricate", "Intrigued", "Intriguing", "Invalid", "Invisible", "Involved", "Irate", "Iron", "Ironic", "Irresponsible", "Irritable", "Irritating", "Isolated", "Jealous", "Jittery", "Joint", "Jolly", "Joyful", "Judicial", "Juicy", "Junior", "Just", "Juvenile", "Keen", "Key", "Kind", "Kindly", "King", "Kissable", "Knowing", "Known", "Lame", "Large", "Last", "Late", "Lateral", "Laughable", "Lavish", "Lawful", "Lazy", "Leading", "Leafy", "Lean", "Legal", "Legendary", "Legitimate", "Leisurely", "Lethal", "Level", "Liberal", "Light", "Likeable", "Likely", "Limited", "Limp", "Linear", "Linguistic", "Liquid", "Little", "Lively", "Living", "Local", "Logical", "Lonely", "Long", "Loose", "Lost", "Loud", "Lousy", "Lovely", "Low", "Loyal", "Lucky", "Lukewarm", "Luminous", "Lunar", "Lush", "Luxurious", "Lyric", "Mad", "Magenta", "Magic", "Magical", "Magnificent", "Main", "Majestic", "Major", "Male", "Malicious", "Mammoth", "Man-made", "Mandatory", "Manic", "Many", "Marginal", "Marine", "Marked", "Married", "Marvelous", "Masculine", "Massive", "Masterful", "Material", "Mathematical", "Mature", "Maximum", "Mean", "Meaningful", "Measurable", "Mechanical", "Medical", "Medieval", "Mediocre", "Medium", "Meek", "Melancholy", "Melodic", "Memorable", "Menacing", "Mental", "Merciful", "Mere", "Merry", "Messy", "Metallic", "Meticulous", "Mighty", "Mild", "Military", "Milky", "Mimicking", "Mindless", "Miniature", "Minimal", "Minor", "Minute", "Miraculous", "Mischievous", "Miserable", "Misguided", "Missing", "Mistaken", "Mixed", "Mobile", "Mocking", "Modern", "Modest", "Moist", "Molecular", "Momentary", "Momentous", "Monetary", "Monstrous", "Monthly", "Monumental", "Moral", "Mortified", "Motionless", "Mountainous", "Mournful", "Moving", "Much", "Muddy", "Multiple", "Mundane", "Municipal", "Murky", "Musical", "Mute", "Mutual"
]

def calculate_checksum(path):
    try:
        if os.path.isfile(path):
            hasher = hashlib.sha256()
            with open(path, 'rb') as file:
                while chunk := file.read(4096):
                    hasher.update(chunk)
            return hasher.hexdigest()
        elif os.path.isdir(path):
            hasher = hashlib.sha256()
            for filename in sorted(os.listdir(path)):
                filepath = os.path.join(path, filename)
                if os.path.isfile(filepath):
                    hasher.update(filename.encode('utf-8'))
                    with open(filepath, 'rb') as file:
                        while chunk := file.read(4096):
                            hasher.update(chunk)
            return hasher.hexdigest()
        else:
            raise ValueError(f"Path '{path}' is not a file or directory.")
    except (IOError, OSError) as e:
        raise RuntimeError(f"Error reading path '{path}': {e}")

def calculate_combined_checksum(paths):
    try:
        hasher = hashlib.sha256()
        for path in sorted(paths):  # Sort paths for consistent results
            if os.path.isfile(path):
                with open(path, 'rb') as file:
                    while chunk := file.read(4096):
                        hasher.update(chunk)
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for filename in sorted(files):  # Sort files for consistent results
                        filepath = os.path.join(root, filename)
                        if os.path.isfile(filepath):
                            hasher.update(filepath.encode('utf-8'))  # Include file paths
                            with open(filepath, 'rb') as file:
                                while chunk := file.read(4096):
                                    hasher.update(chunk)
            else:
                raise ValueError(f"Path '{path}' is not valid.")
        return hasher.hexdigest()
    except (IOError, OSError) as e:
        raise RuntimeError(f"Error processing paths: {e}")

def get_word_from_list(word_list, index):
    if 0 <= index < len(word_list):
        return word_list[index]
    raise IndexError(f"Index {index} is out of range for the word list.")

def count_lines(word_list):
    return len(word_list)

def get_animal_name(paths):
    """Generate an animal name based on a combined checksum of files or directories."""
    combined_checksum = calculate_combined_checksum(paths)
    if combined_checksum:
        checksum_int = int(combined_checksum, 16)
        
        animal_list_length = count_lines(ANIMAL_LIST)
        adjective_list_length = count_lines(ADJECTIVE_LIST)

        animal_index = checksum_int % animal_list_length
        adjective_index = (checksum_int // animal_list_length) % adjective_list_length

        animal = get_word_from_list(ANIMAL_LIST, animal_index)
        adjective = get_word_from_list(ADJECTIVE_LIST, adjective_index)

        return f"{adjective} {animal}"
    else:
        raise ValueError("Checksum calculation failed.")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate a phrase based on a combined checksum of files or directories.")
    parser.add_argument('paths', metavar='path', type=str, nargs='+', help="Paths to the files or directories")
    args = parser.parse_args()

    try:
        result = get_animal_name(args.paths)
        print(f"Generated Animal: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate a phrase based on a combined checksum of files or directories.")
    parser.add_argument('paths', metavar='path', type=str, nargs='+', help="Paths to the files or directories")
    args = parser.parse_args()

    try:
        result = get_animal_name(args.paths)
        print(f"Generated Animal: {result}")
    except Exception as e:
        print(f"Error: {e}")
