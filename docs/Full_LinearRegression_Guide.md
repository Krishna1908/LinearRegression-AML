Linear Regression — Algorithm 1 of 14 (IIT Kanpur AML)
This project demonstrates Linear Regression — a foundational supervised learning algorithm — as part of the Applied Machine Learning (AML) course from IIT Kanpur. It explains the intuition, real-world use, step-by-step math, training logic, and model evaluation in a clear and beginner-friendly format.
________________________________________
1. Definition
Linear Regression is a supervised learning algorithm used to model the relationship between a dependent variable (Y) and one or more independent variables (X) using a straight line.
 It is used to predict continuous numerical outcomes.
________________________________________
2. Why Do We Use It?
To predict continuous outcomes like:
•	 House prices based on area, location, and number of rooms.
•	Salary based on years of experience.
•	Sales forecasting based on advertising spend.
•   Health metrics like blood pressure based on age, weight.
________________________________________
 3. Real-World Analogy
Imagine you're a tailor. You charge ₹100 per meter of cloth.
•	1 meter → ₹100
•	2 meters → ₹200
•	3 meters → ₹300
You’ll notice a clear linear pattern:
"As the cloth length increases, the price increases proportionally."
So, for 4.5 meters → You can predict ₹450.
That’s Linear Regression in action!
________________________________________
 4. What is the Algorithm Trying to Predict?
Linear Regression tries to learn a mapping function from X to Y:
Y = mX + c
Example:
•	X = Hours studied
•	Y = Exam Score
•	Model might learn: Y = 10X + 5
Meaning:
•	Every additional hour studied increases marks by 10
•	Base score (intercept) is 5
________________________________________
5. How Does It Work? (Step-by-Step)
1.	You provide training data: known X and Y
2.	Model starts with random values of m and c
3.	Predicts: Y_pred = mX + c
4.	Calculates error using loss function (e.g., MSE)
5.	Uses Gradient Descent to adjust m and c
6.	Repeats steps 3–5 until error is minimized
________________________________________
6. Math Behind It (Formulas + Terms)
 Cost Function — Mean Squared Error (MSE)

MSE = (1/n) * Σ(Y_actual - Y_pred)^2
Where:
•	n = number of data points
•	Y_actual = real value
•	Y_pred = predicted value

Gradient Descent (to minimize MSE)
m = m - α * ∂(MSE)/∂m
c = c - α * ∂(MSE)/∂c
Where:
•	α = learning rate
•	∂ = partial derivative (gradient)
•	Repeats until slope of error → 0
________________________________________
 7. What is Training vs Prediction?
 Training:
You feed input-output data → Model learns best m and c
 Prediction:
You give new X → Model calculates Y = mX + c
Flow:
Training:
(X, Y) → Learn m, c → Model

Prediction:
New X → Predict Y using mX + c
________________________________________
8. What Do We Get After Training?
•	Final equation: Y = mX + c
•	A trained model that generalizes to new data
•	Evaluation metrics like:
o	R² Score
o	Mean Squared Error
o	Root Mean Squared Error (RMSE)
________________________________________
9. Purpose of Training
•	Find the best-fit line that minimizes error
•	Capture patterns from past data
•	Enable accurate prediction on unseen data
•	Quantify how features impact the output
________________________________________
10. What Can We Measure?
Metric	Description
MSE	Average of squared prediction errors
RMSE	Square root of MSE
R² Score	Measures how well the line fits the data
Coefficients	Slope values (impact of each feature on output)
________________________________________
11. Where Can We Use It in Real Life?
Domain	Use Case
Finance	Predicting stock prices
Health	Estimating patient vitals like BP/sugar
Marketing	Forecasting ad revenue
Education	Predicting student exam scores
Retail	Sales prediction based on pricing
________________________________________
 12. Summary: How Model Learns m and c
Give Input data (X and Y)
and Guess Start with random m, c post that it will
Predict	Compute Y = mX + c and 
Compare	Use loss function to check error and after that it will
Adjust	Apply gradient descent and finally
Repeat	Until loss is minimized
________________________________________
Quick Example
Given:
X = [1, 2, 3, 4]
Y = [50, 55, 65, 70]
1.	Model starts with: Y = X → Predicts Y = [1, 2, 3, 4]
2.	Loss is large → Adjust m and c
3.	After training: Y = 6.25X + 43.5 → Better predictions
________________________________________
Final Notes
•	Linear Regression is your go-to when predicting a quantity.
•	It forms the base for more advanced algorithms.
•	Always visualize your data and line to ensure proper fit.
________________________________________
🏆 Author
Krishna Teja Reddy Lingala
IIT Kanpur Certified | Applied Machine Learning


