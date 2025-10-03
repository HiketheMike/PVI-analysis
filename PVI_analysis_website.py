import streamlit as st
# Removed: import graphviz # Import the graphviz library

st.set_page_config(layout="wide")

st.title("PVI Analysis") # Changed title

# Left-hand sidebar panel
st.sidebar.header("Analysis Options")

# Dropdown list for main analysis type
selected_analysis_type = st.sidebar.selectbox(
    "Select a structure to analyze:",
    ("Revenue Structure", "Cost structure")
)

st.write(f"You selected: **{selected_analysis_type}**")

# Define the structured data for the revenue notes
revenue_structure_data = {

    "Doanh thu từ hoạt động kinh doanh bảo hiểm": {
        "Phí bảo hiểm gốc": [
            "**Số liệu chính xác:** Doanh thu phí bảo hiểm gốc năm 2024 đạt 13.000 tỷ đồng.",
            "**Thành tích nổi bật:**",
            "- Tăng trưởng vượt trội: Gấp gần 2 lần so với mức tăng trưởng chung của thị trường bảo hiểm phi nhân thọ.",
            "- Góp phần tăng doanh thu hoạt động bảo hiểm hợp nhất 39% so với cùng kỳ.",
            "- Khẳng định vị thế số 1: Tổng Công ty Bảo hiểm PVI dẫn đầu thị trường bảo hiểm phi nhân thọ về doanh thu Bảo hiểm gốc.",
            "- Góp phần vào kỷ lục doanh thu: Giúp Tổng Công ty Bảo hiểm PVI lần đầu đạt 20.000 tỷ đồng và PVI Holdings vượt 21.000 tỷ đồng tổng doanh thu hợp nhất."
        ],
        "Phí nhận tái bảo hiểm": [
            "**Thành tích và Số liệu Kinh doanh của Tái Bảo Hiểm (Năm 2024):**",
            "- Doanh thu kỷ lục: Tổng doanh thu của Hanoi Re đạt 3.017,3 tỷ đồng, hoàn thành 106,6% kế hoạch năm.",
            "- Lợi nhuận: Lợi nhuận trước thuế 240 tỷ đồng, lợi nhuận sau thuế 190 tỷ đồng.",
            "- Hiệu quả đầu tư tài chính: Tối ưu hóa dòng tiền và nắm bắt cơ hội thị trường.",
            "- Xếp hạng tín nhiệm quốc tế: A.M. Best điều chỉnh triển vọng nâng hạng năng lực tín dụng dài hạn từ 'ổn định' lên 'tích cực', duy trì xếp hạng năng lực tài chính B++ (Tốt).",
            "- Năng lực và uy tín được khẳng định: PVI khẳng định năng lực tái bảo hiểm vững mạnh và uy tín chuyên nghiệp.",
            "**Định Hướng Chiến Lược và Hoạt Động Của Mảng Tái Bảo Hiểm:**",
            "- Chiến lược phát triển: Tập trung thị trường trong nước, khai thác thận trọng thị trường nước ngoài.",
            "- Mở rộng dịch vụ: Hanoi Re mở rộng tư vấn giám định rủi ro quốc tế và tiên phong cung cấp dịch vụ định phí tại Việt Nam.",
            "- Ứng phó với rủi ro: Tích cực đồng hành cùng đối tác, hỗ trợ giải quyết tổn thất lớn (ví dụ: sau siêu bão Yagi).",
            "- Mục tiêu 2025 và dài hạn: Trở thành nhà Tái bảo hiểm số 1 Việt Nam và có thương hiệu quốc tế; nghiên cứu mở rộng dịch vụ và sản phẩm mới."
        ],
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

if selected_analysis_type == "Revenue Structure":

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