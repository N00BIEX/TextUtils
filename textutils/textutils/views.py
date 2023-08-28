from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    params ={"title":"HOME"}
    return render(request,"home.html",params)
    
def about(request):
    sm_dis = "read the below documentation to know about us"
    quote_t = "mai nii banaya hu...ye jabardasti ka likhwa rha hai "
    params ={"title":"About Us", "small_dis":sm_dis,"text_cont":"","quote":quote_t,"writer":"satish"}
    return render(request,"us.html",params)
        
def analyse(request):
    
    sentence = request.POST.get('text','default')
    rempunc = request.POST.get('removepunc','off')
    cap = request.POST.get('capf','off')
    extraspace = request.POST.get('extraspacerem','off')
    newline = request.POST.get('remnewline','off')
    
    punctuations = '''@#$_&-+()/*"':;!?.,~`|•√π÷×§∆£¢€¥^°={}\%©®™✓[]><'''
    if rempunc == "on":
        
        analyse_punc = ""
        
        for char in sentence:
            if char not in punctuations:
                analyse_punc += char
        
        params ={ "text":analyse_punc}
        sentence = analyse_punc
        #return render(request,"analyse_temp.html",params)
        
    if cap == "on":
        
        analyse_cap = ""
        
        for char in sentence:
                analyse_cap += char.upper()
        
        params ={ "text":analyse_cap}
        sentence = analyse_cap
        #return render(request,"analyse_temp.html",params)
        
        
    if extraspace == "on":
        
        analyse_space = ""
        
        for index , char in enumerate(sentence):
            if not ( sentence[index] == " " and sentence[index+1] == " "):
                
                analyse_space += char
        
        params ={ "text":analyse_space}
        sentence = analyse_space
        #return render(request,"analyse_temp.html",params)
    
    if newline == "on":
        
        analyse_line = ""
        
        for char in sentence:
            if  char != "\n" and char != "\r":
                analyse_line += char
        
        params ={ "text":analyse_line}
        sentence = analyse_line
        #return render(request,"analyse_temp.html",params)
        
    if (newline != "on" and extraspace != "on" and cap != "on" and rempunc != "on"):
        return_default_text = {"title":"HOME","onload":"No option selected" }
        return render(request,"home.html",return_default_text)
    return render(request,"analyse_temp.html",params)