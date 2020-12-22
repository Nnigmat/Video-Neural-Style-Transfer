from string import Template
from os import system
from multiprocessing import Pool

epochs = 80
t = Template('python3 src/main.py --content_path images/input/frame${index}.jpg --style_path images/fire/frame${index}.jpg --max_epochs ${epochs} --output_path images/outputs/output${index}.jpg')

def process(index):
    system(t.substitute(index=index, epochs=epochs))

indicies = [i for i in range(13, 1130)]
with Pool(10) as p:
    p.map(process, indicies)
    
