from pathlib import Path
import simpleaudio
from synth_args import process_commandline
from nltk.corpus import cmudict
import re

# import numpy
# ...others?  (only modules that come as standard with Python3, so
# they will be available on marker machines)

# A pair of classes (Synth and Utterance) to start you off
# (you can change these as you like)


class Synth:
    def __init__(self, wav_folder):
        self.diphones = self.get_wavs(wav_folder)

    def get_wavs(self, wav_folder):
        """Loads all the waveform data contained in WAV_FOLDER.
        Returns a dictionary, with unit names as keys and the corresponding
        loaded audio data as values."""

        diphones = {}

        raise NotImplementedError  # delete and insert code to implement

        return diphones

    def synthesise(self, phones, reverse=False, smooth_concat=False):
        """
        Synthesises a phone list into an audio utterance.
        :param phones: list of phones (list of strings)
        :param smooth_concat:
        :return: synthesised utterance (Audio instance)
        """

        # delete/change this if you want to do Exts. "Crossfade" or "Reverse", otherwise leave this here
        if smooth_concat or reverse:
            raise NotImplementedError  # delete and insert code

        raise NotImplementedError  # delete and insert code to implement

        return simpleaudio.Audio()  # empty for now - change to return the proper utterance waveform!

    def phones_to_diphones(self, phones):
        """
        Converts a list of phones to the corresponding diphone units (to match units in diphones folder).
        :param phones: list of phones (list of strings)
        :return: list of diphones (list of strings)
        """

        raise NotImplementedError  # delete and insert code to implement


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

    def get_phone_seq(self, reverse=None):
        """
        Returns the phone sequence corresponding to the text in this Utterance (i.e. self.phrase)
        :param reverse:  Whether to reverse something.  Either "words", "phones" or None
        :return: list of phones (as strings)
        """

        raise NotImplementedError  # delete and add your code to do the right thing...

        return []  # empty for now - implement code to return the right thing!


# Make this the top-level "driver" function for your programme.  There are some hints here
# to get you going, but you will need to add all the code to make your programme behave
# correctly according to the commandline options given in args (and assignment description!).
def main(args):
    print(args)  # just to demonstrate what the user has asked for - delete this when ready

    utt = Utterance(phrase=args.phrase)
    phone_seq = utt.get_phone_seq(reverse=args.reverse)

    print(phone_seq)

    print(f'Will load wavs from: {args.diphones}')  # just a clue - can be deleted
    diphone_synth = Synth(wav_folder=args.diphones)

    out = diphone_synth.synthesise(phone_seq)

    # do what you like with "out"...

# DO NOT change or add anything below here
# (it just parses the commandline and calls your "main" function
# with the options given by the user)
if __name__ == "__main__":
    main(process_commandline())
