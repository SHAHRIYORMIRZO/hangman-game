import random
import img
from img import stages as st
word_lists = img.word_list
chosen_word = random.choice(word_lists)
word_length = len(chosen_word)
print(img.logo)
print(chosen_word)


output_word = []
end_game = True
for word in range(word_length):
  output_word += '_'
print(output_word)
action = 6
while end_game:
  print(st[action])
  guess = input('Harfni kiriting:\n')
  if guess not in chosen_word:
    action -= 1
    if action == 1:
      print('Ey bola ko\'zingni och oxirgi imkoniyating!!!😵')
    if action == 0:
      print('you lose')
      print(f'Ogohlantirgandim a seni. manbu {chosen_word} sen topolmagan so\'z. Oshqovoq')
      end_game = False
  if guess in output_word:
    print('Bu harfni kiritgansiz')
  for position in range(word_length):
    word = chosen_word[position]
    if word == guess:
      output_word[position] = word
  print(output_word)



  if '_' not in output_word:
    print('You win')
    end_game = False