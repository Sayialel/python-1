from animal import animal

Bird = animal('Bird','Feathers','blue','Present','small')
Bat = animal('Bat','fur','black','present','small')
Human = animal('Human','hair','black','absent','large')

print(Bird.name,Bird.skin_type,Bird.eye_color,Bird.wings,Bird.size)
print(Bat.name,Bat.skin_type,Bat.eye_color,Bat.wings,Bat.size)
print(Human.name,Human.skin_type,Human.eye_color,Human.wings,Human.size)
