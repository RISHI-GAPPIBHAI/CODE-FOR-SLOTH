#My solution for sloth's hex code challenge
#Hey SLOTH IF YOU'RE SEEING THIS, CAN YOU PLEASE TELL ME THE VIDEO EDITING SOFTWARE YOU USE??



def inputs():
    code=input("Enter the hex code")
    return code
def hex_code_verifier():
    hex_code=inputs()
    all_good=True
    list_of_permissible_alphabets=['a','b','c','d','e','f']
    if not hex_code[0]=="#" or not len(hex_code)==7:
        all_good=False
    for character in hex_code[1:]:
        if character.isdigit():
            continue
        if not character.lower() in list_of_permissible_alphabets:
            all_good=False
            break
    return all_good
def main():
    if hex_code_verifier():
        print("Hex code verified")
    else:
        print("Hex code not verified")

if __name__ == '__main__':
    main()