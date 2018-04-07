
# coding: utf-8

# In[5]:


from Bio import SeqIO 
import matplotlib.pyplot as plt
import numpy as np
import argparse


# In[6]:


parser = argparse.ArgumentParser(description='Lets trimmomate your reads!')
parser.add_argument('headcrop',  help='Length of the sequence to crop from the head of the read', metavar='Int', type=int, default=0)
parser.add_argument('tailcrop',  help='Length of the sequence to crop from the tail of the read', metavar='Int', type=int, default=0)
parser.add_argument('window_length',  help='Length of the clipping window = lengthh of the sequence for estimateion of an average quality', metavar='Int', type=int, default=1)
parser.add_argument('quality_theshold',  help='The threshold of an average quality of the clipping window', metavar='Int', type=int, default=30)
parser.add_argument('input',  help='The input fastq file', metavar='fastq', type=str, default='')
parser.add_argument('output',  help='The output fastq file', metavar='fastq', type=str, default='')
args = parser.parse_args()


# In[23]:


with open (args.input) as fastq_in:
    with open (args.output, "w") as fastq_out:
        for record in SeqIO.parse(fastq_in, "fastq"):
            flag = 0
            sum_quality = 0
            current_read = record.seq
            current_read_trimmed = str(current_read)[(args.headcrop):(len(current_read)-args.tailcrop)]
            n = len(record.seq)-args.tailcrop-args.window_length+1
            for index in range(args.headcrop,n):
                flag = 0
                current_window = str(record.seq)[index:index+args.window_length]
                current_quality = record.letter_annotations["phred_quality"][index:index+args.window_length]
                for val in current_quality:
                    sum_quality += val
                    
                average_quality = sum_quality/args.window_length
                if average_quality < args.quality_theshold:
                    trim_index = index
                    flag = 1
                    break
            if flag == 0:
                trim_index = len(current_read_trimmed)
            
            new_record = record[args.headcrop:trim_index]
            SeqIO.write(new_record, fastq_out, "fastq")
            

