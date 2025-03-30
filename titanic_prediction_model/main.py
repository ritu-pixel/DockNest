import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)

    # Convert categorical columns
    df['Sex'] = LabelEncoder().fit_transform(df['Sex'])
    df['Embarked'].fillna('S', inplace=True)
    df['Embarked'] = LabelEncoder().fit_transform(df['Embarked'])

    # Apply mean only to numeric columns
    df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)

    return df

data = load_data()

# Train model
X = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
y = data['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Streamlit UI
st.title("🚢 Titanic Survival Predictor")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ['Male', 'Female'])
age = st.slider("Age", 0, 100, 30)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard", 0, 10, 0)
fare = st.slider("Fare", 0, 500, 50)
embarked = st.selectbox("Port of Embarkation", ['S', 'C', 'Q'])

# Preprocess input data
sex = 0 if sex == 'Male' else 1
embarked = {'S': 2, 'C': 0, 'Q': 1}[embarked]

# Predict survival
if st.button("Predict"):
    input_data = [[pclass, sex, age, sibsp, parch, fare, embarked]]
    prediction = model.predict(input_data)
    result = "Survived" if prediction[0] == 1 else "Did not survive"
    st.success(f"The passenger would have: **{result}**")
