from subprocess import call

call("python3 synthesize.py --model='Tacotron' --checkpoint='pretrained' --GTA=False --name='Tacotron' --text_list='meningar.txt'", shell=True)
