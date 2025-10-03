import streamlit as st
import graphviz # Import the graphviz library

st.set_page_config(layout="wide")

st.title("Mindmap Generator")

# Left-hand sidebar panel
st.sidebar.header("Analysis Options")

# Dropdown list
selected_option = st.sidebar.selectbox(
    "Select a structure to analyze:",
    ("Revenue structure", "Cost structure")
)

st.write(f"You selected: **{selected_option}**")

st.subheader("Mindmap Display Area")

def generate_revenue_mindmap_dot():
    """
    Generates a Graphviz DOT string for the Company Revenue Structure mindmap.
    """
    dot = graphviz.Graph(comment='Company Revenue Structure Mindmap', 
                         graph_attr={
                             'rankdir': 'LR', # Layout from Left to Right
                             'splines': 'curved', # Use curved lines for edges
                             'overlap': 'false', # Prevent node overlap
                             'bgcolor': 'transparent', # Transparent background
                             'nodesep': '0.8', # Minimum space between two adjacent nodes in the same rank
                             'ranksep': '1.5' # Minimum space between ranks
                         })
    
    # Central Node
    dot.node('central', 'Company Revenue Structure', 
             shape='box', style='rounded,filled', fillcolor='#9370DB', fontcolor='white', fontsize='24', penwidth='2')

    # Main Branches
    dot.node('non_insurance_biz', 'Doanh thu kinh doanh phi bảo hiểm và các hoạt động khác', 
             shape='box', style='rounded,filled', fillcolor='#FF69B4', fontcolor='white', fontsize='16')
    dot.node('insurance_biz', 'Doanh thu từ hoạt động kinh doanh bảo hiểm', 
             shape='box', style='rounded,filled', fillcolor='#BA55D3', fontcolor='white', fontsize='16')
    dot.node('financial_activities', 'Doanh thu từ hoạt động tài chính', 
             shape='box', style='rounded,filled', fillcolor='#FFD700', fontcolor='black', fontsize='16')

    dot.edge('central', 'non_insurance_biz', color='#9370DB', penwidth='3')
    dot.edge('central', 'insurance_biz', color='#9370DB', penwidth='3')
    dot.edge('central', 'financial_activities', color='#9370DB', penwidth='3')

    # Sub-branches for Non-insurance business revenue
    dot.node('other_income', 'Thu nhập khác', 
             shape='box', style='rounded,filled', fillcolor='#FFB6C1', fontcolor='black')
    dot.node('office_rental', 'Doanh thu cho thuê văn phòng', 
             shape='box', style='rounded,filled', fillcolor='#FFB6C1', fontcolor='black')
    dot.node('fund_mgmt_consulting', 'Doanh thu từ quản lý quỹ và tư vấn đầu tư', 
             shape='box', style='rounded,filled', fillcolor='#FFB6C1', fontcolor='black')
    dot.node('insurance_auxiliary', 'Dịch vụ phụ trợ bảo hiểm', 
             shape='box', style='rounded,filled', fillcolor='#FFB6C1', fontcolor='black')
    dot.node('total_revenue_2024_non_ins', 'Tổng doanh thu năm 2024', 
             shape='box', style='rounded,filled', fillcolor='#FFB6C1', fontcolor='black')

    dot.edge('non_insurance_biz', 'other_income', color='#FF69B4', penwidth='2')
    dot.edge('non_insurance_biz', 'office_rental', color='#FF69B4', penwidth='2')
    dot.edge('non_insurance_biz', 'fund_mgmt_consulting', color='#FF69B4', penwidth='2')
    dot.edge('non_insurance_biz', 'insurance_auxiliary', color='#FF69B4', penwidth='2')
    dot.edge('non_insurance_biz', 'total_revenue_2024_non_ins', color='#FF69B4', penwidth='2')

    # Sub-sub-branches for Other Income
    dot.node('social_ins_collection', 'Hoạt động thu hộ bảo hiểm xã hội', 
             shape='box', style='rounded,filled', fillcolor='#FFF0F5', fontcolor='black')
    dot.node('health_ins_collection', 'Hoạt động thu hộ bảo hiểm y tế', 
             shape='box', style='rounded,filled', fillcolor='#FFF0F5', fontcolor='black')
    dot.edge('other_income', 'social_ins_collection', color='#FFB6C1', penwidth='1')
    dot.edge('other_income', 'health_ins_collection', color='#FFB6C1', penwidth='1')

    # Sub-sub-branches for Total Revenue 2024 (Non-insurance)
    dot.node('reached_1647_billion', 'Đạt 1.647 tỷ đồng', 
             shape='box', style='rounded,filled', fillcolor='#FFF0F5', fontcolor='black')
    dot.node('completed_126_percent', 'Hoàn thành 126% kế hoạch năm', 
             shape='box', style='rounded,filled', fillcolor='#FFF0F5', fontcolor='black')
    dot.node('growth_2_percent', 'Tăng trưởng 2% so với cùng kỳ', 
             shape='box', style='rounded,filled', fillcolor='#FFF0F5', fontcolor='black')
    dot.node('stable_financial_inv', 'Duy trì hoạt động đầu tư tài chính ổn định', 
             shape='box', style='rounded,filled', fillcolor='#FFF0F5', fontcolor='black')
    dot.edge('total_revenue_2024_non_ins', 'reached_1647_billion', color='#FFB6C1', penwidth='1')
    dot.edge('total_revenue_2024_non_ins', 'completed_126_percent', color='#FFB6C1', penwidth='1')
    dot.edge('total_revenue_2024_non_ins', 'growth_2_percent', color='#FFB6C1', penwidth='1')
    dot.edge('total_revenue_2024_non_ins', 'stable_financial_inv', color='#FFB6C1', penwidth='1')

    # Sub-branches for Insurance business activities
    dot.node('original_premium', 'Phí bảo hiểm gốc', 
             shape='box', style='rounded,filled', fillcolor='#DDA0DD', fontcolor='black')
    dot.node('reinsurance_received', 'Phí nhận tái bảo hiểm', 
             shape='box', style='rounded,filled', fillcolor='#DDA0DD', fontcolor='black')
    dot.node('reinsurance_commission', 'Hoa hồng nhượng tái bảo hiểm', 
             shape='box', style='rounded,filled', fillcolor='#DDA0DD', fontcolor='black')
    dot.node('other_ins_income', 'Thu khác từ hoạt động kinh doanh bảo hiểm', 
             shape='box', style='rounded,filled', fillcolor='#DDA0DD', fontcolor='black')
    dot.node('total_revenue_2024_ins', 'Tổng doanh thu năm 2024', 
             shape='box', style='rounded,filled', fillcolor='#DDA0DD', fontcolor='black')

    dot.edge('insurance_biz', 'original_premium', color='#BA55D3', penwidth='2')
    dot.edge('insurance_biz', 'reinsurance_received', color='#BA55D3', penwidth='2')
    dot.edge('insurance_biz', 'reinsurance_commission', color='#BA55D3', penwidth='2')
    dot.edge('insurance_biz', 'other_ins_income', color='#BA55D3', penwidth='2')
    dot.edge('insurance_biz', 'total_revenue_2024_ins', color='#BA55D3', penwidth='2')

    # Sub-sub-branches for Total Revenue 2024 (Insurance)
    dot.node('largest_contribution', 'Đóng góp lớn nhất: 20.178 tỷ đồng', 
             shape='box', style='rounded,filled', fillcolor='#E6E6FA', fontcolor='black')
    dot.node('completed_125_percent', 'Hoàn thành 125% kế hoạch', 
             shape='box', style='rounded,filled', fillcolor='#E6E6FA', fontcolor='black')
    dot.node('growth_39_percent', 'Tăng trưởng 39% so với năm trước', 
             shape='box', style='rounded,filled', fillcolor='#E6E6FA', fontcolor='black')
    dot.node('growth_int_reinsurance', 'Tăng trưởng từ khai thác nhận tái bảo hiểm quốc tế', 
             shape='box', style='rounded,filled', fillcolor='#E6E6FA', fontcolor='black')
    dot.node('original_premium_13000_billion', 'Doanh thu bảo hiểm gốc: 13.000 tỷ đồng', 
             shape='box', style='rounded,filled', fillcolor='#E6E6FA', fontcolor='black')
    dot.edge('total_revenue_2024_ins', 'largest_contribution', color='#DDA0DD', penwidth='1')
    dot.edge('total_revenue_2024_ins', 'completed_125_percent', color='#DDA0DD', penwidth='1')
    dot.edge('total_revenue_2024_ins', 'growth_39_percent', color='#DDA0DD', penwidth='1')
    dot.edge('total_revenue_2024_ins', 'growth_int_reinsurance', color='#DDA0DD', penwidth='1')
    dot.edge('total_revenue_2024_ins', 'original_premium_13000_billion', color='#DDA0DD', penwidth='1')

    # Sub-branches for Financial activities
    dot.node('bond_investment_profit', 'Lãi đầu tư trái phiếu', 
             shape='box', style='rounded,filled', fillcolor='#FFFACD', fontcolor='black')
    dot.node('dividends_profits', 'Cổ tức và lợi nhuận được chia từ các khoản đầu tư', 
             shape='box', style='rounded,filled', fillcolor='#FFFACD', fontcolor='black')
    dot.node('exchange_rate_profit', 'Lãi từ chênh lệch tỷ giá', 
             shape='box', style='rounded,filled', fillcolor='#FFFACD', fontcolor='black')
    dot.node('stock_trading_profit', 'Lãi kinh doanh cổ phiếu', 
             shape='box', style='rounded,filled', fillcolor='#FFFACD', fontcolor='black')

    dot.edge('financial_activities', 'bond_investment_profit', color='#FFD700', penwidth='2')
    dot.edge('financial_activities', 'dividends_profits', color='#FFD700', penwidth='2')
    dot.edge('financial_activities', 'exchange_rate_profit', color='#FFD700', penwidth='2')
    dot.edge('financial_activities', 'stock_trading_profit', color='#FFD700', penwidth='2')

    return dot.source

# Placeholder for mindmap generation logic
if selected_option == "Revenue structure":
    st.info("Generating mindmap for Revenue Structure...")
    # Generate the DOT string and render it using Streamlit's graphviz component
    graph_dot_string = generate_revenue_mindmap_dot()
    st.graphviz(graph_dot_string)
elif selected_option == "Cost structure":
    st.info("Generate a mindmap for Cost Structure here.")
    # Add your mindmap generation code for