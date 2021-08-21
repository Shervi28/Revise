from os import path
from pydub import AudioSegment
import subprocess
import speech_recognition as sr

filename = "apEnviorment.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

# files                                                                         
#src = "precolumbia.mp3"
#dst = "test-columbia.wav"

# convert wav to mp3                                                            
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")

#subprocess.call(['ffmpeg', '-i', r'C:\Users\sherv\Desktop\IgnitionHacksApp\revise\precolumbia.mp3',
#                r'C:\Users\sherv\Desktop\IgnitionHacksApp\revise\precolumbiatwo.wav'])
#sound = AudioSegment.from_mp3("precolumbia.mp3")
#sound.export("/output/path/file.wav", format="wav")
                                                                         
#from pydub import AudioSegment
#sound = AudioSegment.from_mp3("precolumbia.mp3")
#sound.export("testsubject", format="wav")

#print("pydub")

# importing libraries 
# # # # import speech_recognition as sr 
# # # # import os 
# # # # from pydub import audiosegment
# # # # from pydub.silence import split_on_silence

# # # # # create a speech recognition object
# # # # r = sr.recognizer()

# # # # # a function that splits the audio file into chunks
# # # # # and applies speech recognition
# # # # def get_large_audio_transcription(path):
# # # #     """
# # # #     splitting the large audio file into chunks
# # # #     and apply speech recognition on each of these chunks
# # # #     """
# # # #     # open the audio file using pydub
# # # #     sound = audiosegment.from_wav(path)  
# # # #     # split audio sound where silence is 700 miliseconds or more and get chunks
# # # #     chunks = split_on_silence(sound,
# # # #         # experiment with this value for your target audio file
# # # #         min_silence_len = 500,
# # # #         # adjust this per requirement
# # # #         silence_thresh = sound.dbfs-14,
# # # #         # keep the silence for 1 second, adjustable as well
# # # #         keep_silence=500,
# # # #     )
# # # #     folder_name = "audio-chunks"
# # # #     # create a directory to store the audio chunks
# # # #     if not os.path.isdir(folder_name):
# # # #         os.mkdir(folder_name)
# # # #     whole_text = ""
# # # #     # process each chunk 
# # # #     for i, audio_chunk in enumerate(chunks, start=1):
# # # #         # export audio chunk and save it in
# # # #         # the `folder_name` directory.
# # # #         chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
# # # #         audio_chunk.export(chunk_filename, format="wav")
# # # #         # recognize the chunk
# # # #         with sr.audiofile(chunk_filename) as source:
# # # #             audio_listened = r.record(source)
# # # #             # try converting it to text
# # # #             try:
# # # #                 text = r.recognize_google(audio_listened)
# # # #             except sr.unknownvalueerror as e:
# # # #                 print("error:", str(e))
# # # #             else:
# # # #                 text = f"{text.capitalize()}. "
# # # #                 print(chunk_filename, ":", text)
# # # #                 whole_text += text
# # # #     # return the text for all chunks detected
# # # #     return whole_text

# # # # path = "precolubia.wav"
# # # # print("\nfull text:", get_large_audio_transcription(path))

