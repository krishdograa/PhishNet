RESULTS AND DISCUSSION

![image](https://github.com/user-attachments/assets/d6679560-eb3f-4127-bb6c-62aa280f3803)

The PhishNet system provides a user-friendly web-based interface designed using Flask. This interface allows users to manually input email content or upload email files to verify their authenticity. The design prioritizes ease of use and clarity, ensuring even non-technical users can interact with the system effectively.

![image](https://github.com/user-attachments/assets/66f173e8-cc6e-4251-951e-169389f9c9e3)
 A Legitimate Email


 ![image](https://github.com/user-attachments/assets/f5a66373-0381-47ff-b9ec-097263a290cf)
Legitimate Email Detection by Phishnet


In this case, the system analyzed a benign email and correctly classified it as Not Phishing. The classification was based on NLP features such as absence of urgent phrases, proper grammatical structure, and absence of suspicious links or requests for sensitive information.


 ![image](https://github.com/user-attachments/assets/5b66fbd1-a808-452a-984e-0f08035173e6)
 Phishing Email



This image presents an email with classic phishing traits—such as the use of urgency (“Immediate action required”), suspicious links, and requests for login credentials. The model effectively identified this email as Phishing with a high confidence score.


 ![image](https://github.com/user-attachments/assets/7f4f7420-158a-4646-95aa-b4a284c9817e)
Phishing Email Detection by Phishnet

These results validate the effectiveness of the PhishNet system in detecting phishing emails with high accuracy and providing actionable outputs for users. By combining NLP-based feature extraction with a Random Forest classifier, the system effectively distinguishes between phishing and non-phishing emails, thereby significantly reducing the risk of falling prey to email scams.
The integration of a real-time interface enhances usability and accessibility, especially for non-technical users. These elements contribute to a comprehensive solution for one of the most prevalent threats in cybersecurity today.
