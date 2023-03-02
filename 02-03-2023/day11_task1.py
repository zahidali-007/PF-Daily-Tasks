def convert_upper(input):
    for key, value in input.items():
        input[key] = [sample_input.upper() 
                    for sample_input in value]
    return input


user_input = {"Gfg" : ["ab", "cd"], "Best" : ["gh"], "is" :["kl"]}  

output = convert_upper(user_input)
print(output)
