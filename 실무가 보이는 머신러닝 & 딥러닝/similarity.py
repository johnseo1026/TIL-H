# -*- coding: utf-8 -*-

import sys
from gensim.models import word2vec

# 첫 번째 파라미터는 사용할 모델 파일 이름
model   = word2vec.Word2Vec.load(sys.argv[1])
results = model.most_similar(positive=['woman','king'],
		negative=['man'], topn=1)

for result in results:
    print(result[0], '\t', result[1])