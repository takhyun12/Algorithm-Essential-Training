answer = 0
def dfs(begin: str, target: str, words: list, current_length: int) -> int:
    global answer

    for i in words:
        if target == begin:
            if answer > current_length or answer == 0:
                answer = current_length
            return current_length
        elif len(words) == 0:
            return 0

        if are_words_similar(begin, i):
            index = words.index(i)
            temp = words[:index] + words[index+1:]
            dfs(i, target, temp, current_length+1)

    return 0

def solution(begin: str, target: str, words: list) -> int:
    global answer

    if not target in words:
        return 0

    dfs(begin, target, words, 0)

    return answer

def are_words_similar(s: str, s2: str) -> bool:
    temp = 0

    for i in range(len(s)):
        if s[i] == s2[i]:
            temp += 1

    if temp + 1 == len(s):
        return True

    return False

if __name__ == '__main__':
    begin, target = "hit", "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    words2 = ["hot", "dot", "dog", "lot", "log"]
    words3 = ["hot", "dot", "hog"]

    print(solution(begin, target, words))
    #print(solution(begin, target, words2))
    #print(solution('got', 'hog', words3))
