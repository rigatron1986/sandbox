# import OptionParser class
# from optparse module.
from optparse import OptionParser

# create a OptionParser
# class object
parser = OptionParser()

# ass options
parser.add_option("-f", "--file",
                  dest="filename",
                  help="write report to FILE",
                  metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false",
                  dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print(options)
print(options.filename)
