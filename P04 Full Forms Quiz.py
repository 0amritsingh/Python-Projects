abbreviations = ["NASA", "WHO", "FBI", "UNICEF", "NATO", "LASER", "RADAR", "SCUBA", "JPEG", "GPS"]

full_forms = ["National Aeronautics And Space Administration", "World Health Organization", "Federal Bureau Of Investigation", "United Nations International Children's Emergency Fund", "North Atlantic Treaty Organization", "Light Amplification By Stimulated Emission Of Radiation", "Radio Detection And Ranging", "Self-Contained Underwater Breathing Apparatus", "Joint Photographic Experts Group", "Global Positioning System"]

score = 0
for i in range(len(full_forms)):
    user_input = input(f'Q{i+1}. What does {abbreviations[i]} stands for ?\nA: ')
    if user_input == full_forms[i]:
        score = score + 1
    else: 
        score = score + 0

result = f'Total Correct answers: {score}\nTotal Wrong answers: {len(full_forms)-score}\nTotal Score: {(score/len(full_forms)) * 100}%'
print(result)
                    