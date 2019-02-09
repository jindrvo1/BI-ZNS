questions = [
   ("1. Jdeš jen na jedno?", 0.05),
   ("2. Pivo?", 0.9),
   ("3. Víno?", 0.05),
   ("4. Koktejly?", 0.01),
   ("5. Tvrdej?", 0.6), 
   ("6. Máš spousty peněz?", 0.2),
   ("7. Chceš jíst?", 0.7), 
   ("8. Plnohodnotná večeře?", 0.3),
   ("9. Jsi vegetarián?", 0.1),
   ("10. Máš rád burgery?", 0.8),
   ("11. Chceš si pivo sám točit?", 0.5),
   ("12. Chceš pivo z malýho pivovaru?", 0.7),
   ("13. Máš silnou preferenci vůči Plzni?", 0.9),
   ("14. Máš silnou preferenci vůči Kozlovi?", 0.2),
   ("15. Máš silnou preferenci vůči Budvaru?", 0.3),
   ("16. Chceš to mít fancy?", 0.1),
   ("17. Jdeš sám?", 0.1),
   ("18. Jdeš s kamarády?", 0.8),
   ("19. Jdeš s rodinou?", 0.1),
   ("20. Jdeš s kolegy?", 0.1),
   ("21. Jdeš s přítelkyní?", 0.4),
   ("22. Chceš na ně/ní zapůsobit?", 0.2),
   ("23. Nechceš jít radši s kamarády?", 0.9),
   ("24. Plánuješ se vyndat?", 0.95),
   ("25. Plánujete potom jít do nonstopu?", 0.8),
   ("26. Bydlíš poblíž centra?", 0.5),
   ("27. Jsi ochotnej do centra dojet?", 0.8),
   ("28. Preferuješ metro?", 0.5),
   ("29. Preferuješ tramvaj?", 0.5),
   ("30. Nebojíš se vyšší ceny?", 0.1)
]

conclusions = [
   "1. U Glaubiců",
   "2. Kozlovna",
   "3. Budvarka",
   "4. The Pub",
   "5. U Hrocha",
   "6. Fancy lounge pub",
   "7. Vínograf Wine Bar"
]

relations = [
   [[1, 2, 13, 14], 2],
   [[1, 2, 13, 15], 3],
   [[1, 2, 13, 11], 4],
   [[1, 2, 13, 11, 30], 4],
   [[1, 2, 6, 16, 7, 16], 8],
   [[1, 2, 6, 17, 18, 24], 1],
   [[1, 2, 6, 7, 8, 9, 10], 5],
   [[1, 2, 3, 6, 7, 8, 9, 10], 5],
   [[1, 2, 6, 17, 18, 24, 25], 1],
   [[1, 2, 3, 4, 6, 7 , 8, 9, 10], 5],
   [[1, 2, 6, 17, 18, 24, 26, 27, 29], 1],
   [[1, 2, 6, 17, 18, 24, 26, 27, 28], 1],
   [[1, 2, 3, 4, 5, 6, 7 , 8, 9, 10], 5],
   [[1, 2, 6, 17, 18, 19, 22, 23, 24, 26, 27, 28], 1],
   [[1, 2, 6, 17, 18, 19, 20, 22, 23, 24, 26, 27, 28], 1],
   [[1, 2, 6, 17, 18, 19, 20, 21, 22, 23, 24, 26, 27, 28], 1]
];

def get_results(answers):
   results = []
   pos_answers = [q+1 for q, a in answers.items() if a == "1"]
   print("Pos answers: {}".format(pos_answers))
   for rel in relations:
      if all([x in rel[0] for x in pos_answers]):
         results.append((rel[0], rel[1]))

   return results

def ask_question(answers, results):
   for res in results[0][0]:
      if res-1 not in answers:
         print(questions[res-1])
         new_ans = input()
         answers[res-1] = new_ans

         return answers

answers = {}
results = get_results(answers)

while len(results) > 1:
   answers = ask_question(answers, results)
   results = get_results(answers)
   print("Answers: {}".format(answers))
   print("Results: {}".format(results))
   print()

print("Tak to jdi do hospody {}!".format(conclusions[results[0][1]]))