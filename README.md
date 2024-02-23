# Creating LlamaIndex EmbeddingQAFinetuneDataset compatible inputs
<p align = "center">
  <img src = "https://github.com/SwamiKannan/Creating-Llamaindex-EmbeddingQAFinetuneDataset-for-Finetuning-Embeddings/blob/main/images/cover.png", width = 60%>
</p>

## Introduction
An important lever to improve RAG performance is to finetune the embeddings model itself. The embeddings model is used to tokenize and "embed" the input text into the vecctorstore. Hence, the better your embeddings model aligns to the data and terminology of your domain, the better the RAG will be in extracting the correct documents to be passed to your LLM model. 

LlamaIndex provides a robust library called llama_index.finetuning to accomplish this.For this library to work, we have to instantiate a EmbeddingQAFinetuneDataset object from our data. One way to instantiate this object is using a JSON file in a specific format.

The data in the JSON file is typically a question-answer dataset or a question-reference dataset (where the answer is not explicitly provided but the reference data in which the answer resides is provided. This is an even more powerful paradigm for RAG models since it is the basis on which they work). All guides (including the llamaindex documentation) create this data (question - reference sets from a link or html content using generate_qa_embedding_pairs() i.e. the input is a text file of all the relevant content and the LLM itself creates question-reference datasets. However, <b>this is not suitable for a couple of reasons:</b>
<ol>
<li>Generate_qa_embedding_pairs() uses an LLM to create these question - reference sets. This may be either:
  <ul>
 <li>Expensive (OpenAI or Cohere) or computationally intensive (multi-billion parameter open source models) for large amounts of content e.g. 50K pages in Wikipedia</li>
<li>May not necessarily be coherent question - reference sets depending on the complexity of the model or the nuance in the data </li></ul></li>
<li>There are several open source datasets on HuggingFace which may be both nuanced and relevant to the domain we are targetting. Not leveraging this data would be a massive opportunity loss
</li>
</ol>
Hence, this code converts a standard dictionary (in a provided format) containing question / answers or question / context details into a json file that can be used to finetune your embedding model using LlamaIndex's finetune library

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
