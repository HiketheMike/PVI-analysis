import streamlit as st
# Removed: import graphviz # Import the graphviz library

st.set_page_config(layout="wide")

st.title("PVI Analysis") # Changed title

# Left-hand sidebar panel
st.sidebar.header("Analysis Options")

# Dropdown list for main analysis type
selected_analysis_type = st.sidebar.selectbox(
    "Select a structure to analyze:",
    ("Revenue Structure", "Cost structure", "Competitive Positioning", "Financial investment strategy")
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
            "Doanh thu kỷ lục: Tổng doanh thu của Hanoi Re đạt 3.017,3 tỷ đồng, hoàn thành 106,6% kế hoạch năm.",
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
competitive_positioning_data = {
    "Sức Mạnh Cạnh Tranh Trong Kênh Phân Phối": {
        "Đa Dạng Hóa và Phát Triển Các Kênh Phân Phối Mới": [
                "PVI không ngừng tập trung phát triển các kênh phân phối mới để mở rộng mạng lưới bán hàng.",
                "Một điểm sáng nổi bật là việc hợp tác với hai tổ chức lớn là Bảo hiểm xã hội Việt Nam và Hội Nông dân tại các địa phương để triển khai thu hộ BHXH, BHYT tự nguyện.",
                "Chỉ sau hơn 2 năm tham gia, Bảo hiểm PVI đã vươn lên vị trí thứ 2 trong số gần 600 tổ chức dịch vụ thu hộ BHXH, cho thấy năng lực vượt trội trong việc triển khai và vận hành các kênh phân phối mới, tiếp cận sâu rộng đến các phân khúc khách hàng đa dạng."
            
        ],
        "Đầu Tư Mạnh Mẽ vào Công Nghệ Thông Tin để Hỗ Trợ Phân Phối": [
                "Trung tâm CNTT của PVI đóng vai trò quan trọng trong việc thúc đẩy chuyển đổi số, hỗ trợ hiệu quả kinh doanh và quản trị.",
                "Công ty tập trung triển khai các ứng dụng phần mềm cho kênh thương mại điện tử, nghiên cứu ứng dụng AI và tối ưu hóa các hoạt động giám định, bồi thường, tạo ra trải nghiệm tốt hơn cho khách hàng qua các kênh số."
        ],
        "Tiên Phong và Dẫn Đầu Kênh Thương Mại Điện Tử": [
                "Bảo hiểm PVI đã triển khai mạnh mẽ kênh thương mại điện tử, đạt doanh thu gần 800 tỷ đồng trong năm 2024, tăng trưởng 50%.",
                "Công ty đã đầu tư và ứng dụng công nghệ số, kết nối API với 30 đối tác, sàn điện tử lớn như Vietnam Airlines, Mobifone, Viettel, Thegioididong, Sendo, Shopee.... Việc hợp tác sâu rộng với các hệ sinh thái lớn này tạo ra một kênh phân phối hiện đại, tiếp cận được lượng khách hàng khổng lồ mà các kênh truyền thống khó có được."
        ]
    },  
    "Sức Mạnh Cạnh Tranh Trong Việc Tạo Doanh Thu": {
        "Khai Thác Tái Bảo Hiểm Quốc Tế Nhờ Xếp Hạng Tín Nhiệm Vượt Trội": [
            "Bảo hiểm PVI là doanh nghiệp bảo hiểm duy nhất tại Việt Nam duy trì được xếp hạng năng lực tài chính A- (Xuất sắc) từ A.M. Best.",
            "Lợi thế này cho phép PVI đẩy mạnh hoạt động khai thác nhận tái bảo hiểm từ thị trường quốc tế, một nguồn doanh thu quan trọng mà không nhiều đối thủ trong nước có thể cạnh tranh được. Đây là yếu tố chính giúp doanh thu hoạt động bảo hiểm tăng trưởng 39% trong năm 2024."
        ],
        "Tăng Trưởng Doanh Thu Bảo Hiểm Gốc Vượt Trội So Với Thị Trường": [
            "Doanh thu bảo hiểm gốc của PVI cán mốc 13.000 tỷ đồng, với mức tăng trưởng gấp gần 2 lần so với mức tăng trưởng chung của thị trường bảo hiểm phi nhân thọ.",
            "Sự tăng trưởng ấn tượng này cho thấy PVI không chỉ duy trì thị phần mà còn đang chiếm lĩnh thị phần từ các đối thủ, khẳng định sức mạnh và uy tín thương hiệu trong việc thu hút khách hàng."
        ],
        "Mô Hình Kinh Doanh Đa Trụ Cột, Đảm Bảo Doanh Thu Bền Vững": [
            "PVI phát triển cân đối dựa trên ba trụ cột chính: bảo hiểm phi nhân thọ, tái bảo hiểm, và quản lý quỹ.",
            "Mô hình này tạo ra sự ổn định về doanh thu. Ngay cả khi mảng bảo hiểm bị ảnh hưởng nặng nề bởi siêu bão Yagi, thì doanh thu từ hoạt động tài chính, cho thuê văn phòng và các hoạt động khác vẫn đạt 1.647 tỷ đồng, hoàn thành 126% kế hoạch.",
            "Trung tâm Quản lý và Kinh doanh Dịch vụ (vận hành Tòa nhà PVI) cũng đóng góp một nguồn doanh thu ổn định và hiệu quả, với tỷ lệ lấp đầy bình quân trên 100% kế hoạch."
        ],
        "Năng Lực Tài Chính Vững Mạnh Hỗ Trợ Mở Rộng Kinh Doanh": [
            "Với việc tăng vốn điều lệ lên 3.900 tỷ đồng, Bảo hiểm PVI là doanh nghiệp bảo hiểm phi nhân thọ có quy mô vốn lớn nhất thị trường.",
            "Năng lực tài chính dồi dào là nền tảng để công ty mở rộng hoạt động kinh doanh, chấp nhận các hợp đồng bảo hiểm lớn và tăng cường khai thác thị trường quốc tế, từ đó tạo ra doanh thu lớn hơn."
        ],
        "Hậu Thuẫn Mạnh Mẽ từ Cổ Đông Lớn": [
            "PVI nhận được sự hỗ trợ mạnh mẽ từ các cổ đông chiến lược là Tập đoàn Dầu khí Quốc gia Việt Nam (PVN) và HDI Global SE (thuộc tập đoàn Talanx của Đức). Sự kết hợp này mang lại lợi thế kép: nguồn khách hàng lớn, ổn định từ ngành dầu khí và kinh nghiệm, mạng lưới quốc tế từ tập đoàn bảo hiểm hàng đầu châu Âu."
        ]
    }
}
financial_investment_strategy_data = {
    "Chiến lược quản lí danh mục đâu tư": {
        "Tuân thủ khẩu vị rủi ro và quy định pháp luật": [
            "Chiến lược cốt lõi là duy trì cơ cấu danh mục đầu tư phù hợp với khẩu vị rủi ro đã được Hội đồng Quản trị (HĐQT) phê duyệt.",
            "Mục tiêu của việc này là để đáp ứng các quy định của pháp luật về biên khả năng thanh toán và các yêu cầu kỹ thuật về an toàn vốn, nhằm duy trì và hướng tới nâng hạng tín nhiệm cho các công ty con."
        ],
        "Linh hoạt tái cấu trúc danh mục đầu tư": [
            "Trong bối cảnh thị trường biến động, như lãi suất thấp trong năm 2024, PVI đã chủ động tái cấu trúc danh mục đầu tư. Cụ thể, trong năm 2024, PVI đã tăng đầu tư vào trái phiếu dài hạn và giảm đầu tư vào tiền gửi dài hạn.",
            "PVIAM, đơn vị quản lý tài sản của hệ thống, đã kịp thời dịch chuyển cơ cấu tài sản, tối ưu hóa dòng tiền và sử dụng các công cụ, sản phẩm đầu tư linh hoạt để nâng cao hiệu quả."
        ],
        "Đa dạng hóa danh mục và tìm kiếm cơ hội mới": [
            "PVI có chiến lược triển khai các sản phẩm đầu tư linh hoạt, đa dạng phù hợp với thị trường và khẩu vị rủi ro của công ty.",
            "Trong năm 2025, PVIAM sẽ đa dạng và linh hoạt hơn trong công tác đầu tư để tối ưu hóa hiệu quả. PVIAM cũng có kế hoạch thành lập và vận hành các quỹ mở để phát huy thế mạnh về đầu tư các sản phẩm thu nhập cố định và mở rộng mạng lưới đối tác bên ngoài hệ thống."
        ],
        "Quản lý rủi ro chặt chẽ": [
            "Hệ thống quản trị rủi ro của PVI được xây dựng theo mô hình ba tuyến để giám sát các loại rủi ro, bao gồm rủi ro thị trường (rủi ro giá cổ phiếu, rủi ro lãi suất).",
            "Đối với rủi ro thị trường, PVI quản lý bằng cách xây dựng các quy định, chính sách đầu tư, đa dạng hóa danh mục và thiết lập các hạn mức đầu tư.",
            "PVIAM, với vai trò là đơn vị quản lý quỹ, nhấn mạnh việc tăng cường theo dõi và giám sát trong và sau quá trình đầu tư để đảm bảo an toàn và minh bạch cho danh mục."
        ],
        "Đầu tư có trách nhiệm (ESG)": [
            "PVI cam kết xem xét cẩn trọng các yếu tố liên quan đến môi trường và xã hội trước khi quyết định đầu tư.",
            "Công ty đã khẳng định sẽ không đầu tư vào các doanh nghiệp có lĩnh vực kinh doanh hoặc hành động vi phạm nghiêm trọng đến môi trường. Danh mục đầu tư năm 2024 của PVI không bao gồm các doanh nghiệp khai thác khoáng sản hay các nhà máy điện sử dụng nhiên liệu hóa thạch."
        ]
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
        # ...existing code...
        for sub_cat, items in subcategories.items():
            with st.expander(f"**{sub_cat}**"):
                if items:
                    for item in items:
                        st.markdown(f"{item}") # Removed the prepended hyphen
                else:
                    st.markdown("*(No further details available for this subcategory.)*")

elif selected_analysis_type == "Cost structure":
    st.info("Content for Cost Structure will go here.")

elif selected_analysis_type == "Competitive Positioning":

    main_category_options = list(competitive_positioning_data.keys())
    selected_main_category = st.sidebar.radio(
        "Select a competitive positioning aspect:",
        main_category_options
    )

    if selected_main_category:
        st.subheader(selected_main_category)
        subcategories = competitive_positioning_data[selected_main_category]

        for sub_cat, items in subcategories.items():
            with st.expander(f"**{sub_cat}**"):
                if items:
                    for item in items:
                        st.markdown(f"{item}")
                else:
                    st.markdown("*(No further details available for this subcategory.)*")

elif selected_analysis_type == "Financial investment strategy":
    st.write("### Financial Investment Strategy Details")

    main_category_options = list(financial_investment_strategy_data.keys())
    selected_main_category = st.sidebar.radio(
        "Select a financial investment strategy aspect:",
        main_category_options
    )

    if selected_main_category:
        st.subheader(selected_main_category)
        subcategories = financial_investment_strategy_data[selected_main_category]

        for sub_cat, items in subcategories.items():
            with st.expander(f"**{sub_cat}**"):
                if items:
                    for item in items:
                        st.markdown(f"{item}")
                else:
                    st.markdown("*(No further details available for this subcategory.)*")