import streamlit as st

st.set_page_config(
    page_title="Textile Engineering Calculator Pro",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 Textile Engineering Calculator Pro")
st.caption("Textile Engineering Calculation System")

# Student Information
st.sidebar.header("Student Information")
st.sidebar.write("**Name:** Rabika KZ")
st.sidebar.write("**Roll Number:** 25TE063")
st.sidebar.write("**Department:** Textile Engineering")

st.sidebar.divider()

page = st.sidebar.selectbox(
    "Select Calculator",
    [
        "Home",
        "Yarn Count Converter",
        "Fabric GSM",
        "Fabric Shrinkage",
        "Dyeing Calculator",
        "Production Efficiency",
        "Moisture Testing"
    ]
)

if page == "Home":
    st.header("Welcome, Rabika KZ!")
    st.write("**Roll Number:** 25TE063")
    st.write("**Department:** Textile Engineering")

    st.subheader("Available Calculators")
    st.markdown("""
    - Yarn Count Conversion
    - Fabric GSM
    - Fabric Shrinkage
    - Dyeing and Chemical Calculations
    - Production Efficiency
    - Moisture Testing
    """)

    st.info("Select a calculator from the sidebar.")

elif page == "Yarn Count Converter":
    st.header("Yarn Count Converter")

    count = st.number_input(
        "Enter Yarn Count",
        min_value=0.001,
        value=20.0
    )

    system = st.selectbox(
        "Select Count System",
        ["Ne", "Nm", "Tex", "Denier", "dtex"]
    )

    if st.button("Calculate"):
        if system == "Ne":
            tex = 590.541 / count
        elif system == "Nm":
            tex = 1000 / count
        elif system == "Tex":
            tex = count
        elif system == "Denier":
            tex = count / 9
        else:
            tex = count / 10

        st.success("Conversion Completed")
        st.metric("Tex", f"{tex:.4f}")
        st.metric("Ne", f"{590.541 / tex:.4f}")
        st.metric("Nm", f"{1000 / tex:.4f}")
        st.metric("Denier", f"{tex * 9:.4f}")
        st.metric("dtex", f"{tex * 10:.4f}")

        st.latex(r"Tex = \frac{590.541}{Ne}")
        st.latex(r"Tex = \frac{1000}{Nm}")

elif page == "Fabric GSM":
    st.header("Fabric GSM Calculator")

    mass = st.number_input(
        "Sample Mass (grams)",
        min_value=0.001,
        value=1.5
    )

    area = st.number_input(
        "Sample Area (cm²)",
        min_value=0.001,
        value=100.0
    )

    if st.button("Calculate GSM"):
        gsm = mass * 10000 / area

        st.success(f"Fabric GSM = {gsm:.2f}")
        st.latex(
            r"GSM = \frac{Mass\ (g)\times10000}{Area\ (cm^2)}"
        )

elif page == "Fabric Shrinkage":
    st.header("Fabric Shrinkage Calculator")

    initial = st.number_input(
        "Initial Length",
        min_value=0.001,
        value=100.0
    )

    final = st.number_input(
        "Final Length",
        min_value=0.0,
        value=95.0
    )

    if st.button("Calculate Shrinkage"):
        shrinkage = (initial - final) / initial * 100

        st.metric("Shrinkage", f"{shrinkage:.2f}%")
        st.latex(
            r"Shrinkage(\%) = \frac{Initial-Final}{Initial}\times100"
        )

        if final > initial:
            st.warning("Fabric length increased; this indicates growth.")

elif page == "Dyeing Calculator":
    st.header("Dyeing and Chemical Calculator")

    fabric = st.number_input(
        "Fabric Batch Weight (kg)",
        min_value=0.001,
        value=100.0
    )

    owf = st.number_input(
        "Dye Percentage (% OWF)",
        min_value=0.0,
        value=2.0
    )

    liquor_ratio = st.number_input(
        "Liquor Ratio",
        min_value=0.0,
        value=10.0
    )

    if st.button("Calculate Dye"):
        dye = fabric * owf / 100
        liquor = fabric * liquor_ratio

        st.metric("Dye Required", f"{dye:.3f} kg")
        st.metric("Approximate Liquor Volume", f"{liquor:.2f} L")

        st.caption(
            "Liquor volume assumes approximately 1 kg/L density."
        )

elif page == "Production Efficiency":
    st.header("Production Efficiency Calculator")

    actual = st.number_input(
        "Actual Production (kg)",
        min_value=0.0,
        value=850.0
    )

    theoretical = st.number_input(
        "Theoretical Production (kg)",
        min_value=0.001,
        value=1000.0
    )

    if st.button("Calculate Efficiency"):
        efficiency = actual / theoretical * 100
        st.metric("Efficiency", f"{efficiency:.2f}%")

        st.latex(
            r"Efficiency(\%) = \frac{Actual}{Theoretical}\times100"
        )

elif page == "Moisture Testing":
    st.header("Moisture Regain and Content")

    dry = st.number_input(
        "Oven-Dry Mass (g)",
        min_value=0.001,
        value=100.0
    )

    wet = st.number_input(
        "Conditioned Mass (g)",
        min_value=0.0,
        value=108.0
    )

    if st.button("Calculate Moisture"):
        regain = (wet - dry) / dry * 100
        content = (wet - dry) / wet * 100 if wet > 0 else 0

        st.metric("Moisture Regain", f"{regain:.2f}%")
        st.metric("Moisture Content", f"{content:.2f}%")

        st.latex(
            r"Regain(\%) = \frac{Wet-Dry}{Dry}\times100"
        )
        st.latex(
            r"Content(\%) = \frac{Wet-Dry}{Wet}\times100"
        )

st.divider()

st.caption(
    "Developed by Rabika KZ | Roll No. 25TE063"
)
st.caption("Department: Textile Engineering")
st.caption(
    "Educational version. Verify formulas before industrial use."
)
