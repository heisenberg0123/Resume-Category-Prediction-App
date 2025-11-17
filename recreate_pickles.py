import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC

# load dataset (workspace file)
df = pd.read_csv("UpdatedResumeDataSet.csv")

# minimal cleaning / safety
df = df.dropna(subset=["Resume", "Category"])
df["Resume"] = df["Resume"].astype(str)
df["Category"] = df["Category"].astype(str)

# encode labels
le = LabelEncoder()
y = le.fit_transform(df["Category"])

# vectorize text
tfidf = TfidfVectorizer(stop_words="english", max_features=10000)
X = tfidf.fit_transform(df["Resume"])

# classifier (linear SVC wrapped for multiclass)
clf = OneVsRestClassifier(SVC(kernel="linear", probability=True, random_state=42))
clf.fit(X, y)

# backup existing pickles (optional)
try:
    import shutil, os
    if os.path.exists("tfidf.pkl"):
        shutil.copy2("tfidf.pkl", "tfidf.pkl.bak")
    if os.path.exists("clf.pkl"):
        shutil.copy2("clf.pkl", "clf.pkl.bak")
    if os.path.exists("encoder.pkl"):
        shutil.copy2("encoder.pkl", "encoder.pkl.bak")
except Exception:
    pass

# save new pickles
pickle.dump(tfidf, open("tfidf.pkl", "wb"))
pickle.dump(clf, open("clf.pkl", "wb"))
pickle.dump(le, open("encoder.pkl", "wb"))

print("Saved tfidf.pkl, clf.pkl, encoder.pkl")