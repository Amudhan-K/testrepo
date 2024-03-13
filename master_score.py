import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


data = {
    'text': ["Excellent programming skills in Python and Java.",
             "Strong communication and teamwork abilities.",
             "Experience with data analysis and machine learning algorithms.",
             "Proficient in SQL and database management.",
             "Familiarity with web development frameworks such as Django and Flask.",
             "Good problem-solving skills and attention to detail."],
    'label': ["Software Engineer",
              "Software Engineer",
              "Data Scientist",
              "Data Analyst",
              "Web Developer",
              "Data Analyst"]
}


resume = "Excellent programming skills in Python and Java. Strong communication and teamwork abilities."
job_description = "We are looking for a candidate with excellent programming skills in Python and Java. Good communication and teamwork abilities are a must."


df = pd.DataFrame(data)


X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)


clf = MultinomialNB()
clf.fit(X_train_counts, y_train)


predictions = clf.predict(X_test_counts)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)


df = pd.DataFrame(data)


label_encoder = LabelEncoder()
df['label'] = label_encoder.fit_transform(df['label'])
num_classes = len(label_encoder.classes_)


tokenizer = Tokenizer()
tokenizer.fit_on_texts(df['text'])
X = tokenizer.texts_to_sequences(df['text'])
max_sequence_length = max([len(x) for x in X])
X = pad_sequences(X, maxlen=max_sequence_length)


X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.2, random_state=42)


embedding_dim = 50
vocab_size = len(tokenizer.word_index) + 1

model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_sequence_length))
model.add(Conv1D(128, 5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

predictions = model.predict_classes(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform([resume, job_description])


cosine_sim = cosine_similarity(X[0], X[1])

print("Cosine Similarity:", cosine_sim[0][0])
