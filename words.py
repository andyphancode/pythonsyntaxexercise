def print_upper_words(wordlist, must_start_with):
    """For words that start with any letter in your caselist in wordlist, 
    print it out in uppercase."""

    for word in wordlist:
        for letter in must_start_with:
            if str(word).startswith(letter):
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})