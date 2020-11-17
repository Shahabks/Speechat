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

## Pronunciation
My-Voice-Analysis and MYprosody repos are two capsulated libraries from one of our main projects on speech scoring. The main project (its early version) employed ASR and used the Hidden Markov Model framework to train simple Gaussian acoustic models for each phoneme for each speaker in the given available audio datasets, then calculating all the symmetric K-L divergences for each pair of models for each speaker. What you see in these repos are just an approximate of those model without paying attention to level of accuracy of each phenome rather on fluency 
In the project's machine learning model we considered audio files of speakers who possessed an appropriate degree of pronunciation, either in general or for a specific utterance, word or phoneme, (in effect they had been rated with expert-human graders). Here below the figure illustrates some of the factors that the expert-human grader had considered in rating as an overall score

![image](https://user-images.githubusercontent.com/27753966/98312800-cf583a80-2015-11eb-9ecb-99658ecabdbb.png)

> [S. M. Witt, 2012 “Automatic error detection in pronunciation training: Where we are and where we need to go,” ](https://www.researchgate.net/publication/250306074_Automatic_Error_Detection_in_Pronunciation_Training_Where_we_are_and_where_we_need_to_go)

