# 提示用户输入内容，转化为小写，存入变量
def encode_module():
    flag = False
    result = []
    user_input = ""
    while not flag:
        user_input = input("please input the word you want to encode\n").lower()
        if " " not in user_input:
            flag = True
    shift = int(input("please type the shift number\n"))
    for i in user_input:
        if ord(i) + shift <= 122:
            result.append(chr(ord(i) + shift))
        else:
            result.append(chr(ord(i) + shift - 122 + 97))
    print(f"your encode word is {''.join(result)}")


# 如果有空格需要提示重新输入
# 提示用户输入偏移量
# 转换编码ord+偏移量，并输出 97-122
def decode_module():
    decode_flag = False
    decode_result = []
    user_input = ""
    while not decode_flag:
        user_input = input("please input the word you want to decode\n").lower()
        if " " not in user_input:
            decode_flag = True
    shift = int(input("please type the shift number\n"))
    for i in user_input:
        if ord(i) - shift >= 97:
            decode_result.append(chr(ord(i) - shift))
        else:
            decode_result.append(chr(122 - (97 - ord(i) + shift)))
    print(f"your decode word is {''.join(decode_result)}")


# 提示用户输入编译后的内容
# 提示用户输入偏移量
# 转换编码ord-偏移量，并输出

input_list = ["encode", "decode"]
user_select = ""
while user_select not in input_list:
    user_select = input(
        "welcome the ceaser code program,please select 'encode' for encode the word and select "
        "'decode' to decode the word\n"
    )
    if user_select == "encode":
        encode_module()
    elif user_select == "decode":
        decode_module()
