[![GitHub stars](https://img.shields.io/github/stars/Shahabks/Speechat?style=flat-square)](https://github.com/Shahabks/Speechat/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Shahabks/Speechat?style=flat-square&color=blueviolet)](https://github.com/Shahabks/Speechat/network/members)

# Speechat
## Spoken Language assessment
It takes either real-time streams of speech or a recorded speech and extracts the prosody features, does features engineering, building dataset. The dataset is then plugged in the ML algorithms to predict intonations, prosody, stress, and structures of the spoken language.
By using an ASR engine, it scripts the speech and sends to a language model for some further analysis to measure the pragmatic and sentimental expressions as well as mechanical/structural patterns of the speech.

For further informtion 

https://github.com/Shahabks/my-voice-analysis

https://github.com/Shahabks/myprosody

I just uploaded a folder in which there are some saved labeled datasets + already-trained models + two file are written/coded in praat (*.praat) that you need when you run the python file for training new models. .... also all my experiments
As far as the python libraries are concerned, except "parselmouth" other libraries are standard python libraries. Parselmouth can be installed by pip (https://parselmouth.readthedocs.io/en/docs/examples.html more information).
