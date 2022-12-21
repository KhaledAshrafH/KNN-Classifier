# KNN-Classifier
K-Nearest_Neighbours Classifier implementation from scratch in python and tells whether a banknote is real or not in dataset "BankNote_Authentication.csv".

Whenever you go to the bank to deposit some cash money, the cashier places banknotes in a machine that tells whether a banknote is real or not. In the
“BankNote_Authentication.csv” we have four features: variance, skew, curtosis and entropy and the class attribute refers to whether or not the banknote is real or forged.

# Experiment with different values of k=1,2,3....9
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
 <tr style="mso-yfti-irow:16;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">16<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9951456310679612<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">17<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9951456310679612<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">18<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">19<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">20<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">21<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">22<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">23<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:24;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">24<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:25;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">25<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:26;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">26<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:27;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">27<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:28;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">28<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:29;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">29<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:30;mso-yfti-lastrow:yes;height:21.9pt">
  <td width="359" valign="top" style="width:269.3pt;border:solid black 1.0pt;
  border-top:none;mso-border-top-alt:solid black .75pt;mso-border-alt:solid black .75pt;
  padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">30<o:p></o:p></span></p>
  </td>
  <td width="359" valign="top" style="width:269.3pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  mso-border-top-alt:solid black .75pt;mso-border-left-alt:solid black .75pt;
  mso-border-alt:solid black .75pt;padding:0cm 0cm 0cm 0cm;height:21.9pt">
  <p class="TableParagraph" align="center" style="margin-left:55.65pt;text-align:
  center"><span style="font-size:16.0pt;mso-bidi-font-size:11.0pt">0.9902912621359223<o:p></o:p></span></p></td></tr></tbody></table><br></p></div>
