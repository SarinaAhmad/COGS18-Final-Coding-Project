import random

def beginning():
    
    """This function randomly generated the introduction of the story along with the name of the protagonist"""
    
    intros = ['A long time ago in a land since burned to ash, ', 'Eons ago in a dark kingdom ', 'It was a dark and stormy night when ', 'The sun was shining through the clouds when ', 'The sun was shining on the vast sea when ', 'As the sun rose over the horizon, ', 'As the sun set over the horizon, ']
    
    main_character = ['Aelin', 'Feyre', 'Rowan', 'Rhysand', 'Cassian', 'Azriel', 'Fenrys', 'Chaol', 'Dorian', 'Manon', 'Lysandra', 'Aedion', 'Mor', 'Amren', 'Sam', 'Lorcan', 'Elide', 'Yrene']
    
    intro = random.choice(intros) + random.choice(main_character)+  ' faced a pressing issue. '
    
    return intro



    
def middle():
    
    """This function is for the middle of the story and randomly generates the conflict and the enemy"""
    
    enemy = ['Maeve', 'The King of Adarlan', 'Arobynn', 'Baba Yellowlegs', 'Cairn', 'Erawan', 'Tamlin', 'The King of Hybern', 'Eris', 'Keir', 'Amarantha']
    
    problems = [' suddenly came at them with a knife. ', ' had blindsided them, knocked them out, and had taken them to another location. ', ' was torturing them to the brink of death, and they could not take it anymore. ', ' secretly attacked their camp, and was now shooting them with fire. ', ' was trying to infest them with a demon from another world. ', 
           ' tried to trap them under a mountain in order to take over the kingdom. ', ' had killed their lover, and had now trapped them too in order to kill them. ', ' began to attack with a hoarde of demon spiders. ', ' was using them as an assassin to do their dirty work. ']
    
    conflict = (random.choice(enemy) + random.choice(problems))
    
    return conflict





def ending():
    
    """This function is for the ending of the story, and randomly generates the solution and ending scene"""
    
    solutions = ['They knew they had to act quick, so they grabbed the glass shard to their side, cut themselves free, and killed their enemy. ', 'At that moment they realized that they must survive to restore their kingdom, so they gathered the last of their strength and delivered a killing blow. ', 'It was at that point that the right hand man of the enemy turned on them and helped the hero escape. ', 'However, their lover arrived and rescued them. ', 'Their enemy tried to outwit them, but they had completed their trials, solved the riddle, and escaped. ', 'To do right by their kingdom and friends, the hero decided the only chance for the survival of the greater good was to sacrifice themselves. ', 'This sent the hero into a rage in order to protect their loved ones. They killed every enemy around them. ', 'They knew they were not alone, so they distracted their enemy while their friend snuck up behind and killed them. ']
    
    endings = ['It was at that moment they were suddenly awakened by a firm shake, and they realized it had all been a dream.', 'After the defeat of their enemy, they reclaim their kingdom and become its ruler.', 'As the fight ends, they realize that their lover has been killed, but they know they must continue to fight for their kingdom.', 'And they lived happily ever after.', 'The battle has ended, but there was still a war to be won.']
    
    finale = (random.choice(solutions) + random.choice(endings))
    
    return finale

print(beginning() + middle() + ending())