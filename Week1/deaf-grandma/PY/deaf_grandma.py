
def deaf_grandma():
    bye_count = 0
    
    while True:
        input_text = input('Kid: ')
        if input_text == '':
            print('WHAT?')
        elif not input_text.isupper():
            print('SPEAK UP, KID!')
        elif input_text == "GOODBYE!":
            bye_count  = bye_count + 1
            if bye_count <= 1:
                print('LEAVING SO SOON?')
            elif bye_count >= 2:
                print('LATER SKATER!')
                break
        elif input_text.isupper():
            print('NO, NOT SINCE 1946!')
        
deaf_grandma()


