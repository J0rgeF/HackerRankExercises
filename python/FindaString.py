def count_substring(string, sub_string):
    cnt = 0
    for i in range(0, len(string)):
        if i + (len(sub_string) - 1) < len(string) and string[i] == sub_string[0]:
            for c in range(0, len(sub_string)):
                if string[i + c] != sub_string[c]:
                    break
                if c == len(sub_string) - 1:
                    cnt += 1  
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)