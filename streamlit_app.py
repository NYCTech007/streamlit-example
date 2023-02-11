"""
# Parking data app
This apps shows the findngs of my dataset, provided by NY Open Data:

"""
import streamlit as st
import pandas as pd
import numpy as np
st.header('Parking Cap')
DATA_URL = ('https://raw.githubusercontent.com/NYCTech007/Labs/main/mycsv.csv')
PCT_locs = ('https://raw.githubusercontent.com/NYCTech007/Labs/main/Pct_locs.csv')

#App title
st.title("Top Ticketing Precincts for 2022")
@st.experimental_memo
def load_mapdata(self):
    pctlocz = pd.read_csv(PCT_locs, nrows=self)
    return pctlocz 



# Create a text element and let the reader know the Map is loading.
pctdata_load_state = st.text('Loading Map...')
# Load data into the dataframe.
pctlocz = load_mapdata(1000)
# Notify the reader that the Map was successfully loaded.
pctdata_load_state.text('Map data loaded sucessfully!')



revenue_metric = st.metric(label="NYC's Record Year FY2015", value="59% of annual revenue", delta="$565 million of $957M"), st.text('FY = Fiscal Year'),
col1, col2, col3 = st.columns(3)
col1.metric("FY2022 Parking Fines", "OWED", "-$500 Million")
col3.metric("FY2020 issued tickets", "4,006,011", "Approx $260 Million")
col2.metric("Tickets Issued", "FY2021", "$138.3 Millioin")
DATE_COLUMN = 'ts'
#pctlocs = pd.DataFrame(PCT_locs, columns=["PCT", "longitude", "latitude"])
NYPD =  pctlocz[["PCT", "longitude", "latitude"]]
nypct = pctlocz[["PCT"]]
pctdata = pd.read_csv(DATA_URL)
pctdata_NYPCT  = pctdata.PRECINCT.unique()



# Using "with" notation
with st.sidebar:
    
    option = st.selectbox(
    'Which ticketing precinct interest you?',
    (pctdata_NYPCT))
    
    st.write('You selected Precinct:', option)


    




nyc_map = st.map(pctlocz[["latitude", "longitude"]].dropna(),  zoom=None)
# plot the slider that selects number of tickets
#ticket_slider = st.slider("Number of tickets", 1, int(pctdata["Number of Tickets"].max()))
 

