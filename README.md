# Creating EmbeddingQAFinetuneDataset.from_json() compatible json file
<p align = "center">
  <img src = "https://github.com/SwamiKannan/Creating-Llamaindex-EmbeddingQAFinetuneDataset-for-Finetuning-Embeddings/blob/main/cover.png", width = 60%>
</p>
An important activity to improve RAG performance is to finetune the embeddings model itself to suit the domain that your RAG would capture the data of. LlamaIndex provides a robust library called llama_index.finetuning to accomplish this.
For this library to work, we have to instantiate a EmbeddingQAFinetuneDataset object from our data. This is required in  a json file of a specific format. 

All guides (including the llamaindex documentation) create question - reference sets from a link or html content using generate_qa_embedding_pairs(). However, this is not suitable for a couple of reasons:
<ol>

<li>Generate_qa_embedding_pairs() uses an LLM to create these question - reference sets. This may be either:
  <ul>
 <li>Expensive (OpenAI or Cohere) or computationally intensive (multi-billion parameter open source models) for large amounts of content e.g. 50K pages in Wikipedia</li>
<li>May not necessarily be coherent question - reference sets depending on the complexity of the model or the nuance in the data </li></ul></li>
<li>There are several open source datasets on HuggingFace which may be both nuanced and relevant to the domain we are targetting. Not leveraging this data would be a massive opportunity loss
</li>
</ol>
