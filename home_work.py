import pickle

class AddressBook:


    def save_to_file(self, filename="addressbook.pkl"):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            print("AddressBook saved successfully!")
        except Exception as e:
            print(f"Error saving AddressBook: {e}")

    @classmethod
    def load_from_file(cls, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("AddressBook file not found. Creating a new one.")
            return cls()
        except Exception as e:
            print(f"Error loading AddressBook: {e}")
            return cls()

def main():

    address_book = AddressBook.load_from_file()

    address_book.save_to_file()

if __name__ == "__main__":
    main()