# # # # import streamlit as st
# # # # from streamlit_option_menu import option_menu

# # # # # Import pages
# # # # from pages import (
# # # #     code_analysis,
# # # #     code_generation,
# # # #     collaboration,
# # # #     metrics_dashboard
# # # # )

# # # # def main():
# # # #     st.set_page_config(
# # # #         page_title="Roast Code AI - Advanced Code Companion",
# # # #         page_icon="🔥",
# # # #         layout="wide",
# # # #         initial_sidebar_state="expanded"
# # # #     )
    
# # # #     # Custom CSS
# # # #     with open("frontend/static/css/styles.css") as f:
# # # #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
# # # #     # Sidebar navigation
# # # #     with st.sidebar:
# # # #         st.image("https://img.icons8.com/color/96/000000/python.png", width=100)
# # # #         st.title("🔥 Roast Code AI")
# # # #         st.markdown("---")
        
# # # #         selected = option_menu(
# # # #             menu_title="Navigation",
# # # #             options=["Code Analysis", "Code Generation", "Collaboration", "Metrics Dashboard"],
# # # #             icons=["search", "code-slash", "people", "graph-up"],
# # # #             menu_icon="cast",
# # # #             default_index=0,
# # # #             styles={
# # # #                 "container": {"padding": "0!important"},
# # # #                 "icon": {"color": "orange", "font-size": "18px"},
# # # #                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
# # # #                 "nav-link-selected": {"background-color": "#ff4b4b"},
# # # #             }
# # # #         )
        
# # # #         st.markdown("---")
# # # #         st.markdown("### 🤖 Features")
# # # #         st.markdown("""
# # # #         - Multi-language Support
# # # #         - Real-time Collaboration
# # # #         - AI-powered Code Analysis
# # # #         - Voice Feedback
# # # #         - Code Quality Metrics
# # # #         """)
        
# # # #         st.markdown("---")
# # # #         st.markdown("### 📊 Stats")
# # # #         if 'stats' in st.session_state:
# # # #             cols = st.columns(2)
# # # #             cols[0].metric("Analyses", st.session_state.stats.get('analyses', 0))
# # # #             cols[1].metric("Generations", st.session_state.stats.get('generations', 0))
    
# # # #     # Page routing
# # # #     if selected == "Code Analysis":
# # # #         code_analysis.render()
# # # #     elif selected == "Code Generation":
# # # #         code_generation.render()
# # # #     elif selected == "Collaboration":
# # # #         collaboration.render()
# # # #     elif selected == "Metrics Dashboard":
# # # #         metrics_dashboard.render()

# # # # if __name__ == "__main__":
# # # #     main()

# # # import os
# # # import streamlit as st
# # # import requests

# # # BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5001")

# # # st.set_page_config(page_title="Roast Code AI", page_icon="🔥", layout="wide")

# # # st.title("🔥 Roast Code AI")
# # # st.subheader("Analyze & Generate Code")

# # # option = st.sidebar.selectbox("Choose Page", ["Analyze Code", "Generate Code"])

# # # if option == "Analyze Code":
# # #     code = st.text_area("Enter your code")

# # #     if st.button("Analyze"):
# # #         res = requests.post(f"{BACKEND_URL}/api/analyze", json={"code": code})
# # #         st.json(res.json())

# # # else:
# # #     prompt = st.text_area("Enter what you want to generate")

# # #     if st.button("Generate"):
# # #         res = requests.post(f"{BACKEND_URL}/api/generate", json={"prompt": prompt})
# # #         st.code(res.json()["code"])


# # # frontend/app.py - ENHANCED VERSION WITH NEW FEATURES
# # import os
# # import streamlit as st
# # import requests
# # import json
# # from datetime import datetime
# # from streamlit_option_menu import option_menu
# # import base64
# # from io import BytesIO

# # # Set page config
# # st.set_page_config(
# #     page_title="Roast Code AI 🔥",
# #     page_icon="🔥",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # Backend URL
# # BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5001")

# # # Custom CSS with theme toggle
# # st.markdown("""
# # <style>
# # :root {
# #     --primary: #8B5CF6;
# #     --secondary: #EC4899;
# #     --accent: #10B981;
# #     --dark-bg: #0F172A;
# #     --dark-card: #1E293B;
# #     --dark-text: #F1F5F9;
# #     --dark-border: #334155;
# #     --light-bg: #FFFFFF;
# #     --light-card: #F8FAFC;
# #     --light-text: #1E293B;
# #     --light-border: #E2E8F0;
# # }

# # [data-theme="light"] {
# #     --bg: var(--light-bg);
# #     --card: var(--light-card);
# #     --text: var(--light-text);
# #     --border: var(--light-border);
# # }

# # [data-theme="dark"] {
# #     --bg: var(--dark-bg);
# #     --card: var(--dark-card);
# #     --text: var(--dark-text);
# #     --border: var(--dark-border);
# # }

# # .stApp {
# #     background-color: var(--bg);
# #     color: var(--text);
# # }

# # .main-header {
# #     background: linear-gradient(90deg, var(--primary), var(--secondary));
# #     -webkit-background-clip: text;
# #     -webkit-text-fill-color: transparent;
# #     font-size: 2.5rem;
# #     font-weight: 700;
# #     text-align: center;
# #     margin-bottom: 1rem;
# # }

# # .card {
# #     background: var(--card);
# #     border-radius: 12px;
# #     padding: 1.5rem;
# #     border: 1px solid var(--border);
# #     margin-bottom: 1rem;
# # }

# # .roast-card {
# #     background: rgba(239, 68, 68, 0.1);
# #     border-left: 4px solid #EF4444;
# #     padding: 1rem;
# #     border-radius: 4px;
# #     margin: 1rem 0;
# # }

# # .improvement-card {
# #     background: rgba(16, 185, 129, 0.1);
# #     border-left: 4px solid #10B981;
# #     padding: 1rem;
# #     border-radius: 4px;
# #     margin: 1rem 0;
# # }

# # .metric-card {
# #     background: var(--card);
# #     border-radius: 8px;
# #     padding: 1rem;
# #     text-align: center;
# #     border: 1px solid var(--border);
# # }

# # .metric-value {
# #     font-size: 2rem;
# #     font-weight: 700;
# #     color: var(--primary);
# # }

# # .code-diff {
# #     background: var(--card);
# #     border-radius: 8px;
# #     padding: 1rem;
# #     font-family: 'Fira Code', monospace;
# #     font-size: 14px;
# # }

# # .added {
# #     background: rgba(16, 185, 129, 0.2);
# #     padding: 2px 4px;
# #     border-radius: 2px;
# # }

# # .removed {
# #     background: rgba(239, 68, 68, 0.2);
# #     padding: 2px 4px;
# #     border-radius: 2px;
# # }

# # /* Theme toggle */
# # .theme-toggle {
# #     position: absolute;
# #     top: 10px;
# #     right: 10px;
# # }

# # /* Loading animation */
# # @keyframes spin {
# #     0% { transform: rotate(0deg); }
# #     100% { transform: rotate(360deg); }
# # }

# # .loading {
# #     border: 4px solid var(--border);
# #     border-top: 4px solid var(--primary);
# #     border-radius: 50%;
# #     width: 40px;
# #     height: 40px;
# #     animation: spin 1s linear infinite;
# # }

# # /* Custom scrollbar */
# # ::-webkit-scrollbar {
# #     width: 8px;
# # }

# # ::-webkit-scrollbar-track {
# #     background: var(--card);
# # }

# # ::-webkit-scrollbar-thumb {
# #     background: var(--primary);
# #     border-radius: 4px;
# # }

# # /* Language badges */
# # .lang-badge {
# #     display: inline-block;
# #     padding: 4px 12px;
# #     border-radius: 20px;
# #     font-size: 12px;
# #     font-weight: 600;
# #     margin: 2px;
# # }

# # .lang-python { background: #3776AB; color: white; }
# # .lang-javascript { background: #F7DF1E; color: black; }
# # .lang-java { background: #007396; color: white; }
# # .lang-cpp { background: #00599C; color: white; }

# # /* Intensity badges */
# # .intensity-mild { background: #10B981; color: white; }
# # .intensity-medium { background: #F59E0B; color: white; }
# # .intensity-brutal { background: #EF4444; color: white; }
# # </style>
# # """, unsafe_allow_html=True)

# # # Initialize session state
# # if 'theme' not in st.session_state:
# #     st.session_state.theme = 'dark'
# # if 'analysis_history' not in st.session_state:
# #     st.session_state.analysis_history = []
# # if 'generation_history' not in st.session_state:
# #     st.session_state.generation_history = []

# # def toggle_theme():
# #     st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'

# # def analyze_code(code, language, roast_level):
# #     """Send code to backend for analysis"""
# #     try:
# #         response = requests.post(
# #             f"{BACKEND_URL}/api/analyze",
# #             json={
# #                 "code": code,
# #                 "language": language,
# #                 "roast_level": roast_level
# #             },
# #             timeout=30
# #         )
# #         if response.status_code == 200:
# #             result = response.json()
# #             # Add to history
# #             st.session_state.analysis_history.append({
# #                 "timestamp": datetime.now().isoformat(),
# #                 "language": language,
# #                 "roast_level": roast_level,
# #                 "score": result.get("analysis", {}).get("quality_score", 0),
# #                 "grade": result.get("analysis", {}).get("grade", "N/A")
# #             })
# #             return result
# #         else:
# #             st.error(f"Analysis failed: {response.text}")
# #             return None
# #     except Exception as e:
# #         st.error(f"Connection error: {str(e)}")
# #         return None

# # def generate_code(prompt, language):
# #     """Generate code from prompt"""
# #     try:
# #         response = requests.post(
# #             f"{BACKEND_URL}/api/generate",
# #             json={
# #                 "prompt": prompt,
# #                 "language": language
# #             },
# #             timeout=30
# #         )
# #         if response.status_code == 200:
# #             result = response.json()
# #             # Add to history
# #             st.session_state.generation_history.append({
# #                 "timestamp": datetime.now().isoformat(),
# #                 "language": language,
# #                 "prompt": prompt[:50] + "..." if len(prompt) > 50 else prompt
# #             })
# #             return result
# #         else:
# #             st.error(f"Generation failed: {response.text}")
# #             return None
# #     except Exception as e:
# #         st.error(f"Connection error: {str(e)}")
# #         return None

# # def render_code_diff(original, corrected):
# #     """Render simple code diff"""
# #     original_lines = original.split('\n')
# #     corrected_lines = corrected.split('\n')
    
# #     diff_html = '<div class="code-diff">'
# #     max_lines = max(len(original_lines), len(corrected_lines))
    
# #     for i in range(max_lines):
# #         if i < len(original_lines) and i < len(corrected_lines):
# #             if original_lines[i] != corrected_lines[i]:
# #                 diff_html += f'<div class="removed">- {original_lines[i]}</div>'
# #                 diff_html += f'<div class="added">+ {corrected_lines[i]}</div>'
# #             else:
# #                 diff_html += f'<div>  {original_lines[i]}</div>'
# #         elif i < len(original_lines):
# #             diff_html += f'<div class="removed">- {original_lines[i]}</div>'
# #         elif i < len(corrected_lines):
# #             diff_html += f'<div class="added">+ {corrected_lines[i]}</div>'
    
# #     diff_html += '</div>'
# #     return diff_html

# # def main():
# #     # Theme toggle button
# #     col1, col2, col3 = st.columns([6, 2, 2])
# #     with col3:
# #         if st.button(f"{'🌙' if st.session_state.theme == 'dark' else '☀️'} Theme"):
# #             toggle_theme()
# #             st.rerun()
    
# #     # Header
# #     st.markdown('<h1 class="main-header">🔥 Roast Code AI</h1>', unsafe_allow_html=True)
# #     st.markdown('<p style="text-align: center; color: var(--text); opacity: 0.8;">AI-powered code analysis with sarcastic feedback</p>', unsafe_allow_html=True)
    
# #     # Sidebar
# #     with st.sidebar:
# #         st.markdown("### Navigation")
# #         selected = option_menu(
# #             menu_title=None,
# #             options=["Code Analysis", "Code Generation", "Project Analysis", "History & Metrics"],
# #             icons=["search", "code-slash", "folder", "graph-up"],
# #             default_index=0,
# #             styles={
# #                 "container": {"padding": "0!important"},
# #                 "icon": {"color": "orange", "font-size": "18px"},
# #                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
# #                 "nav-link-selected": {"background": "linear-gradient(90deg, #8B5CF6, #EC4899)"},
# #             }
# #         )
        
# #         st.markdown("---")
# #         st.markdown("### 📊 Quick Stats")
# #         total_analyses = len(st.session_state.analysis_history)
# #         total_generations = len(st.session_state.generation_history)
        
# #         if total_analyses > 0:
# #             avg_score = sum(h["score"] for h in st.session_state.analysis_history) / total_analyses
# #             st.metric("Avg Quality Score", f"{avg_score:.1f}/100")
# #         st.metric("Total Analyses", total_analyses)
# #         st.metric("Total Generations", total_generations)
        
# #         st.markdown("---")
# #         st.markdown("### 🔧 Settings")
        
# #         # Multi-language support
# #         languages = ["python", "javascript", "java", "cpp", "typescript"]
# #         selected_lang = st.selectbox("Default Language", languages, index=0)
        
# #         # Project analysis (new feature)
# #         if selected == "Project Analysis":
# #             uploaded_files = st.file_uploader(
# #                 "Upload project files",
# #                 accept_multiple_files=True,
# #                 type=['py', 'js', 'java', 'cpp', 'txt', 'md']
# #             )
    
# #     # Main content based on selection
# #     if selected == "Code Analysis":
# #         render_code_analysis(selected_lang)
# #     elif selected == "Code Generation":
# #         render_code_generation(selected_lang)
# #     elif selected == "Project Analysis":
# #         render_project_analysis(uploaded_files if 'uploaded_files' in locals() else [])
# #     elif selected == "History & Metrics":
# #         render_history_metrics()

# # def render_code_analysis(default_lang):
# #     """Render code analysis page with side-by-side diff"""
# #     st.markdown("## 🔍 Code Analysis & Roasting")
    
# #     col1, col2 = st.columns([1, 1])
    
# #     with col1:
# #         st.markdown("### 📝 Input Code")
        
# #         # Language selector with badges
# #         language = st.selectbox(
# #             "Programming Language",
# #             ["python", "javascript", "java", "cpp", "typescript"],
# #             index=["python", "javascript", "java", "cpp", "typescript"].index(default_lang)
# #         )
        
# #         # Code editor
# #         default_code = get_default_code(language)
# #         code = st.text_area(
# #             "Paste your code here",
# #             value=default_code,
# #             height=300,
# #             key=f"code_editor_{language}"
# #         )
        
# #         # Roast intensity slider (new feature)
# #         roast_level = st.select_slider(
# #             "Roast Intensity",
# #             options=["mild", "medium", "brutal"],
# #             value="medium",
# #             help="How harsh should the feedback be?"
# #         )
        
# #         # Analyze button
# #         if st.button("🚀 Analyze & Roast", use_container_width=True):
# #             if code.strip():
# #                 with st.spinner("Analyzing your code..."):
# #                     result = analyze_code(code, language, roast_level)
# #                     st.session_state.last_result = result
# #                     st.rerun()
# #             else:
# #                 st.warning("Please enter some code to analyze")
    
# #     with col2:
# #         st.markdown("### 📊 Analysis Results")
        
# #         if 'last_result' in st.session_state and st.session_state.last_result:
# #             result = st.session_state.last_result
            
# #             # Display quality metrics
# #             st.markdown("#### 📈 Quality Metrics")
# #             metrics = result.get("analysis", {}).get("metrics", {})
# #             grade = result.get("analysis", {}).get("grade", "N/A")
# #             score = result.get("analysis", {}).get("quality_score", 0)
            
# #             col_a, col_b, col_c = st.columns(3)
# #             with col_a:
# #                 st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# #                 st.markdown(f'<div class="metric-value">{score}</div>', unsafe_allow_html=True)
# #                 st.markdown('<div>Quality Score</div>', unsafe_allow_html=True)
# #                 st.markdown('</div>', unsafe_allow_html=True)
            
# #             with col_b:
# #                 st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# #                 st.markdown(f'<div class="metric-value">{grade}</div>', unsafe_allow_html=True)
# #                 st.markdown('<div>Grade</div>', unsafe_allow_html=True)
# #                 st.markdown('</div>', unsafe_allow_html=True)
            
# #             with col_c:
# #                 st.markdown('<div class="metric-card">', unsafe_allow_html=True)
# #                 st.markdown(f'<div class="metric-value">{metrics.get("line_count", 0)}</div>', unsafe_allow_html=True)
# #                 st.markdown('<div>Lines</div>', unsafe_allow_html=True)
# #                 st.markdown('</div>', unsafe_allow_html=True)
            
# #             # Display roasts
# #             st.markdown("#### 🔥 Roasts")
# #             roast = result.get("roast", {})
# #             intensity = roast.get("intensity", "medium")
            
# #             st.markdown(f'<div class="roast-card">', unsafe_allow_html=True)
# #             st.markdown(f'**Intensity:** <span class="lang-badge intensity-{intensity}">{intensity.upper()}</span>', unsafe_allow_html=True)
# #             st.markdown(roast.get("text", "No roast generated"))
# #             st.markdown('</div>', unsafe_allow_html=True)
            
# #             # Display issues
# #             issues = result.get("analysis", {}).get("issues", [])
# #             if issues:
# #                 st.markdown("#### ⚠️ Issues Found")
# #                 with st.expander(f"Show {len(issues)} issues"):
# #                     for i, issue in enumerate(issues, 1):
# #                         st.markdown(f"**{i}.** {issue}")
            
# #             # Display suggestions
# #             suggestions = result.get("suggestions", [])
# #             if suggestions:
# #                 st.markdown("#### 💡 Suggestions")
# #                 for i, suggestion in enumerate(suggestions, 1):
# #                     st.markdown(f"**{i}.** {suggestion}")
            
# #             # Side-by-side code diff (new feature)
# #             corrected_code = result.get("corrected_code", "")
# #             if corrected_code and corrected_code != code:
# #                 st.markdown("#### ✨ Improved Code")
                
# #                 diff_view = st.radio(
# #                     "View mode",
# #                     ["Side-by-side", "Diff view", "Improved only"],
# #                     horizontal=True
# #                 )
                
# #                 if diff_view == "Side-by-side":
# #                     col_orig, col_corr = st.columns(2)
# #                     with col_orig:
# #                         st.markdown("**Original Code**")
# #                         st.code(code, language=language)
# #                     with col_corr:
# #                         st.markdown("**Improved Code**")
# #                         st.code(corrected_code, language=language)
                
# #                 elif diff_view == "Diff view":
# #                     # Simple diff rendering
# #                     st.markdown(render_code_diff(code, corrected_code), unsafe_allow_html=True)
                
# #                 else:
# #                     st.code(corrected_code, language=language)
                
# #                 # Download improved code (new feature)
# #                 st.download_button(
# #                     label="📥 Download Improved Code",
# #                     data=corrected_code,
# #                     file_name=f"improved_code.{get_file_extension(language)}",
# #                     mime="text/plain",
# #                     use_container_width=True
# #                 )
        
# #         else:
# #             st.info("👈 Enter code and click 'Analyze & Roast' to see results")

# # def render_code_generation(default_lang):
# #     """Render code generation page"""
# #     st.markdown("## ✨ Code Generation")
    
# #     col1, col2 = st.columns([1, 1])
    
# #     with col1:
# #         st.markdown("### 📝 Code Prompt")
        
# #         language = st.selectbox(
# #             "Generate Code in",
# #             ["python", "javascript", "java", "cpp", "typescript"],
# #             index=["python", "javascript", "java", "cpp", "typescript"].index(default_lang),
# #             key="gen_lang"
# #         )
        
# #         prompt = st.text_area(
# #             "Describe the code you want to generate",
# #             placeholder="e.g., 'Create a function to calculate factorial of a number'",
# #             height=150
# #         )
        
# #         # Complexity level (new feature)
# #         complexity = st.select_slider(
# #             "Code Complexity",
# #             options=["simple", "medium", "complex"],
# #             value="medium"
# #         )
        
# #         if st.button("🚀 Generate Code", use_container_width=True):
# #             if prompt:
# #                 with st.spinner("Generating code..."):
# #                     result = generate_code(prompt, language)
# #                     if result:
# #                         st.session_state.last_generated = result
# #                         st.rerun()
# #             else:
# #                 st.warning("Please enter a prompt")
    
# #     with col2:
# #         st.markdown("### 📄 Generated Code")
        
# #         if 'last_generated' in st.session_state and st.session_state.last_generated:
# #             result = st.session_state.last_generated
            
# #             # Display roast
# #             roast = result.get("roast", "")
# #             if roast:
# #                 st.markdown("#### 😂 AI Says...")
# #                 st.info(roast)
            
# #             # Display generated code
# #             code = result.get("code", "")
# #             if code:
# #                 st.code(code, language=language)
                
# #                 # Download options
# #                 col_dl1, col_dl2 = st.columns(2)
# #                 with col_dl1:
# #                     st.download_button(
# #                         label="📥 Download Code",
# #                         data=code,
# #                         file_name=f"generated_code.{get_file_extension(language)}",
# #                         mime="text/plain",
# #                         use_container_width=True
# #                     )
                
# #                 with col_dl2:
# #                     if st.button("📋 Copy to Clipboard", use_container_width=True):
# #                         st.code(code, language=language)
# #                         st.success("Code copied to clipboard!")
# #         else:
# #             st.info("👈 Enter a prompt and click 'Generate Code'")

# # def render_project_analysis(uploaded_files):
# #     """Render project analysis page (new feature)"""
# #     st.markdown("## 📁 Project Analysis")
    
# #     if uploaded_files:
# #         st.success(f"📂 {len(uploaded_files)} files uploaded")
        
# #         # Analyze each file
# #         for file in uploaded_files:
# #             file_content = file.getvalue().decode("utf-8")
# #             file_ext = os.path.splitext(file.name)[1]
            
# #             with st.expander(f"📄 {file.name}"):
# #                 col_a, col_b = st.columns(2)
                
# #                 with col_a:
# #                     st.code(file_content[:500] + ("..." if len(file_content) > 500 else ""), 
# #                            language=get_language_from_extension(file_ext))
                
# #                 with col_b:
# #                     if st.button(f"Analyze {file.name}", key=f"analyze_{file.name}"):
# #                         with st.spinner(f"Analyzing {file.name}..."):
# #                             result = analyze_code(file_content, get_language_from_extension(file_ext), "medium")
# #                             if result:
# #                                 score = result.get("analysis", {}).get("quality_score", 0)
# #                                 st.metric("Quality Score", f"{score}/100")
                                
# #                                 issues = result.get("analysis", {}).get("issues", [])
# #                                 if issues:
# #                                     st.warning(f"Found {len(issues)} issues")
# #                                     for issue in issues[:3]:
# #                                         st.markdown(f"- {issue}")
        
# #         # Overall project metrics
# #         st.markdown("### 📊 Project Summary")
# #         # (This could be expanded to analyze all files together)
        
# #     else:
# #         st.info("📁 Upload project files to analyze multiple files at once")

# # def render_history_metrics():
# #     """Render history and metrics dashboard (new feature)"""
# #     st.markdown("## 📈 History & Metrics")
    
# #     tab1, tab2 = st.tabs(["Analysis History", "Generation History"])
    
# #     with tab1:
# #         if st.session_state.analysis_history:
# #             # Display as table
# #             import pandas as pd
# #             df = pd.DataFrame(st.session_state.analysis_history)
# #             st.dataframe(df, use_container_width=True)
            
# #             # Charts
# #             col_ch1, col_ch2 = st.columns(2)
# #             with col_ch1:
# #                 st.markdown("### 📊 Score Distribution")
# #                 if 'score' in df.columns:
# #                     st.bar_chart(df['score'])
            
# #             with col_ch2:
# #                 st.markdown("### 📈 Score Over Time")
# #                 if 'timestamp' in df.columns and 'score' in df.columns:
# #                     df['time'] = pd.to_datetime(df['timestamp']).dt.strftime('%H:%M')
# #                     st.line_chart(df.set_index('time')['score'])
# #         else:
# #             st.info("No analysis history yet")
    
# #     with tab2:
# #         if st.session_state.generation_history:
# #             for item in st.session_state.generation_history:
# #                 with st.expander(f"🕒 {item['timestamp'][11:19]} - {item['prompt']}"):
# #                     st.markdown(f"**Language:** {item['language']}")
# #                     st.markdown(f"**Prompt:** {item['prompt']}")
# #         else:
# #             st.info("No generation history yet")

# # def get_default_code(language):
# #     """Get default code example for language"""
# #     examples = {
# #         "python": '''def calculate_average(numbers):
# #     """Calculate average of numbers"""
# #     total = 0
# #     count = 0
# #     for n in numbers:
# #         total += n
# #         count += 1
# #     return total / count

# # # Test the function
# # data = [85, 90, 78, 92, 88]
# # avg = calculate_average(data)
# # print(f"Average: {avg}")''',
        
# #         "javascript": '''function calculateAverage(numbers) {
# #     // Calculate average of numbers
# #     let total = 0;
# #     let count = 0;
# #     for (let n of numbers) {
# #         total += n;
# #         count++;
# #     }
# #     return total / count;
# # }

# # // Test the function
# # const data = [85, 90, 78, 92, 88];
# # const avg = calculateAverage(data);
# # console.log("Average:", avg);''',
        
# #         "java": '''public class Main {
# #     public static double calculateAverage(int[] numbers) {
# #         // Calculate average of numbers
# #         int total = 0;
# #         int count = 0;
# #         for (int n : numbers) {
# #             total += n;
# #             count++;
# #         }
# #         return (double) total / count;
# #     }
    
# #     public static void main(String[] args) {
# #         int[] data = {85, 90, 78, 92, 88};
# #         double avg = calculateAverage(data);
# #         System.out.println("Average: " + avg);
# #     }
# # }''',
        
# #         "cpp": '''#include <iostream>
# # #include <vector>

# # double calculateAverage(std::vector<int> numbers) {
# #     // Calculate average of numbers
# #     int total = 0;
# #     int count = 0;
# #     for (int n : numbers) {
# #         total += n;
# #         count++;
# #     }
# #     return static_cast<double>(total) / count;
# # }

# # int main() {
# #     std::vector<int> data = {85, 90, 78, 92, 88};
# #     double avg = calculateAverage(data);
# #     std::cout << "Average: " << avg << std::endl;
# #     return 0;
# # }'''
# #     }
# #     return examples.get(language, examples["python"])

# # def get_file_extension(language):
# #     """Get file extension for language"""
# #     extensions = {
# #         "python": "py",
# #         "javascript": "js",
# #         "java": "java",
# #         "cpp": "cpp",
# #         "typescript": "ts"
# #     }
# #     return extensions.get(language, "txt")

# # def get_language_from_extension(ext):
# #     """Get language from file extension"""
# #     ext_map = {
# #         ".py": "python",
# #         ".js": "javascript",
# #         ".java": "java",
# #         ".cpp": "cpp",
# #         ".c": "cpp",
# #         ".ts": "typescript"
# #     }
# #     return ext_map.get(ext.lower(), "python")

# # if __name__ == "__main__":
# #     main()

# # frontend/app.py - SIMPLIFIED VERSION
# import os
# import streamlit as st
# import requests
# from datetime import datetime

# # Set page config
# st.set_page_config(
#     page_title="🔥 Roast Code AI",
#     page_icon="🔥",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Backend URL
# BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5001")

# # Custom CSS
# st.markdown("""
# <style>
#     .main-header {
#         background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 2.5rem;
#         font-weight: 700;
#         text-align: center;
#         margin-bottom: 0.5rem;
#     }
    
#     .subheader {
#         text-align: center;
#         color: #666;
#         margin-bottom: 2rem;
#     }
    
#     .card {
#         background: #f8f9fa;
#         border-radius: 10px;
#         padding: 20px;
#         margin-bottom: 20px;
#         border-left: 4px solid #FF6B6B;
#     }
    
#     .roast-card {
#         background: #fff3cd;
#         border-left: 4px solid #ffc107;
#         border-radius: 5px;
#         padding: 15px;
#         margin: 10px 0;
#     }
    
#     .issue-card {
#         background: #f8d7da;
#         border-left: 4px solid #dc3545;
#         border-radius: 5px;
#         padding: 10px;
#         margin: 5px 0;
#     }
    
#     .suggestion-card {
#         background: #d1ecf1;
#         border-left: 4px solid #17a2b8;
#         border-radius: 5px;
#         padding: 10px;
#         margin: 5px 0;
#     }
    
#     .metric-card {
#         background: white;
#         border-radius: 10px;
#         padding: 15px;
#         text-align: center;
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#         margin: 5px;
#     }
    
#     .metric-value {
#         font-size: 24px;
#         font-weight: bold;
#         color: #4ECDC4;
#     }
    
#     .grade-A { color: #28a745; font-weight: bold; }
#     .grade-B { color: #20c997; font-weight: bold; }
#     .grade-C { color: #ffc107; font-weight: bold; }
#     .grade-D { color: #fd7e14; font-weight: bold; }
#     .grade-F { color: #dc3545; font-weight: bold; }
    
#     .intensity-badge {
#         display: inline-block;
#         padding: 3px 10px;
#         border-radius: 15px;
#         font-size: 12px;
#         font-weight: bold;
#         margin-left: 10px;
#     }
    
#     .intensity-mild { background: #28a745; color: white; }
#     .intensity-medium { background: #ffc107; color: black; }
#     .intensity-brutal { background: #dc3545; color: white; }
    
#     .language-badge {
#         display: inline-block;
#         padding: 3px 10px;
#         border-radius: 15px;
#         font-size: 12px;
#         font-weight: bold;
#         background: #6c757d;
#         color: white;
#     }
    
#     .stButton button {
#         background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
#         color: white;
#         border: none;
#         border-radius: 5px;
#         padding: 10px 20px;
#         font-weight: bold;
#         width: 100%;
#     }
    
#     .stButton button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#     }
    
#     .tab-content {
#         padding: 20px;
#     }
# </style>
# """, unsafe_allow_html=True)

# def speak_text(text):
#     """Use browser's speech synthesis"""
#     js_code = f"""
#     <script>
#     if ('speechSynthesis' in window) {{
#         const utterance = new SpeechSynthesisUtterance("{text}");
#         utterance.rate = 1.0;
#         utterance.pitch = 1.0;
#         utterance.volume = 1.0;
#         speechSynthesis.speak(utterance);
#     }} else {{
#         alert("Your browser doesn't support speech synthesis. Try Chrome or Edge.");
#     }}
#     </script>
#     """
#     st.components.v1.html(js_code, height=0)

# def analyze_code(code, language, roast_level):
#     """Send code to backend for analysis"""
#     try:
#         response = requests.post(
#             f"{BACKEND_URL}/api/analyze",
#             json={
#                 "code": code,
#                 "language": language,
#                 "roast_level": roast_level
#             },
#             timeout=10
#         )
        
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"Backend error: {response.status_code}")
#             return None
#     except requests.exceptions.ConnectionError:
#         st.error("Could not connect to backend. Make sure it's running on port 5001.")
#         return None
#     except Exception as e:
#         st.error(f"Error: {str(e)}")
#         return None

# def generate_code(prompt, language):
#     """Generate code from prompt"""
#     try:
#         response = requests.post(
#             f"{BACKEND_URL}/api/generate",
#             json={
#                 "prompt": prompt,
#                 "language": language
#             },
#             timeout=10
#         )
        
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"Backend error: {response.status_code}")
#             return None
#     except requests.exceptions.ConnectionError:
#         st.error("Could not connect to backend.")
#         return None
#     except Exception as e:
#         st.error(f"Error: {str(e)}")
#         return None

# def main():
#     # Header
#     st.markdown('<h1 class="main-header">🔥 Roast Code AI</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subheader">AI-powered code analysis with sarcastic feedback</p>', unsafe_allow_html=True)
    
#     # Create tabs
#     tab1, tab2 = st.tabs(["🔍 Code Analysis", "✨ Code Generation"])
    
#     with tab1:
#         st.markdown("### Analyze Your Code")
        
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             # Language selection
#             language = st.selectbox(
#                 "Language",
#                 ["python", "javascript", "java", "cpp"],
#                 index=0,
#                 key="analysis_lang"
#             )
            
#             # Code input
#             default_code = """def calculate_average(numbers):
#     total = 0
#     count = 0
#     for n in numbers:
#         total += n
#         count += 1
#     return total / count

# # Test
# data = [85, 90, 78, 92, 88]
# avg = calculate_average(data)
# print(f"Average: {avg}")"""
            
#             code = st.text_area(
#                 "Paste your code here:",
#                 value=default_code,
#                 height=300,
#                 key="analysis_code"
#             )
            
#             # Roast intensity
#             roast_level = st.radio(
#                 "Roast Intensity:",
#                 ["mild", "medium", "brutal"],
#                 horizontal=True,
#                 index=1
#             )
            
#             # Analyze button
#             analyze_clicked = st.button("🚀 Analyze & Roast", use_container_width=True)
            
#             if analyze_clicked and code.strip():
#                 with st.spinner("Analyzing your code..."):
#                     result = analyze_code(code, language, roast_level)
                    
#                     if result:
#                         # Store in session state
#                         st.session_state.analysis_result = result
                        
#                         # Auto-play audio roast
#                         if 'roast' in result and 'audio_text' in result['roast']:
#                             speak_text(result['roast']['audio_text'])
            
#             elif analyze_clicked and not code.strip():
#                 st.warning("Please enter some code to analyze!")
        
#         with col2:
#             st.markdown("### Results")
            
#             if 'analysis_result' in st.session_state:
#                 result = st.session_state.analysis_result
                
#                 # Display metrics
#                 st.markdown("#### 📊 Metrics")
#                 metrics = result.get('analysis', {}).get('metrics', {})
                
#                 col_a, col_b, col_c = st.columns(3)
#                 with col_a:
#                     score = metrics.get('quality_score', 0)
#                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{score}/100</div>', unsafe_allow_html=True)
#                     st.markdown('Quality Score')
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with col_b:
#                     grade = metrics.get('grade', 'N/A')
#                     grade_class = f"grade-{grade}"
#                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="{grade_class}">{grade}</div>', unsafe_allow_html=True)
#                     st.markdown('Grade')
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with col_c:
#                     lines = metrics.get('line_count', 0)
#                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{lines}</div>', unsafe_allow_html=True)
#                     st.markdown('Lines')
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Display roast
#                 st.markdown("#### 🔥 Roast")
#                 roast = result.get('roast', {})
#                 roast_text = roast.get('text', 'No roast generated')
#                 intensity = roast.get('intensity', 'medium')
                
#                 st.markdown(f'<div class="roast-card">', unsafe_allow_html=True)
#                 st.markdown(f'<span class="intensity-badge intensity-{intensity}">{intensity.upper()}</span>')
#                 st.markdown(roast_text)
                
#                 # Play audio button
#                 if st.button("🔊 Play Audio Roast", key="play_roast"):
#                     if 'audio_text' in roast:
#                         speak_text(roast['audio_text'])
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Display issues
#                 issues = result.get('analysis', {}).get('issues', [])
#                 if issues:
#                     st.markdown(f"#### ⚠️ Issues ({len(issues)})")
#                     for issue in issues:
#                         st.markdown(f'<div class="issue-card">❌ {issue}</div>', unsafe_allow_html=True)
#                 else:
#                     st.success("🎉 No issues found!")
                
#                 # Display suggestions
#                 suggestions = result.get('analysis', {}).get('suggestions', [])
#                 if suggestions:
#                     st.markdown("#### 💡 Suggestions")
#                     for suggestion in suggestions[:5]:
#                         st.markdown(f'<div class="suggestion-card">💡 {suggestion}</div>', unsafe_allow_html=True)
                
#                 # Display corrected code
#                 corrected_code = result.get('corrected_code', '')
#                 if corrected_code and corrected_code != code:
#                     st.markdown("#### ✨ Improved Code")
#                     with st.expander("View improved code"):
#                         st.code(corrected_code, language='python')
                        
#                         # Download button
#                         st.download_button(
#                             label="📥 Download Improved Code",
#                             data=corrected_code,
#                             file_name="improved_code.py",
#                             mime="text/plain"
#                         )
            
#             else:
#                 st.info("👈 Enter code and click 'Analyze & Roast' to see results")
    
#     with tab2:
#         st.markdown("### Generate Code from Description")
        
#         col1, col2 = st.columns([2, 1])
        
#         with col1:
#             # Language selection
#             gen_language = st.selectbox(
#                 "Language",
#                 ["python", "javascript", "java", "cpp"],
#                 index=0,
#                 key="gen_lang"
#             )
            
#             # Prompt input
#             prompt = st.text_area(
#                 "Describe what you want to generate:",
#                 placeholder="e.g., 'Create a function to calculate factorial of a number'",
#                 height=150,
#                 key="gen_prompt"
#             )
            
#             # Generate button
#             generate_clicked = st.button("🚀 Generate Code", use_container_width=True)
            
#             if generate_clicked and prompt.strip():
#                 with st.spinner("Generating code..."):
#                     result = generate_code(prompt, gen_language)
                    
#                     if result:
#                         # Store in session state
#                         st.session_state.generation_result = result
                        
#                         # Auto-play audio
#                         if 'audio_roast' in result:
#                             speak_text(result['audio_roast'])
            
#             elif generate_clicked and not prompt.strip():
#                 st.warning("Please enter a description!")
        
#         with col2:
#             st.markdown("### Generated Code")
            
#             if 'generation_result' in st.session_state:
#                 result = st.session_state.generation_result
                
#                 # Display roast
#                 roast = result.get('roast', '')
#                 if roast:
#                     st.info(f"**AI says:** {roast}")
                    
#                     # Play audio button
#                     if st.button("🔊 Play Audio", key="play_gen_audio"):
#                         if 'audio_roast' in result:
#                             speak_text(result['audio_roast'])
                
#                 # Display generated code
#                 code = result.get('code', '')
#                 if code:
#                     st.code(code, language='python')
                    
#                     # Download button
#                     st.download_button(
#                         label="📥 Download Code",
#                         data=code,
#                         file_name="generated_code.py",
#                         mime="text/plain"
#                     )
                    
#                     # Copy button
#                     if st.button("📋 Copy to Clipboard", key="copy_gen"):
#                         st.code(code, language='python')
#                         st.success("Code copied to clipboard!")
            
#             else:
#                 st.info("👈 Enter a description and click 'Generate Code'")
    
#     # Footer
#     st.markdown("---")
#     st.markdown(
#         """
#         <div style='text-align: center; color: #666; font-size: 14px;'>
#         <p>🔥 Roast Code AI | Built with Streamlit & Flask | v1.0.0</p>
#         <p>Audio feedback uses your browser's built-in speech synthesis</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# if __name__ == "__main__":
#     main()

# frontend/app.py - ULTRA SIMPLE WORKING VERSION
import os
import streamlit as st
import requests
import json

# Set page config
st.set_page_config(
    page_title="🔥 Roast Code AI",
    page_icon="🔥",
    layout="wide"
)

# Backend URL - IMPORTANT: Change this to your Render backend URL
BACKEND_URL = os.getenv("BACKEND_URL", "https://roast-code-ai-backend.onrender.com")

# Simple CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #FF6B6B;
        font-size: 3rem;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stButton button {
        background-color: #FF6B6B;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
    }
    .metric-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        margin: 5px;
    }
    .roast-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .issue-box {
        background: #f8d7da;
        border-left: 4px solid #dc3545;
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

def speak_text(text):
    """Simple JavaScript for browser TTS"""
    js = f"""
    <script>
    if ('speechSynthesis' in window) {{
        const utterance = new SpeechSynthesisUtterance("{text}");
        speechSynthesis.speak(utterance);
    }}
    </script>
    """
    st.components.v1.html(js, height=0)

def main():
    # Header
    st.markdown('<h1 class="main-title">🔥 Roast Code AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Get sarcastic feedback on your code</p>', unsafe_allow_html=True)
    
    # Create tabs
    tab1, tab2 = st.tabs(["🔍 Code Analysis", "✨ Code Generation"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Your Code")
            
            # Code input
            default_code = '''def calculate_average(numbers):
    total = 0
    count = 0
    for n in numbers:
        total += n
        count += 1
    return total / count

# Test
data = [85, 90, 78, 92, 88]
avg = calculate_average(data)
print(f"Average: {avg}")'''
            
            code = st.text_area("Paste Python code:", value=default_code, height=300)
            
            # Roast intensity
            roast_level = st.selectbox("Roast Intensity:", ["mild", "medium", "brutal"], index=1)
            
            # Analyze button
            if st.button("🚀 Analyze & Roast", type="primary"):
                if code.strip():
                    with st.spinner("Analyzing..."):
                        try:
                            response = requests.post(
                                f"{BACKEND_URL}/api/analyze",
                                json={
                                    "code": code,
                                    "language": "python",
                                    "roast_level": roast_level
                                },
                                timeout=30
                            )
                            
                            if response.status_code == 200:
                                result = response.json()
                                st.session_state.analysis_result = result
                                
                                # Play audio
                                if 'roast' in result and 'audio_text' in result['roast']:
                                    speak_text(result['roast']['audio_text'])
                            else:
                                st.error(f"Error: {response.status_code}")
                        except Exception as e:
                            st.error(f"Could not connect to backend: {str(e)}")
                else:
                    st.warning("Please enter some code!")
        
        with col2:
            st.subheader("Results")
            
            if 'analysis_result' in st.session_state:
                result = st.session_state.analysis_result
                
                # Display metrics
                metrics = result.get('analysis', {}).get('metrics', {})
                
                col_a, col_b = st.columns(2)
                with col_a:
                    score = metrics.get('quality_score', 0)
                    st.metric("Quality Score", f"{score}/100")
                with col_b:
                    grade = metrics.get('grade', 'N/A')
                    st.metric("Grade", grade)
                
                # Display roast
                st.markdown("### 🔥 Roast")
                roast = result.get('roast', {})
                roast_text = roast.get('text', '')
                if roast_text:
                    st.markdown(f'<div class="roast-box">{roast_text}</div>', unsafe_allow_html=True)
                    
                    # Play audio button
                    if st.button("🔊 Play Audio", key="play_audio"):
                        if 'audio_text' in roast:
                            speak_text(roast['audio_text'])
                
                # Display issues
                issues = result.get('analysis', {}).get('issues', [])
                if issues:
                    st.markdown(f"### ⚠️ Issues ({len(issues)})")
                    for issue in issues:
                        st.markdown(f'<div class="issue-box">{issue}</div>', unsafe_allow_html=True)
                else:
                    st.success("🎉 No issues found!")
                
                # Display suggestions
                suggestions = result.get('analysis', {}).get('suggestions', [])
                if suggestions:
                    st.markdown("### 💡 Suggestions")
                    for suggestion in suggestions:
                        st.info(suggestion)
            else:
                st.info("👈 Paste code and click 'Analyze & Roast'")
    
    with tab2:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Generate Code")
            
            prompt = st.text_area(
                "Describe what you want:",
                placeholder="e.g., 'Create a function to calculate factorial'",
                height=150
            )
            
            if st.button("🚀 Generate Code", type="primary"):
                if prompt.strip():
                    with st.spinner("Generating..."):
                        try:
                            response = requests.post(
                                f"{BACKEND_URL}/api/generate",
                                json={
                                    "prompt": prompt,
                                    "language": "python"
                                },
                                timeout=30
                            )
                            
                            if response.status_code == 200:
                                result = response.json()
                                st.session_state.generation_result = result
                                
                                # Play audio
                                if 'audio_roast' in result:
                                    speak_text(result['audio_roast'])
                            else:
                                st.error(f"Error: {response.status_code}")
                        except Exception as e:
                            st.error(f"Could not connect to backend: {str(e)}")
                else:
                    st.warning("Please enter a description!")
        
        with col2:
            st.subheader("Generated Code")
            
            if 'generation_result' in st.session_state:
                result = st.session_state.generation_result
                
                # Display roast
                roast = result.get('roast', '')
                if roast:
                    st.info(f"**AI says:** {roast}")
                    
                    # Play audio button
                    if st.button("🔊 Play", key="play_gen"):
                        if 'audio_roast' in result:
                            speak_text(result['audio_roast'])
                
                # Display code
                code = result.get('code', '')
                if code:
                    st.code(code, language='python')
                    
                    # Download button
                    st.download_button(
                        "📥 Download",
                        data=code,
                        file_name="generated_code.py",
                        mime="text/plain"
                    )
            else:
                st.info("👈 Enter a description and generate code")

if __name__ == "__main__":
    main()