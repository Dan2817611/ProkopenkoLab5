import re
def ukrainian_alphabet(word):
    ukrainian_alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    return [ukrainian_alphabet.index(letter.lower()) for letter in word]

def process_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

            first_sentence = re.match(r'^.*?[.!?]', text, re.DOTALL).group(0)

            print(f"Перше речення: {first_sentence}")

            words = re.findall(r'\w+', text, re.UNICODE)

            ukrainian_words = [word for word in words if re.match(r'^[А-ЯІЇЄҐа-яіїєґ]+$', word, re.UNICODE)]
            english_words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]

            ukrainian_words_sorted = sorted(ukrainian_words, key=ukrainian_alphabet)
            english_words_sorted = sorted(english_words)

            if ukrainian_words_sorted:
                print("\nУкраїнські слова:")
                print(", ".join(ukrainian_words_sorted))
            else:
                print("\nУкраїнських слів не знайдено")

            if english_words_sorted:
                print(" ".join(english_words_sorted))
            else:
                print("\nАнглійських слів не знайдено")

            print(f"\nЗагальна кількість слів: {len(words)}")

    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
process_text('AlpText.txt')



