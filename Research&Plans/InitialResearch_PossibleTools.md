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
- Make sure that the backend will communicate with front-end (flask?)
## Step 4: Build the user interface 
- HTML, JavaScript (front-end)

## Pro's and Cons:

| **Aspect**                    | **Pros**                                                                 | **Cons**                                                               |
|--------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Web Scraping with BeautifulSoup** | - Easy to use and well-documented<br>             | - Issues with dynamic content<br>- Legal concerns<br>
| **Building the Database**      | - Organizes scraped data for fast access<br>- Customizable (SQL/NoSQL)    | - Requires careful data structuring<br>- Choosing between SQL/NoSQL can be tricky |
| **NLP for Data Cleaning** | - Reduces development time by using pre-trained models<br>- Standardizes data effectively<br>- Handles misspellings and variations automatically | - Pre-trained models may not perfectly fit your data<br>- Dependency on third-party APIs or libraries |
| **Query Handling with NLP**    | - Can improve user experience<br>- Corrects spelling/grammar mistakes<br>- Provides flexible input handling | - ML model complexity may slow down real-time response<br>- Difficult to handle out-of-scope queries without a fallback<br> May have to hold a subscription for use of model, costs would depend on usage |
| **Search Functionality**       | - Can use vector similarity for better results<br>- Matches queries even when phrased differently | - Needs optimization for performance<br>- Can return irrelevant results without good embeddings or filters |
| **General Solution**           | - Scalable<br>- Customizable<br>- Improves over time                      | - May need continuous maintenance<br>- Requires initial setup effort   |

---

**Eric Simoni**

**This description will cover Microsoft Bot Framework and Azure Bot Services for building a chatbot.**

## Step 1: Leverage Microsoft Bot Framework's extensive documentation and sample bots
- [Microsoft BotBuilder Samples](https://github.com/Microsoft/BotBuilder-Samples/blob/main/README.md)
- [Azure Bot Service SDK Guide](https://learn.microsoft.com/en-us/azure/bot-service/index-bf-sdk?view=azure-bot-service-4.0)
- The Microsoft Bot Framework provides a variety of well-documented resources, including free downloadable sample bots, to accelerate bot development.

## Step 2: Multi-language support and simple implementation
- The framework supports multiple programming languages, such as C# and Python, making it easy to implement bots with developers' preferred languages.
- It integrates well with existing platforms and has multi-channel support for deploying bots across various channels like web, mobile, or messaging apps.

## Step 3: Microsoft Azure for hosting and scaling
- Azure Bot Services is tightly integrated with the Bot Framework and handles overhead like scaling, security, and hosting, removing the burden of self-hosting or relying on third-party services.
- Azure provides a 30-day free trial, which could allow for testing and exploration of its capabilities without immediate costs.

## Step 4: Build the chatbot and deploy
- Build the bot using the resources provided, ensuring integration with Azure for deployment. Microsoft also offers support during the setup process.
- For non-Azure hosting, other options would need to be explored, which could add complexity.

## Pro's and Cons:

| **Aspect**                    | **Pros**                                                                 | **Cons**                                                               |
|--------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Microsoft Bot Framework**    | - Well-documented resources<br>- Multiple sample bots available<br>- Supports multiple languages (C#, Python)<br>- Simple to implement<br>- Multi-channel support | - Dependency on Azure for full features<br>- Hosting on non-Azure solutions adds complexity |
| **Azure Bot Services**         | - Scalability handled by Azure<br>- Built-in support for bot development<br>- Continuous updates from Microsoft | - Azure incurs costs after trial<br>- Pricing model may be unclear<br>- Potential dependency on Microsoft infrastructure |
| **Support and Updates**        | - Microsoft provides official support<br>- Regular updates ensure platform reliability and new features | - Frequent updates may require adjustments<br>- Compatibility with custom/school security systems can be uncertain |
| **General Solution**           | - Scalable<br>- Flexible deployment options across platforms<br>- Easy setup with Azure | - Long-term dependency on Microsoft<br>- Costs and offical infrastructure support tied to Azure unless alternatives are explored |

---

**Antony Fuentes**

**This description will cover Dialogflow and how it can be used to build a chatbot.**

## Step 1: Using Dialogflow's rich features and prebuilt agents
- [Dialogflow Documentation]( https://cloud.google.com/dialogflow/docs)
- [Dialogflow Prebuilt Agents](https://cloud.google.com/dialogflow/es/docs/prebuilt-agents)
- Dialogflow provides a user-friendly interface, comprehensive documentation, and prebuilt agents that allow for quick start-up and learning. It supports both text-based and voice-based bots.

## Step 2: Multi-language support and pwerful NLP
- Dialogflow uses Google's Natural Language Processing (NLP) capabilities to understand and handle user input in multiple languages, making it powerful for international or multi-lingual projects.
- It also integrates easily with a wide range of programming languages, such as Python, Node.js, and Java, simplifying the development process.

## Step 3: Google Cloud for hosting and scaling
- Dialogflow integrates smoothly with Google Cloud, offering automatic scalability, load balancing, and security. Developers don’t need to worry about managing infrastructure manually
- Google offers a free tier with limitations, but scaling can increase costs based on usage.

## Step 4: Build the chatbot
- Using Dialogflow’s console, developers can design and train the chatbot to respond to various intents and queries.
- The bot can be deployed across multiple channels like websites, mobile apps, and messaging platforms (e.g., Facebook Messenger, Slack).
- Dialogflow provides SDKs and APIs for further customization and integration.

## Pro's and Cons:

| **Aspect**                    | **Pros**                                                                 | **Cons**                                                               |
|--------------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------|
| **Dialogflow Framework**    | - Intuitive and easy-to-use interface<br>- Prebuilt agents and templates available<br>-  Powerful NLP capabilities with Google's AI<br>- Supports multiple languages<br>- Flexible integration with third-party platforms | - Advanced features have a learning curve<br>- Customization requires familiarity with Google Cloud |
| **Google Cloud Hosting**         | -  Scales automatically<br>-  Free tier available with limitations<br>- Google Cloud ensures security and load balancing<br>- Access to Google’s AI and machine learning features | -  Costs increase as usage scales<br>- Requires understanding of Google Cloud services |
| **Support and Updates**        | - Backed by Google with regular updates<br>-  Strong developer community and comprehensive documentation | - Frequent updates may require adjustments<br>-  Limited support if not using Google Cloud for hosting |
| **General Solution**           | - Scalable and flexible<br>-  Strong NLP and AI integrations<br>-  Easily deployable across multiple platforms (web, mobile, messaging apps) | - Full functionality relies on Google Cloud<br>- Long-term dependency on Google's infrastructure |


