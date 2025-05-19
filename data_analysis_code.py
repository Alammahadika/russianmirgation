import feedparser

rss_url = ""  # URL feed
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.published}\n")

rss_urls = ["URL News"]

entries = []

for url in rss_urls:
    feed = feedparser.parse(url)
    entries.extend(feed.entries)

print(f"Total articles retrieved: {len(entries)}")

for entry in entries[:0]:  # collection news quantity
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.published}\n")




#==-===========


import requests
from bs4 import BeautifulSoup

# Sample news URLs from Central Asian sources
NEWS_URLS = [
    "https://asiaplustj.info/en/news/tajikistan/society/20240923/the-west-cautiously-extends-migrant-worker-options-for-central-asia",
    "https://timesca.com/tajik-migrants-facing-xenophobia-in-russia-after-moscow-terrorist-attack/",
    "https://www.gazeta.uz/en/2016/11/04/migration/"
]

def extract_article_data(url):
    """
    Extracts structured information from news articles
    
    Args:
        url (str): URL of the news article
        
    Returns:
        dict: Contains extracted metadata and content
    """
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        return {
            "url": url,
            "title": get_meta_content(soup, 'title') or "No title found",
            "description": get_meta_content(soup, 'description') or "No description",
            "publisher": get_meta_content(soup, 'og:site_name') or "Unknown publisher",
            "first_paragraph": get_first_paragraph(soup) or "No content extracted"
        }
        
    except Exception as e:
        return {"url": url, "error": str(e)}

def get_meta_content(soup, property_name):
    """Helper to extract meta tag content"""
    tag = soup.find("meta", attrs={"name": property_name}) or \
          soup.find("meta", attrs={"property": f"og:{property_name}"})
    return tag.get("content").strip() if tag else None

def get_first_paragraph(soup):
    """Extracts the first meaningful paragraph"""
    for p in soup.find_all("p"):
        if len(p.text.strip()) > 50:  # Minimum character threshold
            return p.text.strip()
    return None

# Execute scraping
if __name__ == "__main__":
    print("🔄 Scraping Central Asian news articles...\n")
    
    results = []
    for url in NEWS_URLS:
        article = extract_article_data(url)
        results.append(article)
        
        # Print formatted output
        print(f"🌐 {article.get('publisher', 'Unknown')}")
        print(f"🔗 {article['url']}")
        print(f"📰 {article.get('title')}")
        print(f"📝 {article.get('description')}")
        print(f"➡️ Excerpt: {article.get('first_paragraph')[:150]}...")
        print("\n" + "─"*80 + "\n")

    print(f"✅ Successfully processed {len([r for r in results if 'error' not in r])}/{len(NEWS_URLS)} articles")
    
    
    #### FOR WEB PAGE ERROR
    
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

# Central Asian news sources to monitor
NEWS_URLS = [
    "https://daryo.uz/en/2022/12/09/russia-lures-uzbek-migrant-workers-to-its-army-by-offering-fast-track-citizenship",
    "https://daryo.uz/en/2022/10/31/jan-sept-2022-over-300-000-russian-citizens-enter-uzbekistan"
]

# Browser headers to avoid bot detection
HEADERS = { 'User-Agent': ''}

def scrape_news_articles(url_list):
    """
    Scrape news articles from given URLs
    
    Args:
        url_list (list): List of news article URLs
        
    Returns:
        list: Dictionary of extracted article data
    """
    articles_data = []
    
    for url in url_list:
        try:
            # Send request with headers
            req = Request(url, headers=HEADERS)
            response = urlopen(req)
            html = response.read()
            
            # Parse HTML content
            soup = BeautifulSoup(html, 'html.parser')
            
            # Extract article components
            article = {
                'URL': url,
                'Title': get_article_title(soup),
                'Description': get_meta_description(soup),
                'First Paragraph': get_first_paragraph(soup),
                'Source': 'Daryo.uz'  # Can be extracted dynamically
            }
            articles_data.append(article)
            
        except Exception as e:
            print(f"⚠️ Error processing {url}: {str(e)}")
            articles_data.append({
                'URL': url,
                'Error': str(e)
            })
    
    return articles_data

def get_article_title(soup):
    """Extract article title"""
    return soup.title.string.strip() if soup.title else "No title found"

def get_meta_description(soup):
    """Extract meta description"""
    meta = soup.find('meta', attrs={'name': 'description'})
    return meta['content'].strip() if meta else "No description available"

def get_first_paragraph(soup):
    """Extract first meaningful paragraph"""
    for p in soup.find_all('p'):
        if p.text.strip() and len(p.text.strip()) > 20:
            return p.text.strip()
    return "No content found"

if __name__ == "__main__":
    print("🚀 Starting Central Asian news scraper...")
    articles = scrape_news_articles(NEWS_URLS)
    
    # Convert to DataFrame for better visualization
    df = pd.DataFrame(articles)
    print("\n📰 Scraped Articles Summary:")
    print(df[['Title', 'Source']])    
    

## DATA ACCURATE



from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

#  Load Data
df = pd.read_excel("/Users/mymac/Desktop/allnews.xlsx")

#  Data Preprocessing
df = df.dropna(subset=['Paragraph', 'Frameworks'])

# Remove classes with less than 2 samples
df = df[df['Frameworks'].map(df['Frameworks'].value_counts()) >= 2]

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X = tfidf.fit_transform(df['Paragraph'])
y = df['Frameworks']

# Train Model on All Data
model = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=42)
model.fit(X, y)

# Predict on the Same Data
y_pred = model.predict(X)

# Evaluate Model
print("Classification Report:")
print(classification_report(y, y_pred))
print(f"Accuracy Score: {accuracy_score(y, y_pred):.2f}")


# LDA



import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# callculate each country - i just showing from Uzbekistan Media
data = pd.read_excel("/Users/mymac/Desktop/Uzbekistan_News_Media copy.xlsx")


# processing text and clening text
def preprocess_text(text):
    text = text.lower()  #  change small words
    text = re.sub(r'[^a-z\s]', '', text)  # delete number 
    return text
  
# Must not have NaN in coulumns 'description'
data['Paragraph'] = data['Paragraph'].fillna('')  # change NaN with string empty

# save decsription in variable
Paragraph = data['Paragraph']


import re

# implementation to columns 'description'
Paragraph = Paragraph.apply(preprocess_text)


# Vectorize teks
vectorizer = CountVectorizer(stop_words='english')  # delete stop words
X = vectorizer.fit_transform(Paragraph)  # Hasilkan bag-of-words

# LDA
lda = LatentDirichletAllocation(n_components=101, random_state=42)  # choose topic
lda.fit(X)

#  showing dominant topic and dominant text
n_top_words = 10  # summary words want to showing
feature_names = vectorizer.get_feature_names_out()  #  get fiture (words)

for topic_idx, topic in enumerate(lda.components_):
    print(f"Topik {topic_idx + 1}:")
    top_words = [feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]
    print(" ".join(top_words))

# Distribution topic for each document
theta = lda.transform(X)  # n_documents x n_topics
print(pd.DataFrame(theta, columns=[f"Topic {i+1}" for i in range(lda.n_components)]))

# Dominant topict each document
dominant_topics = theta.argmax(axis=1)  # Index topic with highest probility 
data['Dominant_Topic'] = dominant_topics + 1  # Indeks start form 0, so add 1
print(data[['Paragraph', 'Dominant_Topic']])



### BIGRAM ANALYSIS


import pandas as pd  
from sklearn.feature_extraction.text import CountVectorizer  
from nltk.corpus import stopwords  
import nltk  
  
# install stopwords dari NLTK (just one time to run)  
nltk.download('stopwords')  
  
# Dataframe  
data = pd.read_excel("/Users/mymac/Downloads/alldominant.xlsx")  
df = pd.DataFrame(data)  
  
# Preprocessing: Lowercase and remove punctuation  
df['Paragraph_cleaned'] = df['Paragraph'].str.lower().str.replace(r'[^\w\s]', '', regex=True)  
  
# Define stopwords  
stop_words = stopwords.words('english')  # using stopwords dari NLTK  
  
# Function to extract bigrams  
def extract_bigrams(text):  
    vectorizer = CountVectorizer(ngram_range=(4, 4), stop_words='english')  # using 'english' sebagai stopwords  
    bigrams = vectorizer.fit_transform([text])  
    bigram_freq = zip(vectorizer.get_feature_names_out(), bigrams.toarray()[0])  
    return sorted(bigram_freq, key=lambda x: x[1], reverse=True)  
  
# Apply bigram extraction per Framework  
results = {}  
for framework in df['Framework'].unique():  
    combined_text = " ".join(df[df['Framework'] == framework]['Paragraph_cleaned'])  
    results[framework] = extract_bigrams(combined_text)  
  
# Display results  
for framework, bigrams in results.items():  
    print(f"Top bigrams for Framework: {framework}")  
    for bigram, freq in bigrams[:2]:  # Top 5 bigrams  
        print(f"{bigram}: {freq}")  
    print()  


## POL SUB ANALYSIS


import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.DataFrame(data)

# Inisialisasi VADER 

analyzer = SentimentIntensityAnalyzer()

# for calculations polarity dan subjectivity
def analyze_sentiment_custom(text):
    scores = analyzer.polarity_scores(text)
    # Hitung polarity sebagai selisih positif dan negatif
    polarity = scores['pos'] - scores['neg']
    # Hitung subjectivity sebagai proporsi (positif + negatif) dari total sentiment (positif + negatif + netral)
    subjectivity = (scores['pos'] + scores['neg']) / (scores['pos'] + scores['neg'] + scores['neu'])
    return polarity, subjectivity

#  colums teks
df[['polarity', 'subjectivity']] = df['Paragraph'].apply(
    lambda x: pd.Series(analyze_sentiment_custom(x))
)

#  polarity dan subjectivity for all dataset
average_polarity = df['polarity'].mean()
average_subjectivity = df['subjectivity'].mean()

print("Dataframe dengan Polarity dan Subjectivity:")
print(df)

print("\nRata-rata Polarity dan Subjectivity Keseluruhan:")
print(f"Polarity: {average_polarity:.2f}, Subjectivity: {average_subjectivity:.2f}")


# Inisialisasi VADER
analyzer = SentimentIntensityAnalyzer()

# polarity with VADER
def calculate_polarity_vader(text):
    scores = analyzer.polarity_scores(text)
    return scores['pos'] - scores['neg']  # Hanya mempertimbangkan positif dan negatif

#  subjectivity with TextBlob
def calculate_subjectivity_textblob(text):
    blob = TextBlob(text)
    return blob.sentiment.subjectivity

# implementation  for polarity and subjectivity
df['polarity'] = df['Paragraph'].apply(calculate_polarity_vader)
df['subjectivity'] = df['Paragraph'].apply(calculate_subjectivity_textblob)

#  polarity dan subjectivity for all dataset
average_polarity = df['polarity'].mean()
average_subjectivity = df['subjectivity'].mean()

print("Dataframe dengan Polarity dan Subjectivity:")
print(df)

print("\nRata-rata Polarity dan Subjectivity Keseluruhan:")
print(f"Polarity: {average_polarity:.2f}, Subjectivity: {average_subjectivity:.2f}")

print(average_polarity)
print(average_subjectivity)

#===== 




    
    
