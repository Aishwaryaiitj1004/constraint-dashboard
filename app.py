import streamlit as st
    st.subheader("Total Downtime Analysis")

    fig1 = px.bar(
        df,
        x="Operation",
        y="TDT",
        color="TDT",
        text="TDT"
    )

    fig1.update_layout(
        xaxis_title="Operation",
        yaxis_title="TDT",
        height=500
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ==========================
    # EFFICIENCY ANALYSIS
    # ==========================

    st.subheader("Efficiency Analysis")

    fig2 = px.bar(
        df,
        x="Operation",
        y="Eff",
        color="Eff",
        text="Eff"
    )

    fig2.update_layout(
        xaxis_title="Operation",
        yaxis_title="Efficiency",
        height=500
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ==========================
    # LOSS DISTRIBUTION
    # ==========================

    st.subheader("Loss Time Distribution")

    loss_df = pd.DataFrame({
        "Loss Type": ["IDT", "NWT", "RWT", "TDT"],
        "Value": [
            df["IDT"].sum(),
            df["NWT"].sum(),
            df["RWT"].sum(),
            df["TDT"].sum()
        ]
    })

    fig3 = px.pie(
        loss_df,
        names="Loss Type",
        values="Value"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
