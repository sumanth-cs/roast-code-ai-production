# import streamlit as st
# from streamlit_option_menu import option_menu

# # Import pages
# from pages import (
#     code_analysis,
#     code_generation,
#     collaboration,
#     metrics_dashboard
# )

# def main():
#     st.set_page_config(
#         page_title="Roast Code AI - Advanced Code Companion",
#         page_icon="🔥",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )
    
#     # Custom CSS
#     with open("frontend/static/css/styles.css") as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
#     # Sidebar navigation
#     with st.sidebar:
#         st.image("https://img.icons8.com/color/96/000000/python.png", width=100)
#         st.title("🔥 Roast Code AI")
#         st.markdown("---")
        
#         selected = option_menu(
#             menu_title="Navigation",
#             options=["Code Analysis", "Code Generation", "Collaboration", "Metrics Dashboard"],
#             icons=["search", "code-slash", "people", "graph-up"],
#             menu_icon="cast",
#             default_index=0,
#             styles={
#                 "container": {"padding": "0!important"},
#                 "icon": {"color": "orange", "font-size": "18px"},
#                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
#                 "nav-link-selected": {"background-color": "#ff4b4b"},
#             }
#         )
        
#         st.markdown("---")
#         st.markdown("### 🤖 Features")
#         st.markdown("""
#         - Multi-language Support
#         - Real-time Collaboration
#         - AI-powered Code Analysis
#         - Voice Feedback
#         - Code Quality Metrics
#         """)
        
#         st.markdown("---")
#         st.markdown("### 📊 Stats")
#         if 'stats' in st.session_state:
#             cols = st.columns(2)
#             cols[0].metric("Analyses", st.session_state.stats.get('analyses', 0))
#             cols[1].metric("Generations", st.session_state.stats.get('generations', 0))
    
#     # Page routing
#     if selected == "Code Analysis":
#         code_analysis.render()
#     elif selected == "Code Generation":
#         code_generation.render()
#     elif selected == "Collaboration":
#         collaboration.render()
#     elif selected == "Metrics Dashboard":
#         metrics_dashboard.render()

# if __name__ == "__main__":
#     main()

# frontend/app.py - SIMPLE VERSION
import streamlit as st
from streamlit_option_menu import option_menu
import requests
import json

st.set_page_config(
    page_title="Roast Code AI",
    page_icon="🔥",
    layout="wide"
)

# Initialize session state
if 'code' not in st.session_state:
    st.session_state.code = ""
if 'result' not in st.session_state:
    st.session_state.result = None

# Sidebar
with st.sidebar:
    st.image("🔥", width=100)
    st.title("Roast Code AI")
    st.markdown("---")
    
    selected = option_menu(
        menu_title="Navigation",
        options=["Code Analysis", "Code Generation"],
        icons=["search", "code-slash"],
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#ff4b4b"},
        }
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    AI-powered code analysis with humorous feedback.
    Paste your code, get roasted, and improve!
    """)

# Main content
if selected == "Code Analysis":
    st.title("🔍 Code Analysis")
    st.markdown("Paste your code below and get AI-powered feedback!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        code = st.text_area(
            "Your Code",
            height=400,
            placeholder="Paste your Python, JavaScript, or other code here...",
            key="code_input"
        )
        
        language = st.selectbox(
            "Language",
            ["python", "javascript", "java", "cpp", "other"]
        )
        
        roast_intensity = st.select_slider(
            "Roast Intensity",
            options=["mild", "medium", "brutal"],
            value="medium"
        )
        
        if st.button("🔥 Analyze & Roast My Code!", type="primary", use_container_width=True):
            if code.strip():
                with st.spinner("Analyzing your code... This might take a moment."):
                    try:
                        # Try to call backend
                        response = requests.post(
                            "/api/analyze",
                            json={
                                "code": code,
                                "language": language,
                                "roast_level": roast_intensity
                            },
                            timeout=30
                        )
                        
                        if response.status_code == 200:
                            st.session_state.result = response.json()
                            st.success("Analysis complete!")
                        else:
                            st.error(f"Backend error: {response.status_code}")
                            # Fallback to mock result
                            st.session_state.result = {
                                "success": True,
                                "analysis": {
                                    "issues": ["Mock analysis - backend not responding"],
                                    "metrics": {"line_count": len(code.splitlines())},
                                    "quality_score": 75,
                                    "grade": "B"
                                },
                                "roast": {
                                    "text": "Your code looks decent! (Mock analysis)",
                                    "intensity": roast_intensity,
                                    "model": "mock"
                                },
                                "suggestions": ["Add comments", "Write tests", "Refactor"]
                            }
                    except requests.exceptions.RequestException:
                        # Fallback to local analysis
                        st.warning("Backend not available. Using mock analysis.")
                        lines = code.splitlines()
                        st.session_state.result = {
                            "success": True,
                            "analysis": {
                                "issues": ["Backend not available - using mock analysis"],
                                "metrics": {"line_count": len(lines)},
                                "quality_score": 80 if len(lines) < 50 else 60,
                                "grade": "A" if len(lines) < 50 else "C"
                            },
                            "roast": {
                                "text": f"Found {len(lines)} lines of code! Looking good!",
                                "intensity": roast_intensity,
                                "model": "local-mock"
                            },
                            "suggestions": ["Connect to backend for full analysis", "Check your deployment"]
                        }
            else:
                st.warning("Please paste some code first!")
    
    with col2:
        st.markdown("### 📊 Quick Stats")
        if code:
            lines = code.splitlines()
            characters = len(code)
            st.metric("Lines", len(lines))
            st.metric("Characters", characters)
            
            if st.session_state.result:
                result = st.session_state.result
                st.markdown("---")
                st.markdown("### 🎯 Results")
                
                # Quality Score
                score = result['analysis'].get('quality_score', 0)
                st.metric("Quality Score", f"{score}/100")
                
                # Grade
                grade = result['analysis'].get('grade', 'N/A')
                st.metric("Grade", grade)
                
                # Roast
                st.markdown("### 😂 Roast")
                st.info(result['roast']['text'])
                
                # Issues
                if result['analysis'].get('issues'):
                    st.markdown("### ⚠️ Issues Found")
                    for issue in result['analysis']['issues'][:5]:
                        st.warning(issue)
                
                # Suggestions
                if result.get('suggestions'):
                    st.markdown("### 💡 Suggestions")
                    for suggestion in result['suggestions']:
                        st.success(suggestion)

elif selected == "Code Generation":
    st.title("✨ Code Generation")
    st.markdown("Describe what you want to code, and AI will generate it!")
    
    prompt = st.text_area(
        "Describe your code",
        placeholder="e.g., 'Create a Python function to calculate factorial'",
        height=150
    )
    
    language = st.selectbox(
        "Target Language",
        ["python", "javascript", "java", "html", "css"]
    )
    
    if st.button("🚀 Generate Code", type="primary"):
        if prompt:
            with st.spinner("Generating code... This might take a moment."):
                try:
                    response = requests.post(
                        "/api/generate",
                        json={"prompt": prompt, "language": language},
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.code(result['code'], language=language)
                        st.success("Code generated successfully!")
                    else:
                        # Fallback
                        st.error("Backend error. Using fallback generation.")
                        st.code(f'''# Generated code for: {prompt}

def solution():
    """
    TODO: Implement based on: {prompt}
    """
    # Your implementation here
    pass

if __name__ == "__main__":
    solution()''', language=language)
                except:
                    # Fallback
                    st.warning("Backend not available. Using template.")
                    st.code(f'''# Generated code for: {prompt}

# TODO: Implement your solution
# Description: {prompt}

def main():
    # Your code here
    print("Hello World!")

if __name__ == "__main__":
    main()''', language=language)
        else:
            st.warning("Please enter a description!")

# Footer
st.markdown("---")
st.markdown("### 🔗 Backend Status")
try:
    health_response = requests.get("/api/health", timeout=5)
    if health_response.status_code == 200:
        st.success("✅ Backend is healthy")
    else:
        st.error("❌ Backend not responding")
except:
    st.warning("⚠️ Backend connection failed - running in fallback mode")