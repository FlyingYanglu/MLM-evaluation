# MLM-evaluation

This is a repo used for evaluation of Masked Language Models.

Metircs:

 1.Extrinsic:
 
   - Mask filling task
   - Sentence Clustering Task
   
 2. Intrinsic (Under Construction):
 
   - pseudo-log-likelihood scores (PLLs)
   - Pseudo-perplexity (PPPL)

**For Mask filling task**

Currently only char level masking task is involved. Later on, we will support any tokenizer to generate masked sentences. 

Step 1: Generate Dataset

><sub> Note: if you only want to test your model on the data from Otaku benchmark and your tokenizer is char-level masking, 
 you can skip this part, as I've generated the dataset for you in the char_mask_task folder. Skip to step 2. </sub>
 
 >To generate custom dataset for your task, 
 
 >>1st install datasets library from Huggingface:
 
 >>You can install it by running `pip install datasets` in a conda environment.
 
 >>2nd: clone this repo and navigate to char_mask_task folder. Create a folder to contain your dataset files.
 
 >>3rd: you need to put your japanese text in a .txt file with one sentence per line. Remember the path of your japanese .txt file
 
 >>4th: go to the folder you created under char_mask_task folder, run `python ../generate.py <Your japanese .txt path>`. Then you should see the dataset generated under the current folder. 
 
 
 Step 2: Evaluate model accuracy
 
 To evaluate your model's mask filling accuracy, you need to load the dataset from the dataset folder. You can do this by `datasets.Dataset.load_from_disk(<Path of the dataset directory>)` 
 
 Then you should see the dataset has three features: 
  
   - masked_sentence contains the masked sentence as a char array. 
   - original_tokens is a list of original tokens in the [mask] location
   - mask is a boolean list specify which index of the char in original sentence is masked.  

You should use your MLM to do this task and predict the token in the [mask] location. Then you can either just compare your pred to 'original_tokens' to get an accuracy score or you can save your prediction for [mask] location in each sentence as a string and write it one string per line to generate a file similar to the original_character.txt under pre generated data.

Then you can run `python calculate_accuracy.py <Path of original_character.txt> <Path of your pred.txt>` to get a score 
 
 
 
 
 
 
