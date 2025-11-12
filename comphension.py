def main():
    try:

        words = get_words("added.txt")
        lowercase_words = [words.lower for word in words]
        counts = {word: lowercase_words.count(word)for word in lowercase_words}
        save_counts(counts)
    except NameError:
        print("here some error")

main()