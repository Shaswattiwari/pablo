import streamlit as st

def variables():
    
    with st.container():
        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                PV_DC_size_start = st.text_input("PV DC size (MW)", value="start_value", key="PV_DC_size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                PV_DC_size_end = st.text_input("", value="end_value", key="PV_DC_size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                Inverter_AC_size_start = st.text_input("Inverter AC size (MW)", value="start_value", key="Inverter_AC_size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                Inverter_AC_size_end = st.text_input("", value="end_value", key="Inverter_AC_size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                Wind_size_start = st.text_input("Wind size (MW)", value="start_value", key="Wind_size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                Wind_size_end = st.text_input("", value="end_value", key="Wind_size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                Power_Evacation_size_start = st.text_input("Power Evacuation size (MW)", value="start_value", key="Power_Evacation_size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                Power_Evacation_size_end = st.text_input("", value="end_value", key="Power_Evacation_size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                LTOA_size_start = st.text_input("LTOA size (MW)", value="start_value", key="LTOA_size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                LTOA_size_end = st.text_input("", value="end_value", key="LTOA_size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                Battery_size_start = st.text_input("Battery size (Kwh)", value="start_value", key="Battery_size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                Battery_size_end = st.text_input("", value="end_value", key="Battery_size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                Electrolyser_Size_start = st.text_input("Electrolyser Size (MW)", value="start_value", key="Electrolyser_Size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                Electrolyser_Size_end = st.text_input("", value="end_value", key="Electrolyser_Size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                Low_bar_H2_Storage_Size_start = st.text_input("Low bar H2 Storage Size", value="start_value", key="Low_bar_H2_Storage_Size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                Low_bar_H2_Storage_Size_end = st.text_input("", value="end_value", key="Low_bar_H2_Storage_Size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                High_bar_H2_Storage_Size_start = st.text_input("High bar H2 Storage Size", value="start_value", key="High_bar_H2_Storage_Size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                High_bar_H2_Storage_Size_end = st.text_input("", value="end_value", key="High_bar_H2_Storage_Size_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                H2_Compressor_Throughput_start = st.text_input("H2 Compressor Throughput", value="start_value", key="H2_Compressor_Throughput_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                H2_Compressor_Throughput_end = st.text_input("", value="end_value", key="H2_Compressor_Throughput_end")

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                Storage_size_start = st.text_input("O2 Storage size", value="start_value", key="Storage_size_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                Storage_size_end = st.text_input("", value="end_value", key="Storage_size_end")    

        with st.container():
            col1, col2, col3 = st.columns([12,1,12])
            with col1:
                compressor_throughput_start = st.text_input("O2 Compressor Throughput", value="start_value", key="compressor_throughput_start")

            with col2:
                st.title("")
                st.markdown("to")

            with col3:
                compressor_throughput_end = st.text_input("", value="end_value", key="compressor_throughput_end")    


