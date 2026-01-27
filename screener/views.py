from django.shortcuts import render
import PyPDF2

# 1. PDF se text nikalne ka function
def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# 2. Skills check karne ka logic
SKILLS = ['python', 'django', 'ml', 'sql', 'react', 'java', 'html', 'css', 'algorithm','english']

def extract_skills(text):
    found = []
    text = text.lower()
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found

# 3. Score calculate karne ka function
def resume_score(skills):
    return len(skills) * 10




def upload_resume(request):
    context = {} # Khali dabba banaya data ke liye
    
    if request.method == 'POST':
        resume_file = request.FILES.get('resume')
        
        if resume_file:
            # 1. Text nikalo
            raw_text = extract_text(resume_file)
            
            # 2. Skills dhundo (Aapne function pehle likha hua hai)
            skills_found = extract_skills(raw_text)
            
            # 3. Score nikalo
            score = resume_score(skills_found)
            
            # --- ZAROORI HISSA ---
            # Ye variables ke naam (skills, score, msg) wahi hone chahiye 
            # jo aapne HTML mein {{ }} ke andar likhe hain.
            context = {
                'skills': skills_found, 
                'score': score,
                'msg': 'Resume Processed Successfully!'
            }
            return render(request, 'upload.html', context)
    
    return render(request, 'upload.html', context)
# 4. Main View jo browser mein page dikhayega
# def upload_resume(request):
#     context = {}
#     if request.method == 'POST':
#         resume_file = request.FILES.get('resume') # HTML name="resume" se match karna chahiye
        
#         if resume_file:
#             # Step A: Text nikalo
#             raw_text = extract_text(resume_file)
#             # Step B: Skills dhundo
#             skills_found = extract_skills(raw_text)
#             # Step C: Score nikalo
#             score = resume_score(skills_found)
            
#             # Data ko template mein bhejne ke liye taiyar karein
#             context = {
#                 'skills': skills_found,
#                 'score': score,
#                 'msg': 'Resume Processed Successfully!'
#             }
#             return render(request, 'upload.html', context)
    
#     return render(request, 'upload.html', context)
