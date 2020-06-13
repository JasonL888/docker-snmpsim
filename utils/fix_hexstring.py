import os
import logging
import getopt
import sys

def fix_hexstring(inputFileName,outputFileName):
    outputFile=open(outputFileName, "w")

    with open(inputFileName, "r") as inputFile:
        prior_line = ""
        line = inputFile.readline()
        while line:
            logger.info("processing - %s" % line)
            if ("Hex-STRING" in prior_line) and (line[:2] != "1."):
                logger.info("Hex-STRING overflow found - to combine")
                prior_line = prior_line.rstrip("\n") + " " + line
                logger.debug("prior_line - %s" % prior_line)
            elif ("Hex-STRING" in prior_line) and (line[:2] == "1."):
                logger.info("writing prior_line - %s" % prior_line)
                outputFile.write(prior_line)
                if ("Hex-STRING" not in line):
                    logger.info("writing line - %s" % line)
                    outputFile.write(line)
                prior_line = line
            elif ("Hex-STRING" in line):
                prior_line = line
            else:
                logger.info("writing line - %s" % line)
                outputFile.write(line)
                prior_line = line
            logger.info("reading next line")
            line = inputFile.readline()

    outputFile.close()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    logger = logging.getLogger('fix_hexstring')
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler('fix_hexstring.log',mode='w')
    fileHandler.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    if len(sys.argv) != 2:
        logger.error('Usage: python fix_hexstring.py infile')
        sys.exit()
    else:
        inputFileName = sys.argv[1]
        outputFileName = inputFileName + ".snmprec"
        logger.info("Fixing %s ... " % inputFileName)
        logger.info("=============")
        fix_hexstring(inputFileName=inputFileName,outputFileName=outputFileName)
        logger.info("=============")
        logger.info("Completed - output %s" % outputFileName)
