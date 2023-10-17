import streamlit as st
from datetime import datetime
import pytz

def time_zone_page():
    st.title("Time Zone")

    # List of time zones
    time_zones = pytz.all_timezones

    # Time zone selection
    selected_time_zone = st.selectbox("Select a time zone", time_zones)

    # Get current time in selected time zone
    tz = pytz.timezone(selected_time_zone)
    current_time = datetime.now(tz)

    st.write("Current time in {}: {}".format(selected_time_zone, current_time.strftime("%Y-%m-%d %H:%M:%S")))
