# K-Nearest Neighbors (KNN) Classifier from Scratch

This repository contains a Python implementation of a K-Nearest Neighbors (KNN) classifier from scratch. The KNN classifier is applied to the "BankNote_Authentication" dataset, which consists of four features (variance, skew, curtosis, and entropy) and a class attribute indicating whether a banknote is real or forged.

## Dataset

The dataset used for training and testing the KNN classifier is provided in the "BankNote_Authentication.csv" file. The dataset is loaded into a pandas DataFrame and then shuffled to ensure randomization during training and testing.

## KNN Classifier Implementation

The KNN classifier is implemented in the `KNN_Classifier` class. The class takes the following inputs during initialization:

- `x_train`: The training data features.
- `y_train`: The training data labels.
- `x_test`: The test data features.
- `k`: The number of nearest neighbors to consider.

The KNN classifier consists of the following methods:

### 1. `euclidean_distance`

This method calculates the Euclidean distance between a training row and a test row. It takes two input vectors and computes the Euclidean distance according to the formula:
```
distance = sqrt(sum((x_train_row[i] - x_test_row[i])^2))
```

### 2. `predict`

This method predicts the class for each test point based on the K-nearest neighbors in the training data. For each test point, the Euclidean distance is calculated between the test point and all training points. The K-nearest neighbors with the smallest distances are determined, and their corresponding class labels are counted. If there is a tie in the number of votes for different classes, the tie is broken in favor of the class that comes first in the training data.

### 3. `calc_accuracy`

This method calculates the accuracy of the KNN classifier by comparing the predicted labels with the true labels for the test data. The accuracy is computed as the ratio of correctly classified instances to the total number of instances in the test set.

## Normalization

Before training and testing the KNN classifier, the feature columns are normalized separately using the mean and standard deviation of the values in the training data. Each feature is transformed using the function:
```
f(v) = (v - mean) / std
```

This normalization ensures that each feature contributes equally to the distance calculation.

## Training and Testing

The dataset is split into 70% for training and 30% for testing. The training and test sets are created by dividing the feature and label arrays accordingly.

The KNN classifier is then trained on the training data and tested on the test data for different values of K ranging from 1 to 9. For each value of K, the classifier's accuracy is calculated and stored in a list.

## Experiment

The KNN classifier is evaluated using different values of K ranging from 1 to 15. The accuracy of the classifier is measured for each K value, and the results are summarized in the following table:

<div class="WordSection1" align="center"><p class="MsoBodyText" align="center" style="margin-top:3.3pt;margin-right:128.15pt;
margin-bottom:0cm;margin-left:127.25pt;margin-bottom:.0001pt;text-align:center"><table class="MsoNormalTable" border="1" cellspacing="0" cellpadding="0" style="margin-left:5.8pt;border-collapse:collapse;mso-table-layout-alt:fixed;
 border:none;mso-border-alt:solid black .75pt;mso-yfti-tbllook:480;mso-padding-alt:
 0cm 0cm 0cm 0cm;mso-border-insideh:.75pt solid black;mso-border-insidev:.75pt solid black">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  mso-border-alt:solid black .75pt;background:#103E91;padding:0cm 0cm 0cm 0cm;
  height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><b style="mso-bidi-font-weight:normal"><span style="font-size:16.0pt;
  mso-bidi-font-size:11.0pt;font-family:&quot;Arial&quot;,sans-serif;mso-hansi-font-family:
  &quot;Arial MT&quot;;mso-bidi-font-family:&quot;Arial MT&quot;;color:white"><b>K</b></span></b><b style="mso-bidi-font-weight:normal"><span style="font-size:16.0pt;mso-bidi-font-size:
  11.0pt;font-family:&quot;Arial&quot;,sans-serif;mso-hansi-font-family:&quot;Arial MT&quot;;
  mso-bidi-font-family:&quot;Arial MT&quot;"><o:p></o:p></span></b></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-left:none;mso-border-left-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  background:#103E91;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><b style="mso-bidi-font-weight:normal"><span style="font-size:16.0pt;
  mso-bidi-font-size:11.0pt;font-family:&quot;Arial&quot;,sans-serif;mso-hansi-font-family:
  &quot;Arial MT&quot;;mso-bidi-font-family:&quot;Arial MT&quot;;color:white"><b>Accuracy</b></span></b><b style="mso-bidi-font-weight:normal"><span style="font-size:16.0pt;mso-bidi-font-size:
  11.0pt;font-family:&quot;Arial&quot;,sans-serif;mso-hansi-font-family:&quot;Arial MT&quot;;
  mso-bidi-font-family:&quot;Arial MT&quot;"><o:p></o:p></span></b></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">2<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">3<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">4<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">5<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">6<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">7<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">8<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-top:.75pt;margin-right:
  0cm;margin-bottom:0cm;margin-left:.55pt;margin-bottom:.0001pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">9<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">10<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">11<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">12<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9975728155339806<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">13<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">1.0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">14<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9975728155339806<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">15<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9975728155339806<o:p></o:p></span></p>
  </td>
 </tr>
 </tbody></table><br></p></div>

## Results

The results of the KNN classifier for different values of K are displayed in the console. The output includes the value of K used for the test set and summary information for each K value, including the number of correctly classified test instances, the total number of instances in the test set, and the accuracy.

An example of the output:
```
K Value: 12
Number of correctly classified instances: 444
Total number of instances: 445
Accuracy: 0.9975728155339806
```

## Conclusion

This code provides implementation of a KNN classifier from scratch using Python. It demonstrates the steps involved in training and testing a KNN classifier, including data normalization, distance calculation, and prediction. By experimenting with different values of K, the code evaluates the performance of the classifier and provides accuracy metrics for each K value.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.


## Team

- [Khaled Ashraf Hanafy Mahmoud - 20190186](https://github.com/KhaledAshrafH).
- [Noura Ashraf Abdelnaby Mansour - 20190592](https://github.com/NouraAshraff).
- [Samaa Khalifa Elsayed Othman - 20190247](https://github.com/SamaaKhalifa).

## License

This program is licensed under the [MIT License](LICENSE.md).

