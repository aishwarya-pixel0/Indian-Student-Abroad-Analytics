# Study Abroad Analytics : Indian Student Dashboard

## Live Dashboard
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://indian-student-abroad-analytics.streamlit.app/)

## Project Overview
- A Streamlit dashboard which showcases the Indian student outflow trend across various countries in the span of 5 years, (2018 - 2022).

- It also displays the **State wise and Country wise** Indian student outflow numbers, providing key insights into the popular destinations chosen by Indian students to
pursue higher education and on the state's socio-economic condition.

- Furthermore, the dashboard aims to provide **Incident analysis** which describes the incidents encountered by Indian students in various countries across the globe.

This, can help prospective students in considering countries to study abroad.

## Datasets
- Country wise student data (2018-2022) - Consists of the Indian student outflow numbers in various countries.
- State wise student data (2016-2021)  - Consists of the State-wise numbers of Indian student outflow.
- Incidents encountered abroad - Consists of the number of incidents encountered by Indian students in various countries abroad. 

## Dataset Sources
Datasets retrieved from [Open Government Data Platform India](https://www.data.gov.in/keywords/Abroad) 


## Project Structure
```
Indian-Student-Abroad-Analytics/
├── data/
├── images/
├── Indian_States.json
├── streamlit_dashboard.py
└── requirements.txt
```
## Dashboard Modules

| Module (Page) | Core Content | Interactive Features |
|---|---|---|
| **Overview** | Project background, objectives, dataset descriptions, KPI metrics (total students, top destination, top sending state, highest incidents) | Expandable dataset previews |
| **Country Analysis** | World choropleth map of student destinations, animated bar chart (2018-2022), multi-country trend line chart, pie chart and treemap of top 10 countries | Visualization selector, country dropdown, year-wise animation slider |
| **State Analysis** | India state choropleth map showing student outflow by state (financial capability proxy), grouped bar chart of top 10 states by year | Visualization selector, hover tooltips |
| **Incident Analysis** | World choropleth map of incidents encountered, bubble chart comparing student volume vs incidents with risk ratio encoding | Visualization selector, hover tooltips with risk ratio, annotated high-risk country flags |

## Data Visualization Techniques
- Choropleth Map
- Line Chart
- Bar Chart
- Scatter Plots / Bubble Charts
- Tree Map
- Pie Chart

## Beyond the Data , What Might Change?
> *Note: The following observations extend beyond the dataset (2018-2022) 
> and reflect current geopolitical and policy developments.*

While the dataset captures trends from 2018-2022, several recent developments 
suggest that the landscape of Indian student migration is shifting significantly.

- **USA**
  
  Despite being the top destination in this dataset, I believe the USA's 
dominance may decline post 2025 due to the *Trump era*.

  The Trump administration's tariff policies, 
  stricter visa regulations and growing anti-immigration sentiment are likely to 
  discourage Indian students from choosing the USA, potentially redirecting them 
  towards *Germany, Ireland and the UK* as alternative destinations.

- **Canada**
  
  Although Canada ranks as the second most preferred destination in 
this dataset, it introduced a cap on international student permits in 2024, 
directly affecting Indian students who form the largest international student 
group in the country. This policy shift is likely to reflect a noticeable *dip* 
in future datasets.

- **Australia**
  
   The sharp drop in Indian students visible in the 2022 line chart 
is not an anomaly. Australia tightened its visa policies post-2023 by placing 
India in the **highest visa risk category**, leading to mass rejections from specific 
Indian states. This trend is likely to continue *reducing* Australia's share in 
the coming years.

- **Germany**
  
  While Germany appears as a smaller tile in the treemap today, I 
believe it is the most significant *emerging destination* for Indian students. 
Its tuition-free public universities, growing number of English taught programs 
and strong post-study work opportunities make it an increasingly attractive 
alternative to the expensive English speaking destinations.

- **UK**
  
  The UK's **Graduate Route visa** introduced in 2021 is clearly visible as 
an upward spike in the animated bar chart. However, ongoing political debates 
about scrapping this route may reverse the gains seen in 2021-2022, making 
the UK's future position *uncertain*.


## How to Run
To run the project, follow these steps:
1. Ensure that you have Python installed on your system.
2. Install the required libraries by running the command: `pip install -r requirements.txt`.
3. Run the script using the command: `streamlit run streamlit_dashboard.py`.
4. Access the visualization interface through the provided URL.

