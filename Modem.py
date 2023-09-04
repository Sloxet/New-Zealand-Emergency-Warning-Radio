import numpy as np
from scipy.io import wavfile

class SAME_Signal_Generator:
    MARK_BIT_FREQUENCY = 2083 + (1 / 3)
    SPACE_BIT_FREQUENCY = 1562.5
    FS = 43750

    @staticmethod
    def Generate_Tone_Signal(frequency, duration):
        t = 1.0 / (520 + (5 / 6))
        samples = np.arange(t * SAME_Signal_Generator.FS) / SAME_Signal_Generator.FS
        return np.sin(2 * np.pi * frequency * samples) * 0.8

    @staticmethod
    def Generate_Byte_Signal(byte_value, mark_freq, space_freq):
        byte_data = np.zeros(0)
        for i in range(0, 8):
            if ord(byte_value) >> i & 1:
                byte_data = np.append(byte_data, SAME_Signal_Generator.Generate_Tone_Signal(mark_freq, 1))
            else:
                byte_data = np.append(byte_data, SAME_Signal_Generator.Generate_Tone_Signal(space_freq, 1))
        return byte_data

    @staticmethod
    def Generate_Header_Signal(header_parts, mark_freq, space_freq):
        byte_data = np.zeros(0)
        for i, part in enumerate(header_parts):
            for char in part:
                byte_data = np.append(byte_data, SAME_Signal_Generator.Generate_Byte_Signal(char, mark_freq, space_freq))
            if i < len(header_parts) - 1:
                if part == header_parts[-4]:
                    byte_data = np.append(byte_data, SAME_Signal_Generator.Generate_Byte_Signal("+", mark_freq, space_freq))
                else:
                    byte_data = np.append(byte_data, SAME_Signal_Generator.Generate_Byte_Signal("-", mark_freq, space_freq))
            elif i == len(header_parts) - 1:
                byte_data = np.append(byte_data, SAME_Signal_Generator.Generate_Byte_Signal("-", mark_freq, space_freq))
        return byte_data

    @staticmethod
    def Generate_Preamble_Signal(mark_freq, space_freq):
        preamble_data = np.zeros(0)
        for _ in range(0, 16):
            preamble_data = np.append(
                preamble_data,
                [
                    SAME_Signal_Generator.Generate_Tone_Signal(mark_freq, 1),
                    SAME_Signal_Generator.Generate_Tone_Signal(mark_freq, 1),
                    SAME_Signal_Generator.Generate_Tone_Signal(space_freq, 1),
                    SAME_Signal_Generator.Generate_Tone_Signal(mark_freq, 1),
                    SAME_Signal_Generator.Generate_Tone_Signal(space_freq, 1),
                    SAME_Signal_Generator.Generate_Tone_Signal(mark_freq, 1),
                    SAME_Signal_Generator.Generate_Tone_Signal(space_freq, 1),
                    SAME_Signal_Generator.Generate_Tone_Signal(mark_freq, 1),
                ],
            )
        return preamble_data

    @staticmethod
    def Generate_Attention_Signal():
        t = 1.0 / SAME_Signal_Generator.FS
        samples = np.arange(int(5 * SAME_Signal_Generator.FS)) / SAME_Signal_Generator.FS
        return np.sin(2 * np.pi * 1050 * samples) * 0.8

    @staticmethod
    def Finalise_SAME_Signal(header_parts, eom, mark_freq, space_freq):
        signal = np.zeros(0)
        for _ in range(3):
            signal = np.append(signal, SAME_Signal_Generator.Generate_Preamble_Signal(mark_freq, space_freq))
            signal = np.append(signal, SAME_Signal_Generator.Generate_Header_Signal(header_parts, mark_freq, space_freq))
            if _ < 2:
                signal = np.append(signal, np.zeros(SAME_Signal_Generator.FS))
        ATTN_EVENTS = [
            "AVW", "BLU", "BZW", "CDW", "CEM", "CFW", "DSW", "EAN", "EQW", "EVI", "EWW", "FFW", "FLW", "FRW", "FSW",
            "FZW", "HMW", "HUW", "HWW", "LEW", "NUW", "RHW", "SMW", "SPW", "SQW", "SSW", "SVR", "TOR", "TRW", "VOW",
            "WSW",
        ]
        if any(event in header_parts for event in ATTN_EVENTS):
            attn_fs = np.zeros(int(SAME_Signal_Generator.FS / 2))
            signal = np.append(signal, attn_fs)
            signal = np.append(signal, SAME_Signal_Generator.Generate_Attention_Signal())
        for _ in range(0, 3):
            signal = np.append(signal, SAME_Signal_Generator.Generate_Preamble_Signal(mark_freq, space_freq))
            for char in eom:
                signal = np.append(signal, SAME_Signal_Generator.Generate_Byte_Signal(char, mark_freq, space_freq))
            if _ < 2:
                signal = np.append(signal, np.zeros(SAME_Signal_Generator.FS))
        return signal

    @staticmethod
    def Export_SAME_Signal(ORG, EEE, PSSCCC, TTTT, JJJHHMM, LLLLLLLL):
        header = [
            "ZCZC", ORG, EEE, PSSCCC, TTTT, JJJHHMM, LLLLLLLL
        ]
        signal = SAME_Signal_Generator.Finalise_SAME_Signal(
            header, "NNNN", SAME_Signal_Generator.MARK_BIT_FREQUENCY, SAME_Signal_Generator.SPACE_BIT_FREQUENCY
        )
        wavfile.write("SAME.WAV", SAME_Signal_Generator.FS, signal.astype(np.float32))
