# Water Quality Checker
![GitHub repo size](https://img.shields.io/github/repo-size/kunal-mallick/Water-Quality?style=social)
![GitHub](https://img.shields.io/github/license/kunal-mallick/Water-Quality?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/kunal-mallick/Water-Quality?style=social)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/kunal-mallick/Water-Quality?style=social)

Water Quality Checker is a tool that can help you determine if the water you drink is safe and pure. It uses machine learning to analyze various parameters of water quality, such as pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity. You need to input these values in the form below and the model will predict whether the water is fit for consumption or not.

Water quality is essential for your health and well-being. According to the World Health Organization, more than two billion people use a drinking water source contaminated with feces. Contaminated water can cause diseases such as diarrhea, cholera, dysentery, typhoid, and polio. Therefore, it is important to test your water quality regularly and take appropriate measures to ensure its safety.

To use the Water Quality Checker, please fill in the following form with the values of the water parameters. You can use a home testing kit or a digital meter to measure these values. If you are not sure how to test your water quality at home, you can refer to this article for some simple ways.

| Parameter |
| --- |
| PH |
| Hardness |
| Solids |
| Chloramines |
| Sulfate |
| Conductivity |
| Organic Carbon |
| Trihalomethanes |
| Turbidity |

After filling in the form, click on the "Predict" button to see the result. The result will tell you if the water is "Safe" or "Unsafe" for drinking.

If you have any questions or feedback about the Water Quality Checker, please feel free to contact me at [email address]. I would love to hear from you and improve this tool for your convenience.
> Live demo [_here_](https://water-quality-checker.streamlit.app/)

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)


## General Information
- Water Quality Checker is a tool that can help you determine if your water is safe to drink or not.
- You need to enter the values of PH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_Carbon, Trihalomethanes, and Turbidity of your water sample.
- The model will analyze the data and predict if the water is potable or not.
- Below is a passage about water and its importance for human health and the environment.
- If you have any questions or feedback, please contact me using the form at the bottom of the page.

## Technologies Used
- Language Used : Jupyter Notebook(Python)

- libraries used
    - Data Preprocessing & EDA :numpy, pandas, matplotlib, seaborn, plotly, sklearn.ensemble(IsolationForest)
    - Feature Engineering & Feature Extraction : sklearn.preprocessing(StandardScaler), sklearn.model_selection(train_test_split)
    - Model Building : pickle, sklearn.linear_model(LogisticRegression), sklearn.neighbors(KNeighborsClassifier), sklearn.tree(DecisionTreeClassifier), sklearn.ensemble(AdaBoostClassifier,RandomForestClassifier,GradientBoostingClassifier,VotingClassifier,StackingClassifier, BaggingClassifier), sklearn.svm(SVC), sklearn.model_selection(GridSearchCV), sklearn.metrics(classification_report)
    - Deployment : pickle, pandas, streamlit, sklearn.preprocessing(StandardScaler)
    - Server Deployment : https://share.streamlit.io/


## Screenshots
![Top](https://raw.githubusercontent.com/kunal-mallick/Water-Quality/main/img/top.png)
![mid](https://raw.githubusercontent.com/kunal-mallick/Water-Quality/main/img/mid.png)
![bottom](https://raw.githubusercontent.com/kunal-mallick/Water-Quality/main/img/bottom.png)


## Setup
- For Online [click here](https://water-quality-checker.streamlit.app/)

- For Offline download everything in requirements.txt and then open the anaconda / python terminal and run this line of code :
 
```bash
cd file path
```
```bash
streamlit run main.py
```


## Usage
- Collect a sample of water from the source you want to test. Make sure the sample is clear and free of any visible particles or debris.
- Use a testing kit or a device to measure the values of the parameters mentioned above. You can find these kits or devices online or in local stores. Follow the instructions carefully and record the results.
- Input the values into the water quality checker function on this page. The function will run the machine learning model and give you a prediction of whether the water is safe to drink or not.
- If the prediction is potable, you can use the water for drinking or other purposes. If the prediction is non-potable, you should avoid using the water or treat it with a suitable method such as boiling, filtering, chlorinating, or distilling.


## Project Status
Project is: complete

## Room for Improvement

Room for improvement:
- Improving Model Performance
- Improving UI 


## Acknowledgements
- This project was based on [kaggle(Water Quality)](https://www.kaggle.com/datasets/adityakadiwal/water-potability).
- Many thanks to
    - [w3schools](https://www.w3schools.com/)
    - [geeksforgeeks](https://www.geeksforgeeks.org/)
    - [coolors](https://coolors.co/palettes/trending/rainbow)
    - [figma](https://www.figma.com/)


## Contact
Created by [@kunal](https://github.com/kunal-mallick) - feel free to contact me!


<!-- Optional -->
## License
This project is open source and available under the [MIT License](https://github.com/kunal-mallick/Water-Quality/blob/main/LICENSE).

<!-- You don't have to include all sections - just the one's relevant to your project -->
