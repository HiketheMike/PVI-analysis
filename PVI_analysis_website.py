import streamlit as st
# Removed: import graphviz # Import the graphviz library

st.set_page_config(layout="wide")

st.title("PVI Analysis") # Changed title

# Left-hand sidebar panel
st.sidebar.header("Analysis Options")

# Dropdown list for main analysis type
selected_analysis_type = st.sidebar.selectbox(
    "Select a structure to analyze:",
    ("Company Revenue Structure", "Cost structure")
)

st.write(f"You selected: **{selected_analysis_type}**")

# Define the structured data for the revenue notes
revenue_structure_data = {
    "Doanh thu kinh doanh phi bảo hiểm và các hoạt động khác": {
        "Thu nhập khác": [
            "Hoạt động thu hộ bảo hiểm xã hội",
            "Hoạt động thu hộ bảo hiểm y tế"
        ],
        "Doanh thu cho thuê văn phòng": [],
        "Doanh thu từ quản lý quỹ và tư vấn đầu tư": [],
        "Dịch vụ phụ trợ bảo hiểm": [],
        "Tổng doanh thu năm 2024 (Phi bảo hiểm)": [
            "Đạt 1.647 tỷ đồng",
            "Hoàn thành 126% kế hoạch năm",
            "Tăng trưởng 2% so với cùng kỳ",
            "Duy trì hoạt động đầu tư tài chính ổn định"
        ]
    },
    "Doanh thu từ hoạt động kinh doanh bảo hiểm": {
        "Phí bảo hiểm gốc": [],
        "Phí nhận tái bảo hiểm": [],
        "Hoa hồng nhượng tái bảo hiểm": [],
        "Thu khác từ hoạt động kinh doanh bảo hiểm": [],
        "Tổng doanh thu năm 2024 (Bảo hiểm)": [
            "Đóng góp lớn nhất: 20.178 tỷ đồng",
            "Hoàn thành 125% kế hoạch",
            "Tăng trưởng 39% so với năm trước",
            "Tăng trưởng từ khai thác nhận tái bảo hiểm quốc tế",
            "Doanh thu bảo hiểm gốc: 13.000 tỷ đồng"
        ]
    },
    "Doanh thu từ hoạt động tài chính": {
        "Lãi đầu tư trái phiếu": [],
        "Cổ tức và lợi nhuận được chia từ các khoản đầu tư": [],
        "Lãi từ chênh lệch tỷ giá": [],
        "Lãi kinh doanh cổ phiếu": []
    }
}

if selected_analysis_type == "Company Revenue Structure":

    # Use st.sidebar.radio for main categories (acting as tabs)
    main_category_options = list(revenue_structure_data.keys())
    selected_main_category = st.sidebar.radio(
        "Select a main revenue category:",
        main_category_options
    )

    if selected_main_category:
        st.subheader(selected_main_category)
        subcategories = revenue_structure_data[selected_main_category]

        for sub_cat, items in subcategories.items():
            with st.expander(f"**{sub_cat}**"):
                if items:
                    for item in items:
                        st.markdown(f"- {item}")
                else:
                    st.markdown("*(No further details available for this subcategory.)*")

elif selected_analysis_type == "Cost structure":
    st.info("Content for Cost Structure will go here.")
    # Add your notes for Cost