import time
from gen_random_values import gen_date, convert_date, gen_digits
from selenium import webdriver


page = webdriver.Firefox()
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/books/')

search = page.find_element_by_class_name('btn-primary')
search.click()
time.sleep(2)

fields = [
    # ['id_title', gen_book()['title']],
    # ['id_author', gen_book()['author']],
    ['id_title', 'Title'],
    ['id_author', 'author'],
    ['id_publication_date', convert_date(gen_date())],
    ['id_pages', gen_digits(4)],
    ['id_price', '3.14'],
]

for field in fields:
    search = page.find_element_by_id(field[0])
    search.send_keys(field[1])
    time.sleep(0.5)


# button = page.find_element_by_id('id_submit')
# button = page.find_element_by_class_name('btn-primary')
# button.click()

# page.quit()
