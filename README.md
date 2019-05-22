# AutoGeneSequenceDownloader
A python script help you download a large number of gene sequences from NCBI
一个帮助你从NCBI批量下载基因序列的python脚本。
How to use that?
如何使用？
First, you should make sure you have python3 and Biopython module.
首先你应该确保安装了python3以及biopython模块。
Second, you should have a txt file with each gene reference for a line.
其次你应该有一个记录了基因索引的txt文件，其中每行一个基因序列索引。
Then just run the script and follow the instructions.
然后运行脚本即可。
Don't worry too much about the line break in the txt file, the script has good robustness.
不必太担心空格以及换行符，这个脚本有一定的容错性。
The script will automatically ignore the invalid references.
脚本会直接忽视无效的索引。
