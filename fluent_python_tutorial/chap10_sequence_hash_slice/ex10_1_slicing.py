class MySeq:
    def __getitem__(self, index):
        return index


if __name__=="__main__":
    s = MySeq()
    print(s[1], s[1:4], s[1:4:2], s[1:4:2, 9], s[1:4:2, 7:9], sep='\n')
    print()
    print(slice)
    print(dir(slice))