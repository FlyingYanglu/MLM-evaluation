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

You should use your MLM to do this task and predict the token in the [mask] location. Then you can either 
   - just compare your pred to 'original_tokens' to get an accuracy score 
   - or you can save your prediction for [mask] location in each sentence as a string and write it one string per line to generate a file similar to the original_character.txt under pre generated data.

Then you can run `python calculate_accuracy.py <Path of original_character.txt> <Path of your pred.txt>` to get a score 
 
 
 **For Sentence Clustering task**
 <sub> Note: This is an adaptation from Evaluation of Pretrained BERT Model by Using Sentence Clusterin by Naoki et al.</sub>
 
 1. For Sentence Clustering Task. You should run your LM through all datasets you want to test clustering on. The dataset should contain sentences from different domain, e.g. medicine journal and fashion journal, so that we can test how well the Bert perform on finding adequate embedding for sentence from different domain. <br> In our scenario, you can use the data from three domains in the Otaku Benchmark dataset. 
 
 2. You should run BERT to generate representation for each japanese original txt file in the data. 


 3. Then you should extract the CLS embedding for each sentence, as we will use it as a representation for the whole sentence. Store the CLS embeddings in a json file similar to the example.json file. 
 
 4. Then under the sent_clustering_task directory, run `python 'calculate clustering score'.py example.json` will generate the performance score for your LM.
 
 **For PPL**
 
 Since this is a intrinsic metric, a google sentence piece tokenizer should be provided. The code helps with generating dataset, but it does not handle how you process the dataset. You can generate custom dataset by using prepare_dataset from the util file. Then you need to use your model to predict the masked tokens in the dataset and record the result in the format as described below. 
 ```yaml
{
   'sent_index': [<IDs of the original sentence included in the prepared dataset>], 'target_logit':[<the log probability of the predicted masked token>]
}
```
Then you can use the dataset_to_logitsls to convert this dataset to a list and then feed it to calculate pppl to get a score for your model. 
