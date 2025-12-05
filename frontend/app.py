# # import os
# # import streamlit as st
# # import requests
# # import json
# # from datetime import datetime

# # # Set page configuration
# # st.set_page_config(
# #     page_title="🔥 Roast Code AI",
# #     page_icon="🔥",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # Backend URL
# # BACKEND_URL = os.getenv("BACKEND_URL", "https://roast-code-ai-backend.onrender.com")

# # # Modern AI-themed CSS with gradient colors
# # st.markdown("""
# # <style>
# # @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&display=swap');

# # :root {
# #     --primary: #8B5CF6;
# #     --secondary: #EC4899;
# #     --accent: #10B981;
# #     --dark-bg: #0F172A;
# #     --dark-card: #1E293B;
# #     --dark-text: #F1F5F9;
# #     --dark-border: #334155;
# #     --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
# #     --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
# #     --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
# #     --gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
# #     --neon-pink: #ff00ff;
# #     --neon-blue: #00ffff;
# #     --neon-green: #00ff00;
# # }

# # * {
# #     font-family: 'Inter', sans-serif;
# # }

# # .stApp {
# #     background-color: var(--dark-bg);
# #     color: var(--dark-text);
# #     background-image: 
# #         radial-gradient(at 40% 20%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
# #         radial-gradient(at 80% 0%, rgba(236, 72, 153, 0.15) 0px, transparent 50%),
# #         radial-gradient(at 0% 50%, rgba(16, 185, 129, 0.1) 0px, transparent 50%),
# #         radial-gradient(at 80% 50%, rgba(59, 130, 246, 0.1) 0px, transparent 50%);
# # }

# # /* Main Header */
# # .main-header {
# #     font-family: 'Fira Code', monospace;
# #     font-weight: 800;
# #     font-size: 3.5rem;
# #     text-align: center;
# #     margin-bottom: 0.5rem;
# #     background: linear-gradient(90deg, var(--neon-pink), var(--neon-blue), var(--neon-green));
# #     -webkit-background-clip: text;
# #     -webkit-text-fill-color: transparent;
# #     text-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
# #     animation: glow 2s ease-in-out infinite alternate;
# # }

# # @keyframes glow {
# #     from { text-shadow: 0 0 10px rgba(255, 0, 255, 0.3); }
# #     to { text-shadow: 0 0 20px rgba(0, 255, 255, 0.4), 0 0 30px rgba(0, 255, 255, 0.2); }
# # }

# # .subheader {
# #     color: var(--dark-text);
# #     text-align: center;
# #     margin-bottom: 2rem;
# #     font-weight: 300;
# #     font-size: 1.2rem;
# #     opacity: 0.9;
# # }

# # /* Cards and Containers */
# # .glass-card {
# #     background: rgba(30, 41, 59, 0.7);
# #     backdrop-filter: blur(10px);
# #     border-radius: 20px;
# #     padding: 2rem;
# #     border: 1px solid rgba(255, 255, 255, 0.1);
# #     box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
# #     margin-bottom: 1.5rem;
# #     transition: transform 0.3s ease, box-shadow 0.3s ease;
# # }

# # .glass-card:hover {
# #     transform: translateY(-5px);
# #     box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
# # }

# # .code-container {
# #     background: rgba(15, 23, 42, 0.9);
# #     border-radius: 12px;
# #     padding: 1.5rem;
# #     border: 1px solid var(--dark-border);
# #     font-family: 'Fira Code', monospace;
# #     font-size: 14px;
# #     margin: 1rem 0;
# # }

# # /* Tabs */
# # .stTabs [data-baseweb="tab-list"] {
# #     gap: 8px;
# #     background-color: transparent;
# #     border-bottom: 2px solid var(--dark-border);
# # }

# # .stTabs [data-baseweb="tab"] {
# #     background: transparent;
# #     border-radius: 10px 10px 0 0;
# #     padding: 12px 24px;
# #     font-weight: 600;
# #     color: var(--dark-text);
# #     border: none;
# #     opacity: 0.7;
# #     transition: all 0.3s ease;
# # }

# # .stTabs [data-baseweb="tab"]:hover {
# #     opacity: 1;
# #     background: rgba(139, 92, 246, 0.1);
# # }

# # .stTabs [aria-selected="true"] {
# #     background: var(--gradient-1);
# #     color: white;
# #     opacity: 1;
# #     box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
# # }

# # /* Buttons */
# # .gradient-button {
# #     background: var(--gradient-2);
# #     color: white;
# #     border: none;
# #     border-radius: 12px;
# #     padding: 14px 28px;
# #     font-weight: 600;
# #     font-size: 16px;
# #     transition: all 0.3s ease;
# #     width: 100%;
# #     cursor: pointer;
# #     position: relative;
# #     overflow: hidden;
# # }

# # .gradient-button::before {
# #     content: '';
# #     position: absolute;
# #     top: 0;
# #     left: -100%;
# #     width: 100%;
# #     height: 100%;
# #     background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
# #     transition: left 0.5s;
# # }

# # .gradient-button:hover::before {
# #     left: 100%;
# # }

# # .gradient-button:hover {
# #     transform: translateY(-3px);
# #     box-shadow: 0 8px 25px rgba(240, 147, 251, 0.4);
# # }

# # .secondary-button {
# #     background: rgba(30, 41, 59, 0.8);
# #     color: var(--dark-text);
# #     border: 2px solid var(--primary);
# #     border-radius: 12px;
# #     padding: 10px 20px;
# #     font-weight: 600;
# #     transition: all 0.3s ease;
# #     width: 100%;
# # }

# # .secondary-button:hover {
# #     background: rgba(139, 92, 246, 0.1);
# #     border-color: var(--secondary);
# # }

# # /* Text Areas and Inputs */
# # .stTextArea textarea {
# #     background-color: rgba(15, 23, 42, 0.9) !important;
# #     color: var(--dark-text) !important;
# #     border: 2px solid var(--dark-border) !important;
# #     border-radius: 12px !important;
# #     font-family: 'Fira Code', monospace !important;
# #     font-size: 14px !important;
# #     padding: 15px !important;
# #     transition: border 0.3s ease !important;
# # }

# # .stTextArea textarea:focus {
# #     border-color: var(--primary) !important;
# #     box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;
# # }

# # /* Metrics Display */
# # .metrics-grid {
# #     display: grid;
# #     grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
# #     gap: 15px;
# #     margin: 1.5rem 0;
# # }

# # .metric-card {
# #     background: var(--gradient-3);
# #     border-radius: 15px;
# #     padding: 1.5rem;
# #     text-align: center;
# #     position: relative;
# #     overflow: hidden;
# # }

# # .metric-card::before {
# #     content: '';
# #     position: absolute;
# #     top: 0;
# #     left: 0;
# #     right: 0;
# #     bottom: 0;
# #     background: rgba(0, 0, 0, 0.2);
# #     z-index: 1;
# # }

# # .metric-value {
# #     font-size: 2.5rem;
# #     font-weight: 800;
# #     color: white;
# #     margin: 0.5rem 0;
# #     position: relative;
# #     z-index: 2;
# # }

# # .metric-label {
# #     font-size: 14px;
# #     color: rgba(255, 255, 255, 0.9);
# #     font-weight: 500;
# #     position: relative;
# #     z-index: 2;
# # }

# # /* Roast Container */
# # .roast-container {
# #     background: rgba(239, 68, 68, 0.1);
# #     border-left: 4px solid var(--neon-pink);
# #     border-radius: 12px;
# #     padding: 1.5rem;
# #     margin: 1.5rem 0;
# #     position: relative;
# #     overflow: hidden;
# # }

# # .roast-container::before {
# #     content: '🔥';
# #     position: absolute;
# #     right: 20px;
# #     top: 50%;
# #     transform: translateY(-50%);
# #     font-size: 3rem;
# #     opacity: 0.2;
# # }

# # /* Issues Container */
# # .issues-container {
# #     background: rgba(245, 158, 11, 0.1);
# #     border-left: 4px solid #F59E0B;
# #     border-radius: 12px;
# #     padding: 1.5rem;
# #     margin: 1rem 0;
# # }

# # /* Suggestions Container */
# # .suggestions-container {
# #     background: rgba(16, 185, 129, 0.1);
# #     border-left: 4px solid var(--accent);
# #     border-radius: 12px;
# #     padding: 1.5rem;
# #     margin: 1rem 0;
# # }

# # /* Badges */
# # .intensity-badge {
# #     display: inline-block;
# #     padding: 6px 16px;
# #     border-radius: 20px;
# #     font-size: 12px;
# #     font-weight: 700;
# #     text-transform: uppercase;
# #     letter-spacing: 1px;
# #     margin: 0 5px;
# # }

# # .intensity-mild {
# #     background: var(--gradient-4);
# #     color: white;
# # }

# # .intensity-medium {
# #     background: linear-gradient(90deg, #f59e0b, #fbbf24);
# #     color: white;
# # }

# # .intensity-brutal {
# #     background: linear-gradient(90deg, #ef4444, #f87171);
# #     color: white;
# # }

# # /* Loading Animation */
# # .loading-container {
# #     display: flex;
# #     justify-content: center;
# #     align-items: center;
# #     flex-direction: column;
# #     padding: 3rem;
# # }

# # .loading-spinner {
# #     width: 60px;
# #     height: 60px;
# #     border: 3px solid transparent;
# #     border-top: 3px solid var(--neon-pink);
# #     border-right: 3px solid var(--neon-blue);
# #     border-bottom: 3px solid var(--neon-green);
# #     border-radius: 50%;
# #     animation: spin 1s linear infinite;
# #     margin-bottom: 1rem;
# # }

# # @keyframes spin {
# #     0% { transform: rotate(0deg); }
# #     100% { transform: rotate(360deg); }
# # }

# # .loading-text {
# #     color: var(--dark-text);
# #     font-size: 1.1rem;
# #     font-weight: 500;
# #     background: var(--gradient-1);
# #     -webkit-background-clip: text;
# #     -webkit-text-fill-color: transparent;
# # }

# # /* Audio Player */
# # .audio-player {
# #     background: rgba(30, 41, 59, 0.8);
# #     border-radius: 12px;
# #     padding: 1rem;
# #     margin: 1rem 0;
# #     border: 1px solid var(--dark-border);
# # }

# # /* Scrollbar */
# # ::-webkit-scrollbar {
# #     width: 10px;
# # }

# # ::-webkit-scrollbar-track {
# #     background: rgba(30, 41, 59, 0.5);
# #     border-radius: 5px;
# # }

# # ::-webkit-scrollbar-thumb {
# #     background: var(--gradient-1);
# #     border-radius: 5px;
# # }

# # ::-webkit-scrollbar-thumb:hover {
# #     background: var(--gradient-2);
# # }

# # /* Footer */
# # .footer {
# #     text-align: center;
# #     margin-top: 3rem;
# #     padding: 2rem;
# #     color: var(--dark-text);
# #     font-size: 14px;
# #     opacity: 0.7;
# #     border-top: 1px solid var(--dark-border);
# # }

# # /* Code Syntax */
# # code {
# #     font-family: 'Fira Code', monospace !important;
# #     background: rgba(15, 23, 42, 0.9) !important;
# #     padding: 2px 6px !important;
# #     border-radius: 4px !important;
# #     border: 1px solid var(--dark-border) !important;
# # }

# # /* Custom select boxes */
# # .stSelectbox div[data-baseweb="select"] {
# #     background-color: rgba(15, 23, 42, 0.9) !important;
# #     color: var(--dark-text) !important;
# #     border: 2px solid var(--dark-border) !important;
# #     border-radius: 12px !important;
# # }

# # /* Radio buttons */
# # .stRadio > div {
# #     background: rgba(30, 41, 59, 0.7);
# #     padding: 15px;
# #     border-radius: 12px;
# #     border: 1px solid var(--dark-border);
# # }

# # /* Alert boxes */
# # .stAlert {
# #     background: rgba(30, 41, 59, 0.8) !important;
# #     color: var(--dark-text) !important;
# #     border: 1px solid var(--dark-border) !important;
# #     border-radius: 12px !important;
# # }

# # /* Success messages */
# # .stSuccess {
# #     background: rgba(16, 185, 129, 0.1) !important;
# #     border: 1px solid var(--accent) !important;
# # }

# # /* Error messages */
# # .stError {
# #     background: rgba(239, 68, 68, 0.1) !important;
# #     border: 1px solid #EF4444 !important;
# # }

# # /* Warning messages */
# # .stWarning {
# #     background: rgba(245, 158, 11, 0.1) !important;
# #     border: 1px solid #F59E0B !important;
# # }

# # /* Info messages */
# # .stInfo {
# #     background: rgba(59, 130, 246, 0.1) !important;
# #     border: 1px solid #3B82F6 !important;
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # # Initialize session state
# # if 'analysis_result' not in st.session_state:
# #     st.session_state.analysis_result = None
# # if 'generation_result' not in st.session_state:
# #     st.session_state.generation_result = None

# # def speak_text(text):
# #     """Use browser's speech synthesis for audio roasts"""
# #     js_code = f"""
# #     <script>
# #     if ('speechSynthesis' in window) {{
# #         // Cancel any ongoing speech
# #         speechSynthesis.cancel();
        
# #         // Create new utterance
# #         const utterance = new SpeechSynthesisUtterance("{text}");
        
# #         // Configure voice
# #         utterance.rate = 1.0;
# #         utterance.pitch = 1.0;
# #         utterance.volume = 1.0;
        
# #         // Try to get a good voice
# #         const voices = speechSynthesis.getVoices();
# #         if (voices.length > 0) {{
# #             // Prefer English voices
# #             const englishVoice = voices.find(voice => voice.lang.startsWith('en'));
# #             if (englishVoice) {{
# #                 utterance.voice = englishVoice;
# #             }}
# #         }}
        
# #         // Speak
# #         speechSynthesis.speak(utterance);
# #     }} else {{
# #         console.log('Speech synthesis not supported');
# #     }}
# #     </script>
# #     """
# #     st.components.v1.html(js_code, height=0)

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
# #             return response.json()
# #         else:
# #             st.error(f"Backend error: {response.status_code}")
# #             return None
# #     except requests.exceptions.ConnectionError:
# #         st.error("Could not connect to backend. Make sure it's running.")
# #         return None
# #     except Exception as e:
# #         st.error(f"Error: {str(e)}")
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
# #             return response.json()
# #         else:
# #             st.error(f"Backend error: {response.status_code}")
# #             return None
# #     except requests.exceptions.ConnectionError:
# #         st.error("Could not connect to backend.")
# #         return None
# #     except Exception as e:
# #         st.error(f"Error: {str(e)}")
# #         return None

# # def show_loading():
# #     """Show loading animation"""
# #     st.markdown("""
# #     <div class="loading-container">
# #         <div class="loading-spinner"></div>
# #         <div class="loading-text">Analyzing your code...</div>
# #     </div>
# #     """, unsafe_allow_html=True)

# # def main():
# #     # Header Section
# #     st.markdown('<h1 class="main-header">🔥 R0AST C0DE AI 🔥</h1>', unsafe_allow_html=True)
# #     st.markdown('<p class="subheader">AI-powered code analysis with a sarcastic twist • Get roasted while you code!</p>', unsafe_allow_html=True)
    
# #     # Create tabs
# #     tab1, tab2 = st.tabs(["🔍 CODE ANALYSIS", "✨ CODE GENERATION"])
    
# #     with tab1:
# #         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
# #         col1, col2 = st.columns([1, 1], gap="large")
        
# #         with col1:
# #             st.markdown("### 📝 YOUR CODE")
            
# #             # Language selection
# #             language = st.selectbox(
# #                 "Select Language",
# #                 ["python", "javascript", "java", "cpp"],
# #                 index=0,
# #                 help="Choose the programming language of your code"
# #             )
            
# #             # Code input with example
# #             default_code = """def calculate_average(numbers):
# #     \"\"\"Calculate average of numbers.\"\"\"
# #     total = 0
# #     count = 0
# #     for n in numbers:
# #         total += n
# #         count += 1
# #     return total / count

# # # Test the function
# # data = [85, 90, 78, 92, 88]
# # avg = calculate_average(data)
# # print(f"Average: {avg}")"""
            
# #             code = st.text_area(
# #                 "Paste your code here:",
# #                 value=default_code,
# #                 height=350,
# #                 placeholder="Paste your code here and prepare to be roasted...",
# #                 help="Enter the code you want to analyze"
# #             )
            
# #             # Roast intensity with style
# #             st.markdown("### ⚡ ROAST INTENSITY")
# #             roast_level = st.radio(
# #                 "",
# #                 ["mild", "medium", "brutal"],
# #                 index=1,
# #                 horizontal=True,
# #                 label_visibility="collapsed"
# #             )
            
# #             # Analyze button
# #             if st.button("🚀 ANALYZE & ROAST MY CODE!", use_container_width=True, type="primary"):
# #                 if code.strip():
# #                     # Show loading
# #                     with st.spinner(""):
# #                         show_loading()
# #                         st.rerun()
                    
# #                     # Actually analyze (this runs after rerun)
# #                     if 'analyzing' not in st.session_state:
# #                         st.session_state.analyzing = True
# #                         result = analyze_code(code, language, roast_level)
# #                         if result:
# #                             st.session_state.analysis_result = result
# #                             st.session_state.analyzing = False
                            
# #                             # Play audio roast automatically
# #                             if 'roast' in result and 'audio_text' in result['roast']:
# #                                 speak_text(result['roast']['audio_text'])
# #                         st.rerun()
# #                 else:
# #                     st.warning("Please enter some code to analyze!")
        
# #         with col2:
# #             st.markdown("### 📊 ANALYSIS RESULTS")
            
# #             if st.session_state.get('analyzing', False):
# #                 show_loading()
# #             elif st.session_state.analysis_result:
# #                 result = st.session_state.analysis_result
                
# #                 # Display metrics in grid
# #                 st.markdown("#### 📈 CODE METRICS")
# #                 metrics = result.get('analysis', {}).get('metrics', {})
                
# #                 col_a, col_b, col_c = st.columns(3)
# #                 with col_a:
# #                     score = metrics.get('quality_score', 0)
# #                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-value">{score}</div>', unsafe_allow_html=True)
# #                     st.markdown('<div class="metric-label">QUALITY SCORE</div>', unsafe_allow_html=True)
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 with col_b:
# #                     grade = metrics.get('grade', 'N/A')
# #                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-value">{grade}</div>', unsafe_allow_html=True)
# #                     st.markdown('<div class="metric-label">GRADE</div>', unsafe_allow_html=True)
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 with col_c:
# #                     lines = metrics.get('line_count', 0)
# #                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
# #                     st.markdown(f'<div class="metric-value">{lines}</div>', unsafe_allow_html=True)
# #                     st.markdown('<div class="metric-label">LINES</div>', unsafe_allow_html=True)
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 # Display roast
# #                 st.markdown("#### 🔥 AI ROAST")
# #                 roast = result.get('roast', {})
# #                 roast_text = roast.get('text', 'No roast generated')
# #                 intensity = roast.get('intensity', 'medium')
                
# #                 st.markdown(f'<div class="roast-container">', unsafe_allow_html=True)
# #                 st.markdown(f'**Intensity:** <span class="intensity-badge intensity-{intensity}">{intensity.upper()}</span>')
# #                 st.markdown(f'**{roast_text}**')
                
# #                 # Audio controls
# #                 col_audio1, col_audio2 = st.columns([1, 1])
# #                 with col_audio1:
# #                     if st.button("🔊 PLAY AUDIO ROAST", use_container_width=True):
# #                         if 'audio_text' in roast:
# #                             speak_text(roast['audio_text'])
                
# #                 with col_audio2:
# #                     if st.button("🔄 REPLAY", use_container_width=True):
# #                         if 'audio_text' in roast:
# #                             speak_text(roast['audio_text'])
                
# #                 st.markdown('</div>', unsafe_allow_html=True)
                
# #                 # Display issues
# #                 issues = result.get('analysis', {}).get('issues', [])
# #                 if issues:
# #                     st.markdown(f"#### ⚠️ ISSUES FOUND ({len(issues)})")
# #                     st.markdown('<div class="issues-container">', unsafe_allow_html=True)
# #                     for i, issue in enumerate(issues, 1):
# #                         st.markdown(f"**{i}.** {issue}")
# #                     st.markdown('</div>', unsafe_allow_html=True)
# #                 else:
# #                     st.success("🎉 No issues found! Your code is looking good!")
                
# #                 # Display suggestions
# #                 suggestions = result.get('analysis', {}).get('suggestions', [])
# #                 if suggestions:
# #                     st.markdown("#### 💡 SUGGESTIONS FOR IMPROVEMENT")
# #                     st.markdown('<div class="suggestions-container">', unsafe_allow_html=True)
# #                     for i, suggestion in enumerate(suggestions[:5], 1):
# #                         st.markdown(f"**{i}.** {suggestion}")
# #                     st.markdown('</div>', unsafe_allow_html=True)
                
# #                 # Display corrected code if available
# #                 if 'corrected_code' in result and result['corrected_code']:
# #                     st.markdown("#### ✨ IMPROVED CODE")
# #                     with st.expander("View improved version", expanded=False):
# #                         st.code(result['corrected_code'], language='python')
                        
# #                         # Download button
# #                         st.download_button(
# #                             label="📥 DOWNLOAD IMPROVED CODE",
# #                             data=result['corrected_code'],
# #                             file_name="improved_code.py",
# #                             mime="text/plain",
# #                             use_container_width=True
# #                         )
            
# #             else:
# #                 st.info("👈 Enter your code and click 'ANALYZE & ROAST' to see the magic!")
# #                 st.markdown("""
# #                 <div style='text-align: center; padding: 2rem;'>
# #                     <div style='font-size: 4rem; margin-bottom: 1rem;'>🔥</div>
# #                     <h3>Ready to roast some code?</h3>
# #                     <p>Paste your code on the left and let our AI give you some tough love!</p>
# #                 </div>
# #                 """, unsafe_allow_html=True)
        
# #         st.markdown('</div>', unsafe_allow_html=True)
    
# #     with tab2:
# #         st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
# #         col1, col2 = st.columns([1, 1], gap="large")
        
# #         with col1:
# #             st.markdown("### 💡 CODE GENERATION")
            
# #             # Language selection
# #             gen_language = st.selectbox(
# #                 "Generate Code In",
# #                 ["python", "javascript", "java", "cpp"],
# #                 index=0,
# #                 key="gen_lang"
# #             )
            
# #             # Prompt input
# #             prompt = st.text_area(
# #                 "Describe what you want to generate:",
# #                 placeholder="e.g., 'Create a function to calculate factorial of a number'",
# #                 height=200,
# #                 help="Describe the code you want AI to generate"
# #             )
            
# #             # Complexity level
# #             st.markdown("### ⚙️ COMPLEXITY LEVEL")
# #             complexity = st.radio(
# #                 "",
# #                 ["simple", "medium", "complex"],
# #                 index=1,
# #                 horizontal=True,
# #                 label_visibility="collapsed"
# #             )
            
# #             # Generate button
# #             if st.button("🚀 GENERATE CODE", use_container_width=True, type="primary"):
# #                 if prompt.strip():
# #                     with st.spinner("AI is thinking..."):
# #                         result = generate_code(prompt, gen_language)
# #                         if result:
# #                             st.session_state.generation_result = result
                            
# #                             # Play audio
# #                             if 'audio_roast' in result:
# #                                 speak_text(result['audio_roast'])
# #                 else:
# #                     st.warning("Please enter a description!")
        
# #         with col2:
# #             st.markdown("### 📄 GENERATED CODE")
            
# #             if st.session_state.generation_result:
# #                 result = st.session_state.generation_result
                
# #                 # Display roast
# #                 roast = result.get('roast', '')
# #                 if roast:
# #                     st.markdown("#### 😂 AI SAYS...")
# #                     st.info(f"**{roast}**")
                    
# #                     # Audio controls
# #                     if st.button("🔊 PLAY AUDIO", use_container_width=True):
# #                         if 'audio_roast' in result:
# #                             speak_text(result['audio_roast'])
                
# #                 # Display generated code
# #                 code = result.get('code', '')
# #                 if code:
# #                     st.markdown("#### ✨ GENERATED CODE")
# #                     st.code(code, language='python')
                    
# #                     # Action buttons
# #                     col_dl, col_cp = st.columns([1, 1])
# #                     with col_dl:
# #                         st.download_button(
# #                             label="📥 DOWNLOAD CODE",
# #                             data=code,
# #                             file_name="generated_code.py",
# #                             mime="text/plain",
# #                             use_container_width=True
# #                         )
                    
# #                     with col_cp:
# #                         if st.button("📋 COPY TO CLIPBOARD", use_container_width=True):
# #                             st.code(code, language='python')
# #                             st.success("Code copied to clipboard!")
                
# #                 # Tips for better generation
# #                 st.markdown("""
# #                 <div style='margin-top: 2rem; padding: 1rem; background: rgba(59, 130, 246, 0.1); border-radius: 10px; border-left: 4px solid #3B82F6;'>
# #                     <h4>💡 Tips for better code generation:</h4>
# #                     <ul style='margin: 0; padding-left: 1.2rem;'>
# #                         <li>Be specific about what you want</li>
# #                         <li>Mention the programming language</li>
# #                         <li>Include requirements or constraints</li>
# #                         <li>Ask for comments or documentation</li>
# #                     </ul>
# #                 </div>
# #                 """, unsafe_allow_html=True)
            
# #             else:
# #                 st.info("👈 Describe what you want and click 'GENERATE CODE'")
# #                 st.markdown("""
# #                 <div style='text-align: center; padding: 2rem;'>
# #                     <div style='font-size: 4rem; margin-bottom: 1rem;'>✨</div>
# #                     <h3>Turn ideas into code!</h3>
# #                     <p>Describe what you want, and our AI will generate the code for you.</p>
# #                     <div style='background: rgba(139, 92, 246, 0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem;'>
# #                         <h4>Try these examples:</h4>
# #                         <p>• "Create a function to calculate factorial"</p>
# #                         <p>• "Generate a palindrome checker"</p>
# #                         <p>• "Write a simple calculator in Python"</p>
# #                     </div>
# #                 </div>
# #                 """, unsafe_allow_html=True)
        
# #         st.markdown('</div>', unsafe_allow_html=True)
    
# #     # Footer
# #     st.markdown("""
# #     <div class="footer">
# #         <p>🔥 ROAST CODE AI • Built with ❤️ using Streamlit & Flask</p>
# #         <p>Because sometimes your code needs a reality check!</p>
# #         <p style="font-size: 12px; margin-top: 1rem; opacity: 0.5;">
# #             Audio feedback powered by your browser's speech synthesis • v2.0
# #         </p>
# #     </div>
# #     """, unsafe_allow_html=True)

# # if __name__ == "__main__":
# #     main()

# # frontend/app.py - FIXED VERSION
# import os
# import streamlit as st
# import requests
# import json
# from datetime import datetime

# # Set page configuration - HIDE SIDEBAR
# st.set_page_config(
#     page_title="🔥 Roast Code AI",
#     page_icon="🔥",
#     layout="wide",
#     initial_sidebar_state="collapsed"  # This collapses the sidebar
# )

# # Backend URL
# BACKEND_URL = os.getenv("BACKEND_URL", "https://roast-code-ai-backend.onrender.com")

# # Modern AI-themed CSS with gradient colors - UPDATED TO HIDE SIDEBAR
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&display=swap');

# :root {
#     --primary: #8B5CF6;
#     --secondary: #EC4899;
#     --accent: #10B981;
#     --dark-bg: #0F172A;
#     --dark-card: #1E293B;
#     --dark-text: #F1F5F9;
#     --dark-border: #334155;
#     --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
#     --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
#     --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
#     --gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
#     --neon-pink: #ff00ff;
#     --neon-blue: #00ffff;
#     --neon-green: #00ff00;
# }

# /* HIDE THE SIDEBAR */
# [data-testid="stSidebar"] {
#     display: none !important;
# }

# [data-testid="collapsedControl"] {
#     display: none !important;
# }

# * {
#     font-family: 'Inter', sans-serif;
# }

# .stApp {
#     background-color: var(--dark-bg);
#     color: var(--dark-text);
#     background-image: 
#         radial-gradient(at 40% 20%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
#         radial-gradient(at 80% 0%, rgba(236, 72, 153, 0.15) 0px, transparent 50%),
#         radial-gradient(at 0% 50%, rgba(16, 185, 129, 0.1) 0px, transparent 50%),
#         radial-gradient(at 80% 50%, rgba(59, 130, 246, 0.1) 0px, transparent 50%);
# }

# /* Main Header */
# .main-header {
#     font-family: 'Fira Code', monospace;
#     font-weight: 800;
#     font-size: 3.5rem;
#     text-align: center;
#     margin-bottom: 0.5rem;
#     background: linear-gradient(90deg, var(--neon-pink), var(--neon-blue), var(--neon-green));
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     text-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
#     animation: glow 2s ease-in-out infinite alternate;
# }

# @keyframes glow {
#     from { text-shadow: 0 0 10px rgba(255, 0, 255, 0.3); }
#     to { text-shadow: 0 0 20px rgba(0, 255, 255, 0.4), 0 0 30px rgba(0, 255, 255, 0.2); }
# }

# .subheader {
#     color: var(--dark-text);
#     text-align: center;
#     margin-bottom: 2rem;
#     font-weight: 300;
#     font-size: 1.2rem;
#     opacity: 0.9;
# }

# /* Cards and Containers */
# .glass-card {
#     background: rgba(30, 41, 59, 0.7);
#     backdrop-filter: blur(10px);
#     border-radius: 20px;
#     padding: 2rem;
#     border: 1px solid rgba(255, 255, 255, 0.1);
#     box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
#     margin-bottom: 1.5rem;
#     transition: transform 0.3s ease, box-shadow 0.3s ease;
# }

# .glass-card:hover {
#     transform: translateY(-5px);
#     box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
# }

# .code-container {
#     background: rgba(15, 23, 42, 0.9);
#     border-radius: 12px;
#     padding: 1.5rem;
#     border: 1px solid var(--dark-border);
#     font-family: 'Fira Code', monospace;
#     font-size: 14px;
#     margin: 1rem 0;
# }

# /* Tabs */
# .stTabs [data-baseweb="tab-list"] {
#     gap: 8px;
#     background-color: transparent;
#     border-bottom: 2px solid var(--dark-border);
# }

# .stTabs [data-baseweb="tab"] {
#     background: transparent;
#     border-radius: 10px 10px 0 0;
#     padding: 12px 24px;
#     font-weight: 600;
#     color: var(--dark-text);
#     border: none;
#     opacity: 0.7;
#     transition: all 0.3s ease;
# }

# .stTabs [data-baseweb="tab"]:hover {
#     opacity: 1;
#     background: rgba(139, 92, 246, 0.1);
# }

# .stTabs [aria-selected="true"] {
#     background: var(--gradient-1);
#     color: white;
#     opacity: 1;
#     box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
# }

# /* Buttons */
# .gradient-button {
#     background: var(--gradient-2);
#     color: white;
#     border: none;
#     border-radius: 12px;
#     padding: 14px 28px;
#     font-weight: 600;
#     font-size: 16px;
#     transition: all 0.3s ease;
#     width: 100%;
#     cursor: pointer;
#     position: relative;
#     overflow: hidden;
# }

# .gradient-button::before {
#     content: '';
#     position: absolute;
#     top: 0;
#     left: -100%;
#     width: 100%;
#     height: 100%;
#     background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
#     transition: left 0.5s;
# }

# .gradient-button:hover::before {
#     left: 100%;
# }

# .gradient-button:hover {
#     transform: translateY(-3px);
#     box-shadow: 0 8px 25px rgba(240, 147, 251, 0.4);
# }

# .secondary-button {
#     background: rgba(30, 41, 59, 0.8);
#     color: var(--dark-text);
#     border: 2px solid var(--primary);
#     border-radius: 12px;
#     padding: 10px 20px;
#     font-weight: 600;
#     transition: all 0.3s ease;
#     width: 100%;
# }

# .secondary-button:hover {
#     background: rgba(139, 92, 246, 0.1);
#     border-color: var(--secondary);
# }

# /* Text Areas and Inputs */
# .stTextArea textarea {
#     background-color: rgba(15, 23, 42, 0.9) !important;
#     color: var(--dark-text) !important;
#     border: 2px solid var(--dark-border) !important;
#     border-radius: 12px !important;
#     font-family: 'Fira Code', monospace !important;
#     font-size: 14px !important;
#     padding: 15px !important;
#     transition: border 0.3s ease !important;
# }

# .stTextArea textarea:focus {
#     border-color: var(--primary) !important;
#     box-shadow: 0 0 0 2px rgba(139, 92, 246, 0.2) !important;
# }

# /* Metrics Display */
# .metrics-grid {
#     display: grid;
#     grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
#     gap: 15px;
#     margin: 1.5rem 0;
# }

# .metric-card {
#     background: var(--gradient-3);
#     border-radius: 15px;
#     padding: 1.5rem;
#     text-align: center;
#     position: relative;
#     overflow: hidden;
# }

# .metric-card::before {
#     content: '';
#     position: absolute;
#     top: 0;
#     left: 0;
#     right: 0;
#     bottom: 0;
#     background: rgba(0, 0, 0, 0.2);
#     z-index: 1;
# }

# .metric-value {
#     font-size: 2.5rem;
#     font-weight: 800;
#     color: white;
#     margin: 0.5rem 0;
#     position: relative;
#     z-index: 2;
# }

# .metric-label {
#     font-size: 14px;
#     color: rgba(255, 255, 255, 0.9);
#     font-weight: 500;
#     position: relative;
#     z-index: 2;
# }

# /* Roast Container */
# .roast-container {
#     background: rgba(239, 68, 68, 0.1);
#     border-left: 4px solid var(--neon-pink);
#     border-radius: 12px;
#     padding: 1.5rem;
#     margin: 1.5rem 0;
#     position: relative;
#     overflow: hidden;
# }

# .roast-container::before {
#     content: '🔥';
#     position: absolute;
#     right: 20px;
#     top: 50%;
#     transform: translateY(-50%);
#     font-size: 3rem;
#     opacity: 0.2;
# }

# /* Issues Container */
# .issues-container {
#     background: rgba(245, 158, 11, 0.1);
#     border-left: 4px solid #F59E0B;
#     border-radius: 12px;
#     padding: 1.5rem;
#     margin: 1rem 0;
# }

# /* Suggestions Container */
# .suggestions-container {
#     background: rgba(16, 185, 129, 0.1);
#     border-left: 4px solid var(--accent);
#     border-radius: 12px;
#     padding: 1.5rem;
#     margin: 1rem 0;
# }

# /* Badges */
# .intensity-badge {
#     display: inline-block;
#     padding: 6px 16px;
#     border-radius: 20px;
#     font-size: 12px;
#     font-weight: 700;
#     text-transform: uppercase;
#     letter-spacing: 1px;
#     margin: 0 5px;
# }

# .intensity-mild {
#     background: var(--gradient-4);
#     color: white;
# }

# .intensity-medium {
#     background: linear-gradient(90deg, #f59e0b, #fbbf24);
#     color: white;
# }

# .intensity-brutal {
#     background: linear-gradient(90deg, #ef4444, #f87171);
#     color: white;
# }

# /* Loading Animation */
# .loading-container {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     flex-direction: column;
#     padding: 3rem;
# }

# .loading-spinner {
#     width: 60px;
#     height: 60px;
#     border: 3px solid transparent;
#     border-top: 3px solid var(--neon-pink);
#     border-right: 3px solid var(--neon-blue);
#     border-bottom: 3px solid var(--neon-green);
#     border-radius: 50%;
#     animation: spin 1s linear infinite;
#     margin-bottom: 1rem;
# }

# @keyframes spin {
#     0% { transform: rotate(0deg); }
#     100% { transform: rotate(360deg); }
# }

# .loading-text {
#     color: var(--dark-text);
#     font-size: 1.1rem;
#     font-weight: 500;
#     background: var(--gradient-1);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# /* Audio Player */
# .audio-player {
#     background: rgba(30, 41, 59, 0.8);
#     border-radius: 12px;
#     padding: 1rem;
#     margin: 1rem 0;
#     border: 1px solid var(--dark-border);
# }

# /* Scrollbar */
# ::-webkit-scrollbar {
#     width: 10px;
# }

# ::-webkit-scrollbar-track {
#     background: rgba(30, 41, 59, 0.5);
#     border-radius: 5px;
# }

# ::-webkit-scrollbar-thumb {
#     background: var(--gradient-1);
#     border-radius: 5px;
# }

# ::-webkit-scrollbar-thumb:hover {
#     background: var(--gradient-2);
# }

# /* Footer */
# .footer {
#     text-align: center;
#     margin-top: 3rem;
#     padding: 2rem;
#     color: var(--dark-text);
#     font-size: 14px;
#     opacity: 0.7;
#     border-top: 1px solid var(--dark-border);
# }

# /* Code Syntax */
# code {
#     font-family: 'Fira Code', monospace !important;
#     background: rgba(15, 23, 42, 0.9) !important;
#     padding: 2px 6px !important;
#     border-radius: 4px !important;
#     border: 1px solid var(--dark-border) !important;
# }

# /* Custom select boxes */
# .stSelectbox div[data-baseweb="select"] {
#     background-color: rgba(15, 23, 42, 0.9) !important;
#     color: var(--dark-text) !important;
#     border: 2px solid var(--dark-border) !important;
#     border-radius: 12px !important;
# }

# /* Radio buttons */
# .stRadio > div {
#     background: rgba(30, 41, 59, 0.7);
#     padding: 15px;
#     border-radius: 12px;
#     border: 1px solid var(--dark-border);
# }

# /* Alert boxes */
# .stAlert {
#     background: rgba(30, 41, 59, 0.8) !important;
#     color: var(--dark-text) !important;
#     border: 1px solid var(--dark-border) !important;
#     border-radius: 12px !important;
# }

# /* Success messages */
# .stSuccess {
#     background: rgba(16, 185, 129, 0.1) !important;
#     border: 1px solid var(--accent) !important;
# }

# /* Error messages */
# .stError {
#     background: rgba(239, 68, 68, 0.1) !important;
#     border: 1px solid #EF4444 !important;
# }

# /* Warning messages */
# .stWarning {
#     background: rgba(245, 158, 11, 0.1) !important;
#     border: 1px solid #F59E0B !important;
# }

# /* Info messages */
# .stInfo {
#     background: rgba(59, 130, 246, 0.1) !important;
#     border: 1px solid #3B82F6 !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # Initialize session state
# if 'analysis_result' not in st.session_state:
#     st.session_state.analysis_result = None
# if 'generation_result' not in st.session_state:
#     st.session_state.generation_result = None

# def speak_text(text):
#     """Use browser's speech synthesis for audio roasts"""
#     js_code = f"""
#     <script>
#     if ('speechSynthesis' in window) {{
#         // Cancel any ongoing speech
#         speechSynthesis.cancel();
        
#         // Create new utterance
#         const utterance = new SpeechSynthesisUtterance("{text}");
        
#         // Configure voice
#         utterance.rate = 1.0;
#         utterance.pitch = 1.0;
#         utterance.volume = 1.0;
        
#         // Try to get a good voice
#         const voices = speechSynthesis.getVoices();
#         if (voices.length > 0) {{
#             // Prefer English voices
#             const englishVoice = voices.find(voice => voice.lang.startsWith('en'));
#             if (englishVoice) {{
#                 utterance.voice = englishVoice;
#             }}
#         }}
        
#         // Speak
#         speechSynthesis.speak(utterance);
#     }} else {{
#         console.log('Speech synthesis not supported');
#     }}
#     </script>
#     """
#     st.components.v1.html(js_code, height=0)

# def analyze_code(code, language, roast_level):
#     """Send code to backend for analysis - FIXED VERSION"""
#     try:
#         response = requests.post(
#             f"{BACKEND_URL}/api/analyze",
#             json={
#                 "code": code,
#                 "language": language,
#                 "roast_level": roast_level
#             },
#             timeout=30
#         )
        
#         if response.status_code == 200:
#             return response.json()
#         else:
#             st.error(f"Backend error: {response.status_code} - {response.text}")
#             return None
#     except requests.exceptions.ConnectionError:
#         st.error("Could not connect to backend. Make sure it's running.")
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
#             timeout=30
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
#     # Header Section
#     st.markdown('<h1 class="main-header">🔥 R0AST C0DE AI 🔥</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="subheader">AI-powered code analysis with a sarcastic twist • Get roasted while you code!</p>', unsafe_allow_html=True)
    
#     # Create tabs
#     tab1, tab2 = st.tabs(["🔍 CODE ANALYSIS", "✨ CODE GENERATION"])
    
#     with tab1:
#         col1, col2 = st.columns([1, 1], gap="large")
        
#         with col1:
#             st.markdown("### 📝 YOUR CODE")
            
#             # Language selection
#             language = st.selectbox(
#                 "Select Language",
#                 ["python", "javascript", "java", "cpp"],
#                 index=0,
#                 help="Choose the programming language of your code"
#             )
            
#             # Code input with example
#             default_code = """def calculate_average(numbers):
#     \"\"\"Calculate average of numbers.\"\"\"
#     total = 0
#     count = 0
#     for n in numbers:
#         total += n
#         count += 1
#     return total / count

# # Test the function
# data = [85, 90, 78, 92, 88]
# avg = calculate_average(data)
# print(f"Average: {avg}")"""
            
#             code = st.text_area(
#                 "Paste your code here:",
#                 value=default_code,
#                 height=350,
#                 placeholder="Paste your code here and prepare to be roasted...",
#                 help="Enter the code you want to analyze",
#                 key="analysis_code"
#             )
            
#             # Roast intensity with style
#             st.markdown("### ⚡ ROAST INTENSITY")
#             roast_level = st.radio(
#                 "",
#                 ["mild", "medium", "brutal"],
#                 index=1,
#                 horizontal=True,
#                 label_visibility="collapsed",
#                 key="roast_level"
#             )
            
#             # Analyze button - SIMPLIFIED LOGIC
#             analyze_button = st.button("🚀 ANALYZE & ROAST MY CODE!", use_container_width=True, type="primary", key="analyze_btn")
            
#             if analyze_button:
#                 if code.strip():
#                     # Clear previous results
#                     st.session_state.analysis_result = None
                    
#                     # Show loading message
#                     with st.spinner("🤖 AI is analyzing your code..."):
#                         # Call the backend
#                         result = analyze_code(code, language, roast_level)
                        
#                         if result:
#                             st.session_state.analysis_result = result
                            
#                             # Play audio roast automatically
#                             if 'roast' in result and 'audio_text' in result['roast']:
#                                 speak_text(result['roast']['audio_text'])
                            
#                             st.success("Analysis complete! Check the results on the right.")
#                         else:
#                             st.error("Failed to analyze code. Please try again.")
#                 else:
#                     st.warning("Please enter some code to analyze!")
        
#         with col2:
#             st.markdown("### 📊 ANALYSIS RESULTS")
            
#             if st.session_state.analysis_result:
#                 result = st.session_state.analysis_result
                
#                 # Display metrics in grid
#                 st.markdown("#### 📈 CODE METRICS")
#                 metrics = result.get('analysis', {}).get('metrics', {})
                
#                 col_a, col_b, col_c = st.columns(3)
#                 with col_a:
#                     score = metrics.get('quality_score', 0)
#                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{score}</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">QUALITY SCORE</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with col_b:
#                     grade = metrics.get('grade', 'N/A')
#                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{grade}</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">GRADE</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 with col_c:
#                     lines = metrics.get('line_count', 0)
#                     st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
#                     st.markdown(f'<div class="metric-value">{lines}</div>', unsafe_allow_html=True)
#                     st.markdown('<div class="metric-label">LINES</div>', unsafe_allow_html=True)
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Display roast
#                 st.markdown("#### 🔥 AI ROAST")
#                 roast = result.get('roast', {})
#                 roast_text = roast.get('text', 'No roast generated')
#                 intensity = roast.get('intensity', 'medium')
                
#                 st.markdown(f'<div class="roast-container">', unsafe_allow_html=True)
#                 st.markdown(f'**Intensity:** <span class="intensity-badge intensity-{intensity}">{intensity.upper()}</span>')
#                 st.markdown(f'**{roast_text}**')
                
#                 # Audio controls
#                 col_audio1, col_audio2 = st.columns([1, 1])
#                 with col_audio1:
#                     if st.button("🔊 PLAY AUDIO ROAST", use_container_width=True, key="play_roast_audio"):
#                         if 'audio_text' in roast:
#                             speak_text(roast['audio_text'])
                
#                 with col_audio2:
#                     if st.button("🔄 REPLAY", use_container_width=True, key="replay_roast"):
#                         if 'audio_text' in roast:
#                             speak_text(roast['audio_text'])
                
#                 st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Display issues
#                 issues = result.get('analysis', {}).get('issues', [])
#                 if issues:
#                     st.markdown(f"#### ⚠️ ISSUES FOUND ({len(issues)})")
#                     st.markdown('<div class="issues-container">', unsafe_allow_html=True)
#                     for i, issue in enumerate(issues, 1):
#                         st.markdown(f"**{i}.** {issue}")
#                     st.markdown('</div>', unsafe_allow_html=True)
#                 else:
#                     st.success("🎉 No issues found! Your code is looking good!")
                
#                 # Display suggestions
#                 suggestions = result.get('analysis', {}).get('suggestions', [])
#                 if suggestions:
#                     st.markdown("#### 💡 SUGGESTIONS FOR IMPROVEMENT")
#                     st.markdown('<div class="suggestions-container">', unsafe_allow_html=True)
#                     for i, suggestion in enumerate(suggestions[:5], 1):
#                         st.markdown(f"**{i}.** {suggestion}")
#                     st.markdown('</div>', unsafe_allow_html=True)
                
#                 # Display corrected code if available
#                 if 'corrected_code' in result and result['corrected_code']:
#                     st.markdown("#### ✨ IMPROVED CODE")
#                     with st.expander("View improved version", expanded=False):
#                         st.code(result['corrected_code'], language='python')
                        
#                         # Download button
#                         st.download_button(
#                             label="📥 DOWNLOAD IMPROVED CODE",
#                             data=result['corrected_code'],
#                             file_name="improved_code.py",
#                             mime="text/plain",
#                             use_container_width=True
#                         )
            
#             else:
#                 # Show useful info instead of empty rectangle
#                 st.markdown("""
#                 <div style='text-align: center; padding: 2rem; background: rgba(30, 41, 59, 0.5); border-radius: 20px; border: 2px dashed var(--dark-border);'>
#                     <div style='font-size: 4rem; margin-bottom: 1rem;'>🔥</div>
#                     <h3>Ready to roast some code?</h3>
#                     <p>Paste your code on the left and let our AI give you some tough love!</p>
                    
#                     <div style='margin-top: 2rem; text-align: left; background: rgba(139, 92, 246, 0.1); padding: 1.5rem; border-radius: 12px;'>
#                         <h4>🔍 What you'll get:</h4>
#                         <p>✅ <strong>Quality Score</strong> - How good is your code?</p>
#                         <p>✅ <strong>AI Roast</strong> - Sarcastic feedback with audio!</p>
#                         <p>✅ <strong>Issues Found</strong> - Problems in your code</p>
#                         <p>✅ <strong>Improvement Suggestions</strong> - How to fix issues</p>
#                         <p>✅ <strong>Improved Code</strong> - Better version of your code</p>
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
    
#     with tab2:
#         col1, col2 = st.columns([1, 1], gap="large")
        
#         with col1:
#             st.markdown("### 💡 CODE GENERATION")
            
#             # Language selection
#             gen_language = st.selectbox(
#                 "Generate Code In",
#                 ["python", "javascript", "java", "cpp"],
#                 index=0,
#                 key="gen_lang"
#             )
            
#             # Prompt input
#             prompt = st.text_area(
#                 "Describe what you want to generate:",
#                 placeholder="e.g., 'Create a function to calculate factorial of a number'",
#                 height=200,
#                 help="Describe the code you want AI to generate",
#                 key="gen_prompt"
#             )
            
#             # Generate button
#             generate_button = st.button("🚀 GENERATE CODE", use_container_width=True, type="primary", key="generate_btn")
            
#             if generate_button:
#                 if prompt.strip():
#                     with st.spinner("🤖 AI is generating your code..."):
#                         result = generate_code(prompt, gen_language)
#                         if result:
#                             st.session_state.generation_result = result
                            
#                             # Play audio
#                             if 'audio_roast' in result:
#                                 speak_text(result['audio_roast'])
                            
#                             st.success("Code generated successfully!")
#                 else:
#                     st.warning("Please enter a description!")
        
#         with col2:
#             st.markdown("### 📄 GENERATED CODE")
            
#             if st.session_state.generation_result:
#                 result = st.session_state.generation_result
                
#                 # Display roast
#                 roast = result.get('roast', '')
#                 if roast:
#                     st.markdown("#### 😂 AI SAYS...")
#                     st.info(f"**{roast}**")
                    
#                     # Audio controls
#                     if st.button("🔊 PLAY AUDIO", use_container_width=True, key="play_gen_audio"):
#                         if 'audio_roast' in result:
#                             speak_text(result['audio_roast'])
                
#                 # Display generated code
#                 code = result.get('code', '')
#                 if code:
#                     st.markdown("#### ✨ GENERATED CODE")
#                     st.code(code, language='python')
                    
#                     # Action buttons
#                     col_dl, col_cp = st.columns([1, 1])
#                     with col_dl:
#                         st.download_button(
#                             label="📥 DOWNLOAD CODE",
#                             data=code,
#                             file_name="generated_code.py",
#                             mime="text/plain",
#                             use_container_width=True,
#                             key="download_gen"
#                         )
                    
#                     with col_cp:
#                         if st.button("📋 COPY TO CLIPBOARD", use_container_width=True, key="copy_gen"):
#                             st.code(code, language='python')
#                             st.success("Code copied to clipboard!")
                
#                 # Tips for better generation
#                 st.markdown("""
#                 <div style='margin-top: 2rem; padding: 1rem; background: rgba(59, 130, 246, 0.1); border-radius: 10px; border-left: 4px solid #3B82F6;'>
#                     <h4>💡 Tips for better code generation:</h4>
#                     <ul style='margin: 0; padding-left: 1.2rem;'>
#                         <li>Be specific about what you want</li>
#                         <li>Mention the programming language</li>
#                         <li>Include requirements or constraints</li>
#                         <li>Ask for comments or documentation</li>
#                     </ul>
#                 </div>
#                 """, unsafe_allow_html=True)
            
#             else:
#                 # Show useful info instead of empty rectangle
#                 st.markdown("""
#                 <div style='text-align: center; padding: 2rem; background: rgba(30, 41, 59, 0.5); border-radius: 20px; border: 2px dashed var(--dark-border);'>
#                     <div style='font-size: 4rem; margin-bottom: 1rem;'>✨</div>
#                     <h3>Turn ideas into code!</h3>
#                     <p>Describe what you want, and our AI will generate the code for you.</p>
                    
#                     <div style='margin-top: 2rem; text-align: left; background: rgba(139, 92, 246, 0.1); padding: 1.5rem; border-radius: 12px;'>
#                         <h4>🎯 Try these examples:</h4>
#                         <p>• <strong>"Create a function to calculate factorial"</strong></p>
#                         <p>• <strong>"Generate a palindrome checker in Python"</strong></p>
#                         <p>• <strong>"Write a simple calculator with add, subtract, multiply, divide"</strong></p>
#                         <p>• <strong>"Create a function to reverse a string"</strong></p>
#                         <p>• <strong>"Generate code to read a file and count words"</strong></p>
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)
    
#     # Footer
#     st.markdown("""
#     <div class="footer">
#         <p>🔥 ROAST CODE AI • Built with ❤️ using Streamlit & Flask</p>
#         <p>Because sometimes your code needs a reality check!</p>
#         <p style="font-size: 12px; margin-top: 1rem; opacity: 0.5;">
#             Audio feedback powered by your browser's speech synthesis • v2.0
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()

# frontend/app.py - FIXED VERSION
import os
import streamlit as st
import requests
import json
from datetime import datetime

# Set page configuration - HIDE SIDEBAR
st.set_page_config(
    page_title="🔥 Roast Code AI",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Backend URL - UPDATE THIS TO YOUR ACTUAL BACKEND URL
BACKEND_URL = os.getenv("BACKEND_URL", "https://roast-code-ai-backend.onrender.com")

# Modern AI-themed CSS with gradient colors
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --primary: #8B5CF6;
    --secondary: #EC4899;
    --accent: #10B981;
    --dark-bg: #0F172A;
    --dark-card: #1E293B;
    --dark-text: #F1F5F9;
    --dark-border: #334155;
    --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    --neon-pink: #ff00ff;
    --neon-blue: #00ffff;
    --neon-green: #00ff00;
}

/* HIDE THE SIDEBAR */
[data-testid="stSidebar"] {
    display: none !important;
}

[data-testid="collapsedControl"] {
    display: none !important;
}

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background-color: var(--dark-bg);
    color: var(--dark-text);
    background-image: 
        radial-gradient(at 40% 20%, rgba(139, 92, 246, 0.15) 0px, transparent 50%),
        radial-gradient(at 80% 0%, rgba(236, 72, 153, 0.15) 0px, transparent 50%),
        radial-gradient(at 0% 50%, rgba(16, 185, 129, 0.1) 0px, transparent 50%),
        radial-gradient(at 80% 50%, rgba(59, 130, 246, 0.1) 0px, transparent 50%);
}

/* Main Header */
.main-header {
    font-family: 'Fira Code', monospace;
    font-weight: 800;
    font-size: 3.5rem;
    text-align: center;
    margin-bottom: 0.5rem;
    background: linear-gradient(90deg, var(--neon-pink), var(--neon-blue), var(--neon-green));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(255, 0, 255, 0.3);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px rgba(255, 0, 255, 0.3); }
    to { text-shadow: 0 0 20px rgba(0, 255, 255, 0.4), 0 0 30px rgba(0, 255, 255, 0.2); }
}

.subheader {
    color: var(--dark-text);
    text-align: center;
    margin-bottom: 2rem;
    font-weight: 300;
    font-size: 1.2rem;
    opacity: 0.9;
}

/* Cards and Containers */
.glass-card {
    background: rgba(30, 41, 59, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    margin-bottom: 1.5rem;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
}

.code-container {
    background: rgba(15, 23, 42, 0.9);
    border-radius: 12px;
    padding: 1.5rem;
    border: 1px solid var(--dark-border);
    font-family: 'Fira Code', monospace;
    font-size: 14px;
    margin: 1rem 0;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: transparent;
    border-bottom: 2px solid var(--dark-border);
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 10px 10px 0 0;
    padding: 12px 24px;
    font-weight: 600;
    color: var(--dark-text);
    border: none;
    opacity: 0.7;
    transition: all 0.3s ease;
}

.stTabs [data-baseweb="tab"]:hover {
    opacity: 1;
    background: rgba(139, 92, 246, 0.1);
}

.stTabs [aria-selected="true"] {
    background: var(--gradient-1);
    color: white;
    opacity: 1;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

/* Buttons */
.gradient-button {
    background: var(--gradient-2);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 14px 28px;
    font-weight: 600;
    font-size: 16px;
    transition: all 0.3s ease;
    width: 100%;
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.gradient-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.5s;
}

.gradient-button:hover::before {
    left: 100%;
}

.gradient-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(240, 147, 251, 0.4);
}

/* Metrics Display */
.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 15px;
    margin: 1.5rem 0;
}

.metric-card {
    background: var(--gradient-3);
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 800;
    color: white;
    margin: 0.5rem 0;
    position: relative;
    z-index: 2;
}

.metric-label {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.9);
    font-weight: 500;
    position: relative;
    z-index: 2;
}

/* Roast Container */
.roast-container {
    background: rgba(239, 68, 68, 0.1);
    border-left: 4px solid var(--neon-pink);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    position: relative;
    overflow: hidden;
}

.roast-container::before {
    content: '🔥';
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 3rem;
    opacity: 0.2;
}

/* Issues Container */
.issues-container {
    background: rgba(245, 158, 11, 0.1);
    border-left: 4px solid #F59E0B;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
}

/* Suggestions Container */
.suggestions-container {
    background: rgba(16, 185, 129, 0.1);
    border-left: 4px solid var(--accent);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
}

/* Badges */
.intensity-badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin: 0 5px;
}

.intensity-mild {
    background: var(--gradient-4);
    color: white;
}

.intensity-medium {
    background: linear-gradient(90deg, #f59e0b, #fbbf24);
    color: white;
}

.intensity-brutal {
    background: linear-gradient(90deg, #ef4444, #f87171);
    color: white;
}

/* Info boxes */
.info-box {
    background: rgba(30, 41, 59, 0.5);
    border-radius: 20px;
    border: 2px dashed var(--dark-border);
    padding: 2rem;
    text-align: center;
    margin: 1rem 0;
}

.info-box h3 {
    color: var(--accent);
    margin-bottom: 1rem;
}

.info-box p {
    color: var(--dark-text);
    opacity: 0.9;
}

.feature-list {
    background: rgba(139, 92, 246, 0.1);
    padding: 1.5rem;
    border-radius: 12px;
    margin-top: 1.5rem;
    text-align: left;
}

.feature-list h4 {
    color: var(--primary);
    margin-bottom: 1rem;
}

.feature-list p {
    margin: 0.5rem 0;
    color: var(--dark-text);
}

.example-list {
    background: rgba(139, 92, 246, 0.1);
    padding: 1.5rem;
    border-radius: 12px;
    margin-top: 1.5rem;
    text-align: left;
}

.example-list h4 {
    color: var(--primary);
    margin-bottom: 1rem;
}

.example-list p {
    margin: 0.5rem 0;
    color: var(--dark-text);
}

/* Tips box */
.tips-box {
    background: rgba(59, 130, 246, 0.1);
    border-radius: 10px;
    border-left: 4px solid #3B82F6;
    padding: 1rem;
    margin-top: 2rem;
}

.tips-box h4 {
    color: #3B82F6;
    margin-bottom: 0.5rem;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(30, 41, 59, 0.5);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb {
    background: var(--gradient-1);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--gradient-2);
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 3rem;
    padding: 2rem;
    color: var(--dark-text);
    font-size: 14px;
    opacity: 0.7;
    border-top: 1px solid var(--dark-border);
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'analysis_result' not in st.session_state:
    st.session_state.analysis_result = None
if 'generation_result' not in st.session_state:
    st.session_state.generation_result = None

def speak_text(text):
    """Use browser's speech synthesis for audio roasts"""
    # Clean text for JavaScript
    clean_text = text.replace('"', '\\"').replace("'", "\\'").replace("\n", " ")
    
    js_code = f"""
    <script>
    if ('speechSynthesis' in window) {{
        // Cancel any ongoing speech
        speechSynthesis.cancel();
        
        // Create new utterance
        const utterance = new SpeechSynthesisUtterance("{clean_text}");
        
        // Configure voice
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        utterance.volume = 1.0;
        
        // Speak
        speechSynthesis.speak(utterance);
    }}
    </script>
    """
    st.components.v1.html(js_code, height=0)

def analyze_code(code, language, roast_level):
    """Send code to backend for analysis"""
    try:
        # Add a timeout and better error handling
        response = requests.post(
            f"{BACKEND_URL}/api/analyze",
            json={
                "code": code,
                "language": language,
                "roast_level": roast_level
            },
            timeout=15
        )
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 502:
            st.error("Backend server is temporarily unavailable. Please try again in a few minutes.")
            return None
        else:
            st.error(f"Server error: {response.status_code}")
            # Try to get more details
            try:
                error_detail = response.json()
                if 'error' in error_detail:
                    st.error(f"Error: {error_detail['error']}")
            except:
                pass
            return None
    except requests.exceptions.ConnectionError:
        st.error(f"Could not connect to backend at {BACKEND_URL}. Please check if the backend is running.")
        return None
    except requests.exceptions.Timeout:
        st.error("Request timed out. The server might be overloaded. Please try again.")
        return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def generate_code(prompt, language):
    """Generate code from prompt"""
    try:
        response = requests.post(
            f"{BACKEND_URL}/api/generate",
            json={
                "prompt": prompt,
                "language": language
            },
            timeout=15
        )
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 502:
            st.error("Backend server is temporarily unavailable. Please try again in a few minutes.")
            return None
        else:
            st.error(f"Server error: {response.status_code}")
            return None
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to backend.")
        return None
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def main():
    # Header Section
    st.markdown('<h1 class="main-header">🔥 R0AST C0DE AI 🔥</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">AI-powered code analysis with a sarcastic twist • Get roasted while you code!</p>', unsafe_allow_html=True)
    
    # Create tabs
    tab1, tab2 = st.tabs(["🔍 CODE ANALYSIS", "✨ CODE GENERATION"])
    
    with tab1:
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("### 📝 YOUR CODE")
            
            # Language selection
            language = st.selectbox(
                "Select Language",
                ["python", "javascript", "java", "cpp"],
                index=0,
                help="Choose the programming language of your code"
            )
            
            # Code input with example
            default_code = """def calculate_average(numbers):
    \"\"\"Calculate average of numbers.\"\"\"
    total = 0
    count = 0
    for n in numbers:
        total += n
        count += 1
    return total / count

# Test the function
data = [85, 90, 78, 92, 88]
avg = calculate_average(data)
print(f"Average: {avg}")"""
            
            code = st.text_area(
                "Paste your code here:",
                value=default_code,
                height=350,
                placeholder="Paste your code here and prepare to be roasted...",
                help="Enter the code you want to analyze",
                key="analysis_code"
            )
            
            # Roast intensity with style
            st.markdown("### ⚡ ROAST INTENSITY")
            roast_level = st.radio(
                "",
                ["mild", "medium", "brutal"],
                index=1,
                horizontal=True,
                label_visibility="collapsed",
                key="roast_level"
            )
            
            # Analyze button
            analyze_button = st.button("🚀 ANALYZE & ROAST MY CODE!", use_container_width=True, type="primary", key="analyze_btn")
            
            if analyze_button:
                if code.strip():
                    # Clear previous results
                    st.session_state.analysis_result = None
                    
                    # Show loading message
                    with st.spinner("🤖 AI is analyzing your code..."):
                        # Call the backend
                        result = analyze_code(code, language, roast_level)
                        
                        if result:
                            st.session_state.analysis_result = result
                            
                            # Play audio roast automatically
                            if 'roast' in result and 'audio_text' in result['roast']:
                                speak_text(result['roast']['audio_text'])
                            
                            st.success("✅ Analysis complete! Check the results on the right.")
                        else:
                            st.error("❌ Failed to analyze code. Please check backend connection.")
                else:
                    st.warning("⚠️ Please enter some code to analyze!")
        
        with col2:
            st.markdown("### 📊 ANALYSIS RESULTS")
            
            if st.session_state.analysis_result:
                result = st.session_state.analysis_result
                
                # Display metrics in grid
                st.markdown("#### 📈 CODE METRICS")
                metrics = result.get('analysis', {}).get('metrics', {})
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    score = metrics.get('quality_score', 0)
                    st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{score}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">QUALITY SCORE</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col_b:
                    grade = metrics.get('grade', 'N/A')
                    st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{grade}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">GRADE</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col_c:
                    lines = metrics.get('line_count', 0)
                    st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
                    st.markdown(f'<div class="metric-value">{lines}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="metric-label">LINES</div>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # Display roast
                st.markdown("#### 🔥 AI ROAST")
                roast = result.get('roast', {})
                roast_text = roast.get('text', 'No roast generated')
                intensity = roast.get('intensity', 'medium')
                
                st.markdown(f'<div class="roast-container">', unsafe_allow_html=True)
                st.markdown(f'**Intensity:** <span class="intensity-badge intensity-{intensity}">{intensity.upper()}</span>')
                st.markdown(f'**{roast_text}**')
                
                # Audio controls
                col_audio1, col_audio2 = st.columns([1, 1])
                with col_audio1:
                    if st.button("🔊 PLAY AUDIO ROAST", use_container_width=True, key="play_roast_audio"):
                        if 'audio_text' in roast:
                            speak_text(roast['audio_text'])
                
                with col_audio2:
                    if st.button("🔄 REPLAY", use_container_width=True, key="replay_roast"):
                        if 'audio_text' in roast:
                            speak_text(roast['audio_text'])
                
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Display issues
                issues = result.get('analysis', {}).get('issues', [])
                if issues:
                    st.markdown(f"#### ⚠️ ISSUES FOUND ({len(issues)})")
                    st.markdown('<div class="issues-container">', unsafe_allow_html=True)
                    for i, issue in enumerate(issues, 1):
                        st.markdown(f"**{i}.** {issue}")
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.success("🎉 No issues found! Your code is looking good!")
                
                # Display suggestions
                suggestions = result.get('analysis', {}).get('suggestions', [])
                if suggestions:
                    st.markdown("#### 💡 SUGGESTIONS FOR IMPROVEMENT")
                    st.markdown('<div class="suggestions-container">', unsafe_allow_html=True)
                    for i, suggestion in enumerate(suggestions[:5], 1):
                        st.markdown(f"**{i}.** {suggestion}")
                    st.markdown('</div>', unsafe_allow_html=True)
            
            else:
                # Show info using Streamlit components instead of raw HTML
                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                st.markdown("### 🔥 Ready to roast some code?")
                st.markdown("Paste your code on the left and let our AI give you some tough love!")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="feature-list">', unsafe_allow_html=True)
                st.markdown("#### 🔍 What you'll get:")
                st.markdown("✅ **Quality Score** - How good is your code?")
                st.markdown("✅ **AI Roast** - Sarcastic feedback with audio!")
                st.markdown("✅ **Issues Found** - Problems in your code")
                st.markdown("✅ **Improvement Suggestions** - How to fix issues")
                st.markdown("✅ **Improved Code** - Better version of your code")
                st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("### 💡 CODE GENERATION")
            
            # Language selection
            gen_language = st.selectbox(
                "Generate Code In",
                ["python", "javascript", "java", "cpp"],
                index=0,
                key="gen_lang"
            )
            
            # Prompt input
            prompt = st.text_area(
                "Describe what you want to generate:",
                placeholder="e.g., 'Create a function to calculate factorial of a number'",
                height=200,
                help="Describe the code you want AI to generate",
                key="gen_prompt"
            )
            
            # Generate button
            generate_button = st.button("🚀 GENERATE CODE", use_container_width=True, type="primary", key="generate_btn")
            
            if generate_button:
                if prompt.strip():
                    with st.spinner("🤖 AI is generating your code..."):
                        result = generate_code(prompt, gen_language)
                        if result:
                            st.session_state.generation_result = result
                            
                            # Play audio
                            if 'audio_roast' in result:
                                speak_text(result['audio_roast'])
                            
                            st.success("✅ Code generated successfully!")
                else:
                    st.warning("⚠️ Please enter a description!")
        
        with col2:
            st.markdown("### 📄 GENERATED CODE")
            
            if st.session_state.generation_result:
                result = st.session_state.generation_result
                
                # Display roast
                roast = result.get('roast', '')
                if roast:
                    st.markdown("#### 😂 AI SAYS...")
                    st.info(f"**{roast}**")
                    
                    # Audio controls
                    if st.button("🔊 PLAY AUDIO", use_container_width=True, key="play_gen_audio"):
                        if 'audio_roast' in result:
                            speak_text(result['audio_roast'])
                
                # Display generated code
                code = result.get('code', '')
                if code:
                    st.markdown("#### ✨ GENERATED CODE")
                    st.code(code, language='python')
                    
                    # Action buttons
                    col_dl, col_cp = st.columns([1, 1])
                    with col_dl:
                        st.download_button(
                            label="📥 DOWNLOAD CODE",
                            data=code,
                            file_name="generated_code.py",
                            mime="text/plain",
                            use_container_width=True,
                            key="download_gen"
                        )
                    
                    with col_cp:
                        if st.button("📋 COPY TO CLIPBOARD", use_container_width=True, key="copy_gen"):
                            st.code(code, language='python')
                            st.success("📋 Code copied to clipboard!")
                
                # Tips for better generation
                st.markdown('<div class="tips-box">', unsafe_allow_html=True)
                st.markdown("#### 💡 Tips for better code generation:")
                st.markdown("• Be specific about what you want")
                st.markdown("• Mention the programming language")
                st.markdown("• Include requirements or constraints")
                st.markdown("• Ask for comments or documentation")
                st.markdown('</div>', unsafe_allow_html=True)
            
            else:
                # Show info using Streamlit components
                st.markdown('<div class="info-box">', unsafe_allow_html=True)
                st.markdown("### ✨ Turn ideas into code!")
                st.markdown("Describe what you want, and our AI will generate the code for you.")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="example-list">', unsafe_allow_html=True)
                st.markdown("#### 🎯 Try these examples:")
                st.markdown('• **"Create a function to calculate factorial"**')
                st.markdown('• **"Generate a palindrome checker in Python"**')
                st.markdown('• **"Write a simple calculator with add, subtract, multiply, divide"**')
                st.markdown('• **"Create a function to reverse a string"**')
                st.markdown('• **"Generate code to read a file and count words"**')
                st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>🔥 ROAST CODE AI • Built with ❤️ using Streamlit & Flask</p>
        <p>Because sometimes your code needs a reality check!</p>
        <p style="font-size: 12px; margin-top: 1rem; opacity: 0.5;">
            Audio feedback powered by your browser's speech synthesis • v2.0
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Debug info (hidden by default, can be enabled for troubleshooting)
    with st.expander("🔧 Debug Info (For Troubleshooting)", expanded=False):
        st.write(f"Backend URL: `{BACKEND_URL}`")
        st.write(f"Analysis Result in Session: {st.session_state.analysis_result is not None}")
        st.write(f"Generation Result in Session: {st.session_state.generation_result is not None}")
        
        # Test backend connection
        if st.button("Test Backend Connection"):
            try:
                response = requests.get(f"{BACKEND_URL}/api/health", timeout=5)
                if response.status_code == 200:
                    st.success(f"✅ Backend is responding! Status: {response.json().get('status', 'Unknown')}")
                else:
                    st.error(f"❌ Backend returned status: {response.status_code}")
            except Exception as e:
                st.error(f"❌ Cannot connect to backend: {str(e)}")

if __name__ == "__main__":
    main()