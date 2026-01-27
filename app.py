import streamlit as st
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Sniper Marketing Co-Pilot",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark mode professional aesthetic
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00d4ff, #7b2cbf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subheader {
        color: #a0a0a0;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .pain-point-card {
        background: linear-gradient(135deg, #1e1e2e 0%, #2a2a3e 100%);
        border-left: 4px solid #00d4ff;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        transition: transform 0.2s;
    }
    .pain-point-card:hover {
        transform: translateX(5px);
    }
    .ad-preview {
        background: linear-gradient(135deg, #2a2a3e 0%, #1e1e2e 100%);
        border: 2px solid #7b2cbf;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(123, 44, 191, 0.3);
    }
    .cta-button {
        background: linear-gradient(90deg, #00d4ff, #7b2cbf);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        text-align: center;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #2d1b00;
        border-left: 4px solid #ff6b00;
        padding: 1rem;
        border-radius: 5px;
        color: #ffa500;
    }
    .success-box {
        background-color: #001a0d;
        border-left: 4px solid #00ff88;
        padding: 1rem;
        border-radius: 5px;
        color: #00ff88;
    }
</style>
""", unsafe_allow_html=True)

# Mock data engine
def generate_pain_points(niche, audience):
    """Simulates finding pain points from Reddit based on user input"""
    pain_point_database = {
        "coffee": [
            {
                "title": "☕ Coffee Stains Ruining My Smile",
                "description": "Frustrated coffee drinkers complaining about teeth staining despite loving their daily brew",
                "sentiment": "High Frustration",
                "mentions": 1247
            },
            {
                "title": "😤 Bitterness Overload Every Morning",
                "description": "Users struggling with overly bitter coffee that ruins their morning routine",
                "sentiment": "Medium Frustration",
                "mentions": 892
            },
            {
                "title": "💸 Expensive Coffee Addiction",
                "description": "People shocked by how much they spend on coffee shops monthly",
                "sentiment": "High Concern",
                "mentions": 2103
            }
        ],
        "fitness": [
            {
                "title": "💪 No Time for the Gym",
                "description": "Busy professionals complaining they can't fit workouts into their schedule",
                "sentiment": "High Frustration",
                "mentions": 3421
            },
            {
                "title": "😓 Plateaued Progress",
                "description": "Fitness enthusiasts stuck at the same weight/strength level for months",
                "sentiment": "Demotivation",
                "mentions": 1876
            },
            {
                "title": "🤕 Injury-Prone Workouts",
                "description": "People getting injured from improper form or overtraining",
                "sentiment": "High Concern",
                "mentions": 1342
            }
        ],
        "productivity": [
            {
                "title": "📧 Email Overload Killing Focus",
                "description": "Professionals drowning in unread emails and losing hours daily",
                "sentiment": "High Stress",
                "mentions": 4567
            },
            {
                "title": "⏰ Meeting Fatigue",
                "description": "Workers complaining about back-to-back meetings with no time for actual work",
                "sentiment": "Burnout",
                "mentions": 3214
            },
            {
                "title": "🔄 Switching Between Apps",
                "description": "Context switching between 10+ tools destroying productivity",
                "sentiment": "Medium Frustration",
                "mentions": 2890
            }
        ],
        "default": [
            {
                "title": f"🎯 {audience} Struggling with Time Management",
                "description": f"Members of your target audience expressing frustration about not having enough time for {niche}",
                "sentiment": "High Frustration",
                "mentions": random.randint(800, 2000)
            },
            {
                "title": f"💰 Cost Concerns in {niche}",
                "description": f"{audience} complaining about the high cost of quality {niche} products/services",
                "sentiment": "Price Sensitivity",
                "mentions": random.randint(1000, 3000)
            },
            {
                "title": f"🤔 Confusion About {niche} Options",
                "description": f"Your audience overwhelmed by too many choices and conflicting information about {niche}",
                "sentiment": "Decision Paralysis",
                "mentions": random.randint(900, 2500)
            }
        ]
    }
    
    niche_lower = niche.lower()
    for key in pain_point_database.keys():
        if key in niche_lower:
            return pain_point_database[key]
    
    return pain_point_database["default"]

def generate_sniper_ad(pain_point, niche, audience):
    """Generates a targeted 'Sniper Ad' based on selected pain point"""
    ad_templates = {
        "stain": {
            "headline": "Finally: Coffee Without the Stains ☕",
            "body": f"Tired of yellow teeth ruining your confidence? Our {niche} solution lets you enjoy your daily brew without the guilt. {audience} are already making the switch.",
            "cta": "Get Stain-Free Coffee →"
        },
        "bitter": {
            "headline": "Say Goodbye to Bitter Mornings 🌅",
            "body": f"Stop forcing down bitter {niche}. Our smooth blend is scientifically engineered for taste, not just caffeine. Join 10,000+ {audience} who love their mornings again.",
            "cta": "Try Smooth Coffee →"
        },
        "expensive": {
            "headline": "$5/Day? That's $1,825/Year on Coffee 💸",
            "body": f"Stop hemorrhaging money at coffee shops. Our premium {niche} costs just $0.50/cup. Perfect for {audience} who love quality but hate waste.",
            "cta": "Calculate Your Savings →"
        },
        "time": {
            "headline": f"Get Results in 15 Minutes/Day ⏰",
            "body": f"No time for {niche}? Wrong. Our system is designed for busy {audience}. Quick, effective, and proven to work.",
            "cta": "Start 15-Min Challenge →"
        },
        "plateau": {
            "headline": "Stuck? Here's Why (And How to Fix It) 📈",
            "body": f"That plateau isn't your fault. 94% of {audience} make the same 3 mistakes. Our {niche} program breaks through in weeks, not months.",
            "cta": "Break Your Plateau →"
        },
        "default": {
            "headline": f"Built for {audience} Who Want Real Results 🎯",
            "body": f"Stop wasting time on generic {niche} solutions. We analyzed 10,000+ {audience} to create something that actually works for YOUR specific needs.",
            "cta": f"See How It Works →"
        }
    }
    
    # Match pain point to template
    pain_lower = pain_point.lower()
    if "stain" in pain_lower:
        return ad_templates["stain"]
    elif "bitter" in pain_lower:
        return ad_templates["bitter"]
    elif "expensive" in pain_lower or "cost" in pain_lower:
        return ad_templates["expensive"]
    elif "time" in pain_lower:
        return ad_templates["time"]
    elif "plateau" in pain_lower:
        return ad_templates["plateau"]
    else:
        return ad_templates["default"]

# Initialize session state
if 'pain_points' not in st.session_state:
    st.session_state.pain_points = None
if 'selected_pain' not in st.session_state:
    st.session_state.selected_pain = None
if 'generated_ad' not in st.session_state:
    st.session_state.generated_ad = None

# Main header
st.markdown('<h1 class="main-header">🎯 Sniper Marketing Co-Pilot</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Turn Reddit Pain Points Into Precision Ad Campaigns</p>', unsafe_allow_html=True)

# Sidebar - The IKEA Effect Input
with st.sidebar:
    st.markdown("# 🎯 SNIPER MARKETING")
    st.markdown("## 🎯 Campaign Setup")
    st.markdown("---")
    
    product_niche = st.text_input(
        "Product Niche",
        placeholder="e.g., Coffee, Fitness, Productivity",
        help="What product or service are you marketing?"
    )
    
    target_audience = st.text_input(
        "Target Audience",
        placeholder="e.g., Remote Workers, Gym Enthusiasts",
        help="Who are you trying to reach?"
    )
    
    st.markdown("---")
    
    if st.button("🔍 Find Pain Points", use_container_width=True, type="primary"):
        if product_niche and target_audience:
            with st.spinner("Analyzing Reddit conversations..."):
                st.session_state.pain_points = generate_pain_points(product_niche, target_audience)
                st.session_state.selected_pain = None
                st.session_state.generated_ad = None
                st.success(f"Found {len(st.session_state.pain_points)} pain points!")
        else:
            st.error("Please fill in both fields")
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Campaigns", "247", "+12")
    with col2:
        st.metric("Avg ROI", "342%", "+23%")
    
    st.markdown("---")
    st.markdown("### 🔗 Resources")
    st.markdown("[📚 Documentation](https://example.com)")
    st.markdown("[🎥 Video Tutorial](https://example.com)")
    st.markdown("[💬 Community](https://example.com)")

# Main content area
if st.session_state.pain_points:
    st.markdown("## 💡 Discovered Pain Points")
    st.markdown("**Select the pain point that best matches your campaign goals:**")
    
    # Display pain points in columns
    cols = st.columns(3)
    for idx, pain in enumerate(st.session_state.pain_points):
        with cols[idx]:
            st.markdown(f"""
            <div class="pain-point-card">
                <h3>{pain['title']}</h3>
                <p style="color: #b0b0b0;">{pain['description']}</p>
                <hr style="border-color: #404040;">
                <p><strong>Sentiment:</strong> <span style="color: #ff6b6b;">{pain['sentiment']}</span></p>
                <p><strong>Mentions:</strong> <span style="color: #00d4ff;">{pain['mentions']:,}</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Select This Pain Point", key=f"pain_{idx}", use_container_width=True):
                st.session_state.selected_pain = pain
                st.session_state.generated_ad = generate_sniper_ad(
                    pain['title'],
                    product_niche,
                    target_audience
                )
                st.rerun()

# Display generated ad
if st.session_state.generated_ad and st.session_state.selected_pain:
    st.markdown("---")
    st.markdown("## 🎯 Your Sniper Ad")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        ad = st.session_state.generated_ad
        st.markdown(f"""
        <div class="ad-preview">
            <h2 style="color: #00d4ff; margin-bottom: 1rem;">{ad['headline']}</h2>
            <p style="font-size: 1.1rem; color: #e0e0e0; line-height: 1.6; margin-bottom: 2rem;">
                {ad['body']}
            </p>
            <div class="cta-button">
                {ad['cta']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📈 Ad Performance Prediction"):
            metric_cols = st.columns(4)
            with metric_cols[0]:
                st.metric("Est. CTR", "4.2%", "+1.8%")
            with metric_cols[1]:
                st.metric("Conv. Rate", "12.5%", "+3.2%")
            with metric_cols[2]:
                st.metric("CPA", "$18.50", "-$6.20")
            with metric_cols[3]:
                st.metric("ROAS", "5.8x", "+2.1x")
            
            st.markdown("**Why This Works:**")
            st.markdown(f"- Directly addresses pain point: _{st.session_state.selected_pain['title']}_")
            st.markdown(f"- Targets high-intent audience: {target_audience}")
            st.markdown(f"- Uses social proof and specificity")
            st.markdown(f"- Clear, benefit-driven CTA")
    
    with col2:
        st.markdown("### 🎨 Ad Variations")
        st.info("**A/B Test Ideas:**\n- Test different headlines\n- Vary social proof numbers\n- Try urgency vs. value CTAs")
        
        st.markdown("### 🎯 Targeting")
        st.success(f"**Audience:** {target_audience}\n**Interest:** {product_niche}\n**Pain Point:** {st.session_state.selected_pain['sentiment']}")
        
        st.markdown("### 📱 Platforms")
        platforms = st.multiselect(
            "Deploy to:",
            ["Facebook Ads", "Google Ads", "Reddit Ads", "LinkedIn Ads"],
            default=["Reddit Ads"]
        )

# Welcome Screen - Show only if no pain points generated yet
if not st.session_state.pain_points:
    st.info("👈 **Get started:** Enter your Product Niche and Target Audience in the sidebar, then click 'Find Pain Points'")
    
    # Show demo metrics
    st.markdown("## 🔥 Why Sniper Marketing?")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Avg ROI", "342%", "+89%")
    with col2:
        st.metric("Cost Savings", "67%", "+12%")
    with col3:
        st.metric("Time Saved", "23hrs/mo", "+8hrs")
    with col4:
        st.metric("Campaigns", "2.4K+", "+340")
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Precision Targeting")
        st.markdown("Stop wasting budget on broad audiences. Find exact pain points your audience is discussing right now.")
    
    with col2:
        st.markdown("### 🛡️ Built-in Safety")
        st.markdown("Set kill switches and budget limits. Never overspend or underperform without knowing immediately.")
    
    with col3:
        st.markdown("### ⚡ Lightning Fast")
        st.markdown("From pain point discovery to live ad in under 5 minutes. No more weeks of research and testing.")

# Safety Shield UI - Always shows at bottom
st.markdown("---")
st.markdown("## 🛡️ Safety Shield - Budget Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💰 Daily Budget")
    daily_budget = st.number_input("Set Daily Limit ($)", min_value=10, max_value=10000, value=100, step=10)
    st.progress(min(75/100, 1.0))
    st.caption(f"Spent: $75 / ${daily_budget}")

with col2:
    st.markdown("### 🔴 Kill Switch")
    kill_switch_metric = st.selectbox(
        "Auto-pause when:",
        ["CPA exceeds $50", "ROAS drops below 2x", "CTR below 1%", "Budget depleted"]
    )
    st.markdown('<div class="warning-box">⚠️ Kill switch is ACTIVE</div>', unsafe_allow_html=True)

with col3:
    st.markdown("### 📊 Real-Time Status")
    campaign_status = st.radio("Campaign Status", ["Active", "Paused", "Testing"], horizontal=True)
    if campaign_status == "Active":
        st.markdown('<div class="success-box">✅ Campaign running smoothly</div>', unsafe_allow_html=True)

# Advanced controls in expander
with st.expander("⚙️ Advanced Safety Controls"):
    col1, col2 = st.columns(2)
    with col1:
        st.slider("Max CPA ($)", 0, 200, 50)
        st.slider("Min ROAS", 1.0, 10.0, 3.0, 0.5)
    with col2:
        st.number_input("Monthly Cap ($)", min_value=100, value=3000, step=100)
        st.checkbox("Auto-optimize bids", value=True)

# Feedback & Waitlist - Always shows at bottom
st.markdown("---")
st.markdown("## 🚀 Join the Revolution")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 💬 Give Feedback")
    st.markdown("Help us build the perfect marketing co-pilot")
    if st.button("📝 Open Feedback Form", use_container_width=True, type="secondary"):
        st.markdown("[Click here to share your thoughts](https://forms.google.com/)")
        st.balloons()

with col2:
    st.markdown("### ⚡ Get Early Access")
    email = st.text_input("Enter your email", placeholder="you@company.com")
    if st.button("🎯 Join Waitlist", use_container_width=True, type="primary"):
        if email and "@" in email:
            st.success(f"🎉 {email} added to waitlist!")
            st.snow()
        else:
            st.error("Please enter a valid email")

# Footer - Always shows at bottom
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #606060; padding: 2rem 0;">
    <p>🎯 Sniper Marketing Co-Pilot v1.0 | Built for Precision Marketers</p>
    <p style="font-size: 0.9rem;">Stop spraying ads everywhere. Start sniping pain points.</p>
</div>
""", unsafe_allow_html=True)
