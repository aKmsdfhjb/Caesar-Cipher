def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text
text=('\n Enter Text: ')
shift=('\n ENter shit: ')
print('***OPTION***')
n=input('1. Encrypt \n 2.Decrypt')
match n:
  case n:
      def encrypt(text, shift):
        return caesar(text, shift)
  case n:
    def decrypt(text, shift):
      return caesar(text, shift, encrypt=False)


    

