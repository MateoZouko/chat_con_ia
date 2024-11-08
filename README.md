# Chat con IA

## Descripción
Este proyecto es una implementación de un chat con IA utilizando **Python** y **Flask**, en el cual tuve que utilizar varias tecnologías específicas como **LangChain**, **Llama 2**, y **FAISS** para proporcionar respuestas inteligentes basadas en el contexto de documentos cargados y vectorizados. El objetivo principal es crear un sistema capaz de extraer información relevante de documentos vectorizados para responder a prompts de manera precisa y en base al contexto.

## Tecnologías Utilizadas
- **Flask**: Framework web para manejar rutas y la lógica del servidor.
- **LangChain**: Herramienta para la carga y procesamiento de documentos.
- **Llama 2**: Modelo de lenguaje para la generación de respuestas.
- **SentenceTransformers**: Utilizado para generar embeddings básicos a partir de textos.
- **FAISS**: Base de datos vectorial para almacenamiento y búsqueda eficiente de los embeddings.

## Funcionalidades
- **Conexión con Llama 2** para obtener respuestas basadas en texto.
- **Carga de documentos** usando LangChain para preparar el contexto con el cual quieremos obtener las respuestas.
- **Vectorización** mediante SentenceTransformers para convertir textos en vectores de embeddings.
- **Almacenamiento y búsqueda** de embeddings usando FAISS para consultas rápidas.
- **Respuestas contextuales** basadas en los documentos vectorizados para preguntas del usuario.

## Rutas
- **`/api/chat/ask`**: Ruta para interactuar con el chatbot y recibir respuestas contextuales.
- **`/api/chat/add_document`**: Ruta para cargar documentos y realizar su vectorización.

## Desafíos y Aprendizajes
Durante el desarrollo del proyecto, enfrenté varios desafíos técnicos, entre ellos la dificultad de integrar el modelo llama 2, pero principalmente el mayor desafío fue la optimizacion de la vectorización y la carga y procesamiento de documentos. Esto debido a que tuve que hacerlo con tecnologías que no conocia previamente en un tiempo acotado. Esto hizo al proyecto una experiencia muy valiosa a la hora de aprender sobre la implementacion de ia y modelos de lenguaje, pero principalmente a adaptarse y aprender rapidamente tecnologías a las que no estas acostumbrado a la hora de enfrentar un proyecto nuevo.
