import re
import string
import pickle 
import os

end_result = {}

REGEX = '(SM [0-9][0-9][0-9]\.)|(L\/R [0-9][0-9][0-9]\.)|([^, 1-9][0-9][0-9][0-9]\.)'

for file in os.listdir(os.path.join(os.path.dirname(__file__), "files")):
	if file.endswith(".txt"):
		file = os.path.join('files/', file)
		print file
		with open(file, 'r') as myfile:
			data = myfile.read().replace('\n', '')

		temp = re.findall(REGEX, data)
		course_codes = []

		mod=string.maketrans('','')
		nodigs=mod.translate(mod, string.digits)
		for i in temp:
			for j in i:
				if j != '' and j != 'L/R' and j!= 'SM':
					i = j
			course_codes.append(i.translate(mod, nodigs))

		temp2 = re.split(REGEX, data)
		course_descriptions = []
		for i in temp2:
			if i != None:
				if len(i) > 10:
					index = re.search('(Page [0-9] of [0-9])|(Page [0-9][0-9] of [0-9])', i)
					if index == None:
						course_descriptions.append(i)
					else:
						course_descriptions.append(i[:index.start()])

		nobars=mod.translate(mod, string.ascii_uppercase)
		department_code = re.findall('\{\w+\}', data)[0].translate(mod, nobars)

		temp_dictionary = {}
		if len(course_codes) == len(course_descriptions):
			print 'yes'
		for i in range(0, len(course_codes)):
			temp_dictionary[course_codes[i]] = course_descriptions[i+1]

		end_result[department_code] = temp_dictionary

fp = open( "save.p", "ab" )
for i in end_result:
	pickle.dump({i:end_result[i]},  fp)
print end_result['CIS']['262']
