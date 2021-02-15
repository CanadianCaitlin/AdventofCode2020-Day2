def password_check(input):
    password_count = 0
    with open('input.txt') as f:
        for line in f:
            password = line.split(" ", 2)[2]
            letter = line.split(":", 1)[0][-1]
            policy = line.split(" ", 1)[0]
            min_num = int(policy.split("-")[0])
            max_num = int(policy.split("-")[1])

            count = 0
            for character in password:
                if character == letter:
                    count += 1
            
            if count >= min_num and count <= max_num:
                password_count += 1
    
    return password_count

print(password_check("input.txt"))

