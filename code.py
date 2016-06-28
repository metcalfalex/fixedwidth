# http://stackoverflow.com/questions/4914008/efficient-way-of-parsing-fixed-width-files-in-python

import struct
import csv

file_in = 'data_04.txt'
fieldwidths = (11,-1,11,-1,6,-1,8,-1,8,-1,8,-1,11,-1,6,-1,54,-1,6,-1,7,-1,7,-1,6,-1,6,-1,21,-1,40,-1,11,-1,1)
# Use negative to imdicate spaces/buffers between date containing columns

delimiter_out = '\t'
quotechar_out = '"'
# quote char doesn't seem to be working? ... Alex to fix

def fwp(line_in):
	fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's')
                        	for fw in fieldwidths)
	fieldstruct = struct.Struct(fmtstring)
	parse = fieldstruct.unpack_from
	fields = parse(line_in)
	return(fields)

with open(file_in, "r") as fi:
	header_line = next(fi)
	with open('out_01.txt','w') as fo:
		fo_csv = csv.writer(fo,delimiter=delimiter_out, quotechar=quotechar_out)
		fo_csv.writerow(fwp(header_line))
		for row in fi:
			fo_csv.writerow(fwp(row))
