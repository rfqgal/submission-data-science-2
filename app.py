import streamlit as st
import pandas as pd
import joblib
import sklearn

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

def categorical_input(label, options, help_text=""):
    return st.selectbox(label, options, help=help_text)

marital_statuses = ['Single', 'Married', 'Widower', 'Divorced', 'Facto union', 'Legally separated']
application_modes = [
    '1 - 1st phase - general contingent',
    '2 - Ordinance No. 612/93',
    '5 - 1st phase - special contingent (Azores Island)',
    '7 - Holders of other higher courses',
    '10 - Ordinance No. 854-B/99',
    '15 - International student (bachelor)',
    '16 - 1st phase - special contingent (Madeira Island)',
    '17 - 2nd phase - general contingent',
    '18 - 3rd phase - general contingent',
    '26 - Ordinance No. 533-A/99, item b2) (Different Plan)',
    '27 - Ordinance No. 533-A/99, item b3 (Other Institution)',
    '39 - Over 23 years old',
    '43 - Change of course',
    '44 - Technological specialization diploma holders',
    '51 - Change of institution/course',
    '53 - Short cycle diploma holders',
    '57 - Change of institution/course (International)',
]
courses = [
    '33 - Biofuel Production Technologies',
    '171 - Animation and Multimedia Design',
    '8014 - Social Service (evening attendance)',
    '9003 - Agronomy',
    '9070 - Communication Design',
    '9085 - Veterinary Nursing',
    '9119 - Informatics Engineering',
    '9130 - Equinculture',
    '9147 - Management',
    '9238 - Social Service',
    '9254 - Tourism',
    '9500 - Nursing',
    '9556 - Oral Hygiene',
    '9670 - Advertising and Marketing Management',
    '9773 - Journalism and Communication',
    '9853 - Basic Education',
    '9991 - Management (evening attendance)',
]
attendances = ['Daytime', 'Evening']
parent_qualifications = [
    "1 - Secondary Education - 12th Year of Schooling or Equivalent",
    "2 - Higher Education - Bachelor's Degree",
    "3 - Higher Education - Degree",
    "4 - Higher Education - Master's",
    "5 - Higher Education - Doctorate",
    "6 - Frequency of Higher Education",
    "9 - 12th Year of Schooling - Not Completed",
    "10 - 11th Year of Schooling - Not Completed",
    "11 - 7th Year (Old)",
    "12 - Other - 11th Year of Schooling",
    "14 - 10th Year of Schooling",
    "18 - General Commerce Course",
    "19 - Basic Education 3rd Cycle (9th/10th/11th Year) or Equivalent",
    "22 - Technical-Professional Course",
    "26 - 7th Year of Schooling",
    "27 - 2nd Cycle of the General High School Course",
    "29 - 9th Year of Schooling - Not Completed",
    "30 - 8th Year of Schooling",
    "34 - Unknown",
    "35 - Can't Read or Write",
    "36 - Can Read Without Having a 4th Year of Schooling",
    "37 - Basic Education 1st Cycle (4th/5th Year) or Equivalent",
    "38 - Basic Education 2nd Cycle (6th/7th/8th Year) or Equivalent",
    "39 - Technological Specialization Course",
    "40 - Higher Education - Degree (1st Cycle)",
    "41 - Specialized Higher Studies Course",
    "42 - Professional Higher Technical Course",
    "43 - Higher Education - Master (2nd Cycle)",
    "44 - Higher Education - Doctorate (3rd Cycle)",
]
fathers_occupations = [
    '0 - Student',
    '1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
    '2 - Specialists in Intellectual and Scientific Activities',
    '3 - Intermediate Level Technicians and Professions',
    '4 - Administrative staff',
    '5 - Personal Services, Security and Safety Workers and Sellers',
    '6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
    '7 - Skilled Workers in Industry, Construction and Craftsmen',
    '8 - Installation and Machine Operators and Assembly Workers',
    '9 - Unskilled Workers',
    '10 - Armed Forces Professions',
    '90 - Other Situation',
    '99 - (blank)',
    '101 - Armed Forces Officers',
    '102 - Armed Forces Sergeants',
    '103 - Other Armed Forces personnel',
    '112 - Directors of administrative and commercial services',
    '114 - Hotel, catering, trade and other services directors',
    '121 - Specialists in the physical sciences, mathematics, engineering and related techniques',
    '122 - Health professionals',
    '123 - teachers',
    '124 - Specialists in finance, accounting, administrative organization, public and commercial relations',
    '131 - Intermediate level science and engineering technicians and professions',
    '132 - Technicians and professionals, of intermediate level of health',
    '134 - Intermediate level technicians from legal, social, sports, cultural and similar services',
    '135 - Information and communication technology technicians',
    '141 - Office workers, secretaries in general and data processing operators',
    '143 - Data, accounting, statistical, financial services and registry-related operators',
    '144 - Other administrative support staff',
    '151 - personal service workers',
    '152 - sellers',
    '153 - Personal care workers and the like',
    '154 - Protection and security services personnel',
    '161 - Market-oriented farmers and skilled agricultural and animal production workers',
    '163 - Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence',
    '171 - Skilled construction workers and the like, except electricians',
    '172 - Skilled workers in metallurgy, metalworking and similar',
    '174 - Skilled workers in electricity and electronics',
    '175 - Workers in food processing, woodworking, clothing and other industries and crafts',
    '181 - Fixed plant and machine operators',
    '182 - assembly workers',
    '183 - Vehicle drivers and mobile equipment operators',
    '192 - Unskilled workers in agriculture, animal production, fisheries and forestry',
    '193 - Unskilled workers in extractive industry, construction, manufacturing and transport',
    '194 - Meal preparation assistants',
    '195 - Street vendors (except food) and street service providers',
]
mothers_occupation_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 122, 123, 125, 131, 132, 134, 141, 143, 144, 151, 152, 153, 171, 173, 175, 191, 192, 193, 194]
mothers_occupations = [occupation for occupation in fathers_occupations if int(occupation.split(' - ')[0]) in mothers_occupation_ids]
yesOrNo = ['Yes', 'No']
genders = ['Male', 'Female']

st.title("🎓Student Dropout Prediction")

st.write("Fill out this form to predict probability student dropout")

with st.form('student_form'):
    st.header("📋 Student Information")
    marital_status = categorical_input("Marital Status", marital_statuses,
                                       "The marital status of the student.")
    application_mode = categorical_input("Application Mode", application_modes,
                                         "Method of application used by the student.")
    course = categorical_input("Code Course Taken By Student", courses,
                               "The course taken by the student.")
    attendance = categorical_input("Time Attendance", attendances,
                                   "Whether the student attends classes during the day or in the evening.")
    mothers_qualification = categorical_input("Mother Qualification", parent_qualifications,
                                              "The qualification of the student's mother.")
    fathers_qualification = categorical_input("Father Qualification", parent_qualifications,
                                              "The qualification of the student's father.")
    mothers_occupation = categorical_input('Mother Occupation', mothers_occupations,
                                           "The occupation of the student's mother.")
    fathers_occupation = categorical_input("Father Occupation", fathers_occupations,
                                           "The occupation of the student's father.")
    displaced = categorical_input("Displace", yesOrNo,
                                  "Is a displaced student?")
    debtor = categorical_input("Debtor", yesOrNo,
                               "Is student debt tuition?")
    tuition_paid = categorical_input("Tuition fees up to date", yesOrNo,
                                     "Did student's tuition fees up to date?")
    gender = categorical_input("Gender", genders,
                               "Gender of Student")
    scholarship = categorical_input("Scholarship Holder", yesOrNo,
                                    "Is the student scholarship holder/awardee?")
    prev_grade = st.number_input("Grade of previous qualification", min_value=0.0, max_value=200.0, value=14.0)
    admission_grade = st.number_input("Admission grade", min_value=0.0, max_value=200.0, value=13.0)
    age = st.number_input("Age at enrollment", min_value=15, max_value=80, value=18)
    enrolled_1st = st.number_input("Number of curricular units enrolled by the student in the first semester.",
                                   min_value=0, value=6)
    enrolled_2nd = st.number_input("Number of curricular units enrolled by the student in the second semester.",
                                   min_value=0, value=6)
    unemployment = st.number_input("Unemployement Rate (%)", min_value=0.0, max_value=100.0, value=8.0)
    inflation = st.number_input("Inflation Rate (%)", min_value=0.0, max_value=100.0, value=2.0)
    gdp = st.number_input("GDP", min_value=0.0, value=0.79)

    submitted = st.form_submit_button("Prediksi")

# Prediksi
if submitted:
    student_form = pd.DataFrame([{
        'Marital_status': marital_status,
        'Application_mode': application_mode.split(' - ')[0],
        'Course': course.split(' - ')[0],
        'Daytime_evening_attendance': attendance,
        'Mothers_qualification': mothers_qualification.split(' - ')[0],
        'Fathers_qualification': fathers_qualification.split(' - ')[0],
        'Mothers_occupation': mothers_occupation.split(' - ')[0],
        'Fathers_occupation': fathers_occupation.split(' - ')[0],
        'Displaced': displaced,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_paid,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Previous_qualification_grade': prev_grade,
        'Admission_grade': admission_grade,
        'Age_at_enrollment': age,
        'Curricular_units_1st_sem_enrolled': enrolled_1st,
        'Curricular_units_2nd_sem_enrolled': enrolled_2nd,
        'Unemployment_rate': unemployment,
        'Inflation_rate': inflation,
        'GDP': gdp
    }])

    prediction = model.predict(student_form)[0]
    probability = model.predict_proba(student_form)[0][1]

    prediction_label = "🔴 Dropout" if prediction == 1 else "🟢 No Dropout"
    if probability > 0.5:
        st.warning("⚠️ High risk of Dropout")
    else:
        st.info("✅ Likely to Stay")

    st.success(f"Result: {prediction_label}")
    st.write(f"**Probability of Dropout:** {probability:.2%}")
