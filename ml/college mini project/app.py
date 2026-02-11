import io
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
# 1. Page Configuration (MUST be the first command)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title='Socio-Economic Country Clustering',
    layout='wide',
    page_icon='⚖️',
    initial_sidebar_state='expanded'
)

# Safe Import for Plotly
try:
    import plotly.express as px
    import plotly.graph_objects as go
    PLOTLY_AVAILABLE = True
except Exception:
    PLOTLY_AVAILABLE = False

# ML Imports
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.neighbors import NearestNeighbors

# -----------------------------------------------------------------------------
# 2. Custom CSS & Styling (Professional Academic Theme)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Main Layout settings */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Headers */
    h1 {
        color: #003366; /* Navy Blue */
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        border-bottom: 2px solid #FFD700; /* Gold underline */
        padding-bottom: 10px;
    }
    h2, h3 {
        color: #004080;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Custom Info Cards */
    .info-box {
        background-color: #f8f9fa;
        border-left: 5px solid #003366;
        padding: 15px;
        margin: 10px 0;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Metrics Styling */
    [data-testid="stMetricValue"] {
        color: #003366;
        font-weight: bold;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #f0f2f6;
    }
    
    /* Button Styling */
    div.stButton > button {
        background-color: #003366;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #004080;
        border: 1px solid #FFD700;
        color: #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. Helper Functions
# -----------------------------------------------------------------------------
@st.cache_data
def load_default():
    return pd.read_csv('Country-data.csv')

def get_country_flag(country_name):
    """
    Returns flag emoji for a country using country name mapping.
    Falls back to 🌍 if country not found.
    """
    # Comprehensive country to flag emoji mapping
    flag_map = {
        'Afghanistan': '🇦🇫', 'Albania': '🇦🇱', 'Algeria': '🇩🇿', 'Angola': '🇦🇴',
        'Argentina': '🇦🇷', 'Armenia': '🇦🇲', 'Australia': '🇦🇺', 'Austria': '🇦🇹',
        'Azerbaijan': '🇦🇿', 'Bahamas': '🇧🇸', 'Bahrain': '🇧🇭', 'Bangladesh': '🇧🇩',
        'Barbados': '🇧🇧', 'Belarus': '🇧🇾', 'Belgium': '🇧🇪', 'Belize': '🇧🇿',
        'Benin': '🇧🇯', 'Bhutan': '🇧🇹', 'Bolivia': '🇧🇴', 'Bosnia and Herzegovina': '🇧🇦',
        'Botswana': '🇧🇼', 'Brazil': '🇧🇷', 'Brunei': '🇧🇳', 'Bulgaria': '🇧🇬',
        'Burkina Faso': '🇧🇫', 'Burundi': '🇧🇮', 'Cambodia': '🇰🇭', 'Cameroon': '🇨🇲',
        'Canada': '🇨🇦', 'Cape Verde': '🇨🇻', 'Central African Republic': '🇨🇫',
        'Chad': '🇹🇩', 'Chile': '🇨🇱', 'China': '🇨🇳', 'Colombia': '🇨🇴',
        'Comoros': '🇰🇲', 'Congo, Dem. Rep.': '🇨🇩', 'Congo, Rep.': '🇨🇬',
        'Costa Rica': '🇨🇷', 'Cote d\'Ivoire': '🇨🇮', 'Croatia': '🇭🇷', 'Cuba': '🇨🇺',
        'Cyprus': '🇨🇾', 'Czech Republic': '🇨🇿', 'Denmark': '🇩🇰', 'Djibouti': '🇩🇯',
        'Dominican Republic': '🇩🇴', 'Ecuador': '🇪🇨', 'Egypt': '🇪🇬',
        'El Salvador': '🇸🇻', 'Equatorial Guinea': '🇬🇶', 'Eritrea': '🇪🇷',
        'Estonia': '🇪🇪', 'Ethiopia': '🇪🇹', 'Fiji': '🇫🇯', 'Finland': '🇫🇮',
        'France': '🇫🇷', 'Gabon': '🇬🇦', 'Gambia': '🇬🇲', 'Georgia': '🇬🇪',
        'Germany': '🇩🇪', 'Ghana': '🇬🇭', 'Greece': '🇬🇷', 'Guatemala': '🇬🇹',
        'Guinea': '🇬🇳', 'Guinea-Bissau': '🇬🇼', 'Guyana': '🇬🇾', 'Haiti': '🇭🇹',
        'Honduras': '🇭🇳', 'Hong Kong': '🇭🇰', 'Hungary': '🇭🇺', 'Iceland': '🇮🇸',
        'India': '🇮🇳', 'Indonesia': '🇮🇩', 'Iran': '🇮🇷', 'Iraq': '🇮🇶',
        'Ireland': '🇮🇪', 'Israel': '🇮🇱', 'Italy': '🇮🇹', 'Jamaica': '🇯🇲',
        'Japan': '🇯🇵', 'Jordan': '🇯🇴', 'Kazakhstan': '🇰🇿', 'Kenya': '🇰🇪',
        'Korea, North': '🇰🇵', 'Korea, South': '🇰🇷', 'Kuwait': '🇰🇼',
        'Kyrgyzstan': '🇰🇬', 'Laos': '🇱🇦', 'Latvia': '🇱🇻', 'Lebanon': '🇱🇧',
        'Lesotho': '🇱🇸', 'Liberia': '🇱🇷', 'Libya': '🇱🇾', 'Lithuania': '🇱🇹',
        'Luxembourg': '🇱🇺', 'Macedonia': '🇲🇰', 'Madagascar': '🇲🇬', 'Malawi': '🇲🇼',
        'Malaysia': '🇲🇾', 'Maldives': '🇲🇻', 'Mali': '🇲🇱', 'Malta': '🇲🇹',
        'Mauritania': '🇲🇷', 'Mauritius': '🇲🇺', 'Mexico': '🇲🇽', 'Moldova': '🇲🇩',
        'Mongolia': '🇲🇳', 'Montenegro': '🇲🇪', 'Morocco': '🇲🇦', 'Mozambique': '🇲🇿',
        'Myanmar': '🇲🇲', 'Namibia': '🇳🇦', 'Nepal': '🇳🇵', 'Netherlands': '🇳🇱',
        'New Zealand': '🇳🇿', 'Nicaragua': '🇳🇮', 'Niger': '🇳🇪', 'Nigeria': '🇳🇬',
        'Norway': '🇳🇴', 'Oman': '🇴🇲', 'Pakistan': '🇵🇰', 'Panama': '🇵🇦',
        'Papua New Guinea': '🇵🇬', 'Paraguay': '🇵🇾', 'Peru': '🇵🇪',
        'Philippines': '🇵🇭', 'Poland': '🇵🇱', 'Portugal': '🇵🇹', 'Qatar': '🇶🇦',
        'Romania': '🇷🇴', 'Russia': '🇷🇺', 'Rwanda': '🇷🇼', 'Saudi Arabia': '🇸🇦',
        'Senegal': '🇸🇳', 'Serbia': '🇷🇸', 'Sierra Leone': '🇸🇱', 'Singapore': '🇸🇬',
        'Slovakia': '🇸🇰', 'Slovenia': '🇸🇮', 'Somalia': '🇸🇴', 'South Africa': '🇿🇦',
        'South Sudan': '🇸🇸', 'Spain': '🇪🇸', 'Sri Lanka': '🇱🇰', 'Sudan': '🇸🇩',
        'Suriname': '🇸🇷', 'Swaziland': '🇸🇿', 'Sweden': '🇸🇪', 'Switzerland': '🇨🇭',
        'Syria': '🇸🇾', 'Taiwan': '🇹🇼', 'Tajikistan': '🇹🇯', 'Tanzania': '🇹🇿',
        'Thailand': '🇹🇭', 'Togo': '🇹🇬', 'Trinidad and Tobago': '🇹🇹',
        'Tunisia': '🇹🇳', 'Turkey': '🇹🇷', 'Turkmenistan': '🇹🇲', 'Uganda': '🇺🇬',
        'Ukraine': '🇺🇦', 'United Arab Emirates': '🇦🇪', 'United Kingdom': '🇬🇧',
        'United States': '🇺🇸', 'Uruguay': '🇺🇾', 'Uzbekistan': '🇺🇿',
        'Venezuela': '🇻🇪', 'Vietnam': '🇻🇳', 'Yemen': '🇾🇪', 'Zambia': '🇿🇲',
        'Zimbabwe': '🇿🇼'
    }
    return flag_map.get(country_name, '🌍')

def hopkins(X, n_samples=50, random_state=42):
    """
    Calculates the Hopkins statistic to test for spatial randomness.
    Close to 1 = Highly clustered. Close to 0.5 = Random.
    """
    X = np.asarray(X)
    if n_samples > X.shape[0]:
        n_samples = max(1, X.shape[0] // 2)
    rng = np.random.default_rng(random_state)
    real_idx = rng.choice(X.shape[0], size=n_samples, replace=False)
    real_points = X[real_idx]
    
    mins = X.min(axis=0)
    maxs = X.max(axis=0)
    random_points = rng.uniform(low=mins, high=maxs, size=(n_samples, X.shape[1]))
    
    nbrs = NearestNeighbors(n_neighbors=2).fit(X)
    u_dist = nbrs.kneighbors(random_points, n_neighbors=1, return_distance=True)[0].ravel()
    w_dist = nbrs.kneighbors(real_points, n_neighbors=2, return_distance=True)[0][:,1]
    
    H = u_dist.sum() / (u_dist.sum() + w_dist.sum())
    return H

# -----------------------------------------------------------------------------
# 4. Sidebar Navigation
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### Navigation")
    page = st.radio(
        'Go to:', 
        ['Project Overview', 'Data Upload & Processing', 'Visualizations & KPIs', 'Data Analysis (EDA)', 'Model & Prediction'],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### Project: Global Aid Decision Support System")
    # Strategic Global Aid Allocator
    st.caption("**Author:** P Uday Kranth")
    st.caption("**Context:** M.Sc. Mini Project")
    st.caption("**Topic:** Unsupervised Learning")
    st.caption("**Algorithm:** K-Means Clustering")
    st.markdown("---")
    st.info("Ensure you upload and preprocess data before running models.")

# -----------------------------------------------------------------------------
# PAGE: Project Overview (About)
# -----------------------------------------------------------------------------
if page == 'Project Overview':
    st.title("Global Aid Decision Support System")
    st.markdown("### Strategic Allocation of NGO Funds using Machine Learning")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-box">
        <b>Problem Statement</b><br>
        Non-Governmental Organizations (NGOs) often struggle to allocate limited financial resources effectively. 
        Manual classification of countries based on single indicators (like GDP alone) can be misleading.
        This project utilizes <b>K-Means Clustering</b> to categorize countries based on a multidimensional analysis 
        of health, economic, and social factors.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Methodology")
        st.write("1. **Data Ingestion**: Loading socio-economic datasets.")
        st.write("2. **Preprocessing**: Standardization (Scaling) to ensure fair weighting of features.")
        st.write("3. **EDA**: Analyzing distributions and correlations.")
        st.write("4. **Clustering**: Applying K-Means algorithm to identify distinct socio-economic groups.")

    with col2:
        st.image("https://img.icons8.com/clouds/500/000000/world-map.png", caption="Global Analysis")
        st.markdown("""
        **Data Source:** Help International
        **Features:** 9 Key Indicators
        **Observations:** 167 Countries
        """)

# -----------------------------------------------------------------------------
# PAGE: Data Upload & Processing
# -----------------------------------------------------------------------------
elif page == 'Data Upload & Processing':
    st.title("Data Management")
    
    # File Uploader
    st.markdown("### 1. Data Ingestion")
    col1, col2 = st.columns([1, 2])
    with col1:
        use_default = st.checkbox('Use Default Dataset (Country-data.csv)', value=True)
    with col2:
        uploaded = st.file_uploader('Or Upload Custom CSV', type=['csv'])

    # Load Logic
    if uploaded:
        df = pd.read_csv(uploaded)
        st.session_state['df_raw'] = df
        st.success('User file loaded successfully.')
    elif use_default:
        try:
            df = load_default()
            st.session_state['df_raw'] = df
        except:
            st.error("Default file not found. Please upload a CSV.")
            st.stop()
    
    if 'df_raw' in st.session_state:
        st.dataframe(st.session_state['df_raw'].head(), use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 2. Preprocessing Pipeline")
        st.write("The following steps will be applied:")
        st.markdown("- **Renaming Columns** for readability.")
        st.markdown("- **Handling Missing Values** (Dropping NAs).")
        st.markdown("- **Standard Scaling** (Normalizing data to mean=0, std=1).")
        
        if st.button('Execute Preprocessing', type="primary"):
            df_proc = st.session_state['df_raw'].copy()
            
            # 1. Rename
            mapping = {
                'child_mort': 'Child Mortality', 'health': 'Health Spending %', 
                'life_expec': 'Life Expectancy', 'total_fer': 'Total Fertility',
                'imports': 'Imports %', 'exports': 'Exports %',
                'income': 'Net Income', 'inflation': 'Inflation', 'gdpp': 'GDP per Capita'
            }
            df_proc = df_proc.rename(columns=mapping)
            
            # 2. Drop NA
            df_proc = df_proc.dropna().reset_index(drop=True)
            
            # 3. Scale
            numeric_cols = list(mapping.values())
            present_cols = [c for c in numeric_cols if c in df_proc.columns]
            
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(df_proc[present_cols])
            
            # Save to session
            st.session_state['df'] = df_proc
            st.session_state['numeric_cols'] = present_cols
            st.session_state['scaler'] = scaler
            st.session_state['X_scaled'] = X_scaled
            
            st.success(f"Preprocessing Complete. Dataset Shape: {df_proc.shape}")

# -----------------------------------------------------------------------------
# PAGE: Data Visualizations & KPIs
# -----------------------------------------------------------------------------
elif page == 'Visualizations & KPIs':
    st.title("Strategic Indicators (KPIs)")
    
    if 'df' not in st.session_state:
        st.warning("Please preprocess the data in the 'Data Upload' tab first.")
    else:
        df = st.session_state['df']
        
        # KPI Row
        st.markdown("#### Global Averages")
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Life Expectancy", f"{df['Life Expectancy'].mean():.1f} Years")
        k2.metric("GDP per Capita", f"${df['GDP per Capita'].mean():,.0f}")
        k3.metric("Child Mortality", f"{df['Child Mortality'].mean():.1f}")
        k4.metric("Net Income", f"${df['Net Income'].mean():,.0f}")
        
        st.markdown("---")
        
        # Tabs for different viz types
        tab_corr, tab_dist, tab_rank = st.tabs(["Correlations", "Distributions", "Rankings"])
        
        with tab_corr:
            st.markdown("##### Feature Correlation Matrix")
            st.write("Highlights relationships between variables. Red indicates positive correlation, Blue indicates negative.")
            corr = df.select_dtypes(include=np.number).corr()
            if PLOTLY_AVAILABLE:
                fig = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', aspect="auto")
                st.plotly_chart(fig, use_container_width=True)
            else:
                fig, ax = plt.subplots(figsize=(10,6))
                sns.heatmap(corr, annot=True, cmap='RdBu_r', ax=ax)
                st.pyplot(fig)
                
        with tab_dist:
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                st.markdown("**GDP Distribution (Sorted Line Plot)**")
                # Using Line chart of sorted values to avoid "trusting together" bars
                sorted_gdp = df['GDP per Capita'].sort_values().reset_index(drop=True)
                if PLOTLY_AVAILABLE:
                     fig = px.line(sorted_gdp, y="GDP per Capita", title="GDP per Capita (Low to High)", labels={'index': 'Country Rank'})
                     fig.update_traces(line_color='#003366')
                     st.plotly_chart(fig, use_container_width=True)
                else:
                    st.line_chart(sorted_gdp)

            with col_d2:
                # Changed to Child Mortality as requested
                st.markdown("**Child Mortality Distribution (Sorted Line Plot)**")
                sorted_mort = df['Child Mortality'].sort_values().reset_index(drop=True)
                if PLOTLY_AVAILABLE:
                     fig = px.line(sorted_mort, y="Child Mortality", title="Child Mortality Rate (Low to High)", labels={'index': 'Country Rank'})
                     fig.update_traces(line_color='#FFD700')
                     st.plotly_chart(fig, use_container_width=True)
                else:
                    st.line_chart(sorted_mort)

        with tab_rank:
            st.markdown("##### Countries requiring immediate attention (High Child Mortality)")
            top_mort = df.nlargest(10, 'Child Mortality')[['country', 'Child Mortality', 'GDP per Capita']]
            st.table(top_mort.style.background_gradient(cmap='Reds'))

# -----------------------------------------------------------------------------
# PAGE: EDA
# -----------------------------------------------------------------------------
elif page == 'Data Analysis (EDA)':
    st.title("Exploratory Data Analysis")
    if 'df' not in st.session_state:
        st.warning("Data not ready.")
    else:
        df = st.session_state['df']
        
        with st.expander("Show Descriptive Statistics", expanded=True):
            st.dataframe(df.describe().T, use_container_width=True)

        col_hop, col_viz = st.columns([1, 2])
        
        with col_hop:
            st.markdown("### Clustering Tendency")
            st.write("We use the **Hopkins Statistic** to assess if the data has meaningful clusters.")
            
            st.markdown("""
            **Hypothesis Interpretation:**
            * **H > 0.7**: High probability of clustering (Data is not random).
            * **H ≈ 0.5**: Data is randomly distributed (No clusters).
            * **H < 0.3**: Data is regularly distributed.
            """)
            
            if st.button("Calculate Hopkins Statistic"):
                H = hopkins(st.session_state['X_scaled'])
                st.metric("Hopkins Score", f"{H:.4f}")
                if H > 0.7:
                    st.success("Result: High clustering tendency detected.")
                elif H > 0.5:
                     st.info("Result: Moderate clustering tendency.")
                else:
                    st.warning("Result: Low clustering tendency (Data may be random).")
        
        with col_viz:
            st.markdown("### Bivariate Analysis: Wealth vs Health")
            # If clusters exist, use them for color
            c_col = 'cluster_label' if 'cluster_label' in df.columns else None
            
            if PLOTLY_AVAILABLE:
                fig = px.scatter(
                    df, x='GDP per Capita', y='Child Mortality', 
                    color=c_col, hover_name='country', log_x=True,
                    color_discrete_sequence=px.colors.qualitative.G10,
                    title="Economic Power vs Public Health"
                )
                st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------------------------------------
# PAGE: Model Prediction
# -----------------------------------------------------------------------------
elif page == 'Model & Prediction':
    st.title("K-Means Clustering Model")
    
    if 'X_scaled' not in st.session_state:
        st.error("Please preprocess data first.")
        st.stop()
        
    X = st.session_state['X_scaled']
    df = st.session_state['df']

    # Settings Sidebar
    st.sidebar.markdown("### Model Hyperparameters")
    k_clusters = st.sidebar.slider("Number of Clusters (k)", 2, 8, 3)
    
    # Tabs
    tab_train, tab_pred = st.tabs(["Model Training", "Country Prediction"])
    
    with tab_train:
        st.markdown("### 1. Optimal Cluster Identification")
        if st.button("Analyze Optimal k (Elbow & Silhouette)"):
            ks = range(2, 8)
            inertias, silhouettes = [], []
            for k in ks:
                km = KMeans(n_clusters=k, random_state=42).fit(X)
                inertias.append(km.inertia_)
                silhouettes.append(silhouette_score(X, km.labels_))
            
            # Plot
            fig, ax = plt.subplots(1, 2, figsize=(12, 4))
            
            # Elbow
            ax[0].plot(ks, inertias, 'o-', color='#003366')
            ax[0].set_title('Elbow Method (Inertia)')
            ax[0].set_xlabel('k'); ax[0].set_ylabel('Inertia')
            ax[0].grid(True)
            
            # Silhouette
            ax[1].plot(ks, silhouettes, 'o-', color='#FFD700')
            ax[1].set_title('Silhouette Score')
            ax[1].set_xlabel('k'); ax[1].set_ylabel('Score')
            ax[1].grid(True)
            
            st.pyplot(fig)
            st.info(f"Recommended k based on Silhouette: **{ks[np.argmax(silhouettes)]}**")

        st.markdown("---")
        st.markdown("### 2. Run Clustering")
        
        if st.button("Train Model", type="primary"):
            km = KMeans(n_clusters=k_clusters, random_state=42)
            clusters = km.fit_predict(X)
            df['cluster'] = clusters
            
            # Dynamic Labeling (Logic: Low GDP = Underdeveloped)
            means = df.groupby('cluster')['GDP per Capita'].mean().sort_values()
            labels = ['Underdeveloped', 'Developing', 'Developed']
            
            # Map labels logically
            label_map = {}
            sorted_clusters = means.index.tolist()
            
            # Interpolate labels if k != 3
            for i, c_id in enumerate(sorted_clusters):
                if i == 0: label_map[c_id] = 'Underdeveloped'
                elif i == len(sorted_clusters)-1: label_map[c_id] = 'Developed'
                else: label_map[c_id] = 'Developing'
                
            df['cluster_label'] = df['cluster'].map(label_map)
            
            # Save state
            st.session_state['km'] = km
            st.session_state['label_map'] = label_map
            st.session_state['df'] = df
            
            st.success("Model Trained Successfully!")
            
            # Final Viz
            if PLOTLY_AVAILABLE:
                # Custom colors for the 3 main categories
                color_map = {
                    'Underdeveloped': '#D9534F', # Red
                    'Developing': '#F0AD4E',     # Orange
                    'Developed': '#5CB85C'       # Green
                }
                
                fig = px.scatter(
                    df, x='GDP per Capita', y='Child Mortality', 
                    color='cluster_label', size='Net Income',
                    hover_name='country', log_x=True,
                    color_discrete_map=color_map,
                    title="Final Cluster Segmentation"
                )
                st.plotly_chart(fig, use_container_width=True)

    with tab_pred:
        if 'km' not in st.session_state:
            st.warning("Train the model first.")
        else:
            # NEW FEATURE: Country Selector
            st.markdown("### 🌍 Check Existing Country Classification")
            st.write("Select a country from the dropdown to view its development status.")
            
            if 'cluster_label' in df.columns:
                # Create dropdown with country names
                country_list = sorted(df['country'].unique().tolist())
                selected_country = st.selectbox(
                    "Choose a Country:",
                    options=['-- Select a Country --'] + country_list,
                    index=0
                )
                
                if selected_country != '-- Select a Country --':
                    # Get country data
                    country_data = df[df['country'] == selected_country].iloc[0]
                    country_status = country_data['cluster_label']
                    
                    # Display result with appropriate styling
                    st.markdown("---")
                    result_msg = f"**{selected_country}** is classified as: **{country_status}**"
                    
                    if country_status == 'Underdeveloped':
                        st.error(result_msg)
                    elif country_status == 'Developing':
                        st.warning(result_msg)
                    elif country_status == 'Developed':
                        st.success(result_msg)
                    else:
                        st.info(result_msg)
                    
                    # Show key metrics
                    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
                    col_m1.metric("GDP per Capita", f"${country_data['GDP per Capita']:,.0f}")
                    col_m2.metric("Life Expectancy", f"{country_data['Life Expectancy']:.1f} yrs")
                    col_m3.metric("Child Mortality", f"{country_data['Child Mortality']:.1f}")
                    col_m4.metric("Net Income", f"${country_data['Net Income']:,.0f}")
            else:
                st.info("Train the model first to see country classifications.")
            
            st.markdown("---")
            st.markdown("### 🔮 Simulate New Country Data")
            st.write("Input socio-economic parameters to predict classification.")
            
            with st.form("pred_form"):
                st.markdown("#### Country Info")
                country_name_input = st.text_input("Country Name", value="New Country")

                st.markdown("#### Economic Indicators")
                col_p1, col_p2 = st.columns(2)
                with col_p1:
                    # Removed limits (min_value=None) as requested
                    gdpp = st.number_input("GDP per Capita ($)", value=1000.0)
                    income = st.number_input("Net Income ($)", value=1500.0)
                    child_mort = st.number_input("Child Mortality (per 1000)", value=50.0)
                with col_p2:
                    life_expec = st.number_input("Life Expectancy (Years)", value=65.0)
                    inflation = st.number_input("Inflation (%)", value=5.0)
                    imports = st.number_input("Imports (% GDP)", value=30.0)
                
                submitted = st.form_submit_button("Predict Status")
                
                if submitted:
                    # Prepare input vector (Using means for missing features)
                    cols_needed = st.session_state['numeric_cols']
                    input_vec = []
                    
                    user_vals = {
                        'GDP per Capita': gdpp, 'Net Income': income, 
                        'Child Mortality': child_mort, 'Life Expectancy': life_expec,
                        'Inflation': inflation, 'Imports %': imports
                    }
                    
                    for c in cols_needed:
                        if c in user_vals:
                            input_vec.append(user_vals[c])
                        else:
                            input_vec.append(df[c].mean()) # Fill unknowns with average
                            
                    # Scale & Predict
                    vec_scaled = st.session_state['scaler'].transform([input_vec])
                    pred_cluster = st.session_state['km'].predict(vec_scaled)[0]
                    pred_label = st.session_state['label_map'].get(pred_cluster, "Unknown")
                    
                    st.markdown("---")
                    
                    # Output logic as requested: "Developed" / "Underdeveloped" etc.
                    result_msg = f"The country **{country_name_input}** is classified as: **{pred_label}**"
                    
                    if pred_label == 'Underdeveloped':
                        st.error(result_msg)
                    elif pred_label == 'Developing':
                        st.warning(result_msg)
                    elif pred_label == 'Developed':
                        st.success(result_msg)
                    else:
                        st.info(result_msg)