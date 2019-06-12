import re
message = 'Call me at 422-343-1123 tomorrow, or at 349-434-2233 at my office'
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.findall(message)
print(mo)
