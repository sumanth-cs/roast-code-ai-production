# # # import asyncio
# # # import json
# # # import os
# # # import uuid
# # # from datetime import datetime
# # # from typing import List, Dict, Optional

# # # import redis
# # # from flask import Flask, request, jsonify, session
# # # from flask_cors import CORS
# # # from flask_socketio import SocketIO, join_room, leave_room, emit
# # # from werkzeug.security import generate_password_hash, check_password_hash

# # # from services.code_quality import CodeQualityAnalyzer
# # # from services.llm_service import LLMService
# # # from services.multilingual import MultiLanguageSupport
# # # from services.tts_service import TTSService
# # # from utils.cache import CacheManager
# # # from models.collaboration import CollaborationSession

# # # # Initialize Flask app
# # # app = Flask(__name__)
# # # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
# # # app.config['REDIS_URL'] = os.getenv('REDIS_URL', 'redis://localhost:6379')

# # # # Enable CORS
# # # CORS(app, supports_credentials=True, origins=os.getenv('ALLOWED_ORIGINS', '*').split(','))

# # # # Initialize SocketIO for real-time collaboration
# # # socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# # # # Initialize services
# # # redis_client = redis.from_url(app.config['REDIS_URL'])
# # # cache_manager = CacheManager(redis_client)
# # # code_analyzer = CodeQualityAnalyzer()
# # # llm_service = LLMService()
# # # multilingual = MultiLanguageSupport()
# # # tts_service = TTSService()

# # # # Store active collaboration sessions
# # # active_sessions: Dict[str, CollaborationSession] = {}

# # # @app.route('/api/analyze', methods=['POST'])
# # # async def analyze_code():
# # #     """Analyze code with multi-language support"""
# # #     try:
# # #         data = request.json
# # #         code = data.get('code', '')
# # #         language = data.get('language', 'python')
# # #         roast_level = data.get('roast_level', 'medium')
# # #         user_id = data.get('user_id', str(uuid.uuid4()))
        
# # #         if not code:
# # #             return jsonify({"error": "No code provided"}), 400
        
# # #         # Check cache first
# # #         cache_key = f"analysis:{hash(code)}:{language}:{roast_level}"
# # #         cached_result = cache_manager.get(cache_key)
# # #         if cached_result:
# # #             return jsonify(cached_result)
        
# # #         # Analyze code based on language
# # #         if language == 'python':
# # #             analysis = code_analyzer.analyze_python(code)
# # #         elif language == 'javascript':
# # #             analysis = code_analyzer.analyze_javascript(code)
# # #         elif language == 'java':
# # #             analysis = code_analyzer.analyze_java(code)
# # #         elif language == 'cpp':
# # #             analysis = code_analyzer.analyze_cpp(code)
# # #         else:
# # #             analysis = code_analyzer.analyze_generic(code, language)
        
# # #         # Generate roast with AI
# # #         roast = await llm_service.generate_roast(
# # #             code=code,
# # #             issues=analysis['issues'],
# # #             language=language,
# # #             intensity=roast_level
# # #         )
        
# # #         # Generate suggestions for improvement
# # #         suggestions = await llm_service.generate_suggestions(
# # #             code=code,
# # #             issues=analysis['issues'],
# # #             language=language
# # #         )
        
# # #         # Generate audio roast
# # #         audio_data = await tts_service.generate_audio_roast(
# # #             roast_text=roast['text'],
# # #             intensity=roast_level,
# # #             language=language
# # #         )
        
# # #         # Generate corrected code
# # #         corrected_code = await llm_service.correct_code(
# # #             code=code,
# # #             issues=analysis['issues'],
# # #             language=language
# # #         )
        
# # #         # Calculate comprehensive metrics
# # #         metrics = code_analyzer.calculate_comprehensive_metrics(
# # #             code=code,
# # #             analysis=analysis,
# # #             language=language
# # #         )
        
# # #         # Prepare response
# # #         result = {
# # #             "success": True,
# # #             "analysis": analysis,
# # #             "roast": roast,
# # #             "suggestions": suggestions,
# # #             "corrected_code": corrected_code,
# # #             "metrics": metrics,
# # #             "audio": audio_data,
# # #             "language": language,
# # #             "timestamp": datetime.utcnow().isoformat()
# # #         }
        
# # #         # Cache the result
# # #         cache_manager.set(cache_key, result, ttl=3600)
        
# # #         # Track user analytics
# # #         track_analysis_metrics(user_id, language, metrics)
        
# # #         return jsonify(result)
        
# # #     except Exception as e:
# # #         app.logger.error(f"Analysis error: {str(e)}")
# # #         return jsonify({
# # #             "error": "Internal server error",
# # #             "message": str(e)
# # #         }), 500

# # # @app.route('/api/generate', methods=['POST'])
# # # async def generate_code():
# # #     """Generate code based on prompt with multi-language support"""
# # #     try:
# # #         data = request.json
# # #         prompt = data.get('prompt', '')
# # #         language = data.get('language', 'python')
# # #         complexity = data.get('complexity', 'medium')
# # #         user_id = data.get('user_id', str(uuid.uuid4()))
        
# # #         if not prompt:
# # #             return jsonify({"error": "No prompt provided"}), 400
        
# # #         # Generate code using LLM
# # #         generated_code = await llm_service.generate_code_from_prompt(
# # #             prompt=prompt,
# # #             language=language,
# # #             complexity=complexity
# # #         )
        
# # #         # Analyze the generated code
# # #         analysis = code_analyzer.analyze_code(generated_code, language)
        
# # #         # Generate a roast for the generated code
# # #         roast = await llm_service.generate_roast(
# # #             code=generated_code,
# # #             issues=analysis['issues'],
# # #             language=language,
# # #             intensity='medium'
# # #         )
        
# # #         # Generate audio
# # #         audio_data = await tts_service.generate_audio_roast(
# # #             roast_text=roast['text'],
# # #             intensity='medium',
# # #             language=language
# # #         )
        
# # #         result = {
# # #             "success": True,
# # #             "code": generated_code,
# # #             "analysis": analysis,
# # #             "roast": roast,
# # #             "audio": audio_data,
# # #             "language": language,
# # #             "timestamp": datetime.utcnow().isoformat()
# # #         }
        
# # #         # Track generation metrics
# # #         track_generation_metrics(user_id, language, len(generated_code))
        
# # #         return jsonify(result)
        
# # #     except Exception as e:
# # #         app.logger.error(f"Generation error: {str(e)}")
# # #         return jsonify({"error": str(e)}), 500

# # # @app.route('/api/languages', methods=['GET'])
# # # def get_supported_languages():
# # #     """Get list of supported programming languages"""
# # #     languages = multilingual.get_supported_languages()
# # #     return jsonify({
# # #         "success": True,
# # #         "languages": languages,
# # #         "count": len(languages)
# # #     })

# # # @app.route('/api/metrics/history', methods=['GET'])
# # # def get_user_metrics_history():
# # #     """Get user's analysis history and metrics"""
# # #     user_id = request.args.get('user_id')
# # #     if not user_id:
# # #         return jsonify({"error": "User ID required"}), 400
    
# # #     history = get_user_history(user_id)
# # #     metrics = calculate_user_metrics(user_id)
    
# # #     return jsonify({
# # #         "success": True,
# # #         "history": history,
# # #         "metrics": metrics
# # #     })

# # # @app.route('/api/collaboration/create', methods=['POST'])
# # # def create_collaboration_session():
# # #     """Create a new collaboration session"""
# # #     data = request.json
# # #     session_name = data.get('name', f"Session-{datetime.now().strftime('%Y%m%d-%H%M%S')}")
# # #     language = data.get('language', 'python')
# # #     user_id = data.get('user_id')
    
# # #     if not user_id:
# # #         return jsonify({"error": "User ID required"}), 400
    
# # #     session_id = str(uuid.uuid4())
# # #     collaboration_session = CollaborationSession(
# # #         session_id=session_id,
# # #         name=session_name,
# # #         creator_id=user_id,
# # #         language=language
# # #     )
    
# # #     active_sessions[session_id] = collaboration_session
# # #     collaboration_session.add_participant(user_id, "host")
    
# # #     return jsonify({
# # #         "success": True,
# # #         "session_id": session_id,
# # #         "session": collaboration_session.to_dict()
# # #     })

# # # @app.route('/api/collaboration/<session_id>/join', methods=['POST'])
# # # def join_collaboration_session(session_id):
# # #     """Join an existing collaboration session"""
# # #     data = request.json
# # #     user_id = data.get('user_id')
# # #     username = data.get('username', f"User-{user_id[:8]}")
    
# # #     if session_id not in active_sessions:
# # #         return jsonify({"error": "Session not found"}), 404
    
# # #     session = active_sessions[session_id]
# # #     session.add_participant(user_id, username)
    
# # #     return jsonify({
# # #         "success": True,
# # #         "session": session.to_dict()
# # #     })

# # # # WebSocket event handlers
# # # @socketio.on('join_session')
# # # def handle_join_session(data):
# # #     """Handle client joining a collaboration session"""
# # #     session_id = data.get('session_id')
# # #     user_id = data.get('user_id')
# # #     username = data.get('username')
    
# # #     if session_id in active_sessions:
# # #         join_room(session_id)
# # #         session = active_sessions[session_id]
# # #         session.add_participant(user_id, username)
        
# # #         emit('user_joined', {
# # #             'user_id': user_id,
# # #             'username': username,
# # #             'participants': session.participants,
# # #             'timestamp': datetime.utcnow().isoformat()
# # #         }, room=session_id)
        
# # #         emit('session_update', session.to_dict(), room=session_id)

# # # @socketio.on('code_update')
# # # def handle_code_update(data):
# # #     """Handle real-time code updates"""
# # #     session_id = data.get('session_id')
# # #     user_id = data.get('user_id')
# # #     code = data.get('code')
# # #     cursor_position = data.get('cursor_position')
    
# # #     if session_id in active_sessions:
# # #         session = active_sessions[session_id]
# # #         session.update_code(code)
# # #         session.update_cursor_position(user_id, cursor_position)
        
# # #         emit('code_updated', {
# # #             'user_id': user_id,
# # #             'code': code,
# # #             'cursor_position': cursor_position,
# # #             'timestamp': datetime.utcnow().isoformat()
# # #         }, room=session_id, include_self=False)

# # # @socketio.on('leave_session')
# # # def handle_leave_session(data):
# # #     """Handle client leaving a collaboration session"""
# # #     session_id = data.get('session_id')
# # #     user_id = data.get('user_id')
    
# # #     if session_id in active_sessions:
# # #         leave_room(session_id)
# # #         session = active_sessions[session_id]
# # #         session.remove_participant(user_id)
        
# # #         emit('user_left', {
# # #             'user_id': user_id,
# # #             'participants': session.participants,
# # #             'timestamp': datetime.utcnow().isoformat()
# # #         }, room=session_id)
        
# # #         # If no participants left, clean up session
# # #         if not session.participants:
# # #             del active_sessions[session_id]

# # # @socketio.on('chat_message')
# # # def handle_chat_message(data):
# # #     """Handle chat messages in collaboration session"""
# # #     session_id = data.get('session_id')
# # #     user_id = data.get('user_id')
# # #     message = data.get('message')
    
# # #     if session_id in active_sessions:
# # #         session = active_sessions[session_id]
# # #         chat_message = {
# # #             'user_id': user_id,
# # #             'username': session.participants.get(user_id, {}).get('username'),
# # #             'message': message,
# # #             'timestamp': datetime.utcnow().isoformat()
# # #         }
        
# # #         session.add_chat_message(chat_message)
        
# # #         emit('new_chat_message', chat_message, room=session_id)

# # # # Utility functions
# # # def track_analysis_metrics(user_id, language, metrics):
# # #     """Track analysis metrics for user analytics"""
# # #     key = f"user:{user_id}:analytics"
# # #     redis_client.hincrby(key, f"total_analysis_{language}", 1)
# # #     redis_client.hincrby(key, "total_analysis", 1)
    
# # #     # Store metrics history
# # #     history_key = f"user:{user_id}:analysis_history"
# # #     history_entry = {
# # #         'timestamp': datetime.utcnow().isoformat(),
# # #         'language': language,
# # #         'metrics': metrics
# # #     }
# # #     redis_client.lpush(history_key, json.dumps(history_entry))
# # #     redis_client.ltrim(history_key, 0, 99)  # Keep last 100 entries

# # # def track_generation_metrics(user_id, language, code_length):
# # #     """Track code generation metrics"""
# # #     key = f"user:{user_id}:analytics"
# # #     redis_client.hincrby(key, f"generations_{language}", 1)
# # #     redis_client.hincrby(key, "total_generations", 1)
# # #     redis_client.hincrby(key, "total_code_generated", code_length)

# # # def get_user_history(user_id):
# # #     """Get user's analysis history"""
# # #     history_key = f"user:{user_id}:analysis_history"
# # #     history = redis_client.lrange(history_key, 0, 49)  # Last 50 entries
# # #     return [json.loads(entry) for entry in history]

# # # def calculate_user_metrics(user_id):
# # #     """Calculate comprehensive user metrics"""
# # #     key = f"user:{user_id}:analytics"
# # #     analytics = redis_client.hgetall(key)
    
# # #     return {
# # #         'total_analysis': int(analytics.get(b'total_analysis', 0)),
# # #         'total_generations': int(analytics.get(b'total_generations', 0)),
# # #         'total_code_generated': int(analytics.get(b'total_code_generated', 0)),
# # #         'languages_used': {
# # #             lang.decode().replace('total_analysis_', ''): int(count)
# # #             for lang, count in analytics.items()
# # #             if lang.startswith(b'total_analysis_')
# # #         }
# # #     }

# # # @app.route('/api/health', methods=['GET'])
# # # def health_check():
# # #     """Health check endpoint"""
# # #     return jsonify({
# # #         "status": "healthy",
# # #         "timestamp": datetime.utcnow().isoformat(),
# # #         "services": {
# # #             "redis": redis_client.ping(),
# # #             "llm": llm_service.is_available(),
# # #             "tts": tts_service.is_available()
# # #         },
# # #         "active_sessions": len(active_sessions)
# # #     })

# # # if __name__ == '__main__':
# # #     port = int(os.getenv('PORT', 5001))
# # #     socketio.run(app, host='0.0.0.0', port=port, debug=os.getenv('FLASK_DEBUG', 'False') == 'True')

# # import os
# # from datetime import datetime
# # from flask import Flask, request, jsonify
# # from flask_cors import CORS

# # app = Flask(__name__)
# # CORS(app)

# # @app.get("/api/health")
# # def health():
# #     return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

# # @app.post("/api/analyze")
# # def analyze():
# #     data = request.json
# #     code = data.get("code", "")
# #     language = data.get("language", "python")

# #     if not code:
# #         return {"error": "No code provided"}, 400

# #     lines = code.splitlines()
# #     line_count = len(lines)

# #     quality_score = 90 if line_count < 50 else 70
# #     grade = "A" if quality_score >= 90 else "B"

# #     roast = "🔥 Your code is clean!" if quality_score > 80 else "⚠️ Needs improvement."

# #     return {
# #         "success": True,
# #         "analysis": {
# #             "metrics": {
# #                 "line_count": line_count,
# #                 "character_count": len(code),
# #                 "quality_score": quality_score
# #             },
# #             "quality_score": quality_score,
# #             "grade": grade,
# #             "issues": []
# #         },
# #         "roast": {"text": roast, "intensity": "medium"},
# #         "timestamp": datetime.utcnow().isoformat()
# #     }

# # @app.post("/api/generate")
# # def generate():
# #     data = request.json
# #     prompt = data.get("prompt", "")

# #     if not prompt:
# #         return {"error": "Provide a prompt"}, 400

# #     generated = f"""
# # # Generated code for: {prompt}
# # def solution():
# #     pass
# # """

# #     return {"success": True, "code": generated}

# # if __name__ == "__main__":
# #     port = int(os.getenv("PORT", 5001))
# #     app.run(host="0.0.0.0", port=port)


# # backend/app.py - ENHANCED VERSION
# import os
# import json
# import ast
# import tempfile
# import base64
# from datetime import datetime
# from io import BytesIO
# import requests
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import autopep8
# from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel
# import random
# import re

# app = Flask(__name__)
# CORS(app)

# # Load environment variables
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# # Initialize AI models
# try:
#     tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
#     tokenizer.pad_token = tokenizer.eos_token
#     model = GPT2LMHeadModel.from_pretrained('distilgpt2')
#     roast_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
#     code_generator = pipeline('text-generation', model='distilgpt2', tokenizer='distilgpt2')
# except:
#     roast_generator = None
#     code_generator = None

# # Roast templates from previous project
# ROAST_TEMPLATES = {
#     "no_docstring": {
#         "mild": ["Bruh, no docstring? Did you forget what `{name}` does?",],
#         "medium": ["Look, I'm just an AI, but even I need an instruction manual.",],
#         "brutal": ["Bruh, you're not a hero for skipping the docs on `{name}`. You're just lazy.",]
#     },
#     "single_letter_var": {
#         "mild": ["A single letter variable, `{name}`? How original.",],
#         "medium": ["Bruh, '{name}'? You're not saving bytes, you're just making me sad.",],
#         "brutal": ["'{name}'? What a trash variable name.",]
#     },
#     # ... (include all roast templates from previous project)
# }

# CODE_EXAMPLES = {
#     "add two numbers": {
#         "code": "def add_numbers(a, b):\n    return a + b",
#         "roast": "A function for adding two numbers, bruh?"
#     },
#     # ... (include other examples)
# }

# def analyze_code(code, language="python"):
#     """Enhanced code analysis from previous project"""
#     issues = []
#     metrics = {}
    
#     if language == "python":
#         try:
#             tree = ast.parse(code)
#             for node in ast.walk(tree):
#                 if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
#                     if not ast.get_docstring(node):
#                         name = getattr(node, 'name', 'module')
#                         issues.append(f"No docstring for {node.__class__.__name__.lower()} '{name}'")
                
#                 if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
#                     if len(node.id) == 1:
#                         issues.append(f"Single-letter variable name '{node.id}'")
#                     elif node.id.lower() in ['foo', 'bar', 'baz', 'temp', 'data']:
#                         issues.append(f"Generic variable name '{node.id}'")
                
#                 if isinstance(node, ast.FunctionDef):
#                     body_lines = len(node.body)
#                     if body_lines > 20:
#                         issues.append(f"Overly long function '{node.name}'")
            
#             # Count nesting
#             def count_nesting(node, depth=0):
#                 if isinstance(node, (ast.For, ast.While, ast.If, ast.Try, ast.With)):
#                     depth += 1
#                     for child in ast.iter_child_nodes(node):
#                         depth = max(depth, count_nesting(child, depth))
#                 return depth
            
#             max_nesting = max(count_nesting(node) for node in ast.walk(tree))
#             if max_nesting > 3:
#                 issues.append(f"Excessive nesting with depth {max_nesting}")
                
#         except SyntaxError as e:
#             error_msg = str(e).split('\n')[0]
#             issues.append(f"Syntax error: {error_msg}")
    
#     # Basic metrics
#     lines = code.splitlines()
#     metrics = {
#         "line_count": len(lines),
#         "character_count": len(code),
#         "function_count": code.count('def ') + code.count('class '),
#         "complexity": code.count('if ') + code.count('for ') + code.count('while '),
#         "issue_count": len(issues)
#     }
    
#     # Quality score (0-100)
#     quality_score = 100
#     quality_score -= len(issues) * 5
#     quality_score -= metrics["complexity"] * 2
#     quality_score = max(0, min(100, quality_score))
    
#     # Grade
#     if quality_score >= 90:
#         grade = 'A'
#     elif quality_score >= 80:
#         grade = 'B'
#     elif quality_score >= 70:
#         grade = 'C'
#     elif quality_score >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
    
#     metrics["quality_score"] = quality_score
#     metrics["grade"] = grade
    
#     return issues, metrics

# def generate_roast(issues, roast_level="medium"):
#     """Generate roasts from templates"""
#     if not issues:
#         return ["Wow, your code is actually decent. I'm almost disappointed."]
    
#     roasts = []
    
#     # Add general roast
#     general_roasts = ROAST_TEMPLATES.get("general", {}).get(roast_level, [])
#     if general_roasts:
#         roasts.append(random.choice(general_roasts))
    
#     # Add specific roasts for issues
#     for issue in issues[:3]:
#         roast = None
        
#         if "No docstring" in issue:
#             templates = ROAST_TEMPLATES.get("no_docstring", {}).get(roast_level, [])
#         elif "Single-letter variable" in issue:
#             templates = ROAST_TEMPLATES.get("single_letter_var", {}).get(roast_level, [])
#         elif "Generic variable" in issue:
#             templates = ROAST_TEMPLATES.get("generic_var", {}).get(roast_level, [])
#         elif "Overly long function" in issue:
#             templates = ROAST_TEMPLATES.get("long_function", {}).get(roast_level, [])
#         elif "Excessive nesting" in issue:
#             templates = ROAST_TEMPLATES.get("excessive_nesting", {}).get(roast_level, [])
#         else:
#             templates = ROAST_TEMPLATES.get("pylint", {}).get(roast_level, [])
        
#         if templates:
#             roast = random.choice(templates)
#             # Extract names for formatting
#             if "{name}" in roast:
#                 if "No docstring" in issue:
#                     name = issue.split("'")[1] if "'" in issue else "this element"
#                 elif "Single-letter variable" in issue:
#                     name = issue.split("'")[1] if "'" in issue else "x"
#                 else:
#                     name = "your code"
#                 roast = roast.format(name=name)
#             roasts.append(roast)
    
#     return roasts[:5]  # Limit to 5 roasts

# def correct_code(code):
#     """Correct Python code"""
#     try:
#         # Try to parse first
#         ast.parse(code)
#         # Apply formatting
#         corrected = autopep8.fix_code(code, options={'aggressive': 1})
#         return corrected
#     except SyntaxError:
#         return code  # Return original if syntax error

# def generate_code_from_prompt(prompt):
#     """Generate code based on prompt"""
#     prompt_lower = prompt.lower()
    
#     # Check examples first
#     for key in CODE_EXAMPLES:
#         if key in prompt_lower:
#             return CODE_EXAMPLES[key]["code"], CODE_EXAMPLES[key]["roast"]
    
#     # Try AI generation
#     if code_generator:
#         try:
#             code_prompt = f"# Python code for: {prompt}\n"
#             generated = code_generator(
#                 code_prompt,
#                 max_new_tokens=200,
#                 temperature=0.3
#             )[0]['generated_text']
            
#             # Extract code after prompt
#             code = generated.replace(code_prompt, "").strip()
#             roast = "Here's some generated code. It might need some tweaking!"
#             return code, roast
#         except:
#             pass
    
#     # Fallback
#     fallback_code = f'''# Generated code for: {prompt}
# def solution():
#     """
#     TODO: Implement your solution here
#     """
#     # Your code goes here
#     result = None
#     return result

# if __name__ == "__main__":
#     solution()'''
    
#     return fallback_code, "Generated some basic code structure for you!"

# @app.route('/health', methods=['GET'])
# def health_check():
#     return jsonify({
#         "status": "healthy",
#         "timestamp": datetime.utcnow().isoformat(),
#         "features": ["analysis", "generation", "roasting", "correction"]
#     })

# @app.route('/api/analyze', methods=['POST'])
# def analyze_code_endpoint():
#     try:
#         data = request.json
#         code = data.get('code', '')
#         language = data.get('language', 'python')
#         roast_level = data.get('roast_level', 'medium')
        
#         if not code:
#             return jsonify({"error": "No code provided"}), 400
        
#         # Analyze code
#         issues, metrics = analyze_code(code, language)
        
#         # Generate roasts
#         roasts = generate_roast(issues, roast_level)
        
#         # Generate corrected code
#         corrected_code = correct_code(code) if language == 'python' else code
        
#         # Generate suggestions
#         suggestions = [
#             "Add comments to explain complex logic",
#             "Break long functions into smaller ones",
#             "Use meaningful variable names",
#             "Add error handling where appropriate"
#         ]
        
#         # Add issue-specific suggestions
#         if issues:
#             if any("No docstring" in issue for issue in issues):
#                 suggestions.append("Add docstrings to functions and classes")
#             if any("Single-letter" in issue for issue in issues):
#                 suggestions.append("Use descriptive variable names")
#             if any("Excessive nesting" in issue for issue in issues):
#                 suggestions.append("Reduce nesting depth by extracting helper functions")
        
#         return jsonify({
#             "success": True,
#             "analysis": {
#                 "issues": issues,
#                 "metrics": metrics,
#                 "quality_score": metrics.get("quality_score", 0),
#                 "grade": metrics.get("grade", "N/A")
#             },
#             "roast": {
#                 "text": " ".join(roasts),
#                 "individual_roasts": roasts,
#                 "intensity": roast_level
#             },
#             "suggestions": suggestions[:5],
#             "corrected_code": corrected_code,
#             "timestamp": datetime.utcnow().isoformat()
#         })
        
#     except Exception as e:
#         return jsonify({
#             "error": "Internal server error",
#             "message": str(e)
#         }), 500

# @app.route('/api/generate', methods=['POST'])
# def generate_code_endpoint():
#     try:
#         data = request.json
#         prompt = data.get('prompt', '')
#         language = data.get('language', 'python')
        
#         if not prompt:
#             return jsonify({"error": "No prompt provided"}), 400
        
#         code, roast = generate_code_from_prompt(prompt)
        
#         return jsonify({
#             "success": True,
#             "code": code,
#             "roast": roast,
#             "language": language,
#             "timestamp": datetime.utcnow().isoformat()
#         })
        
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/api/languages', methods=['GET'])
# def get_languages():
#     return jsonify({
#         "languages": [
#             {"id": "python", "name": "Python", "ext": ".py"},
#             {"id": "javascript", "name": "JavaScript", "ext": ".js"},
#             {"id": "java", "name": "Java", "ext": ".java"},
#             {"id": "cpp", "name": "C++", "ext": ".cpp"},
#             {"id": "typescript", "name": "TypeScript", "ext": ".ts"}
#         ]
#     })

# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 5001))
#     app.run(host="0.0.0.0", port=port, debug=os.getenv("FLASK_DEBUG", "False") == "True")

# backend/app.py - LIGHTWEIGHT VERSION
import os
import json
import ast
import random
import re
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import autopep8
import requests

app = Flask(__name__)
CORS(app)

# Simple roast templates (no heavy AI models)
ROAST_TEMPLATES = {
    "no_docstring": {
        "mild": [
            "No docstring found. Documentation helps others understand your code!",
            "Consider adding a docstring to explain what this does.",
            "Missing documentation - future you will thank you for adding some!"
        ],
        "medium": [
            "Bruh, no docstring? Did you forget what this does?",
            "This code is undocumented - it's like a mystery box!",
            "Where are the docs? Even my calculator has a manual!"
        ],
        "brutal": [
            "Zero documentation? That's brave... or just lazy!",
            "This code is more undocumented than a secret government project!",
            "No docs? Good luck to whoever has to maintain this!"
        ]
    },
    "single_letter_var": {
        "mild": [
            "Consider using more descriptive variable names.",
            "Single-letter variables can be hard to understand.",
            "Try naming variables based on their purpose."
        ],
        "medium": [
            "Single-letter variables? How original!",
            "Bruh, you're not saving bytes with 'x' and 'y'!",
            "I've seen more creative names on a license plate!"
        ],
        "brutal": [
            "Single-letter variables? Did your keyboard break?",
            "This variable naming is what happens when creativity dies!",
            "I'd rather read binary than try to understand 'a', 'b', 'c'!"
        ]
    },
    "long_function": {
        "mild": [
            "This function is getting long. Consider breaking it up.",
            "Long functions can be hard to maintain and test.",
            "Try to keep functions focused on a single responsibility."
        ],
        "medium": [
            "This function is longer than my last relationship!",
            "Bruh, this function needs its own zip code!",
            "Is this a function or a novel?"
        ],
        "brutal": [
            "This function is so long, I need a snack break to read it!",
            "I've seen shorter Russian novels than this function!",
            "This function needs an intermission!"
        ]
    },
    "syntax_error": {
        "mild": [
            "There's a syntax error in your code. Check the highlighted line.",
            "Python can't understand this syntax. Let's fix it!",
            "Syntax error detected - every programmer's favorite!"
        ],
        "medium": [
            "Oops! Syntax error! Did you type this with your eyes closed?",
            "Python says 'no' to this syntax!",
            "This code has more errors than my first dating profile!"
        ],
        "brutal": [
            "Syntax error! My cat could write better Python!",
            "This isn't code, it's modern art! Unparseable art!",
            "Even autocorrect wouldn't know what to do with this!"
        ]
    },
    "general_good": {
        "mild": ["Nice code! Keep up the good work!", "Clean and readable - well done!", "Good job on this code!"],
        "medium": ["Not bad! Could use some polish, but good effort!", "Decent code! Room for improvement though.", "You're on the right track!"],
        "brutal": ["It works... that's something, right?", "This code exists. That's an accomplishment!", "Hey, at least it's not PHP!"]
    }
}

# Code examples for generation
CODE_EXAMPLES = {
    "add": '''def add_numbers(a, b):
    """Add two numbers together."""
    return a + b

result = add_numbers(5, 3)
print(f"Sum: {result}")''',
    
    "factorial": '''def factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120''',
    
    "fibonacci": '''def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

print(fibonacci(10))''',
    
    "palindrome": '''def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False''',
    
    "calculator": '''def calculator(a, b, operation):
    """Basic calculator with four operations."""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Unsupported operation")

# Example usage
print(calculator(10, 5, 'add'))'''
}

def analyze_python_code(code):
    """Lightweight Python code analysis"""
    issues = []
    suggestions = []
    
    try:
        # Try to parse the code
        tree = ast.parse(code)
        
        # Check for issues
        for node in ast.walk(tree):
            # Check for missing docstrings
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                if not ast.get_docstring(node):
                    name = getattr(node, 'name', 'module')
                    issues.append(f"No docstring for {node.__class__.__name__.lower()} '{name}'")
                    suggestions.append(f"Add a docstring to {name} explaining its purpose")
            
            # Check for single-letter variables
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if len(node.id) == 1 and node.id.isalpha():
                    issues.append(f"Single-letter variable name '{node.id}'")
                    suggestions.append(f"Rename '{node.id}' to something more descriptive")
            
            # Check for generic variable names
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if node.id.lower() in ['data', 'temp', 'var', 'value', 'stuff', 'things']:
                    issues.append(f"Generic variable name '{node.id}'")
                    suggestions.append(f"Use a more specific name than '{node.id}'")
            
            # Check for long functions
            if isinstance(node, ast.FunctionDef):
                body_lines = len(node.body)
                if body_lines > 20:
                    issues.append(f"Overly long function '{node.name}' ({body_lines} lines)")
                    suggestions.append(f"Break '{node.name}' into smaller functions")
        
        # Check line length
        lines = code.splitlines()
        for i, line in enumerate(lines, 1):
            if len(line) > 79:  # PEP 8 recommends 79 chars
                issues.append(f"Line {i} too long ({len(line)} characters)")
                suggestions.append("Keep lines under 79 characters for readability")
        
        # Check for TODO/FIXME comments
        if 'TODO' in code or 'FIXME' in code:
            issues.append("TODO/FIXME comments found")
            suggestions.append("Address TODO/FIXME comments before finalizing code")
        
        # Count functions and classes
        function_count = code.count('def ')
        class_count = code.count('class ')
        
        # Calculate metrics
        line_count = len(lines)
        char_count = len(code)
        
        # Calculate quality score (simplified)
        quality_score = 100
        quality_score -= len(issues) * 5
        quality_score -= (function_count * 2) if function_count > 5 else 0
        quality_score = max(0, min(100, quality_score))
        
        # Determine grade
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
        
        metrics = {
            "line_count": line_count,
            "character_count": char_count,
            "function_count": function_count,
            "class_count": class_count,
            "quality_score": quality_score,
            "grade": grade,
            "issue_count": len(issues)
        }
        
    except SyntaxError as e:
        # Handle syntax errors
        error_msg = str(e).split('\n')[0]
        issues = [f"Syntax error: {error_msg}"]
        suggestions = ["Fix the syntax error to proceed with analysis"]
        metrics = {
            "line_count": len(code.splitlines()),
            "character_count": len(code),
            "function_count": 0,
            "class_count": 0,
            "quality_score": 40,
            "grade": 'F',
            "issue_count": 1
        }
    except Exception as e:
        # Handle other errors
        issues = [f"Analysis error: {str(e)}"]
        suggestions = ["Try with simpler code or check for syntax errors"]
        metrics = {
            "line_count": len(code.splitlines()),
            "character_count": len(code),
            "function_count": 0,
            "class_count": 0,
            "quality_score": 50,
            "grade": 'F',
            "issue_count": 1
        }
    
    return issues, suggestions, metrics

def generate_roast(issues, intensity="medium"):
    """Generate roast based on issues"""
    if not issues:
        category = "general_good"
    elif any("Syntax error" in issue for issue in issues):
        category = "syntax_error"
    elif any("No docstring" in issue for issue in issues):
        category = "no_docstring"
    elif any("Single-letter" in issue for issue in issues):
        category = "single_letter_var"
    elif any("Overly long" in issue for issue in issues):
        category = "long_function"
    else:
        category = "general_good"
    
    templates = ROAST_TEMPLATES.get(category, {}).get(intensity, [])
    if templates:
        return random.choice(templates)
    else:
        return "Let's take a look at your code..."

def correct_code(code):
    """Simple code correction using autopep8"""
    try:
        corrected = autopep8.fix_code(code)
        return corrected
    except:
        return code

def generate_code_from_prompt(prompt):
    """Generate code based on prompt keywords"""
    prompt_lower = prompt.lower()
    
    # Check for keywords
    if any(word in prompt_lower for word in ['add', 'sum', 'plus', 'addition']):
        return CODE_EXAMPLES["add"], "Here's a simple addition function!"
    elif any(word in prompt_lower for word in ['factorial', '!', 'fact']):
        return CODE_EXAMPLES["factorial"], "Factorial calculation coming right up!"
    elif any(word in prompt_lower for word in ['fibonacci', 'fib']):
        return CODE_EXAMPLES["fibonacci"], "Fibonacci sequence - a classic!"
    elif any(word in prompt_lower for word in ['palindrome', 'reverse', 'mirror']):
        return CODE_EXAMPLES["palindrome"], "Palindrome checker - reads the same forwards and backwards!"
    elif any(word in prompt_lower for word in ['calculator', 'calculate', 'math']):
        return CODE_EXAMPLES["calculator"], "A basic calculator for you!"
    elif any(word in prompt_lower for word in ['hello', 'world', 'print']):
        return '''print("Hello, World!")''', "The classic Hello World!"
    else:
        # Generate simple function based on prompt
        func_name = prompt_lower.split()[0] if prompt_lower.split() else "solution"
        return f'''def {func_name}():
    """{prompt}"""
    # Your implementation here
    pass

if __name__ == "__main__":
    {func_name}()''', f"Generated a function skeleton for '{prompt}'"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "roast-code-ai",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    })

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        code = data.get('code', '').strip()
        language = data.get('language', 'python')
        roast_level = data.get('roast_level', 'medium')
        
        if not code:
            return jsonify({"error": "No code provided"}), 400
        
        # Currently only support Python
        if language != 'python':
            return jsonify({
                "error": f"Language '{language}' not fully supported yet",
                "suggestion": "Try with Python code"
            }), 400
        
        # Analyze code
        issues, suggestions, metrics = analyze_python_code(code)
        
        # Generate roast
        roast_text = generate_roast(issues, roast_level)
        
        # Generate corrected code
        corrected_code = correct_code(code)
        
        # Generate audio roast text (for TTS)
        audio_roast = f"Code analysis complete. {roast_text} Found {len(issues)} issues."
        
        return jsonify({
            "success": True,
            "analysis": {
                "issues": issues,
                "suggestions": suggestions,
                "metrics": metrics,
                "quality_score": metrics.get("quality_score", 0),
                "grade": metrics.get("grade", "N/A")
            },
            "roast": {
                "text": roast_text,
                "intensity": roast_level,
                "audio_text": audio_roast
            },
            "corrected_code": corrected_code,
            "language": language,
            "timestamp": datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt', '').strip()
        language = data.get('language', 'python')
        
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400
        
        if language != 'python':
            return jsonify({
                "error": f"Language '{language}' not fully supported yet",
                "suggestion": "Try with Python generation"
            }), 400
        
        # Generate code
        code, roast = generate_code_from_prompt(prompt)
        
        # Generate audio roast
        audio_roast = f"Code generated! {roast}"
        
        return jsonify({
            "success": True,
            "code": code,
            "roast": roast,
            "audio_roast": audio_roast,
            "language": language,
            "timestamp": datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/audio', methods=['POST'])
def text_to_speech():
    """Simple text-to-speech endpoint using browser's TTS"""
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        return jsonify({
            "success": True,
            "text": text,
            "message": "Use browser's SpeechSynthesis API for TTS",
            "instruction": "Use: speechSynthesis.speak(new SpeechSynthesisUtterance('text'))"
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/languages', methods=['GET'])
def get_languages():
    return jsonify({
        "languages": [
            {"id": "python", "name": "Python", "supported": True},
            {"id": "javascript", "name": "JavaScript", "supported": False},
            {"id": "java", "name": "Java", "supported": False},
            {"id": "cpp", "name": "C++", "supported": False}
        ]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)