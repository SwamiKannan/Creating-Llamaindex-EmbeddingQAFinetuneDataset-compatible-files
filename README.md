# Creating EmbeddingQAFinetuneDataset.from_json() compatible json file

An important activity to improve RAG performance is to finetune the embeddings model itself to suit the domain that your RAG would capture the data of. LlamaIndex provides a robust library called llama_index.finetuning to accomplish this.
For this library to work, we have to instantiate a EmbeddingQAFinetuneDataset object from our data. This is required in  a json file of a specific format. 

This format is not clearly described as most tutorials create QA embeddings from 
