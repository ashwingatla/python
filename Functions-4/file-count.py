# A function to read a file and count the frequency of each word
## Read the file file.txt and print the number of times a word repeats

def count_frequency(file_name):
    ## Read the file
    word_count={}
    with open (file_name,"r") as file:
        for line in file:
            words=line.split()
            for word in words:
                word_count[word] = word_count.get(word,0)+1
    return word_count

file_name = 'file.txt'
word_count_list = count_frequency(file_name)
print(word_count_list)