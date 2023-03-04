def gum_gum_for_jay_jay():
    result = 0
    while (1):
        try:
            list = input()
            if list == 'gum gum for jay jay':
                result += 1
        except EOFError:
            break
    return result

if __name__ == "__main__":
    print(gum_gum_for_jay_jay())
