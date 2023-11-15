#!/usr/bin/env python
# coding: utf-8

# C:\Users\Admin

# In[10]:


get_ipython().system('pip install gtts')


# In[11]:


get_ipython().system('pip install torch')
get_ipython().system('pip install torchaudio')


# In[12]:


import torch
import torchaudio


# In[13]:


from gtts import gTTS


# In[14]:


language ="en"
text = "hi hello udhaya "

speech = gTTS(text=text,lang=language,slow= False,tld="com.au")
speech.save("speech0555.mp3")


# In[1]:


get_ipython().system('pip install transformers')
get_ipython().system('pip install huggingface transformers')


# In[1]:


from transformers import pipeline


# In[ ]:


get_ipython().system('conda install -c anaconda ffmpeg')


# In[ ]:


get_ipython().system('pip install ffmpeg-python')


# In[18]:


STT = pipeline("automatic-speech-recognition")

x = STT("speech0555.mp3")
print(x)

