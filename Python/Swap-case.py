def swap_case(s):
    out = ''
    for ind, let in enumerate(s):
        if let.isalpha():
            if let.islower():
                out += s[ind].capitalize()
            else:
                out += s[ind].lower()
        else:
            out += let
    return out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)