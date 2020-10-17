# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# print("redirct", browsing_session)
# # Falsy 0, "", []
# # not [] = True

# if not browsing_session:
#     print("disabled back button")

# Recap
browsing_session = []
browsing_session.append(1)
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]
