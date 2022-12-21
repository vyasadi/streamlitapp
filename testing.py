
import streamlit as st
import pandas as pd




header=st.container()
dataset=st.container()

with header:
    st.title('Welcome to this marketing dashboard')
    st.markdown('Let us help you observe insights')

with dataset:
    st.header('Please choose the options below to get your desired result')
    data = pd.read_csv("samplepython.csv",skipfooter=2,engine="python")
    #selection=st.columns(1)
    a=st.selectbox('How many rows you want to see', options=[5,6,7],index=0)
    b=st.text_input('How do yo want to group by','Date')
    c=st.slider('What impression threshold you want',min_value=200000,max_value=700000,value=300000,step=10000)
    datanew = data.groupby(b)['Impressions'].sum()
    datanew = datanew.to_frame(name="TotalImpressions")
    datanew=datanew[datanew['TotalImpressions']>=c]

    st.bar_chart(datanew)

    st.write(datanew.head(n=a))


    @st.cache
    def convert_df_to_csv(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')


    st.download_button(
        label="Download data as CSV",
        data=convert_df_to_csv(data),
        file_name='large_df.csv',
        mime='text/csv',
    )







