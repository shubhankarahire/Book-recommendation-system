import streamlit as st
import  pandas as pd
import pickle


popular_books_dict = pickle.load(open("popular_books","rb"))
popular_books_df = pd.DataFrame(popular_books_dict)

# popular books poster
def fetch_popular_poster(book):

    popular_books_poster = popular_books_df[popular_books_df["title"] == book]["thumbnail"].values[0]

    return popular_books_poster

# top 5 recommender
popular_books_list =[]
popular_books_poster = []
for i in popular_books_df["title"]:
    popular_books_list.append(i)
    popular_books_poster.append(fetch_popular_poster(i))

# recommended book poster
def fetch_Poster(book):


    book_poster = books_df[books_df["title"] == book]["thumbnail"].values[0]

    return book_poster

# recommender function
def recommend(book):
    book_index = books_df[books_df["title"] == book].index[0]
    distance = similarity[book_index]
    book_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_books = list()
    recommended_books_posters = list()

    for i in book_list:
        book_id = i[0]
        recommended_books.append(books_df.iloc[i[0]].title)
        recommended_books_posters.append(fetch_Poster(books_df.iloc[i[0]].title))


    return  recommended_books, recommended_books_posters


#creating header
#st.header('Book Recommendation System')

books_dict = pickle.load(open("Book_dict.pkl","rb"))
books_df = pd.DataFrame(books_dict)

similarity = pickle.load(open("similarity.pkl","rb"))


#creating title
st.title("Book Recommendation System")

# Home page
st.markdown("Top 5 books")
col1,col2,col3,col4,col5 = st.columns(5)
#col6,col7,col8,col9,col10

with col1:
   st.subheader(popular_books_list[0])
   st.image(popular_books_poster[0])

with col2:
   st.subheader(popular_books_list[1])
   st.image(popular_books_poster[1])

with col3:
   st.subheader(popular_books_list[2])
   st.image(popular_books_poster[2])

with col4:
   st.subheader(popular_books_list[3])
   st.image(popular_books_poster[3])

with col5:
   st.subheader(popular_books_list[4])
   st.image(popular_books_poster[4])




#creating drop down list
selected_book_name = st.selectbox(
    "Select book name from drop down menu\nWhile typing book name do not type coma ( , )",
    books_df["title"].values)


if st.button('Recommend', type="primary"):
    names,posters = recommend(selected_book_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])