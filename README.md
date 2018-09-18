Detta är en version av repot https://github.com/Rayhane-mamah/Tacotron-2 som är modifierad för att köras med svensk data. Den innehåller även vissa andra tillägg och modifikationer i parametrar.

1. Installera CUDA (helst 9.0), cudnn (helst 7.0.5) och Tensorflow (helst 1.10). Kör kommandot "pip3 install -r requirements.txt" i mappen "Tacotron-2". Här finns bra instruktioner för att installera Cuda+cudnn: https://gist.github.com/zhanwenchen/e520767a409325d9961072f666815bb8

2. Datasetet som man vill använda ska placeras i mappen "Tacotron-2/basedata"

3. Datasettet bör vara på formen som man kan se på de exempelfiler jag lämnat i mappen. 16-bit mono wav med 22050Hz i samplingsfrekvens. Vill man använda annan samplingsfrekvens behöver man ändra "sample_rate" i "Tacotron-2/hparams.py" plus eventuellt en del andra parametrar. Filnamnen spelar ingen roll, men måste stämma överrens med transkripten i "metadata.csv". 

4. "metadata.csv" är på formen <filnamn(utan ".wav")|transkript|normaliserat transkript>. Koden läser bara det "normaliserat transkript" så "transkript" är egentligen överflödig information. (kvarlämning från hur LJspeechdatasettet ser ut). Siffror behöver inte normaliseras till text.

5. Koden innehåller en funktion som trimmar bort tystnad. Hur känslig den parametern är kan man justera med parametern "trim_top_db". Lägre värde innebär mer aggressiv trimmning.

6. Förbered träningssettet genom att köra kommandot "python3 preprocess.py"

7. Träna modellen genom att köra "python3 train.py --model="Tacotron" (vill du försöka träna wavenet också så justera hur länge du vill träna varje modell i train.py och kör sen "python3 train.py")

8. Syntetisera meningarna i "Tacotron-2/meningar.txt" genom att köra "python3 syntetiserameningar.py" De syntetiserade meningarna och tillhörande plots kommer att hamna i "Tacotron-2/tacotron_output/logs-eval". Vill du syntetisera från en annan tidpunkt i träningshistorien så ändra översta raden i filen "Tacotron-2/logs-Tacotron/taco-pretrained/checkpoint till en checkpoint som finns sparad i samma mapp.


NOTES:
(För att syntetisera krävs att du har tränat en modell i minst 5000 steg så att det finns en checkpoint i "Tacotron-2/logs-Tacotron/taco-pretrained". )

Koden innehåller ett verktyg som normaliserar siffror i text till ord på svenska. Koden är alltså anpassad för användning med svensk data. Den skiljer sig också från originalrepot (https://github.com/Rayhane-mamah/Tacotron-2) på det vis att den använder pre-emphasis och vissa andra modifikationer.

"Stödfiler" är lite filer som användes för att konvertera datan till den form som accepteras av koden. Användes visserligen på denna data: https://www.nb.no/sprakbanken/show?serial=oai%3Anb.no%3Asbr-18&lang=en men kanske går att återanvända på annat.

Övrig information om koden och hur den ska användas kan ni hitta på https://github.com/Rayhane-mamah/Tacotron-2

Viktiga parametrar i filen "Tacotron-2/hparams.py":

	Problem med OOM (får slut på minne i grafikkortet):
		tacotron_batch_size
		outputs_per_step (kallas för "reduction factor = r" i Tacotron-artikeln)

	Manlig vs kvinnlig talare:
		fmin
		fmax
	Griffin_lim:
		power
	Annat:
		cleaners
		tacotron_test_size 
		hop_size
		win_size
		sample_rate
		trim_top_db


Övriga kommandon:

Write command in terminal before training to decide which GPU that should be used.
	export CUDA_VISIBLE_DEVICES=1
	export CUDA_VISIBLE_DEVICES=0

run this command in the Tacotron-2 folder to be able to use griffin_lim_synthesis_tool.ipynb
	jupyter notebook --ip=127.0.0.1 --port=31337

Synthesize command
	python3 synthesize.py --model='Tacotron' --checkpoint='pretrained' --name='Tacotron-2' --text_list=''

normalization command
	ffmpeg-normalize *.wav --dual-mono -ext "wav" -f -nt rms -t -19


