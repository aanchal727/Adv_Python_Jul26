def count_characters(text):
    char_count={}

# Convert the string to lowercase
    text=text.lower()
# Count only alphabetic characters
    for ch in text:
        if ch.isalpha():
            if ch in char_count:
                char_count[ch]+=1
            else:
                char_count[ch]=1
# Return dictionary in alphabetical order
    sorted_count = {}

    for key in sorted(char_count):
        sorted_count[key]=char_count[key]
    return sorted_count
# Example
text = "Hello World 123!!"
print(count_characters(text))