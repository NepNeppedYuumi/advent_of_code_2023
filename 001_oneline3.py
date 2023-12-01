print(sum(map(lambda x: int(x[0] + x[-1]),map(lambda line:
               ''.join(next((line[i] if line[i].isnumeric() else str(y)
                             for y, word in enumerate(
                   ('one', 'two', 'three', 'four', 'five', 'six', 'seven',
                    'eight',
                    'nine'), start=1)
                             if line[i].isnumeric() or
                             line[i:i + len(word)] == word), '')
                       for i in range(len(line))
                       )
               , map(str.strip, open('001.txt', 'r'))))))


print(sum(map(lambda x:int(x[0]+x[-1]),map(lambda line:''.join(next((line[i]if line[i].isnumeric()else str(y)for y,word in enumerate(('one','two','three','four','five','six','seven','eight','nine'),start=1)if line[i].isnumeric()or line[i:i+len(word)]==word),'')for i in range(len(line))),map(str.strip,open('001.txt','r'))))))

