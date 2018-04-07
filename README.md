# Classwork1_python
Запуск через коммандную строку: python3 Trimmomatic.py 10 5 4 35 /test_classwork2.fastq /test_classwork2_out.fastq
(После названия скрипта через пробел необходимо ввести последовательно: headcrop, tailcrop, window length, quality threshold, input file name with path, output file name with path).
При вызове help выдаст описание параметров:

python3 Trimmomatic.py -h
usage: Trimmomatic.py [-h] Int Int Int Int fastq fastq

Lets trimmomate your reads!

positional arguments:

  Int         Length of the sequence to crop from the head of the read
  
  Int         Length of the sequence to crop from the tail of the read
  
  Int         Length of the clipping window = lengthh of the sequence for estimateion of an average quality
              
  Int         The threshold of an average quality of the clipping window
  
  fastq       The input fastq file
  
  fastq       The output fastq file

**описание кода**
