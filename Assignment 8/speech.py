import speech_recognition as sr
import os
import re
import distance
import matplotlib.pyplot as plt


class Speech:
	def __init__(self):
		self.original = []
		self.recognized = []
		self.similarity = []

	def read_original(self, inFile):
		file = open(inFile)
		self.original = file.readlines()
		self.original = [line.rstrip() for line in self.original]
		file.close()
		#print(self.original)

	def conv_audio(self, inDir):
		r = sr.Recognizer()
		files = sorted(os.listdir(inDir))
		for file in files:
			path = os.path.join(inDir, file)
			audio_file = sr.AudioFile(path)
			with audio_file as source:
				# r.adjust_for_ambient_noise(source)
				audio = r.record(source)
				line = r.recognize_google(audio)
				self.recognized.append(line)
		#print(self.recognized)

	def comp_string(self):
		original = [s.replace("'", "").replace("’", "").replace("-", "").lower() for s in self.original]
		recognized = [s.replace("'", "").replace("’", "").replace("-", "").lower() for s in self.recognized]
		for i in range(len(original)):
			ori = list(filter(None, re.split('[, .]+', original[i])))
			rec = list(filter(None, re.split('[, .]+', recognized[i])))
			#print(ori)
			#print(rec)
			self.similarity.append(distance.levenshtein(ori, rec))
		return self.similarity


if __name__ == '__main__':
	S = Speech()
	S.read_original('How Speech Recognition Works.txt')
	S.conv_audio('audio')
	simE = S.comp_string()
	female = Speech()
	female.read_original('How Speech Recognition Works.txt')
	female.conv_audio('audio_female')
	simF = female.comp_string()
	bengali = Speech()
	bengali.read_original('How Speech Recognition Works.txt')
	bengali.conv_audio('audio_bengali')
	simB = bengali.comp_string()
	# against female
	plt.boxplot([simE, simF], labels=['Male', 'Female'])
	plt.title('Male vs. Female')
	plt.ylabel('Levenshtein Distance')
	plt.show()
	# against Bengali
	plt.boxplot([simE, simB], labels=['English', 'Bengali'])
	plt.title('English vs. Bengali')
	plt.ylabel('Levenshtein Distance')
	plt.show()
