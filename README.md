# Creating an EmbeddingQAFinetuneDataset.from_json() compatible json file from external datasets
<p align = "center">
  <img src = "https://github.com/SwamiKannan/Creating-Llamaindex-EmbeddingQAFinetuneDataset-for-Finetuning-Embeddings/blob/main/cover.png", width = 60%>
</p>

## Introduction
An important activity to improve RAG performance is to finetune the embeddings model itself to suit the domain that your RAG would capture the data of. LlamaIndex provides a robust library called llama_index.finetuning to accomplish this.
For this library to work, we have to instantiate a EmbeddingQAFinetuneDataset object from our data. This is required in  a json file of a specific format. 

All guides (including the llamaindex documentation) create question - reference sets from a link or html content using generate_qa_embedding_pairs(). However, <b>this is not suitable for a couple of reasons:</b>
<ol>

<li>Generate_qa_embedding_pairs() uses an LLM to create these question - reference sets. This may be either:
  <ul>
 <li>Expensive (OpenAI or Cohere) or computationally intensive (multi-billion parameter open source models) for large amounts of content e.g. 50K pages in Wikipedia</li>
<li>May not necessarily be coherent question - reference sets depending on the complexity of the model or the nuance in the data </li></ul></li>
<li>There are several open source datasets on HuggingFace which may be both nuanced and relevant to the domain we are targetting. Not leveraging this data would be a massive opportunity loss
</li>
</ol>
Hence, this code converts a standard dictionary (in a provided format) containing question / answers or question / context details into a json file that can be used to finetune your embedding model using LlamaIndex's finetune library
<sub>
 Image credit:Base Image  for cover generated using <a href="https://www.segmind.com/models/sdxl1.0-txt2img">Segmind's Stable Diffusion XL 1.0 model</a>
 Prompt: cinematic film still, 4k, realistic, of a man casting spells on documents, Fujifilm XT3, long shot, ((low light:1.4)), landscape , very wide angle shot, somber, vignette, highly detailed, high budget Hollywood movie, bokeh, cinemascope, moody, epic, neon, gorgeous, film grain, grainy
</sub>
