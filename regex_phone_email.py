text = 'Lorem ipsum dolor sit amet, consectet 777-777-8888 ur adipiscing elit. Profectus in exilium Tubulus statim nec respondere ausus; Quid igitur, inquit, eos responsuros putas? Atqui reperies, inquit, in hoc (800)800-8000 quidem pertinacem; Non modo carum sibi weiss.steven@gmail.com quemque, verum etiam vehementer carum esse? zoe@zoe.net Teneo, inquit, finem illi videri nihil dolere. Duo enim genera quae erant, fecit tria.'

phoneNumRegex = re.compile(r'''(
    (\d\d\d | \(\d\d\d \))?
    (\s|-|\.)?
    (\d\d\d)
    (\s|-|\.)?
    (\d\d\d\d)
    (\s*(ext|x|ext.)\s*(|d{2, 5}))?
    )''', re.VERBOSE)
    
email_pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"   

pattern = re.compile(email_pattern, re.VERBOSE)

matches = []
for groups in phoneNumRegex.findall(text):
    phoneNum = '-'.join( [groups[1], groups[3], groups[5]] )
    if groups[8] != '':
        phoneNum ++ ' x' + groups[8]
    matches.append(phoneNum)
    
for groups in pattern.findall(text):
    matches.append(groups)
print(matches)


