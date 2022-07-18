def generate_hashtag(s):
    lst = [elem.capitalize() for elem in s.split()]
    new_s = '#'+''.join(lst)
    return new_s if 1<len(new_s)<140 else False



print(generate_hashtag(' '))      #'#Codewars'
print(generate_hashtag('Codewars      is'))      #'#Codewars'
print(generate_hashtag('Codewars Is Nice'))    #'#CodewarsIsNice'
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))