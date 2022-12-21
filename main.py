from datetime import date
from datetime import datetime

import numpy as np
import pandas as pd
from fpdf import FPDF
from matplotlib import pyplot as plt


class PDF(FPDF):
    def __init__(self):
        super().__init__()

    def header(self):
        self.set_font('Arial', '', 12)
        # self.cell(0, 8, 'KNN Implementation Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')


class KNN_Classifier:
    def __init__(self, x_train, y_train, x_test, k):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.k = k
        self.accuracy = 0
        self.predicted_list = []

    # To calc distance for each training row
    def euclidean_distance(self, x_train_row, x_test_row):
        Sum = np.sum((x_train_row - x_test_row) ** 2)  # (x_train_row[i]-x_test_row[i])^2
        return np.sqrt(Sum)

    # To predict the class for specific point
    def predict(self):
        # predict for each x_test point with all point in training data
        for i in self.x_test:
            distances = []
            for j in self.x_train:
                x_train_row = j
                x_test_row = i
                distance = self.euclidean_distance(x_train_row, x_test_row)
                distances.append(distance)
            neighbors = np.array(distances)

            # Sort distances ascending attached with indices and take the first k points
            neighbors = neighbors.argsort()[: self.k]
            count = [0, 0]  # Encode 0 => class0 && 1 => class1
            for idx in neighbors:
                if self.y_train[idx] == 0:
                    count[0] += 1
                else:
                    count[1] += 1

            # To handle tie case
            if count[0] == count[1]:
                predicted_res = self.y_train[0]
            # Assign class for the prediction point
            elif count[0] > count[1]:
                predicted_res = 0
            else:
                predicted_res = 1

            self.predicted_list.append(predicted_res)
        return self.predicted_list

    # To return the calculated accuracy
    def calc_accuracy(slef, y_test, predicted):
        correctCnt = 0
        for i in range(len(y_test)):
            if y_test[i] == predicted[i]:
                correctCnt += 1
        accuracy = correctCnt / len(y_test)
        return accuracy


# To read the data
df = pd.read_csv('BankNote_Authentication.csv')

# To shuffle the data
df = df.sample(frac=1)

# Separate X and Y inside the data
X = df.iloc[:, df.columns != 'class'].values
Y = df['class'].values

# Normalize for each feature
X[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
X[:, 2] = (X[:, 2] - X[:, 2].mean()) / X[:, 2].std()
X[:, 3] = (X[:, 3] - X[:, 3].mean()) / X[:, 3].std()

# Split the dataset into training and testing sets
x_train = X[0:960]
y_train = Y[0:960]
x_test = X[960:]
y_test = Y[960:]

# For Comparison between SkiLearn Classifier Accuracy and My Model Accuracy
from sklearn.neighbors import KNeighborsClassifier

# model =  KNN_Classifier(x_train, y_train, x_test, k=7)
# Y_pred = model.predict()
# model1 = KNeighborsClassifier(n_neighbors=7)
# model1.fit(x_train, y_train)
# # Prediction on test set
# Y_pred1 = model1.predict(x_test)
# accuracy1 = model.calc_accuracy(y_test, Y_pred)
# accuracy2 = model.calc_accuracy(y_test, Y_pred1)
# print(f"when k = {7}:\nmy accuracy : {accuracy1}\nsklearn accuracy : {accuracy2}\n")

# To construct pdf content
linesStr = ""
scores = []
for k in range(1, 68):
    knn_classifier = KNN_Classifier(x_train, y_train, x_test, k=k)
    y_predicted = knn_classifier.predict()
    accuracy = knn_classifier.calc_accuracy(y_test, y_predicted)
    scores.append({'k': k, 'accuracy': accuracy})
    linesStr += f"\nk value : {k}\nNumber of correctly classified instances : {accuracy * len(y_test)}"
    linesStr += f"\nTotal number of instances : {len(y_test)}\nAccuracy : {accuracy}\n"
    print(f"k value : {k}\nNumber of correctly classified instances : {accuracy * len(y_test)}"
          f"\nTotal number of instances : {len(y_test)}\nAccuracy : {accuracy}\n")

# plotting Accuracy
score_list = pd.DataFrame(scores)
best_k = score_list.sort_values(by='accuracy', ascending=False).iloc[0]
print(score_list)
plt.figure(figsize=(6, 6))
plt.plot(score_list['k'], score_list['accuracy'], lw=3, c='#087E8B')
plt.scatter(best_k['k'], best_k['accuracy'], s=10, c='#087E8B')
plt.xlabel('K', size=10)
plt.ylabel('Accuracy', size=10)
plt.savefig("output.png")
plt.show()

# Generating Pdf
margin = 8
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 24)
pdf.set_text_color(190, 0, 0)
pdf.cell(w=0, h=20, txt="K-Nearest Neighbours(KNN) Classifier Report", ln=1)
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', 'B', 16)
pdf.cell(w=30, h=margin, txt="Date: ", ln=0)
pdf.cell(w=30, h=margin, txt=str(date.today().strftime("%d/%m/%Y")), ln=1)
pdf.cell(w=30, h=margin, txt="Time: ", ln=0)
pdf.cell(w=30, h=margin, txt=str(datetime.now().strftime("%H:%M:%S")), ln=1)
pdf.cell(w=30, h=margin, txt="Authors: ", ln=0)
pdf.cell(w=30, h=margin, txt="Khaled Ashraf, Noura Ashraf, Samaa Khalifa", ln=1)
pdf.ln(margin)
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(16, 63, 145)
pdf.cell(0, 8, 'Accuracy with different K', 0, 10, 'C')
pdf.set_text_color(0, 0, 0)
pdf.set_font('Arial', '', 16)
pdf.multi_cell(w=0, h=5, txt=linesStr)
pdf.ln(margin)

pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(16, 63, 145)
pdf.cell(0, 8, 'Plotting Accuracy', 0, 10, 'C')
pdf.image('./output.png', x=55, y=None, w=100, h=0, type='PNG', link='')
pdf.ln(margin)
pdf.set_font('Arial', 'B', 18)
pdf.set_text_color(16, 63, 145)
pdf.cell(0, 8, 'Table for each K with its Accuracy', 0, 10, 'C')
pdf.ln(margin)

pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(16, 63, 145)
# Table Header
pdf.set_font('Arial', 'B', 16)
pdf.cell(w=95, h=margin, txt='K', border=1, ln=0, align='C', fill=True)
pdf.cell(w=95, h=margin, txt='Accuracy', border=1, ln=1, align='C', fill=True)
# Table contents
pdf.set_font('Arial', '', 16)
pdf.set_text_color(0, 0, 0)
for i in range(0, len(score_list)):
    pdf.cell(w=95, h=margin,
             txt=str(score_list['k'].iloc[i]),
             border=1, ln=0, align='C')
    pdf.cell(w=95, h=margin,
             txt=str(score_list['accuracy'].iloc[i].astype(str)),
             border=1, ln=1, align='C')

pdf.output(f'./KNN_Report.pdf', 'F')
