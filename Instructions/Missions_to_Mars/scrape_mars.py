from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import codecs

def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('div', class_='col-md-8')

    # # Iterate through each book
    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        news_date=article.find('div', class_="list_date").text
        news_title = article.find('div', class_="content_title").text
        news_p = article.find('div', class_="article_teaser_body").text
        break

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    images = soup.find_all('a', class_='fancybox-thumbs')

    # # Iterate through each book
    for image in images:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        featured_image_url=f"https://spaceimages-mars.com/{image['href']}"

        print(featured_image_url)

        break

    url = 'https://galaxyfacts-mars.com/'

    tables=pd.read_html(url)
    mars_fact_df=tables[0]

    column_name=[mars_fact_df.iloc[0][x] for x in range(len(mars_fact_df.iloc[0]))]
    mars_fact_df.columns=column_name
    mars_fact_df=mars_fact_df.iloc[1:,:]
    mars_fact_df.to_html('templates/mars_fact_table.html', index=False, classes="table table-striped")
    file = codecs.open("templates/mars_fact_table.html", "r", "utf-8")
    mars_fact_table=file.read()

    # %% [markdown]
    # <strong>Mars Hemispheres</strong>
    # - Visit the Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
    # - You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # - Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # - Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

    # %%
    url = 'https://marshemispheres.com/'
    browser.visit(url)


    # %%
    url_list=[]
    hemisphere_title_list=[]

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    hemisphere_articles = soup.find_all('div', class_='description')

    # Iterate through each book
    for hemisphere_article in hemisphere_articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        url_string = hemisphere_article.a['href']
        url_list.append(f"https://marshemispheres.com/{url_string}")
        title_string= hemisphere_article.a.h3.text
        hemisphere_title_list.append(title_string)
        print('-----------')
        print(title_string)
        print('https://marshemispheres.com/' + url_string)



    # %%
    hemisphere_image_list=[]

    for urls in url_list:
        url=urls
        browser.visit(url)
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain book information
        hemisphere_images = soup.find_all('ul')
        hemisphere_image_list.append(f"https://marshemispheres.com/{hemisphere_images[0].find('a')['href']}")


    # %%
    hemisphere_image_urls = [
        {"title": hemisphere_title_list[0], "img_url": hemisphere_image_list[0]},
        {"title": hemisphere_title_list[1], "img_url": hemisphere_image_list[1]},
        {"title": hemisphere_title_list[2], "img_url": hemisphere_image_list[2]},
        {"title": hemisphere_title_list[3], "img_url": hemisphere_image_list[3]},
    ]


    # %%
    browser.quit()

    mars_data= {
        "news_title":news_title,
        "news_p":news_p,
        "featured_image_url":featured_image_url,
        "mars_fact":mars_fact_table,
        "hemisphere_image_urls":hemisphere_image_urls
    }

    return mars_data


