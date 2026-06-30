import streamlit as st


def render_header(icon: str, title: str, subtitle: str = ""):
    """Render a consistent page header with icon and title."""
    st.markdown(f"""
    <div class="main-header fade-in">
        <div class="main-header-icon">{icon}</div>
        <div>
            <div class="main-header-title">{title}</div>
            {f'<div class="main-header-subtitle">{subtitle}</div>' if subtitle else ''}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_card(title: str = "", icon: str = "", key: str = ""):
    """Open a glass-card container. Use with `with` or call start_card/end_card manually."""
    icon_html = f"<span>{icon}</span>" if icon else ""
    title_html = f"<div class='glass-card-title'>{icon_html} {title}</div>" if title else ""
    card_key = f"card-{key}" if key else ""
    start = f"""
    <div class="glass-card fade-in" id="{card_key}">
        {title_html}
    """
    st.markdown(start, unsafe_allow_html=True)
    # We use a container inside so streamlit elements render inside the card
    return st.container()


def end_card():
    """Close a glass-card container."""
    st.markdown("</div>", unsafe_allow_html=True)


def render_metric_card(value: str, label: str):
    """Render a styled metric card."""
    st.markdown(f"""
    <div class="metric-card fade-in">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def render_skill_tags(skills: list, variant: str = "default"):
    """Render a list of skills as styled tags.
    
    Args:
        skills: List of skill strings.
        variant: 'default', 'matching', or 'missing'.
    """
    if not skills:
        st.markdown("<p style='color: #64748B; font-size: 0.85rem;'>No skills listed</p>", unsafe_allow_html=True)
        return
    
    cls = f"skill-tag-{variant}" if variant != "default" else "skill-tag"
    tags_html = "".join(f'<span class="{cls}">{skill}</span>' for skill in skills)
    st.markdown(f'<div class="fade-in">{tags_html}</div>', unsafe_allow_html=True)


def render_status_badge(status: str, score: int = None):
    """Render a status badge based on match score.
    
    Args:
        status: 'excellent', 'good', or 'review'.
        score: Optional match percentage to display.
    """
    labels = {
        "excellent": ("🟢 Excellent Match", "status-badge-excellent"),
        "good": ("🟡 Good Match", "status-badge-good"),
        "review": ("🔴 Needs Review", "status-badge-review"),
    }
    label, cls = labels.get(status, ("Unknown", "status-badge-review"))
    
    score_text = f" — {score}%" if score is not None else ""
    st.markdown(
        f'<span class="status-badge {cls} fade-in">{label}{score_text}</span>',
        unsafe_allow_html=True
    )


def render_page_title(title: str):
    """Render the sidebar logo and branding."""
    st.sidebar.markdown("""
    <div class="sidebar-logo">
        <div class="sidebar-logo-icon">TL</div>
        <div>
            <div class="sidebar-logo-text">TalentLensAI</div>
            <div class="sidebar-logo-sub">Smart Hiring</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render the app footer."""
    st.markdown("""
    <div class="app-footer">
        <p>TalentLensAI — AI-Powered Resume Analysis & Candidate Matching</p>
    </div>
    """, unsafe_allow_html=True)


def render_info_box(content: str):
    """Render an info box with styled content. Returns HTML string."""
    return f'<div class="info-box fade-in">{content}</div>'


def render_success_box(content: str):
    """Render a success box. Returns HTML string."""
    return f'<div class="success-box fade-in">{content}</div>'


def render_warning_box(content: str):
    """Render a warning box. Returns HTML string."""
    return f'<div class="warning-box fade-in">{content}</div>'


def render_error_box(content: str):
    """Render an error box. Returns HTML string."""
    return f'<div class="error-box fade-in">{content}</div>'


def render_divider():
    """Render a styled divider. Returns HTML string."""
    return '<div class="custom-divider"></div>'
