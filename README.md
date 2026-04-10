Loan Approval Risk Analysis DSS

Decision Problem
Financial institutions struggle to accurately assess the viability of loan applicants which results in the institutions losing money and increasing their “bad debt” ratio.
This DSS system will help make the decision of who to approve loans to much easier for the decision makers by using data obtained to predict potential defaulters as well as using the information to provide recommendations of what amount to approve to the applicants. This will help the bank prevent accumulating bad debts and ensure qualified borrowers get the money.

Decision Makers 
The main decision makers in this case are the loan officers and credit risk analysts who need to be able to justify their decisions 
Inputs, Outputs and Decision Criteria 

Inputs:
•	Applicant information- age, income, employment status, education level.
•	Financial History- credit score, existing debts and repayment history. 
•	Loan details- loan amount, reason for loan and duration to pay the loan.

Outputs:
•	A risk score 
•	The final recommendation

Decision Criteria:
•	Debt-to-income ratio- this shows the primary threshold for risk
•	Credit Score threshold- categorizing the applicant into risk tiers such as; low, medium, high.

System Architecture
Using a dataset that has all the relevant information such as credit scores and employment status 
The decision engine will utilize a predictive model such as regression to calculate the probability of defaulting. In addition, it will also incorporate a rule-based inference engine to make sure strict bank policies are followed such as, if age < 18, reject immediately.
For presentation, a Python-based application Streamlit will be used as the user interface to display all the necessary information.
 
<img width="1447" height="1061" alt="Screenshot 2026-04-10 094037" src="https://github.com/user-attachments/assets/6951a8a1-56a6-4d55-9ea9-ff977943f475" />
<img width="1230" height="1023" alt="Screenshot 2026-04-10 094053" src="https://github.com/user-attachments/assets/7d297bf3-3a43-445d-b61c-3079a477441e" />
<img width="1351" height="989" alt="Screenshot 2026-04-10 094146" src="https://github.com/user-attachments/assets/0350e39f-3df8-4978-9ca8-7bfdf4819cc1" />

<img width="1546" height="802" alt="image" src="https://github.com/user-attachments/assets/5d5903d2-217d-440c-8866-58f20fa1c077" />

Theo Wabwire 671398 - Data Cleaning and EDA
Lewis Wahome 671032 - Model and system development

How to Run
python model/train_model.py
streamlit run app/app.py

Lewis Wahome
