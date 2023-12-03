import re
import os
import nltk
from nltk.corpus import cmudict
from simpleaudio import Audio

'''
# Access the CMU Pronouncing Dictionary
pronouncing_dict = cmudict.dict()

# Check the pronunciation of a word
word_to_check = "example"
pronunciation = pronouncing_dict.get(word_to_check.lower())  # Convert to lowercase for case-insensitive lookup

print(pronouncing_dict["hello"])

if pronunciation:
    print(f"Pronunciation of {word_to_check}: {pronunciation[0]}")
else:
    print(f"Pronunciation of {word_to_check} not found in the CMU Pronouncing Dictionary.")
'''


class Utterance:

    def __init__(self, phrase, ignore_emph=True):
        """
        Constructor takes a phrase to process.
        :param phrase: a string which contains the phrase to process.
        """
        print(f'Processing phrase: {phrase}')  # just a hint - can be deleted
        self.phrase = phrase

        # if you choose to do Exts "Emphasis", delete these lines (and implement what's required!)
        # otherwise, leave these here
        if not ignore_emph:
            raise NotImplementedError

        # do anything else you want here!

    def normalise_text (self):
        # convert to lower case
        self.phrase = self.phrase.lower()

        # remove punctuation
        punctuation = re.compile(r'[^\w\s]')
        self.phrase = punctuation.sub('', self.phrase)
        self.phrase = nltk.word_tokenize(self.phrase)

    def get_phone_seq(self, reverse=None):
        """
        Returns the phone sequence corresponding to the text in this Utterance (i.e. self.phrase)
        :param reverse:  Whether to reverse something.  Either "words", "phones" or None
        :return: list of phones (as strings)
        """
        all_phone = []
        pronouncing_dict = cmudict.dict()
        self.normalise_text()

        # Check the pronunciation of a word
        for word in self.phrase:
            phone_list = pronouncing_dict.get(word)[0]
            all_phone.append (phone_list)
        # raise NotImplementedError  # delete and add your code to do the right thing...
        all_phone_new = [phone for element in all_phone for phone in element]
        all_phone_new.insert(0, 'PAU')
        all_phone_new.append('PAU')

        return all_phone_new


    def expand_phone_seq (self):
        phone_seq_new = []
        phone_seq = self.get_phone_seq()
        for i in range(len(phone_seq)-1):
            diphone = phone_seq[i] + '-' + phone_seq[i+1]
            phone_seq_new.append(diphone)

        return phone_seq_new


class Synth:
    def __init__(self, wav_folder):
        self.diphones = self.get_wavs(wav_folder)

    def get_wavs(self, wav_folder):
        """Loads all the waveform data contained in WAV_FOLDER.
        Returns a dictionary, with unit names as keys and the corresponding
        loaded audio data as values."""

        diphones = {}

        for folder, directory, audios in os.walk(wav_folder, topdown=False):
            for audio in audios:
                # compile the regular expression as "xxx.wav"
                re_diphones = re.compile(r'^(.+)(.wav)$')
                # convert diphone name into uppercase, aligned with the CMUdict
                diphone_name = re_diphones.match(str(audio)).groups()[0].upper()
                diphone_path = os.path.join(wav_folder, audio) # output: 'AO-ZH': 'diphones/ao-zh.wav'
                diphone = Audio()
                diphone.load(diphone_path)
                diphones[diphone_name] = diphone

        return diphones

    def synthesise(self, phones, reverse=False, smooth_concat=False):
        """
        Synthesises a phone list into an audio utterance.
        :param phones: list of phones (list of strings)
        :param smooth_concat:
        :return: synthesised utterance (Audio instance)
        """

        # delete/change this if you want to do Exts. "Crossfade" or "Reverse", otherwise leave this here
        # if smooth_concat or reverse:
            # raise NotImplementedError  # delete and insert code

        # raise NotImplementedError  # delete and insert code to implement
        diphone_list = self.phones_to_diphones(phones)
        diphone_sequence = np.array()
        for diphone_name in diphone_list:
            new_diphone_sequence = self.diphones [diphone_name].data
            diphone_sequence = np.concatenate((diphone_sequence, new_diphone_sequence), axis=1)

        diphone_instance = Audio()
        diphone_instance.data = diphone_sequence

        return diphone_instance  # empty for now - change to return the proper utterance waveform!

    def phones_to_diphones(self, phones):
        """
        Converts a list of phones to the corresponding diphone units (to match units in diphones folder).
        :param phones: list of phones (list of strings)
        :return: list of diphones (list of strings)
        """

        diphone_seq = []
        for i in range(len(phones) - 1):
            diphone = phone_seq[i] + '-' + phone_seq[i + 1]
            diphone_seq.append(diphone)

        return diphone_seq

        # raise NotImplementedError  # delete and insert code to implement



my_sentence = Utterance("Hello, my dear friend!")
print(my_sentence.expand_phone_seq())

all_diphones = Synth('diphones')
print(all_diphones.diphones['AA-AA'])
print(type(all_diphones.diphones['AA-AA'].data))
#all_diphones.diphones['AA-F'].play()

'''
my_data = Audio()
my_data.load('diphones/aa-aa.wav')
my_data.play()
'''