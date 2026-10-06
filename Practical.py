'''# Practical 1: Inverted index construction using the postings method (with user input)
n = int(input("Enter number of documents: "))
docs = {}
for i in range(1, n + 1):
    docs[i] = input("Enter text of document " + str(i) + ": ")
pairs = []
for doc_id, text in docs.items():
    for word in text.lower().split():
        word = word.strip(".,;:!?")     
        pairs.append((word, doc_id))

pairs.sort()

index = {}
for term, doc_id in pairs:
    if term not in index:
        index[term] = []
    if doc_id not in index[term]:
        index[term].append(doc_id)
        
print("\nTerm\tDF\tPostings")
for term in index:
    print(term, len(index[term]), index[term], sep="\t")

def search(t1, op, t2):
    p1 = index.get(t1, [])
    p2 = index.get(t2, [])
    result = []
    if op == "AND":
        for d in p1:
            if d in p2:
                result.append(d)
    elif op == "OR":
        result = sorted(set(p1 + p2))
    elif op == "NOT":                    
        for d in p1:
            if d not in p2:
                result.append(d)
    return result

print("\nQuery format: term1 AND/OR/NOT term2")
t1 = input("Enter term 1: ").lower()
op = input("Enter operator (AND / OR / NOT): ").upper()
t2 = input("Enter term 2: ").lower()

print("Result documents:", search(t1, op, t2))'''




'''
# Practical 2: Boolean retrieval model

n = int(input("Enter number of documents: "))
docs = []
for i in range(n):
    docs.append(input("Enter text of document " + str(i + 1) + ": "))

vocab = set()
for text in docs:
    for word in text.lower().split():
        vocab.add(word.strip(".,;:!?"))
vocab = sorted(vocab)

matrix = {}
for term in vocab:
    row = []
    for text in docs:
        words = [w.strip(".,;:!?") for w in text.lower().split()]
        if term in words:
            row.append(1)
        else:
            row.append(0)
    matrix[term] = row

print("\nExample query: cow AND NOT tuesday")
query = input("Enter Boolean query: ")

print("\nTerm-Document Incidence Matrix")
print("Term\t" + "\t".join("D" + str(i + 1) for i in range(n)))
for term in vocab:
    print(term + "\t" + "\t".join(str(b) for b in matrix[term]))

tokens = query.split()

result = None
op = "AND"  
negate = False

print("\nQuery term vectors")
for tok in tokens:
    word = tok.upper()
    if word == "AND" or word == "OR":
        op = word
    elif word == "NOT":
        negate = True
    else:
        term = tok.lower()
        vec = matrix.get(term, [0] * n)      
        if negate:
            vec = [1 - b for b in vec]       
            print("NOT " + term + " :", vec)
            negate = False
        else:
            print(term + " :", vec)

        if result is None:
            result = vec
        elif op == "AND":
            result = [a & b for a, b in zip(result, vec)]
        else:
            result = [a | b for a, b in zip(result, vec)]
print("\nBitwise result:", result)
print("Retrieved documents:", end=" ")
found = False
for i in range(n):
    if result[i] == 1:
        print("D" + str(i + 1), end=" ")
        found = True
if not found:
    print("None", end="")
print()
'''



'''
# Practical 2B: Vector Space Model with TF-IDF and cosine similarity
import math
from collections import Counter
n = int(input("Enter number of documents: "))
documents = []
for i in range(n):
    doc = input("Enter Document" + str(i + 1) + ": ").lower()
    for ch in ".,;:!?":
        doc = doc.replace(ch, "")         
    documents.append(doc)

query = input("Enter Query (ex. harsh is giving exam): ").lower()
for ch in ".,;:!?":
    query = query.replace(ch, "")

print("\nSTEP 1 : Documents and Query")
for i in range(n):
    print("Document", i + 1, ":", documents[i])
print("Query :", query)

print("\nSTEP 2 : Frequency Table")
freqs = []
for i in range(n):
    freq = Counter(documents[i].split())
    freqs.append(freq)
    print("\nDocument", i + 1)
    for word, count in freq.items():
        print(word, ":", count)

vocabulary = []
for doc in documents:
    for word in doc.split():
        if word not in vocabulary:
            vocabulary.append(word)
print("\nSTEP 3 : Vocabulary")
print(vocabulary)

print("\nSTEP 4 : Arranged Vocabulary (ascending)")
for i in range(n):
    print("Document", i + 1, ":", sorted(freqs[i]))
vocabulary.sort()
print("All documents :", vocabulary)

idf = {}
for word in vocabulary:
    df = 0
    for doc in documents:
        if word in doc.split():
            df += 1
    idf[word] = math.log10(n / df)

print("\nSTEP 5 : Vectors (TF-IDF)")
doc_vectors = []
for i in range(n):
    vec = []
    for word in vocabulary:
        vec.append(freqs[i][word] * idf[word])   # tf * idf
    doc_vectors.append(vec)
    print("Document", i + 1, ":", [round(x, 3) for x in vec])

q_freq = Counter(query.split())
q_vec = []
for word in vocabulary:
    q_vec.append(q_freq[word] * idf[word])
print("Query      :", [round(x, 3) for x in q_vec])

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    len_a = math.sqrt(sum(x * x for x in a))
    len_b = math.sqrt(sum(y * y for y in b))
    if len_a == 0 or len_b == 0:
        return 0
    return dot / (len_a * len_b)

print("\nSTEP 6 : Cosine Similarity")
scores = []
for i in range(n):
    s = cosine(doc_vectors[i], q_vec)
    scores.append((s, i + 1))
    print("Document", i + 1, ":", round(s, 4))

scores.sort(reverse=True)
print("\nSTEP 7 : Ranked Documents")
rank = 1
for s, d in scores:
    print("Rank", rank, ": Document", d, "(score =", round(s, 4), ")")
    rank += 1
'''




'''
# Practical 3: Edit distance (Levenshtein) using a matrix

str1 = input("Enter first string (ex.EDITING): ")
str2 = input("Enter second string: ")
m = len(str1)
n = len(str2)
dp = []
for i in range(m + 1):
    dp.append([0] * (n + 1))

for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]          
        else:
            delete  = dp[i - 1][j]
            insert  = dp[i][j - 1]
            replace = dp[i - 1][j - 1]
            dp[i][j] = 1 + min(delete, insert, replace)

print("\nEdit Distance Matrix:")
for row in dp:
    print(row)

print("\nFinal Edit Distance =", dp[m][n])

'''


'''
# PR4, Q.A, Evaluation Metrics for IR System
relevant = {"D1","D2","D4","D5"}
retrieved = {"D1","D2","D3","D5"}
true_pos = len(relevant.intersection(retrieved))
retrieved_doc = len(retrieved)
relevant_doc = len(relevant)
precision = true_pos / retrieved_doc
recall = true_pos / relevant_doc
f_measure = (2* precision * recall) / (precision + recall)
print("Relevant Documents:")
print(relevant)
print("\n Retrieved Documents:")
print(retrieved)
print("\nPrecision:")
print(round(precision, 2))
print("\nRecall")
print(round(recall, 2))
print("\nF-Measure:")
print(round(f_measure, 2))
'''

'''
#PR 4, Q.B - average precision and evaluation metrics
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import average_precision_score
actual = [1, 1, 0, 1, 0]
predicted = [1, 1, 1, 0, 0]
precision = precision_score(actual, predicted)
recall = recall_score(actual, predicted)
f_measure = f1_score(actual, predicted)
average_precision = average_precision_score(actual, predicted)
print("Precision:")
print(round(precision, 2))
print("\nRecall:")
print(round(recall, 2))
print("\nF-Measure:")
print(round(f_measure, 2))
print("\nAverage Precision:")
print(round(average_precision, 2))
'''


'''
# Pr 5, Naive Bayes Classification using sklearn CategoricalNB and numpy
import numpy as np
from sklearn.naive_bayes import CategoricalNB

data = [
    ["y", "y", "y", "Covid"],
    ["y", "n", "y", "Covid"],
    ["y", "y", "n", "Covid"],
    ["n", "y", "y", "Flu"],
    ["n", "y", "n", "Flu"],
    ["n", "n", "y", "Flu"]
]

def encode(v):
    return 1 if v == "y" else 0

X = np.array([[encode(r[0]), encode(r[1]), encode(r[2])] for r in data])
y = np.array([r[3] for r in data])

covid = input("Enter covid (y/n): ").lower()
flu = input("Enter flu (y/n): ").lower()
fever = input("Enter fever (y/n): ").lower()

test = np.array([[encode(covid), encode(flu), encode(fever)]])

model = CategoricalNB(alpha=1e-10, min_categories=2)
model.fit(X, y)

print("\nClasses:", model.classes_)
print("Prior Probabilities =", np.round(np.exp(model.class_log_prior_), 3))
names = ["Covid", "Flu", "Fever"]
for k, disease in enumerate(model.classes_):
    print("\nDisease:", disease)
    for i in range(3):
        value = test[0][i]
        p = np.exp(model.feature_log_prob_[i][k][value])
        print("P(" + names[i] + "=" + ("y" if value == 1 else "n") + "|" + disease + ") =", round(p, 3))

proba = model.predict_proba(test)[0]
print()
for k, disease in enumerate(model.classes_):
    print("P(" + disease + " | input) =", round(proba[k], 4))

prediction = model.predict(test)[0]
print("\nFinal Prediction:", prediction)'
'''








'''
# PR 5, Support Vector Machine Classification using sklearn SVC and numpy
import numpy as np
from sklearn.svm import SVC

data = [
    ["y", "y", "y", "Covid"],
    ["y", "n", "y", "Covid"],
    ["y", "y", "n", "Covid"],
    ["n", "y", "y", "Flu"],
    ["n", "y", "n", "Flu"],
    ["n", "n", "y", "Flu"]
]

def encode(v):
    return 1 if v == "y" else 0

X = np.array([[encode(r[0]), encode(r[1]), encode(r[2])] for r in data])
y = np.array([r[3] for r in data])

covid = input("Enter covid (y/n): ").lower()
flu = input("Enter flu (y/n): ").lower()
fever = input("Enter fever (y/n): ").lower()

test = np.array([[encode(covid), encode(flu), encode(fever)]])

model = SVC(kernel="linear", C=1000)
model.fit(X, y)

print("\nClasses:", model.classes_)
print("\nSupport Vectors:")
print(model.support_vectors_)
print("Number of support vectors per class:", model.n_support_)

w = model.coef_[0]
b = model.intercept_[0]
print("\nWeight vector w =", np.round(w, 3))
print("Bias b =", round(b, 3))

score = np.dot(w, test[0]) + b
print("\nDecision value w.x + b =", round(score, 3))
print("Margin width = 2/||w|| =", round(2 / np.linalg.norm(w), 3))

prediction = model.predict(test)[0]
print("\nFinal Prediction:", prediction)
'''











'''
# PR6, K-Means clustering (user input)
import math

n = int(input("Enter number of data points: "))
points = []
for i in range(n):
    x, y = input("Enter P" + str(i + 1) + " (x y): ").split()
    points.append((float(x), float(y)))

k = int(input("Enter number of clusters K: "))
centroids = []
for i in range(k):
    x, y = input("Enter K" + str(i + 1) + " centroid (x y): ").split()
    centroids.append((float(x), float(y)))

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

print("\nStep 1 : Initial centroids")
for i in range(k):
    print("K" + str(i + 1), "=", centroids[i])

iteration = 1
while True:
    print("\n========== Iteration", iteration, "==========")

    print("\nStep 2 : Euclidean distances")
    header = "Point\t" + "\t".join("K" + str(j + 1) for j in range(k)) + "\tCluster"
    print(header)

    clusters = [[] for _ in range(k)]
    for i in range(n):
        dists = []
        for j in range(k):
            dists.append(distance(points[i], centroids[j]))
        nearest = dists.index(min(dists))         
        clusters[nearest].append(points[i])
        row = "P" + str(i + 1) + "\t" + "\t".join(str(round(d, 2)) for d in dists)
        print(row + "\tK" + str(nearest + 1))

    print("\nStep 3 : Clusters")
    for j in range(k):
        print("K" + str(j + 1), ":", clusters[j])

    new_centroids = []
    for j in range(k):
        if len(clusters[j]) > 0:
            mx = sum(p[0] for p in clusters[j]) / len(clusters[j])
            my = sum(p[1] for p in clusters[j]) / len(clusters[j])
            new_centroids.append((round(mx, 2), round(my, 2)))
        else:
            new_centroids.append(centroids[j])      

    print("\nStep 4 : New centroids")
    for j in range(k):
        print("K" + str(j + 1), "=", new_centroids[j])

    if new_centroids == centroids:
        print("\nCentroids did not change. Clustering is complete.")
        break
    centroids = new_centroids
    iteration += 1

print("\nFinal clusters")
for j in range(k):
    print("K" + str(j + 1), ":", clusters[j], " centroid =", centroids[j])
'''
