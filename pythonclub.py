from selenium import webdriver
import json
import os 


dir_path = os.path.dirname(os.path.realpath(__file__))
# Criar instância do navegador
chrome = webdriver.Chrome(executable_path=dir_path + "\chromedriver.exe")

# Abrir a página do Python Club
chrome.get('http://pythonclub.com.br/')

# Seleciono todos os elementos que possuem a class post
posts = chrome.find_elements_by_class_name('post')

object_post = []

# Para cada post printar as informações
for post in posts:

    # O elemento `a` com a class `post-title`
    # contém todas as informações que queremos mostrar
    post_title = post.find_element_by_class_name('post-title')

    # `get_attribute` serve para extrair qualquer atributo do elemento
    post_link = post_title.get_attribute('href')

    post_author = post.find_element_by_class_name('avatar').get_attribute('alt')

    # printar informações
    print("Títutlo: {}, \nLink: {}\n Author: {}\n\n".format(post_title.text, post_link, post_author))
    object_post.append({'Title': post_title.text, 'Link': post_link, 'Author': post_author})

list_post = object_post
print(list_post)

with open('posts_python_club.json', 'w') as file_posts: 
    json.dump(list_post, file_posts, indent=2)

# Fechar navegador
chrome.quit()
