# Dataset-for-statement-level-code-summarization
This dataset is built specifically for research on statement-level code summarization, based on the CodeSearchNet dataset with filtering and selection. It includes two popular languages, Java and Python, and consists of 12 parameters. The dataset contains a test set, training set, and validation set.
The parameters of the dataset are as follows:

code：Statement-level code

comments：Statement-level code comments

lines：Lines of code itemize

repo： the owner/repo

path：the full path to the original file 

func_name：the function or method name 

original_string：the raw string before tokenization or parsing 

language：the programming language

Allcodes:the part of the original\_string that is code

code_tokens/function_tokens:tokenized version of code

docstring:the top-level comment or docstring, if it exists in the original string

docstring_tokens:tokenized version of docstring
