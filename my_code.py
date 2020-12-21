from string import Template
from os import system

epochs = 100
t = Template('python3 src/main.py --content_path images/input/frame${index}.jpg --style_path images/fire/frame${index}.jpg --max_epochs ${epochs} --output_path images/outputs/output${index}.jpg')

for i in range(1130):
    system(t.substitute(index=i, epochs=epochs))
