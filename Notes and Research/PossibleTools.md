**Kennedy Martin**
**This description will cover solving this problem with web scraping, building a database, and then using a ml model in the background to do the language
processing for both cleaning the database information initially as well as cleaning the queries.**

## Step 1: Web Scraping the appropriate pages using beautiful soup
- https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
- Beautiful soup is well documented and allows us to put information into a parse tree so that we can then extract whatever information we are looking for.
## Step 2: Build a database/Fill database
- This database will hold the cleaned information from the site (that we acquired from web scraping) and the corresponding answers
    - Need to decide what kind of database to use, potentially a relational database as a lot of the information will be courses, course prerequisites, etc.
- When a query is sent, it will be cleaned in the background by an NLP and then matched to an "input" option in our database, then the corresponding the output/result will be sent out.
## Step 3:  
- Build program that will accept user input, send to NLP for cleaning, search the database for the best match, and then issue a response.

## Pro's and Cons:

| **Aspect**                    | **Pros**                                                                 | **Cons**                                                               |
|--------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Web Scraping with BeautifulSoup** | - Easy to use and well-documented<br>             | - Issues with dynamic content<br>- Legal concerns (check `robots.txt`)<br>
| **Building the Database**      | - Organizes scraped data for fast access<br>- Customizable (SQL/NoSQL)    | - Requires careful data structuring<br>- Choosing between SQL/NoSQL can be tricky |
| **NLP for Data Cleaning** | - Reduces development time by using pre-trained models<br>- Standardizes data effectively<br>- Handles misspellings and variations automatically | - Pre-trained models may not perfectly fit your data<br>- Dependency on third-party APIs or libraries |
| **Query Handling with NLP**    | - Can improve user experience<br>- Corrects spelling/grammar mistakes<br>- Provides flexible input handling | - ML model complexity may slow down real-time response<br>- Difficult to handle out-of-scope queries without a fallback |
| **Search Functionality**       | - Can use vector similarity for better results<br>- Matches queries even when phrased differently | - Needs optimization for performance<br>- Can return irrelevant results without good embeddings or filters |
| **General Solution**           | - Scalable<br>- Customizable<br>- Improves over time                      | - May need continuous maintenance<br>- Requires initial setup effort   |
















