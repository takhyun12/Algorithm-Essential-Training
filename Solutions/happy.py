def solution(message: str) -> str:
    happy_count: int = message.count(':-)')
    sad_count: int = message.count(':-(')

    if happy_count == 0 and sad_count == 0:
        return "none"
    elif happy_count > sad_count:
        return "happy"
    elif happy_count < sad_count:
        return "sad"
    elif happy_count == sad_count:
        return "unsure"


if __name__ == '__main__':
    message_list = ["How are you :-) doing :-( today :-)?", ":)", "This:-(is str:-(:-(ange te:-)xt."]
    for message in message_list:
        print(solution(message))
