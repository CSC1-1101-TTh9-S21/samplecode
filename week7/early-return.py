def gete(s1):
    news = ""
    for c in s1:
        news = news + c
        if c == "e":
            return news
    return news

def main():
    print(gete("ineffective"))
    print(gete("ipad"))

main()
