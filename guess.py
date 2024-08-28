import tkinter as tk
from tkinter import messagebox
import random

class AnimalGuessGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Animal Guessing Game")
        self.geometry("400x300")

        # Dictionary of animals and their hints
        self.animals = {
            "Elephant": "I am the largest land animal with big ears and a long trunk.",
            "Giraffe": "I have a very long neck and legs and am the tallest land animal.",
            "Tiger": "I am a big cat with stripes, living in the jungle, known for my roar.",
            "Kangaroo": "I hop and carry my baby in a pouch, living in Australia.",
            "Penguin": "I am a flightless bird, great at swimming, living in cold regions.",
            "Lion": "I am known as the king of the jungle with a mane and live in prides.",
            "Zebra": "I have black and white stripes and resemble a horse, living in Africa.",
            "Panda": "I am a bear with black and white fur, fond of eating bamboo.",
            "Polar Bear": "I am a white bear from the Arctic and an excellent swimmer.",
            "Rhino": "I have a thick skin and horns on my nose, and am a large herbivore.",
            "Gorilla": "I am a strong ape living in African forests.",
            "Hippopotamus": "I am a large semi-aquatic animal, spending much time in the water.",
            "Koala": "I am a marsupial from Australia, sleeping in trees and eating eucalyptus.",
            "Sloth": "I am a slow-moving mammal, hanging upside down in trees.",
            "Cheetah": "I am the fastest land animal, known for my speed and spots.",
            "Ostrich": "I am the largest bird and cannot fly but can run very fast.",
            "Hawk": "I am a bird of prey with keen vision and hunting skills.",
            "Dolphin": "I am an intelligent marine mammal, known for my playful behavior.",
            "Whale": "I am the largest animal on Earth and live in the ocean.",
            "Seal": "I am a marine mammal, spending time on both land and in the water.",
            "Walrus": "I am a large marine mammal with tusks and whiskers, lounging on ice floes.",
            "Jaguar": "I am a powerful cat from the Americas, known for my rosettes.",
            "Leopard": "I am a big cat with a spotted coat and am skilled at climbing.",
            "Puma": "Also known as a mountain lion, I am a large cat from the Americas.",
            "Crocodile": "I am a large reptile with a powerful bite, living in rivers and swamps.",
            "Alligator": "I am similar to a crocodile, found in the southeastern U.S. and China.",
            "Komodo Dragon": "I am the largest lizard in the world, native to Indonesia.",
            "Iguana": "I am a large lizard from tropical areas, known for my spiny crest.",
            "Chameleon": "I am a lizard known for changing colors to blend into my surroundings.",
            "Tarantula": "I am a large spider, intimidating in appearance but generally harmless.",
            "Scorpion": "I am an arachnid with a venomous sting and pincers.",
            "Butterfly": "I am an insect with colorful wings and a life cycle from caterpillar.",
            "Moth": "I am similar to a butterfly but often nocturnal and attracted to light.",
            "Beetle": "I am an insect with a hard shell, one of the largest insect groups.",
            "Ant": "I am a small insect living in colonies and working together.",
            "Honeybee": "I produce honey and pollinate plants.",
            "Ladybug": "I am a beetle with red or orange wings and black spots.",
            "Wasp": "I am known for my sting and aggressive summer behavior.",
            "Dragonfly": "I am an insect with large eyes, capable of quick, hovering flight.",
            "Grasshopper": "I am known for jumping and making a chirping sound.",
            "Cockroach": "I am a resilient insect, adaptable to various environments.",
            "Termite": "I am known for consuming wood and living in colonies.",
            "Frog": "I am an amphibian with jumping ability and a croaking sound.",
            "Toad": "I am similar to a frog but with drier, bumpier skin.",
            "Newt": "I am an amphibian similar to a salamander, living both in water and on land.",
            "Salamander": "I am an amphibian with a lizard-like appearance, capable of tail regeneration.",
            "Snake": "I am a legless reptile known for slithering and, in some species, a venomous bite.",
            "Lizard": "I am a reptile with four legs and a long tail, found in various environments.",
            "Gecko": "I am a lizard known for climbing walls and making chirping sounds.",
            "Chinchilla": "I am a small rodent with soft fur from the Andes mountains.",
            "Guinea Pig": "I am a small, friendly rodent known for squeaky sounds.",
            "Hamster": "I am a small rodent with cheek pouches, often kept as a pet.",
            "Rat": "I am an adaptable, intelligent rodent, often found in urban areas.",
            "Mouse": "I am a small, quick-moving rodent.",
            "Squirrel": "I am a rodent with a bushy tail, known for storing nuts for winter.",
            "Capybara": "I am the largest rodent, native to South America, often found near water.",
            "Beaver": "I am a large rodent known for building dams from wood.",
            "Porcupine": "I am a rodent with sharp quills used for defense.",
            "Hedgehog": "I am a small mammal with a spiky coat and nocturnal habits.",
            "Armadillo": "I am a mammal with a hard shell, native to the Americas.",
            "Ocelot": "I am a small wild cat with a spotted coat.",
            "Serval": "I am a wild cat with long legs and large ears, from Africa.",
            "Bengal Tiger": "I am a tiger subspecies from India with orange and black stripes.",
            "Snow Leopard": "I am a big cat adapted to cold regions, known for my spotted fur.",
            "Jaguarundi": "I am a sleek wild cat from Central and South America with a uniform coat.",
            "Cougar": "Also known as the mountain lion, I am a large cat from the Americas.",
            "Lynx": "I am a medium-sized wild cat with tufted ears and a short tail, found in northern regions.",
            "Siamese Cat": "I am a domestic cat breed with a slender body, blue eyes, and color points.",
            "Maine Coon": "I am a large domestic cat breed known for my friendly nature and tufted ears.",
            "Persian Cat": "I am a domestic cat breed with a luxurious coat and a flat face.",
            "Ragdoll Cat": "I am a domestic cat breed known for my docile temperament and tendency to go limp when picked up.",
            "Sphynx Cat": "I am a domestic cat breed with no fur and distinctive wrinkled skin.",
            "Scottish Fold": "I am a domestic cat breed with folded ears and a sweet disposition.",
            "Abyssinian": "I am a domestic cat breed with a short, ticked coat and an active personality.",
            "British Shorthair": "I am a domestic cat breed with a round face and dense coat, known for being calm.",
            "Norwegian Forest Cat": "I am a domestic cat breed with long fur and a bushy tail, adapted to cold climates.",
            "Turkish Angora": "I am a domestic cat breed with a long, silky coat and playful personality.",
            "Burmese": "I am a domestic cat breed with a sleek body and affectionate nature.",
            "Siberian": "I am a domestic cat breed with a dense coat and friendly demeanor.",
            "Russian Blue": "I am a domestic cat breed with a short, blue-gray coat and striking green eyes.",
        }

        self.setup_ui()

    def setup_ui(self):
        # Welcome label
        tk.Label(self, text="Welcome to the Animal Guessing Game!").pack(pady=10)

        # Name entry
        tk.Label(self, text="What's your name?").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        # Start button
        tk.Button(self, text="Start Game", command=self.start_game).pack(pady=10)

        # Hint label
        self.hint_label = tk.Label(self, text="", wraplength=350)
        self.hint_label.pack(pady=10)

        # Guess entry
        self.guess_entry = tk.Entry(self, state=tk.DISABLED)
        self.guess_entry.pack(pady=5)

        # Submit guess button
        self.guess_button = tk.Button(self, text="Submit Guess", command=self.submit_guess, state=tk.DISABLED)
        self.guess_button.pack(pady=10)

        # Attempts left label
        self.attempts_label = tk.Label(self, text="")
        self.attempts_label.pack(pady=10)

    def start_game(self):
        # Get player's name and start the game
        self.name = self.name_entry.get().strip()
        if not self.name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        
        self.attempts = 5
        self.animal, self.hint = random.choice(list(self.animals.items()))
        self.hint_label.config(text=f"Hint: {self.hint}")
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

    def submit_guess(self):
        # Check the player's guess
        guess = self.guess_entry.get().strip()
        if guess.lower() == self.animal.lower():
            messagebox.showinfo("Congratulations!", f"Well done, {self.name}! You guessed the animal correctly.")
            self.reset_game()
        else:
            self.attempts -= 1
            if self.attempts > 0:
                self.attempts_label.config(text=f"Incorrect. Attempts left: {self.attempts}")
            else:
                messagebox.showinfo("Game Over", f"Sorry, you're out of attempts. The correct answer was: {self.animal}")
                self.reset_game()

    def reset_game(self):
        # Reset the game for a new round
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)
        self.start_game()

if __name__ == "__main__":
    app = AnimalGuessGame()
    app.mainloop()
