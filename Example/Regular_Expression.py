#importing regular expresion and implementing some cases of them
import re
t = "The BMW 5 Series Sedan M Automobiles combine typical M sportiness with the comfort and elegance of a business saloon in an outstanding manner. Explore four unique M Automobiles with strong personalities: an outstanding output of 635 hp (467 kW) and an acceleration from 0 to 100 km/h in only 3.0 seconds make the BMW M5 CS the most powerful BMW M5 Sedan there has ever been. Part of a limited production series, the special model with unique M specific suspension and design components exclusively available for this model guarantee a pure motorsport sensation. Boasting a maximum output of 625 hp (460 kW) and suspension set-up optimised for performance, the BMW M5 Competition with M xDrive exceeds the highest expectations. The high-performance sports saloon underlines this visually with numerous design features in black high-gloss. In addition to the M xDrive designed for maximum traction and dynamics, the BMW M5 has a suspension that meets every demand for sporty ride comfort over long distances. Interacting with the 600 hp (441 kW) 8-cylinder M engine, this creates driving dynamics distinguished by power and agility. Rounding off the quartet is the BMW M550i xDrive Sedan. The athletic BMW 5 Series Sedan delivers 530 hp (390 kW) and impresses with an especially balanced combination of sportiness, comfort and efficiency."
#this search of word BMW is found on the provided text
x = re.search("BMW", t)
if x:
  print("YES")
else:
  print("No")
#this finds BMW and replace it with word M5ALB in the text
x = re.sub("BMW", "M5ALB", t)
print(x)