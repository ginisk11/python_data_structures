def flip_case(phrase, to_swap):
    lst=[]
    for letter in phrase:
        if letter.lower()==to_swap:
            lst.append(letter.upper())
        else:
            lst.append(letter)

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
