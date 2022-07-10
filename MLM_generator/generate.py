from generate_data import generate_data
import sys
import os
import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# data_loc = "sample_data/humanTranslation.txt"
# output_dir =  os.getcwd()
# generate_txt = False
# generate_dataset = False
# generate_json = False
# combine = False
# lang = "en"

# Adding optional argument
parser.add_argument("-i", "--data_loc", default = "sample_data/humanTranslation.txt", type = str)
parser.add_argument("-o", "--output_dir", default = "generated_data", help = "file output dir", type = str)
parser.add_argument("-t", "--generate_txt", default =False, action='store_true')
parser.add_argument("-d", "--generate_dataset", default =False,action='store_true')
parser.add_argument("-j", "--generate_json", default =False,action='store_true')
parser.add_argument("-c", "--combine", default =False,action='store_true')
parser.add_argument("-l", "--lang", default = "en")
args = parser.parse_args()

# if args.Output:
#     print("Displaying Output as: % s" % args.Output)
 
 

 
# # Options
# options = ["idjcl:t:o:"]


# # Long options
# long_options = ["data_loc =", "output_dir =", "generate_txt", "generate_dataset" , "generate_json" , "combine" , "language =" ]




# try:
#     # Parsing argument
#     arguments, values = getopt.getopt(argumentList, options, long_options)
    
#     # checking each argument
#     for currentArgument, currentValue in arguments:
        
#         if currentArgument in ("-t", "--generate_txt"):
#             generate_txt = True
            
#         elif currentArgument in ("-o", "--output_dir"):
#             output_dir = currentValue

#         elif currentArgument in ("-i", "--data_loc"):
#             data_loc = currentValue

#         elif currentArgument in ("-d", "--generate_dataset"):
#             generate_dataset = True
            
             
#         elif currentArgument in ("-j", "--generate_json"):
#             generate_json = True
            
        
#         elif currentArgument in ("-c", "--combine"):
#             combine = True

#         elif currentArgument in ("-l", "--language"):
#             lang = currentValue

# except getopt.error as err:
#     # output error, and return with an error code
#     print (str(err))
#   # json file argument

# print("start generation")
# # Open the test dataset human translation file and detokenize the references
if __name__ == '__main__':
    if args.output_dir and not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)
# print(*args)
generate_data(**vars(args))
