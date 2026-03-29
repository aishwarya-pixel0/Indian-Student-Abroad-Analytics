#importing necessary libraries
import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import json

#loading datasets
country_data = pd.read_csv("data/country wise(18-22).csv")
state_data = pd.read_csv("data/state wise(16-21).csv")
incident_data = pd.read_csv("data/Incidents encountered.csv")

#creating dataframes
country_df = pd.DataFrame(country_data)
state_df = pd.DataFrame(state_data)
incident_df = pd.DataFrame(incident_data)

country_df.drop(columns = 'Sl. No.',inplace=True)
state_df.drop(columns = 'Sl. No.',inplace = True)
incident_df.drop(columns = 'Sl. No',inplace = True)
state_df.rename(columns={'201 6': '2016'}, inplace=True)
state_df.rename(columns={'State (as Per the Place (RPO) of Issuance of Passport)': 'State'}, inplace=True)
state_df.rename(columns={'2021 (Till 28.02.2021)': '2021'}, inplace=True)
#sidebar
st.sidebar.title("Navigation")
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
options = ['Overview','Country Analysis','State Analysis','Incident Analysis']
page = st.sidebar.radio("Go to : ",options)




if page=="Overview":
    #overview - layout
    st.title("Study Abroad Analytics : Indian Students Dashboard")
    st.write("This project showcases analytics regarding Indian Students studying abroad and highlights the risk and oppurtonities.\n"
             "It explores Indian student migration across countries highlighting preferable destinations for higher education through the country dataset,"
             "and highlights the risks/incidents encountered in various countries through the incidents dataset.\n\n"
             "By this dashboard, I try to provide a comprehensive view of the opportunities and risks associated with studying abroad and "
             "hence helping prospective students make well informed decisions.")
    st.divider()
    #providing KPI's
    years = ['2018', '2019', '2020', '2021', '2022']
    total_students = int(country_df[years].sum().sum())
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Total Indian students abroad : ",value=f"{total_students:,}")
    with col2:
        st.metric(label="Top Destination : ",value="USA",delta="29.4% share")
    with col3:
        st.metric(label="Top Sending State",value="Andhra Pradesh")
    with col4:
        st.metric(label="Highest Incidents",value="Canada",
                  delta="91 incidents",
        delta_color="inverse" )
    st.divider()


    st.subheader("Country Wise Student Dataset")
    with st.expander("Show Country dataset"):
        st.write(country_df)
    st.info("This dataset holds information regarding the number of Indian Students who have gone abroad to "
            "pursue higher education across the globe in the years 2018 - 2022.\n\n"
            "It helps identify global education trends and the most preferred destinations abroad.")
    st.divider()

    st.subheader("State Wise Student Dataset")
    with st.expander("Show State dataset"):
        st.write(state_df)
    st.info("This dataset holds information regarding the state-wise distribution of Indian Students who have gone abroad to "
            "pursue higher education across the globe in the years 2016 - 2021.\n\n "
            "It highlights regional patterns and identifies which states contribute the most to international student mobility, or as I would like to say \n\n"
            "**<The Indian Students Exodus>**.")
    st.divider()

    st.subheader("Incidents Dataset")
    with st.expander("Show Incident dataset"):
        st.write(incident_df)
    st.info("This dataset holds information regarding the number of incidents encountered by Indian students studying "
            "abroad categorised by Country.\n\n"
            "It provides insights into safety concerns and helps assess potential risks associated with different destinations abroad.")
    st.divider()

elif page=="Country Analysis":

    years = ['2018', '2019', '2020', '2021', '2022']
    country_df['Total'] = country_df[years].sum(axis=1)
    vis_option = st.radio("Select Visualization : ",['Choropleth Map','Animated Bar Chart',
                               'Multi Country Line Chart','Pie Chart','Tree Map'])
    melted_country_df = pd.melt(country_df, id_vars=['Country'], value_vars=years, var_name='Years',
                                value_name='Number of Students')

    top10_country = country_df.sort_values(by='Total', ascending=False).head(10)
    #Choropleth
    if vis_option=="Choropleth Map":
        fig1 = px.choropleth(country_df,locations="Country",locationmode="country names",
                                    color="Total",color_continuous_scale="reds",labels={"Total":"Number of Students"},
                                    range_color=(0,country_df['Total'].quantile(0.85)),hover_name='Country',hover_data={'Total':True},title="Indian Students studying abroad")
        fig1.update_traces(
                    hovertemplate="<b>%{hovertext}</b><br>Students: %{z}<extra></extra>"
                )
        fig1.update_layout(title="Student distribution country wise",width=800,height=600)
        st.plotly_chart(fig1)
        st.divider()

        #Analysis
        st.caption("The Choropleth map shows the hotspot regions chosen by Indian Students as a mode for higher studies.")
        st.info("Some key observations include : ")
        st.info("1. The regions of North America, Europe and Russia constitute a major proportion of "
                "Indian Student population, with USA, Canada, UK and Australia forming the 'Big 4' destinations "
                "for higher studies abroad.\n"
                "These areas provide quality education, better research opportunities, strong job markets "
                "which act as secondary factors."
                "")
        st.info("2. The regions of Middle East (UAE, Saudi Arabia) and South East Asia (Singapore,Malaysia) "
                "show moderate proportion of Indian Student population.\n"
                "These areas showcase **proximity** to India which ensures easy travel for students, and "
                "the low cost **affordability** of living and education act as key factors. ")
        st.divider()

    #Animated Bar Chart

    elif vis_option=="Animated Bar Chart":

        df_top10 = melted_country_df[melted_country_df['Country'].isin(top10_country['Country'])]
        fig2 = px.bar(df_top10,x="Number of Students",y="Country",animation_frame="Years",animation_group='Country',
                          hover_name='Country')
        fig2.update_layout(title="Animated Bar Chart")
        st.plotly_chart(fig2,use_container_width=True)
        st.divider()

        #Analysis
        st.caption(
            "The Animated Bar Chart shows the trend of the Top10 countries over a timeline of 5 years.")
        st.divider()
        st.success("Some key observations include : ")
        with st.container():
            st.info("1. The regions of USA and Canada showcase a continuous trend of being the top destinations"
                            " chosen by Indian students for higher education.\n\n"
                            "")
            st.error("In the year 2020, these regions saw a sudden drop and the plausible cause for this "
                     "includes the COVID-19 pandemic and uncertain Visa approval during the Trump era. ")
        with st.container():
            st.info("2. UK has seen a **moderate** increase in the Indian student population when compared to USA, Canada and Australia.\n"
            " ")
            st.success("UK saw a drastic **increase** in the number of Indian Students (around 8k) during the COVID-19 pandemic "
                   "while other countries saw a major drop.\n\n "
                   "The plausible causes for this include the introduction of the **Graduation Route**,"
                   " which allows students to stay and work in the UK for 2 years.\n\n"
                   "This has attracted the Indian Student community as a long term career investment"
                   " for pursuing higher education during tough times as the pandemic. "
                   " ")
            img1 = Image.open("images/1.png")
            img2 = Image.open("images/2.png")
            with st.container():
                col1, col2 = st.columns(2, gap="large")
                with col1:
                    st.image(img1,caption="Excerpts from Indian Express",use_container_width=True )
                with col2:
                    st.image(img2,use_container_width=True)
        st.error("3. Ukraine saw a drastic drop of Indian student population in the year 2022, primarily"
                 " due to the **Russian invasion of Ukraine**, which began on February 24, 2022.\n\n "
                 "This conflict created an unsafe environment, forcing the mass evacuation of around "
                 "20,000 Indian citizens the majority being medical students through **Operation Ganga**.")
        img3 = Image.open("images/3.png")
        st.image(img3,caption="When the Ukraine war broke out, "
                              "India swiftly launched 'Operation Ganga' to evacuate thousands of its citizens")
        st.divider()
        #Line Chart(Multi Country)
    elif vis_option=="Multi Country Line Chart":
        selected_country = st.selectbox("Select Countries ",options = top10_country['Country'])
        filtered_df = melted_country_df[melted_country_df['Country']==selected_country]
        df_top10 = melted_country_df[melted_country_df['Country'].isin(top10_country['Country'])]
        fig3 = px.line(filtered_df,x='Years',y='Number of Students',color='Country',
                           title = f"{selected_country} - Student Trend over the years")
        fig3.update_xaxes(type='category')
        st.plotly_chart(fig3)
        st.divider()
        #color_discrete_sequence = px.colors.qualitative.Pastel
        st.caption("The line chart shows the year-on-year trend for a selected country.")
        st.divider()
        st.info("Some key observations include :  ")
        st.error("1. **Australia** experienced a significant drop in Indian student visa approvals around 2022 due to a, "
                 "deliberate crackdown on visa fraud and **non-genuine** applicants,"
                " with India being placed in the highest-risk assessment category.\n\n"
                 "Several Australian universities in Victoria and New South Wales (NSW) banned recruitment from "
                 "specific Indian states due to concerns over visa fraud.")
        st.error("2. The drastic drop in Indian students in **Kyrgyzstan**, particularly around 2022, was driven primarily "
                 "by severe safety concerns stemming from mob violence against foreign students, "
                 "widespread social media hate campaigns, and subsequent fears for security.\n\n"
                 " Regional issues, such as the 2022 border conflict between Kyrgyzstan and Tajikistan, "
                 "also contributed to a less stable perception of the country.")
        img4 = Image.open("images/4.png")
        img5 = Image.open("images/5.png")
        with st.container():
            col1, col2 = st.columns(2, gap="large")
            with col1:
                st.image(img4,use_container_width=True)
            with col2:
                st.image(img5,caption = "Excerpt from India Today",width=400)
        st.divider()
    elif vis_option=="Pie Chart":
        fig4 = px.pie(top10_country,names='Country',values='Total',
                      )
        fig4.update_traces(textposition="inside",textinfo = 'label+percent')
        fig4.update_layout(title="Top 10 countries by student distribution",width=800,height=600)
        st.plotly_chart(fig4)
        st.divider()
        st.info("The pie chart highlights the concentration of Indian student preference.  "
                    " USA and Canada together account for over 56% of the top 10 share.\n\n "
                    "This dominance points to factors like QS-ranked universities, post-study "
                    "work visa opportunities, and established Indian diaspora networks. \n\nThe "
                    "remaining 44% is spread across 8 countries, showing a long-tail distribution.")
        st.divider()
    elif vis_option=="Tree Map":
        fig5 = px.treemap(top10_country,path=['Country'],values='Total',
                          title='Top 10 countries by student distribution')
        fig5.update_traces(root_color="white")
        st.plotly_chart(fig5)
        st.divider()
        st.info("The treemap provides an at a glance proportional view of the top 10 "
                "destinations. \n\nThe USA's tile dwarfs the others, visually reinforcing it's " 
                "status as the primary choice. \n\nSmaller tiles for Germany and Singapore hint "
                "at emerging preferences for non-English, affordable, high-quality education "
                "systems.")
        st.divider()

elif page=="State Analysis":
    years = ['2016', '2017', '2018', '2019', '2020', '2021']
    state_df = state_df[~state_df['State'].isin(['Total', 'Passport Issued from Indian Mission Abroad'])]
    state_df['Total'] = state_df[years].sum(axis=1)
    option = ['Choropleth Map','Bar Chart']
    vis_option =  st.radio("Select Visualization : " , option)
    #load json file
    with open("Indian_States.json") as f:
         india_geo = json.load(f)
    if vis_option=="Choropleth Map":
        fig1 = px.choropleth(state_df,geojson=india_geo,featureidkey="properties.NAME_1",locations='State',
                              color='Total', color_continuous_scale="YlOrRd",range_color=(0, state_df['Total'].quantile(0.75)),
                             title="State wise students going abroad")
        #lower percentile the more the contrast it gives - 0.85
        fig1.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig1,use_container_width=True)
        st.divider()

        #Analysis
        st.info("Some key observations include : ")
        st.info("1. Southern Indian states marked in blood red including Andhra Pradesh, Telangana, Karnataka, Kerala and Tamil Nadu "
                "are hotspots for major Indian student outflow abroad. ")
        st.success("This indicates that Southern Indian states benefit from wider availability of "
                   " **education loans, scholarships, and family support**, enabling more students to pursue higher education overseas. ")
        st.success("a) **Access to Loans**: There is better access to formal banking credit and education loans for international study in these regions. \n\n"
                   "b) **Disposable Income & Investment** : Families in southern states often have higher disposable incomes "
                    "and are more likely to treat education debt as a long-term investment.\n\n"
                   "c) **Role of Gender Dynamics** : In Kerala specifically, international migration is seen as a way for "
                   "female students to escape restrictive traditional social norms,"
                   "leading to a high outflow of female students. ")

        st.info("2. The states of Punjab, Gujarat, Maharashtra and the capital Delhi also  showcase "
                "high proportions in the outflow of students due to strong cultural migration, high aspiration, and localized counseling ecosystems, "
                "despite lower traditional bank loan access.  ")
        st.warning("Punjab, historically known as the '**Granary of India**' due to its agricultural output, "
                   "faces economic challenges like reduced agricultural returns and limited employment, "
                   "prompting a trend of youth migration in search of educational and economic opportunities abroad.")
        st.info("3. Low outflow of Indian students in North-Eastern states")
        st.error(" a) This indicates that most north-east states have low per capita income, and "
                 "lack of awareness about foreign opportunities. \n\n"
                 " b) **Internal Migration** : In these states, students often migrate to metropolitan states like Delhi, Bengaluru, Mumbai"
                 " for higher education making these alternatives instead of studying abroad.")
        st.divider()

    elif vis_option=="Bar Chart":
        top10_states = state_df.sort_values(by='Total',ascending=False).head(10)
        melted_state_df = pd.melt(top10_states,id_vars = ['State'],value_vars=years,var_name='Year',
                                  value_name='Students')
        fig2 = px.bar(melted_state_df,x='State',y='Students',color='Year',
                      title='State wise outflow of Indian Students abroad',
                      barmode='group',color_discrete_sequence=px.colors.qualitative.Plotly)

        fig2.update_layout(xaxis_tickangle=45)
        st.plotly_chart(fig2)
        st.divider()

        #   Analysis
        st.success("Some key observations include : ")
        st.info("1. Over the years Andhra Pradesh stands highest in the number of outflow of Indian students abroad." )
        st.success("This indicates the following : \n\n"
                   "a) **Robust financial support** through loans and access to education loans, "
                   "viewing higher education abroad as a long term investment rather than a liability.\n\n"
                   "b) **Rich Educational ecosystem** which focuses on early exposure to STEM degrees and strong test prep centers,"
                   " counselling areas. \n\n"
                   "c) **Strong Diaspora Network** plays a crucial role where students follow family members or community "
                   " who have already settled abroad. Hence, reducing the perceived risk of navigation and following a structured path ahead.")

        st.info("Growing Trend seen in Uttar Pradesh and Chandigarh. ")
        st.success("Chandigarh boasts one of the highest per capita income despite low total numbers"
                   " indicating strong financial support systems, enhanced culture of education and opportunities "
                   "of international institutions for employment pipelines")
        st.error("Uttar Pradesh has a moderate per capita income even though its large population.\n\n"
                 "This indicates that while aspirations are growing, the state is still developing "
                 "the high-end private education access and income levels seen in leading states.")
        st.divider()

elif page=="Incident Analysis":
    options = ['Choropleth Map','Bubble Chart']
    vis_options = st.radio("Select Visualization : ",options)
    if vis_options=='Choropleth Map':
        fig1 = px.choropleth(incident_df,locations = "Country",locationmode="country names",color="Number of Incidents",
                             color_continuous_scale="reds",labels={"Number of Incidents":"Incidents"},range_color=(0,incident_df['Number of Incidents'].quantile(0.95)),
                             hover_name='Country',hover_data={'Number of Incidents':True},title="Incidents encountered by Indian students studying abroad")
        st.plotly_chart(fig1,use_container_width=True)
        st.divider()
        #Analysis
        st.info("Some key observations include : ")
        st.error("1. Canada (highlighted in dark red)"
                 " has the highest density of incidents when compared to other countries.\n\n"
                 "This plausible cause for this includes the accusations made by Canada regarding India's alleged involvement"
                 " in the June 2023 killing of Sikh activist **Hardeep Singh Nijjar**, who was running a Sikh terrorist camp"
                 " and seeking an independent Sikh State under the **Khalistan Movement**. \n\n"
                 "It has led to the deterioration of the diplomatic ties between India and Canada.\n\n"
                 "Other reasons include financial struggles, fraudulent agents and documents and targeted crime.")

        st.warning("2. The regions of USA, Russia and Australia show a moderate incident rate, but given the massive "
                   "Indian student population, this can be controlled.\n\n"
                   "But, still Indian students need to stay cautious about these countries despite its reputation"
                   " as a welcoming destination for higher studies.")
        img6 = Image.open("images/6.png")
        img7 = Image.open("images/7.png")
        with st.container():
            col1, col2 = st.columns(2, gap="large")
            with col1:
                st.image(img6, caption="Excerpt from NBC News", use_container_width=True)
            with col2:
                st.image(img7, caption="International "
                                       "Indian Students In Canadian Province Face Deportation", width="stretch")
        st.divider()

    elif vis_options=="Bubble Chart":
        years = ['2018', '2019', '2020', '2021', '2022']
        country_df['Total'] = country_df[years].sum(axis=1)
        #merge datasets country and incident
        merged_df = pd.merge(
            country_df[['Country', 'Total']],
            incident_df[['Country', 'Number of Incidents']],
            on='Country',
            how='inner'
        )
        merged_df['bubble_size'] = ((merged_df['Number of Incidents'] - merged_df['Number of Incidents'].min()) /
                                    (merged_df['Number of Incidents'].max() - merged_df[
                                        'Number of Incidents'].min())) * 100 + 10

        merged_df['Risk Ratio'] = (merged_df['Number of Incidents'] / merged_df['Total']) * 1000

        risk_threshold = merged_df['Risk Ratio'].mean()
        population_threshold = merged_df['Total'].quantile(0.60)

        #countries having higher risk ratio
        outliers = merged_df[(merged_df['Risk Ratio']>risk_threshold)&(merged_df['Total']<population_threshold)]
        #checking for countries having high risk ratio
        # print(outliers[['Country', 'Total', 'Number of Incidents', 'Risk Ratio']].sort_values('Risk Ratio',
        #                                                                                       ascending=False))
        fig2 = px.scatter(
            merged_df,
            x='Total',
            y='Number of Incidents',
            size='bubble_size',
            color='Country',
            hover_name='Country',
            hover_data={
                'Risk Ratio': ':.2f',
                'bubble_size': False,
                'Total': True,
                'Number of Incidents': True
            },
            color_discrete_sequence=px.colors.qualitative.Plotly,
            size_max=60,
            title='Student Volume vs Incidents (Is a popular country risky?)'
        )


        for _,row in outliers.iterrows():
            fig2.add_annotation(x=row['Total'],y=row['Number of Incidents'],text=f"🚨 {row['Country']}",
            arrowhead=2,arrowcolor="red",arrowsize=1.5,ax=50,ay=-40, font=dict(
            color="red",
            size=11,
            family="Arial"
        ),
        bgcolor="rgba(255,0,0,0.15)",
        bordercolor="red",
        borderwidth=1,
        borderpad=4
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.divider()
        #Analysis
        st.info("Some key observations include : ")
        st.warning("1. **Canada** is the clear outlier with a large orange bubble. It has the highest population and the "
                 "highest number of incidents.\n\n"
                   "But, high student volume is not always equal to high risk, **Australia** denoted by the blue bubble "
                   "has nearly 240k population of Indian students but has encountered only about 35 incidents.\n\n"
                   "**This suggests that student volume alone cannot predict the incident rate**.")
        st.error("2. **Suriname** stands the highest in the risk ratio with where around 3 incidents are encountered "
                 "per 1000 students, thus making its risk ratio the highest.\n\n"
                 "Hence, prospective students should take utmost caution while considering **Suriname** as their"
                 " educational destination.")
        st.warning("3. Other countries which have clustered near 0 indicate that most of them have lower population, "
                   "and low incident rate indicating a negligible risk ratio.\n\n"
                   "Hence, these countries aren't much popular study destinations among students.")
        st.divider()

