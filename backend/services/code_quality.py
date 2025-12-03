# import ast
# import subprocess
# import tempfile
# import os
# from typing import Dict, List, Any
# import lizard
# import radon
# from radon.complexity import cc_visit
# from radon.metrics import mi_visit
# from radon.raw import analyze
# import javalang
# import esprima
# import clang.cindex

# class CodeQualityAnalyzer:
#     """Comprehensive code quality analyzer for multiple languages"""
    
#     def __init__(self):
#         self.supported_languages = {
#             'python': self.analyze_python,
#             'javascript': self.analyze_javascript,
#             'java': self.analyze_java,
#             'cpp': self.analyze_cpp,
#             'typescript': self.analyze_typescript,
#             'go': self.analyze_go,
#             'rust': self.analyze_rust,
#             'ruby': self.analyze_ruby
#         }
    
#     def analyze_code(self, code: str, language: str) -> Dict[str, Any]:
#         """Analyze code based on language"""
#         if language in self.supported_languages:
#             return self.supported_languages[language](code)
#         else:
#             return self.analyze_generic(code, language)
    
#     def analyze_python(self, code: str) -> Dict[str, Any]:
#         """Comprehensive Python code analysis"""
#         issues = []
#         metrics = {}
        
#         try:
#             # Parse AST
#             tree = ast.parse(code)
            
#             # Basic metrics
#             lines = code.splitlines()
#             metrics['line_count'] = len(lines)
#             metrics['character_count'] = len(code)
            
#             # Complexity analysis
#             complexity_results = cc_visit(code)
#             metrics['cyclomatic_complexity'] = max([func.complexity for func in complexity_results] + [0])
#             metrics['function_count'] = len(complexity_results)
            
#             # Maintainability index
#             mi_score = mi_visit(code, multi=True)
#             metrics['maintainability_index'] = mi_score
            
#             # Raw metrics
#             raw_metrics = analyze(code)
#             metrics['comment_lines'] = raw_metrics.comments
#             metrics['blank_lines'] = raw_metrics.blank
#             metrics['code_lines'] = raw_metrics.loc
            
#             # Check for issues
#             self._check_python_issues(tree, issues)
            
#             # Run pylint for additional checks
#             pylint_issues = self._run_pylint(code)
#             issues.extend(pylint_issues)
            
#             # Security analysis
#             security_issues = self._check_security(code)
#             issues.extend(security_issues)
            
#             # Performance analysis
#             performance_issues = self._check_performance(code)
#             issues.extend(performance_issues)
            
#         except SyntaxError as e:
#             issues.append(f"Syntax error: {str(e)}")
#         except Exception as e:
#             issues.append(f"Analysis error: {str(e)}")
        
#         return {
#             'issues': issues,
#             'metrics': metrics,
#             'grade': self._calculate_grade(metrics, len(issues))
#         }
    
#     def analyze_javascript(self, code: str) -> Dict[str, Any]:
#         """JavaScript code analysis"""
#         issues = []
#         metrics = {}
        
#         try:
#             # Parse with esprima
#             tree = esprima.parseScript(code, loc=True)
            
#             # Basic metrics
#             lines = code.splitlines()
#             metrics['line_count'] = len(lines)
#             metrics['character_count'] = len(code)
            
#             # Analyze structure
#             issues.extend(self._analyze_javascript_structure(tree))
            
#             # Run ESLint if available
#             eslint_issues = self._run_eslint(code)
#             issues.extend(eslint_issues)
            
#         except Exception as e:
#             issues.append(f"JavaScript parsing error: {str(e)}")
        
#         return {
#             'issues': issues,
#             'metrics': metrics,
#             'grade': self._calculate_grade(metrics, len(issues))
#         }
    
#     def analyze_java(self, code: str) -> Dict[str, Any]:
#         """Java code analysis"""
#         issues = []
#         metrics = {}
        
#         try:
#             # Parse with javalang
#             tree = javalang.parse.parse(code)
            
#             # Basic metrics
#             lines = code.splitlines()
#             metrics['line_count'] = len(lines)
#             metrics['character_count'] = len(code)
            
#             # Analyze structure
#             issues.extend(self._analyze_java_structure(tree))
            
#         except Exception as e:
#             issues.append(f"Java parsing error: {str(e)}")
        
#         return {
#             'issues': issues,
#             'metrics': metrics,
#             'grade': self._calculate_grade(metrics, len(issues))
#         }
    
#     def analyze_cpp(self, code: str) -> Dict[str, Any]:
#         """C++ code analysis"""
#         issues = []
#         metrics = {}
        
#         try:
#             # Use lizard for C++ analysis
#             analysis = lizard.analyze_file.analyze_source_code("temp.cpp", code)
            
#             metrics['line_count'] = analysis.nloc
#             metrics['function_count'] = len(analysis.function_list)
#             metrics['cyclomatic_complexity'] = max([f.cyclomatic_complexity for f in analysis.function_list] + [0])
            
#         except Exception as e:
#             issues.append(f"C++ analysis error: {str(e)}")
        
#         return {
#             'issues': issues,
#             'metrics': metrics,
#             'grade': self._calculate_grade(metrics, len(issues))
#         }
    
#     def analyze_generic(self, code: str, language: str) -> Dict[str, Any]:
#         """Generic code analysis for unsupported languages"""
#         lines = code.splitlines()
        
#         metrics = {
#             'line_count': len(lines),
#             'character_count': len(code),
#             'function_count': 0,
#             'cyclomatic_complexity': 0,
#             'maintainability_index': 0
#         }
        
#         issues = [f"Limited analysis for {language} language"]
        
#         return {
#             'issues': issues,
#             'metrics': metrics,
#             'grade': 'N/A'
#         }
    
#     def calculate_comprehensive_metrics(self, code: str, analysis: Dict, language: str) -> Dict[str, Any]:
#         """Calculate comprehensive code quality metrics"""
#         metrics = analysis['metrics'].copy()
        
#         # Calculate additional metrics
#         metrics['issue_density'] = len(analysis['issues']) / max(metrics['line_count'], 1)
        
#         # Calculate quality score (0-100)
#         quality_score = 100
#         quality_score -= len(analysis['issues']) * 2  # Deduct for issues
#         quality_score -= min(metrics['cyclomatic_complexity'] * 5, 30)  # Deduct for complexity
        
#         if metrics['maintainability_index'] > 0:
#             quality_score += min(metrics['maintainability_index'] / 2, 30)
        
#         metrics['quality_score'] = max(0, min(100, quality_score))
        
#         # Determine grade
#         if metrics['quality_score'] >= 90:
#             metrics['grade'] = 'A'
#         elif metrics['quality_score'] >= 80:
#             metrics['grade'] = 'B'
#         elif metrics['quality_score'] >= 70:
#             metrics['grade'] = 'C'
#         elif metrics['quality_score'] >= 60:
#             metrics['grade'] = 'D'
#         else:
#             metrics['grade'] = 'F'
        
#         return metrics
    
#     def _check_python_issues(self, tree: ast.AST, issues: List[str]):
#         """Check Python AST for issues"""
#         for node in ast.walk(tree):
#             # Check for missing docstrings
#             if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
#                 if not ast.get_docstring(node):
#                     issues.append(f"No docstring for {node.__class__.__name__.lower()} '{getattr(node, 'name', 'module')}'")
            
#             # Check for single-letter variables
#             if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
#                 if len(node.id) == 1 and node.id.isalpha():
#                     issues.append(f"Single-letter variable name '{node.id}'")
            
#             # Check for overly long functions
#             if isinstance(node, ast.FunctionDef):
#                 body_lines = len(node.body)
#                 if body_lines > 50:
#                     issues.append(f"Overly long function '{node.name}' ({body_lines} lines)")
    
#     def _run_pylint(self, code: str) -> List[str]:
#         """Run pylint analysis"""
#         issues = []
#         try:
#             with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
#                 f.write(code)
#                 temp_file = f.name
            
#             result = subprocess.run(
#                 ['pylint', '--disable=all', '--enable=C,R,W', temp_file],
#                 capture_output=True,
#                 text=True
#             )
            
#             for line in result.stdout.splitlines():
#                 if ':' in line:
#                     parts = line.split(':')
#                     if len(parts) >= 4:
#                         issue = parts[3].strip()
#                         if issue:
#                             issues.append(issue)
            
#             os.unlink(temp_file)
#         except:
#             pass
        
#         return issues[:10]  # Limit to 10 issues
    
#     def _run_eslint(self, code: str) -> List[str]:
#         """Run ESLint for JavaScript"""
#         issues = []
#         try:
#             with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
#                 f.write(code)
#                 temp_file = f.name
            
#             result = subprocess.run(
#                 ['npx', 'eslint', '--format=compact', temp_file],
#                 capture_output=True,
#                 text=True
#             )
            
#             for line in result.stdout.splitlines():
#                 if 'error' in line.lower() or 'warning' in line.lower():
#                     issues.append(line.strip())
            
#             os.unlink(temp_file)
#         except:
#             pass
        
#         return issues
    
#     def _check_security(self, code: str) -> List[str]:
#         """Check for security issues"""
#         issues = []
        
#         # Python security checks
#         dangerous_patterns = [
#             ('eval(', 'Use of eval() is dangerous'),
#             ('exec(', 'Use of exec() is dangerous'),
#             ('pickle.loads', 'Unpickling untrusted data is dangerous'),
#             ('subprocess.call', 'Shell injection possible'),
#             ('os.system', 'Shell injection possible'),
#             ('input()', 'raw_input() in Python 2'),
#         ]
        
#         for pattern, message in dangerous_patterns:
#             if pattern in code:
#                 issues.append(f"Security: {message}")
        
#         return issues
    
#     def _check_performance(self, code: str) -> List[str]:
#         """Check for performance issues"""
#         issues = []
        
#         # Performance anti-patterns
#         performance_patterns = [
#             ('for key in dict.keys():', 'Use "for key in dict:" instead'),
#             ('list.append() in loop', 'Consider list comprehension'),
#             ('string += in loop', 'Use str.join() instead'),
#         ]
        
#         for pattern, message in performance_patterns:
#             if pattern in code:
#                 issues.append(f"Performance: {message}")
        
#         return issues
    
#     def _analyze_javascript_structure(self, tree) -> List[str]:
#         """Analyze JavaScript structure"""
#         issues = []
        
#         # TODO: Implement detailed JS structure analysis
#         # This would involve traversing the esprima AST
        
#         return issues
    
#     def _analyze_java_structure(self, tree) -> List[str]:
#         """Analyze Java structure"""
#         issues = []
        
#         # TODO: Implement detailed Java structure analysis
#         # This would involve traversing the javalang AST
        
#         return issues
    
#     def _calculate_grade(self, metrics: Dict, issue_count: int) -> str:
#         """Calculate code quality grade"""
#         if not metrics:
#             return 'N/A'
        
#         score = 100
        
#         # Deduct for issues
#         score -= min(issue_count * 5, 50)
        
#         # Deduct for high complexity
#         if 'cyclomatic_complexity' in metrics:
#             complexity = metrics['cyclomatic_complexity']
#             if complexity > 20:
#                 score -= 30
#             elif complexity > 10:
#                 score -= 20
#             elif complexity > 5:
#                 score -= 10
        
#         # Add for maintainability
#         if 'maintainability_index' in metrics:
#             mi = metrics['maintainability_index']
#             if mi > 80:
#                 score += 20
#             elif mi > 60:
#                 score += 10
        
#         if score >= 90:
#             return 'A'
#         elif score >= 80:
#             return 'B'
#         elif score >= 70:
#             return 'C'
#         elif score >= 60:
#             return 'D'
#         else:
#             return 'F'

# backend/services/code_quality.py - SIMPLIFIED FOR DEPLOYMENT
import re
from typing import Dict, List, Any
import ast

class CodeQualityAnalyzer:
    """Lightweight code quality analyzer for deployment"""
    
    def __init__(self):
        self.supported_languages = ['python', 'javascript', 'java']
        
    def analyze_code(self, code: str, language: str = 'python') -> Dict[str, Any]:
        """Universal analysis function"""
        if language == 'python':
            return self.analyze_python(code)
        else:
            return self.analyze_generic(code, language)
    
    def analyze_python(self, code: str) -> Dict[str, Any]:
        """Simple Python analysis without radon"""
        issues = []
        metrics = {}
        
        try:
            # Basic metrics
            lines = code.splitlines()
            metrics['line_count'] = len(lines)
            metrics['character_count'] = len(code)
            
            # Check for syntax errors
            try:
                ast.parse(code)
            except SyntaxError as e:
                issues.append(f"Syntax error: {str(e)}")
            
            # Simple complexity analysis
            complexity_score = self._calculate_simple_complexity(code)
            metrics['cyclomatic_complexity'] = complexity_score
            
            # Count functions/classes
            functions = self._count_functions(code)
            metrics['function_count'] = functions
            
            # Find issues
            issues.extend(self._check_python_smells(code))
            
        except Exception as e:
            issues.append(f"Analysis error: {str(e)}")
        
        # Calculate quality score
        quality_score = self._calculate_quality_score(metrics, issues)
        
        return {
            'issues': issues,
            'metrics': metrics,
            'quality_score': quality_score,
            'grade': self._score_to_grade(quality_score)
        }
    
    def analyze_generic(self, code: str, language: str) -> Dict[str, Any]:
        """Generic analysis for other languages"""
        lines = code.splitlines()
        metrics = {
            'line_count': len(lines),
            'character_count': len(code),
            'function_count': 0,
            'cyclomatic_complexity': 0
        }
        
        issues = self._check_generic_issues(code, language)
        quality_score = 80  # Default score
        
        return {
            'issues': issues,
            'metrics': metrics,
            'quality_score': quality_score,
            'grade': self._score_to_grade(quality_score)
        }
    
    def _calculate_simple_complexity(self, code: str) -> int:
        """Simple complexity calculation"""
        complexity = 0
        complexity += code.count('if ')
        complexity += code.count('for ')
        complexity += code.count('while ')
        complexity += code.count('def ')
        complexity += code.count('class ')
        complexity += code.count('try:')
        complexity += code.count('except')
        complexity += code.count(' and ')
        complexity += code.count(' or ')
        return max(1, complexity)
    
    def _count_functions(self, code: str) -> int:
        """Count function definitions"""
        count = 0
        count += code.count('def ')
        count += code.count('lambda ')
        return count
    
    def _check_python_smells(self, code: str) -> List[str]:
        """Check for common Python code smells"""
        issues = []
        
        # Long lines
        lines = code.splitlines()
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                issues.append(f"Line {i}: Line too long ({len(line)} chars)")
        
        # Too many nested blocks
        if code.count('    ') > 20:
            issues.append("Too much nesting (more than 20 levels)")
        
        # Magic numbers
        magic_numbers = re.findall(r'\b[0-9]{3,}\b', code)
        if magic_numbers:
            issues.append(f"Magic numbers found: {', '.join(set(magic_numbers[:3]))}")
        
        # Missing docstrings
        if 'def ' in code and '"""' not in code and "'''" not in code:
            issues.append("Consider adding docstrings to functions")
        
        # Hardcoded credentials
        dangerous_patterns = [
            (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password'),
            (r'api_key\s*=\s*["\'][^"\']+["\']', 'Hardcoded API key'),
            (r'secret\s*=\s*["\'][^"\']+["\']', 'Hardcoded secret'),
        ]
        
        for pattern, message in dangerous_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                issues.append(f"Security: {message}")
        
        return issues[:10]  # Limit issues
    
    def _check_generic_issues(self, code: str, language: str) -> List[str]:
        """Check for generic issues"""
        issues = []
        
        # Long lines
        lines = code.splitlines()
        for i, line in enumerate(lines, 1):
            if len(line) > 120:
                issues.append(f"Line {i}: Line too long ({len(line)} chars)")
        
        # Comment ratio
        comment_keywords = ['//', '#', '/*', '*', '<!--']
        code_lines = len([l for l in lines if l.strip()])
        comment_lines = len([l for l in lines if any(k in l for k in comment_keywords)])
        
        if code_lines > 0 and comment_lines / code_lines < 0.1:
            issues.append("Low comment density (less than 10%)")
        
        # Language-specific advice
        language_advice = {
            'javascript': ['Use const/let instead of var', 'Add semicolons', 'Check for console.log in production'],
            'java': ['Add @Override annotations', 'Use try-with-resources', 'Check for null safety'],
            'cpp': ['Check memory management', 'Use smart pointers', 'Avoid raw pointers'],
        }
        
        if language in language_advice:
            issues.extend(language_advice[language][:2])
        
        return issues
    
    def _calculate_quality_score(self, metrics: Dict, issues: List[str]) -> int:
        """Calculate quality score (0-100)"""
        score = 100
        
        # Deduct for issues
        score -= min(len(issues) * 5, 50)
        
        # Deduct for high complexity
        complexity = metrics.get('cyclomatic_complexity', 0)
        if complexity > 15:
            score -= 30
        elif complexity > 10:
            score -= 20
        elif complexity > 5:
            score -= 10
        
        # Deduct for long code
        line_count = metrics.get('line_count', 0)
        if line_count > 200:
            score -= 10
        elif line_count > 100:
            score -= 5
        
        # Ensure score is between 0-100
        return max(0, min(100, score))
    
    def _score_to_grade(self, score: int) -> str:
        """Convert score to letter grade"""
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

# Create analyzer instance
analyzer = CodeQualityAnalyzer()