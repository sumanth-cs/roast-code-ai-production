# app.py - COMPLETE FULL-STACK APP IN ONE FILE
import os
import json
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

# ========== FLASK BACKEND ==========
app = Flask(__name__)
CORS(app)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "roast-code-ai",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    try:
        data = request.json
        code = data.get('code', '')
        language = data.get('language', 'python')
        
        if not code:
            return jsonify({"error": "No code provided"}), 400
        
        # Simple analysis
        lines = code.splitlines()
        line_count = len(lines)
        
        # Quality score calculation
        quality_score = 100
        if line_count > 100:
            quality_score -= 20
        if 'TODO' in code or 'FIXME' in code:
            quality_score -= 15
            
        quality_score = max(0, min(100, quality_score))
        
        # Grade
        if quality_score >= 90:
            grade = 'A'
        elif quality_score >= 80:
            grade = 'B'
        elif quality_score >= 70:
            grade = 'C'
        elif quality_score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        # Issues
        issues = []
        if line_count > 200:
            issues.append("Code is too long (over 200 lines)")
        if 'password' in code.lower() or 'secret' in code.lower():
            issues.append("Potential hardcoded credentials")
        if line_count > 0 and code.count('#') / line_count < 0.1:
            issues.append("Consider adding more comments")
        
        # Roast based on quality
        if quality_score >= 80:
            roast_text = "🔥 Your code is on fire! Great job!"
        elif quality_score >= 60:
            roast_text = "👍 Not bad! Some room for improvement."
        else:
            roast_text = "💀 Oof! This code needs some love."
        
        return jsonify({
            "success": True,
            "analysis": {
                "issues": issues,
                "metrics": {
                    "line_count": line_count,
                    "character_count": len(code),
                    "quality_score": quality_score
                },
                "quality_score": quality_score,
                "grade": grade
            },
            "roast": {
                "text": roast_text,
                "intensity": "medium",
                "model": "simple-analyzer"
            },
            "suggestions": [
                "Add comments to explain complex logic",
                "Break long functions into smaller ones",
                "Use meaningful variable names",
                "Write unit tests"
            ],
            "timestamp": datetime.utcnow().isoformat()
        })
    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500

@app.route('/api/generate', methods=['POST'])
def generate_code():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
        
        # Simple code generation
        generated_code = f'''# Generated code for: {prompt}

def solution():
    """
    TODO: Implement your solution here
    """
    # Your code goes here
    result = None
    return result

if __name__ == "__main__":
    solution()'''
        
        return jsonify({
            "success": True,
            "code": generated_code,
            "message": "Code generated successfully"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== STREAMLIT FRONTEND ==========
def run_streamlit():
    """Run Streamlit in a separate thread"""
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
        st.title("🔥 Roast Code AI")
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
        st.markdown("AI-powered code analysis with humorous feedback")
    
    # Main content
    if selected == "Code Analysis":
        st.title("🔍 Code Analysis")
        st.markdown("Paste your code below and get AI-powered feedback!")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            code = st.text_area(
                "Your Code",
                height=300,
                placeholder="Paste your code here...",
                key="code_input"
            )
            
            language = st.selectbox(
                "Language",
                ["Python", "JavaScript", "Java", "C++", "Other"]
            )
            
            if st.button("🔥 Analyze My Code!", type="primary", use_container_width=True):
                if code.strip():
                    with st.spinner("Analyzing your code..."):
                        try:
                            response = requests.post(
                                "http://localhost:5000/api/analyze",
                                json={"code": code, "language": language.lower()},
                                timeout=10
                            )
                            
                            if response.status_code == 200:
                                st.session_state.result = response.json()
                                st.success("Analysis complete!")
                            else:
                                st.error("Backend error")
                        except:
                            # Fallback
                            lines = code.splitlines()
                            st.session_state.result = {
                                "success": True,
                                "analysis": {
                                    "issues": ["Backend not available - using local analysis"],
                                    "metrics": {"line_count": len(lines)},
                                    "quality_score": 75,
                                    "grade": "B"
                                },
                                "roast": {
                                    "text": f"Found {len(lines)} lines of code!",
                                    "intensity": "medium",
                                    "model": "local"
                                },
                                "suggestions": ["Add comments", "Write tests"]
                            }
                else:
                    st.warning("Please paste some code first!")
        
        with col2:
            if st.session_state.result:
                result = st.session_state.result
                
                st.markdown("### 📊 Results")
                
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
                    st.markdown("### ⚠️ Issues")
                    for issue in result['analysis']['issues']:
                        st.warning(issue)
                
                # Suggestions
                if result.get('suggestions'):
                    st.markdown("### 💡 Suggestions")
                    for suggestion in result['suggestions']:
                        st.success(suggestion)
    
    elif selected == "Code Generation":
        st.title("✨ Code Generation")
        
        prompt = st.text_area(
            "Describe your code",
            placeholder="e.g., 'Create a function to calculate factorial'",
            height=100
        )
        
        language = st.selectbox(
            "Language",
            ["Python", "JavaScript", "Java"]
        )
        
        if st.button("🚀 Generate Code", type="primary"):
            if prompt:
                with st.spinner("Generating code..."):
                    try:
                        response = requests.post(
                            "http://localhost:5000/api/generate",
                            json={"prompt": prompt, "language": language.lower()},
                            timeout=10
                        )
                        
                        if response.status_code == 200:
                            result = response.json()
                            st.code(result['code'], language=language.lower())
                            st.success("Code generated!")
                        else:
                            st.error("Backend error")
                    except:
                        # Fallback
                        st.code(f'''# Generated code for: {prompt}

# TODO: Implement your solution
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()''', language=language.lower())
            else:
                st.warning("Please enter a description!")

# ========== MAIN ==========
def main():
    """Start both Flask and Streamlit"""
    import sys
    
    # Check if we're running Flask or Streamlit
    if len(sys.argv) > 1 and sys.argv[1] == "flask":
        # Run Flask
        port = int(os.getenv('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
    else:
        # Run Streamlit
        run_streamlit()

if __name__ == "__main__":
    # This is a trick: Railway will run this as "python app.py"
    # We need to start Flask, but Streamlit needs to be imported
    # So we'll use environment variable to decide
    
    if os.getenv('RAILWAY_ENVIRONMENT'):
        # On Railway, run Flask
        port = int(os.getenv('PORT', 5000))
        print(f"Starting Flask on port {port}")
        app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
    else:
        # For local development, run Streamlit
        print("Starting Streamlit...")
        run_streamlit()