def assumptions():
    import streamlit as st 


    st.subheader("Client Contract Parameters")
    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                h2_flow_rate_value = st.text_input("Customer required H2 flow rate", value="default_value", key="h2_flow_rate_value")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                h2_flow_rate_unit = st.selectbox("Unit", options, key="h2_flow_rate_unit")
                value1 = f"{h2_flow_rate_value} {h2_flow_rate_unit}"
            

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                h2_flow_supply_at_flow = st.text_input("Hours of H2 supply at flow rate", value="default_value", key="h2_flow_supply_at_flow")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                h2_flow_supply_at_flow_unit = st.selectbox("Unit", options, key="h2_flow_supply_at_flow_unit")
                value2 = f"{h2_flow_supply_at_flow} {h2_flow_supply_at_flow_unit}"


    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Project_contract_lifetime = st.text_input("Project contract lifetime", value="default_value", key="Project_contract_lifetime")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Project_contract_lifetime_unit = st.selectbox("Unit", options, key="Project_contract_lifetime_unit")
                value3 = f"{Project_contract_lifetime} {Project_contract_lifetime_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                supply_pressure_option = st.radio("Supply pressure vs. EL", ["High", "Low"], key="supply_pressure_option")
                
                
            with col2:
                Contract_pricing_currency = st.radio("Contract pricing currency", ["USD", "INR"], key="Contract_pricing_currency")
                


    st.subheader("Merchant Market Parameters")

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Market_Sell_Limit = st.text_input("02 Market Sell Limit", value="default_value", key="Market_Sell_Limit")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Market_Sell_Limit_unit = st.selectbox("Unit", options, key="Market_Sell_Limit_unit")
                value4 = f"{Market_Sell_Limit} {Market_Sell_Limit_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Excess_production_H2_Merchant_Limit = st.text_input("Excess production H2 Merchant Limit", value="default_value", key="Excess_production_H2_Merchant_Limit")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Excess_production_H2_Merchant_Limit_unit = st.selectbox("Unit", options, key="Excess_production_H2_Merchant_Limit_unit")
                value5 = f"{Excess_production_H2_Merchant_Limit} {Excess_production_H2_Merchant_Limit_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                Market_Sell_option = st.radio("02 Market Sell", ["Yes", "No"], key="Market_Sell_option")
                

            with col2:
                Merchant_Market_Sell_option = st.radio("Merchant Market Sell", ["Yes", "No"], key="Merchant_Market_Sell_option")
            


    st.subheader("Power Mgmt Parameters")
    with st.container():
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                Inject_excess_power_to_grid = st.radio("Inject excess power to grid", ["Yes", "No"], key="Inject_excess_power_to_grid")
                st.write("Inject excess power to grid:", Inject_excess_power_to_grid)

            with col2:
                Draw_power_from_grid = st.radio("Draw power from grid", ["Yes", "No"], key="Draw_power_from_grid")
                


    st.subheader("Battery & PV Parameters")
    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Battery_Round_Trip_Efficiency= st.text_input("Battery Round Trip Efficiency", value="default_value", key="Battery_Round_Trip_Efficiency")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Battery_Round_Trip_Efficiency_unit = st.selectbox("Unit", options, key="Battery_Round_Trip_Efficiency_unit")
                value6 = f"{Battery_Round_Trip_Efficiency} {Battery_Round_Trip_Efficiency_unit}"
            

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Battery_Life = st.text_input("Battery Life", value="default_value", key="Battery_Life")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Battery_Life_unit = st.selectbox("Unit", options, key="Battery_Life_unit")
                value7 = f"{Battery_Life} {Battery_Life_unit}"
        

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Battery_Annual_Degradation = st.text_input("Battery Annual Degradation", value="default_value", key="Battery_Annual_Degradation")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Battery_Annual_Degradation_unit = st.selectbox("Unit", options, key="Battery_Annual_Degradation_unit")
                value8 = f"{Battery_Annual_Degradation} {Battery_Annual_Degradation_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                PV_Annual_Degradation_input = st.text_input("PV Annual Degradation", value="default_value", key="PV_Annual_Degradation_input")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                PV_Annual_Degradation_unit = st.selectbox("Unit", options, key="PV_Annual_Degradation_unit")
                value9 = f"{PV_Annual_Degradation_input} {PV_Annual_Degradation_unit}"
                


    with st.container():
        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                PV_Type_option = st.radio("Select PV Type:", ["Poly", "Mono"], key="PV_Type_option")
                

            with col2:
                mounted_option = st.radio("Select mounting type:", ["Rooftop", "Ground Mounted"], key="mounted_option")
                



    st.subheader("Electrolyser Parameters")
    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Stack_Conversion= st.text_input("Stack Conversion(100 flow)", value="default_value", key="Stack_Conversion")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Stack_Conversion_unit = st.selectbox("Unit", options, key="Stack_Conversion_unit")
                value6 = f"{Stack_Conversion} {Stack_Conversion_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Stack_Conversion_min_turndown_flow= st.text_input("Stack Conversion (min turndown flow)", value="default_value", key="Stack_Conversion_min_turndown_flow")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Stack_Conversion_min_turndown_flow_unit = st.selectbox("Unit", options, key="Stack_Conversion_min_turndown_flow_unit")
                value7 = f"{Stack_Conversion_min_turndown_flow} {Stack_Conversion_min_turndown_flow_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Turndown_Ration = st.text_input("Min. Turndown Ration", value="default_value", key="Turndown_Ration")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Turndown_Ration_unit = st.selectbox("Unit", options, key="Turndown_Ration_unit")
                value8 = f"{Turndown_Ration} {Turndown_Ration_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Stack_Annual_Degradation = st.text_input("Stack Annual Degradation", value="default_value", key="Stack_Annual_Degradation")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Stack_Annual_Degradation_unit = st.selectbox("Unit", options, key="Stack_Annual_Degradation_unit")
                value9 = f"{Stack_Annual_Degradation} {Stack_Annual_Degradation_unit}"
                

    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                Lifetime_of_Electroluser_Stack = st.text_input("Lifetime of Electroluser Stack", value="default_value", key="Lifetime_of_Electroluser_Stack")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                Lifetime_of_Electroluser_Stack_unit = st.selectbox("Unit", options, key="Lifetime_of_Electroluser_Stack_unit")
                value9 = f"{Lifetime_of_Electroluser_Stack} {Lifetime_of_Electroluser_Stack_unit}"


    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                AUX_Rated_power_during_El_ops = st.text_input("AUX Rated power(during El ops)", value="default_value", key="AUX_Rated_power_during_El_ops")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                AUX_Rated_power_during_El_ops_unit = st.selectbox("Unit", options, key="AUX_Rated_power_during_El_ops_unit")
                value9 = f"{AUX_Rated_power_during_El_ops} {AUX_Rated_power_during_El_ops_unit}"


    with st.container():
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                AUX_Rated_power_outside_El_ops = st.text_input("AUX Rated power(outside El ops)", value="default_value", key="AUX_Rated_power_outside_El_ops")

            with col2:
                options = ["Option 1", "Option 2", "Option 3"]
                AUX_Rated_power_outside_El_ops_unit = st.selectbox("Unit", options, key="AUX_Rated_power_outside_El_ops_unit")
                value9 = f"{AUX_Rated_power_outside_El_ops} {AUX_Rated_power_outside_El_ops_unit}"



    with st.container():
        with st.container():
                electrolyser_type = st.radio("Electrolyser Type:", ["AEC", "PEM"], key="electrolyser_type")