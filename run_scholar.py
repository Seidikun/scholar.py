# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:01:26 2020

@author: seidi
"""

import scholar 
import random
import time

querier = scholar.ScholarQuerier()
settings = scholar.ScholarSettings()
querier.apply_settings(settings)

query = scholar.SearchScholarQuery()
query.set_words("computing")
query.set_num_page_results(2)

# =============================================================================
# for s in range(0,1000,20):
# =============================================================================
# =============================================================================
#   query.set_start(s)
# =============================================================================
querier.send_query(query)

articles = querier.articles
for art in articles:
    print(art.as_csv() + '\n')
      
# =============================================================================
#   time_wait = random.randint(2,5)
#   time.sleep(time_wait)
#       
# =============================================================================
