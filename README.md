# Creating LlamaIndex EmbeddingQAFinetuneDataset compatible inputs
<p align = "center">
  <img src = "https://github.com/SwamiKannan/Creating-Llamaindex-EmbeddingQAFinetuneDataset-for-Finetuning-Embeddings/blob/main/images/cover.png", width = 60%>
</p>

## Introduction
An important lever to improve RAG performance is to finetune the embeddings model itself.

The embeddings model is used to tokenize and "embed" the input text into the vectorstore. Hence, the better your embeddings model aligns to the data and terminology of your domain, the better the RAG will be in extracting the correct documents to be passed to your LLM model. 

LlamaIndex provides a robust library called <a href="https://docs.llamaindex.ai/en/stable/optimizing/fine-tuning/fine-tuning.html"><b>llama_index.finetuning</b></a> to accomplish this. To use this library, we have to instantiate a <a href="https://github.com/run-llama/llama_index/blob/main/llama-index-finetuning/llama_index/finetuning/embeddings/common.py">EmbeddingQAFinetuneDataset</a> object from our data. One way to instantiate this object is using a JSON file in a specific format.

The data in the JSON file is typically a question-answer dataset or a question-reference dataset (where the answer is not explicitly provided but the reference data in which the answer resides is provided. This is an even more powerful paradigm for RAG models since it is the basis on which they work). All guides <a href="https://docs.llamaindex.ai/en/stable/examples/finetuning/embeddings/finetune_embedding.html">(including the llamaindex documentation)</a> create this data (question - reference sets from a link or html content using generate_qa_embedding_pairs() i.e. the input is a text file of all the relevant content and the LLM itself creates question-reference datasets. <br>
However, <b>this is not suitable for a couple of reasons:</b>
<ol>
<li>Generate_qa_embedding_pairs() uses an LLM to create these question - reference sets. This may be either:
  <ul>
 <li>Expensive (OpenAI or Cohere) or computationally intensive (multi-billion parameter open source models) for large amounts of content e.g. 50K pages in Wikipedia</li>
<li>May not necessarily be coherent question - reference sets depending on the complexity of the model or the nuance in the data </li></ul></li>
<li>There are several open source datasets on HuggingFace which may be both nuanced and relevant to the domain we are targetting. Not leveraging this data would be a massive opportunity loss
</li>
</ol>
Hence, this repo seeks to leverage external question-answer and question-reference datasets already available on <a href="https://huggingface.co/docs/datasets/index">Huggingface</a> or any other data. The repo takes as input,  a simple dictionary or a json file, in a pre-defined format containing question / answers or question / reference details and transforms it into a EmbeddingQAFinetuneDataset-compatible json file that can, as a downstream activity, be used to finetune your embedding model.

## Usage
1. In the main.py file, review the create_dataset() function to understand the structure of the file that needs to be provided as an input.
2. Create your json input file in the format as in create_dataset(). You can also refer to the structure below in the "Input template" section
3. Run the following from a command prompt:
   
   ```
   python main.py <filename>
   ```
5. The code also prints out the number of items in your json file to confirm processing.
   
## Image credits:
 <b>Image credit: </b>Base Image  for cover generated using <a href="https://www.segmind.com/models/sdxl1.0-txt2img">Segmind's Stable Diffusion XL 1.0 model</a> <br>
 <b>Prompt: </b>cinematic film still, 4k, realistic, of a man casting spells on documents, Fujifilm XT3, long shot, ((low light:1.4)), landscape , very wide angle shot, somber, vignette, highly detailed, high budget Hollywood movie, bokeh, cinemascope, moody, epic, neon, gorgeous, film grain, grainy
</sub>
