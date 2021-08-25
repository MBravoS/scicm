"""
Author: Robin Cook, Matias Bravo
Date: 09/08/19
"""

changelog = "../changelog.txt"
setup = "../setup.cfg"

import os
import re
from datetime import date

import numpy as np
from argparse import ArgumentParser, RawTextHelpFormatter

def prepend(filename, line):
	with open(filename, 'r+') as f: 
		content = f.read() 
		f.seek(0, 0) 
		f.write(line.rstrip('\r') + '\n' + content)

def get_version():
	# Check the versions in all of these files
	versions = []
	for filename in [changelog,setup]:
		with open(filename, 'r') as file:
			if ('changelog' in filename):
				versions.append(file.readline().split(' (')[0])
			else:
				for line in file.readlines():
					if ('setup' in filename and line.strip().startswith("version =")):
						versions.append(line.split(" = ")[1].replace('\n',''))
						break
				else: # No line matching pattern found in file
					versions.append(None)
					print(f"\nWARNING: Could not find version in file \"{filename}\"!\n")
	
	if ( len(set(versions)) > 1 ): # Make sure all versions are equal
		print("\nWARNING: Not all versions match across files. Got versions:")
		for version, filename in zip(versions, [changelog,setup]):
			print(f"{filename:<14}: {version}")
		
		choice = input("\nAre you sure you want to proceed (y/n)? ")
		if (choice.lower() == 'n'):
			exit()
		else:
			versions = list(filter(None.__ne__, versions)) # Filter out any Nones
			versionStr =  versions[np.argmax([int(version.replace('.','')) for version in versions])]
			return [int(kk) for kk in versionStr.split('.')]
	return [int(kk) for kk in versions[0].split('.')]

def set_versions(version, message):
	# Loop through all files
	for filename in [changelog,setup]:
		if ('changelog' in filename):
			string = (f"{version} ({date.today().strftime('%d/%m/%Y')}):\n{message}\n")
			prepend(filename, string)
		else:
			with open(filename, 'r') as file:
				lines = file.readlines()
			
			for ii, line in enumerate(lines):
				if ('setup' in filename and line.strip().startswith("version = ")):
					lines[ii] = f"version = {version}\n"
					break
			else: # No line matching pattern found in file
				print(f"\nWARNING: Could not find version in file \"{filename}\"!\n")
			
			with open(filename, 'w') as file:
				file.writelines(lines)
	return (None)

parser = ArgumentParser(description="Parse argument for changing versions:\n" 
									"  * Major (+M/--major): When a major update/new feature has been made to the code.\n"
									"  * Minor (+m/--minor): The addition of small changes to an existing function.\n"
									"  * Bug (+b/--bug): Small adjustments and bug fixes.\n", formatter_class=RawTextHelpFormatter, prefix_chars='-+')
parser.add_argument('-f','--full',
					action='store',dest='full',type=str,default=False,
					help="Change the full version number X.X.X",metavar="VERSION")
parser.add_argument('+M','--major',
					action='store',dest='major',nargs='?',type=int,default=False,const=True,
					help="Increase the major version number X.0.0",metavar="MAJOR")
parser.add_argument('+m','--minor',
					action='store',dest='minor',nargs='?',type=int,default=False,const=True,
					help="Increase the minor version number -.X.0",metavar="MINOR")
parser.add_argument('+b','--bug',
					action='store',dest='bug',nargs='?',type=int,default=False,const=True,
					help="Increase the minor version number -.-.X",metavar="BUG")
parser.add_argument('-m','--message',
					action='store',dest='message',type=str,nargs='*',default=[''],
					help="The message to be added to changelog.txt. If no --message given, do not add to changelog.txt",metavar="MESSAGE")
parser.add_argument('-c','--current',
					action='store_true',dest='current',default=False,
					help="Print the current version and exit.")

args = parser.parse_args()

# Get the current version
currVersion = get_version()
currVersionStr = ".".join(map(str,currVersion))

# Print current version and YEET on out of there
print(f"INFO: Current version is: {currVersionStr}")
if (args.current == True): exit()

# Validate inputs
nArgs = sum([not args.full is False, not args.major is False, not args.minor is False, not args.bug is False ])

if (nArgs == 1):
	if (args.full):
		newVersion = args.full.split('.')
		if (len(newVersion) != 4 or len(args.full) < 7):
			print(f"\nERROR: --full argument not valid, must have the format X.X.X, but {args.full} was given.\n  -- ABORTING --\n"); exit()
	
	elif (not args.major is False):
		newVersion = [currVersion[0]+args.major,currVersion[1],0] if (args.major is True) else [args.major,currVersion[1],0]
	elif (not args.minor is False):
		newVersion = [currVersion[0],currVersion[1]+args.minor,0] if (args.minor is True) else [currVersion[0],args.minor,0]
	elif (not args.bug is False): 
		newVersion = [currVersion[0],currVersion[1],currVersion[2]+args.bug] if (args.bug is True) else [currVersion[0],currVersion[1],args.bug]

elif (nArgs == 0):
	print("\nERROR: Nothing specified to change version number. Use one of [+v.+M.+m.+b] | -f.\n  -- ABORTING --\n"); exit()
else:
	print("\nERROR: Too many arguments given. Use one of [+v.+M.+m.+b] | -f.\n  -- ABORTING --\n"); exit()

#if ( int("".join(map(str, newVersion))) < int("".join(map(str, currVersion))) ):
invalid_version=True
for i in range(len(newVersion)):
	if int(newVersion[i])>int(currVersion[i]):
		invalid_version=False
	elif int(newVersion[i])<int(currVersion[i]):
		break
if invalid_version:
	print(f"\nERROR: the new version ({'.'.join(map(str, newVersion))}) specified is older than the current version ({'.'.join(map(str, currVersion))})\n  -- ABORTING --\n"); exit()


newVersionStr = ".".join([str(kk) for kk in newVersion])
print(f"INFO: New version is {newVersionStr}")


message = '\n'.join(["-"+m if m.lstrip()[0] not in ['-','*','>'] else m for m in args.message])
print(f"INFO: Prepending the following message to changelog.txt:\n\n{newVersionStr} ({date.today().strftime('%d/%m/%Y')}):\n{message}\n")

choice = input("Commit to changes (y/n)? ")
if (choice.lower() == 'n'):
	exit()
else:
	set_versions(version=newVersionStr,message=message)


