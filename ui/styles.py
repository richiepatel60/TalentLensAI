import streamlit as st


def load_css():
    st.markdown("""
    <style>
        /* ── Font Imports ── */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        /* ── Reset & Base ── */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        html {
            scroll-behavior: smooth;
        }

        .stApp {
            background: linear-gradient(135deg, #0F0F1A 0%, #1A1A2E 50%, #0F0F1A 100%);
        }

        /* ── Remove Default Streamlit Chrome ── */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        header { visibility: hidden; }

        .stAppToolbar {
            display: none !important;
        }

        /* ── Sidebar ── */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #12122A 0%, #1A1A2E 100%);
            border-right: 1px solid rgba(99, 102, 241, 0.15);
            backdrop-filter: blur(20px);
        }

        section[data-testid="stSidebar"] .stRadio {
            padding: 0 0.5rem;
        }

        section[data-testid="stSidebar"] .stRadio > label {
            display: flex;
            align-items: center;
            padding: 0.75rem 1rem;
            margin-bottom: 0.25rem;
            border-radius: 12px;
            color: #94A3B8;
            font-weight: 500;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        section[data-testid="stSidebar"] .stRadio > label:hover {
            background: rgba(99, 102, 241, 0.08);
            color: #E2E8F0;
        }

        section[data-testid="stSidebar"] .stRadio > div[data-testid="stRadioSelected"] {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.1));
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 12px;
            color: #E2E8F0 !important;
        }

        section[data-testid="stSidebar"] .stRadio > div {
            gap: 0 !important;
        }

        /* ── Sidebar Logo ── */
        .sidebar-logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 1.5rem 1rem 2rem;
            border-bottom: 1px solid rgba(99, 102, 241, 0.1);
            margin-bottom: 1.5rem;
        }

        .sidebar-logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #6366F1, #8B5CF6);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            font-weight: 700;
            color: white;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }

        .sidebar-logo-text {
            font-size: 1.1rem;
            font-weight: 700;
            color: #E2E8F0;
            letter-spacing: -0.02em;
        }

        .sidebar-logo-sub {
            font-size: 0.7rem;
            color: #64748B;
            font-weight: 400;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }

        /* ── Main Content ── */
        .main-header {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1.5rem 0;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid rgba(99, 102, 241, 0.1);
        }

        .main-header-icon {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #6366F1, #8B5CF6);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            box-shadow: 0 4px 16px rgba(99, 102, 241, 0.25);
        }

        .main-header-title {
            font-size: 1.6rem;
            font-weight: 800;
            color: #F1F5F9;
            letter-spacing: -0.03em;
            line-height: 1.2;
        }

        .main-header-subtitle {
            font-size: 0.85rem;
            color: #64748B;
            font-weight: 400;
        }

        /* ── Cards ── */
        .glass-card {
            background: linear-gradient(135deg, rgba(26, 26, 46, 0.8), rgba(15, 15, 26, 0.6));
            border: 1px solid rgba(99, 102, 241, 0.12);
            border-radius: 16px;
            padding: 1.5rem;
            backdrop-filter: blur(20px);
            transition: all 0.3s ease;
            margin-bottom: 1rem;
        }

        .glass-card:hover {
            border-color: rgba(99, 102, 241, 0.25);
            box-shadow: 0 8px 32px rgba(99, 102, 241, 0.1);
            transform: translateY(-1px);
        }

        .glass-card-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #E2E8F0;
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* ── Metric Card ── */
        .metric-card {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(139, 92, 246, 0.05));
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 8px 32px rgba(99, 102, 241, 0.15);
            transform: translateY(-2px);
        }

        .metric-value {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #6366F1, #A78BFA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1;
        }

        .metric-label {
            font-size: 0.85rem;
            color: #94A3B8;
            margin-top: 0.5rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* ── Status Badges ── */
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            padding: 0.35rem 0.85rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            letter-spacing: 0.02em;
        }

        .status-badge-excellent {
            background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(34, 197, 94, 0.05));
            color: #4ADE80;
            border: 1px solid rgba(34, 197, 94, 0.25);
        }

        .status-badge-good {
            background: linear-gradient(135deg, rgba(234, 179, 8, 0.15), rgba(234, 179, 8, 0.05));
            color: #FBBF24;
            border: 1px solid rgba(234, 179, 8, 0.25);
        }

        .status-badge-review {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(239, 68, 68, 0.05));
            color: #F87171;
            border: 1px solid rgba(239, 68, 68, 0.25);
        }

        /* ── Skill Tags ── */
        .skill-tag {
            display: inline-block;
            padding: 0.3rem 0.75rem;
            margin: 0.2rem 0.3rem;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(139, 92, 246, 0.08));
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 8px;
            font-size: 0.8rem;
            color: #A5B4FC;
            font-weight: 500;
            transition: all 0.2s ease;
        }

        .skill-tag:hover {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.2), rgba(139, 92, 246, 0.15));
            border-color: rgba(99, 102, 241, 0.4);
            transform: translateY(-1px);
        }

        .skill-tag-matching {
            background: linear-gradient(135deg, rgba(34, 197, 94, 0.12), rgba(34, 197, 94, 0.08));
            border-color: rgba(34, 197, 94, 0.2);
            color: #86EFAC;
        }

        .skill-tag-missing {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.12), rgba(239, 68, 68, 0.08));
            border-color: rgba(239, 68, 68, 0.2);
            color: #FCA5A5;
        }

        /* ── Info Box ── */
        .info-box {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.08), rgba(99, 102, 241, 0.05));
            border: 1px solid rgba(59, 130, 246, 0.15);
            border-left: 4px solid #6366F1;
            border-radius: 12px;
            padding: 1.25rem;
            color: #CBD5E1;
            font-size: 0.9rem;
            line-height: 1.6;
        }

        /* ── Success / Warning / Error Boxes ── */
        .success-box {
            background: linear-gradient(135deg, rgba(34, 197, 94, 0.08), rgba(34, 197, 94, 0.03));
            border: 1px solid rgba(34, 197, 94, 0.15);
            border-left: 4px solid #22C55E;
            border-radius: 12px;
            padding: 1rem 1.25rem;
            color: #BBF7D0;
            font-size: 0.9rem;
        }

        .warning-box {
            background: linear-gradient(135deg, rgba(234, 179, 8, 0.08), rgba(234, 179, 8, 0.03));
            border: 1px solid rgba(234, 179, 8, 0.15);
            border-left: 4px solid #EAB308;
            border-radius: 12px;
            padding: 1rem 1.25rem;
            color: #FDE68A;
            font-size: 0.9rem;
        }

        .error-box {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.08), rgba(239, 68, 68, 0.03));
            border: 1px solid rgba(239, 68, 68, 0.15);
            border-left: 4px solid #EF4444;
            border-radius: 12px;
            padding: 1rem 1.25rem;
            color: #FCA5A5;
            font-size: 0.9rem;
        }

        /* ── Divider ── */
        .custom-divider {
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.2), transparent);
            margin: 1.5rem 0;
        }

        /* ── File Uploader ── */
        .stFileUploader > div {
            border: 2px dashed rgba(99, 102, 241, 0.25) !important;
            border-radius: 16px !important;
            background: rgba(99, 102, 241, 0.03) !important;
            padding: 1.5rem !important;
            transition: all 0.3s ease !important;
        }

        .stFileUploader > div:hover {
            border-color: rgba(99, 102, 241, 0.5) !important;
            background: rgba(99, 102, 241, 0.06) !important;
        }

        /* ── Text Areas ── */
        .stTextArea textarea {
            background: rgba(26, 26, 46, 0.6) !important;
            border: 1px solid rgba(99, 102, 241, 0.15) !important;
            border-radius: 12px !important;
            color: #E2E8F0 !important;
            font-size: 0.9rem !important;
            line-height: 1.6 !important;
            transition: all 0.2s ease !important;
        }

        .stTextArea textarea:focus {
            border-color: rgba(99, 102, 241, 0.5) !important;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
        }

        /* ── Radio Buttons ── */
        .stRadio > div {
            display: flex !important;
            gap: 0.75rem !important;
        }

        .stRadio > div > label {
            background: rgba(26, 26, 46, 0.6) !important;
            border: 1px solid rgba(99, 102, 241, 0.12) !important;
            border-radius: 10px !important;
            padding: 0.5rem 1rem !important;
            color: #94A3B8 !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            transition: all 0.2s ease !important;
            cursor: pointer !important;
        }

        .stRadio > div > label:hover {
            border-color: rgba(99, 102, 241, 0.3) !important;
            background: rgba(99, 102, 241, 0.06) !important;
            color: #E2E8F0 !important;
        }

        .stRadio > div > label[data-selected="true"] {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(139, 92, 246, 0.1)) !important;
            border-color: rgba(99, 102, 241, 0.4) !important;
            color: #E2E8F0 !important;
        }

        /* ── Buttons ── */
        .stButton button {
            background: linear-gradient(135deg, #6366F1, #8B5CF6) !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.6rem 2rem !important;
            color: white !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            letter-spacing: 0.02em !important;
            box-shadow: 0 4px 16px rgba(99, 102, 241, 0.3) !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
        }

        .stButton button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4) !important;
        }

        .stButton button:active {
            transform: translateY(0) !important;
        }

        /* ── Progress / Spinner ── */
        .stSpinner > div {
            border-color: #6366F1 !important;
        }

        /* ── Expander ── */
        .streamlit-expanderHeader {
            background: rgba(26, 26, 46, 0.6) !important;
            border: 1px solid rgba(99, 102, 241, 0.1) !important;
            border-radius: 12px !important;
            color: #E2E8F0 !important;
            font-weight: 500 !important;
            padding: 0.75rem 1rem !important;
        }

        .streamlit-expanderContent {
            border: 1px solid rgba(99, 102, 241, 0.1) !important;
            border-top: none !important;
            border-radius: 0 0 12px 12px !important;
            background: rgba(26, 26, 46, 0.3) !important;
            padding: 1rem !important;
        }

        /* ── Column Gap Fix ── */
        div[data-testid="column"] {
            gap: 1rem !important;
        }

        /* ── Subheader ── */
        .stSubheader {
            color: #E2E8F0 !important;
            font-weight: 600 !important;
            letter-spacing: -0.01em !important;
        }

        /* ── Write / Text ── */
        .stMarkdown p {
            color: #CBD5E1;
            line-height: 1.6;
        }

        /* ── Footer ── */
        .app-footer {
            text-align: center;
            padding: 2rem 0 1rem;
            border-top: 1px solid rgba(99, 102, 241, 0.08);
            margin-top: 3rem;
        }

        .app-footer p {
            color: #475569;
            font-size: 0.8rem;
        }

        /* ── Animated Entry ── */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .fade-in {
            animation: fadeInUp 0.4s ease-out;
        }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar {
            width: 6px;
        }

        ::-webkit-scrollbar-track {
            background: transparent;
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(99, 102, 241, 0.2);
            border-radius: 3px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(99, 102, 241, 0.4);
        }
    </style>
    """, unsafe_allow_html=True)
