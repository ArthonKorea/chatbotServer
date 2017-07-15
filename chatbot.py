# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:17:08 2017
@author: Life Semantics
"""

import pandas as pd
import http.server
import socketserver
from konlpy.tag import Kkma
from konlpy.utils import pprint

class bot(object):
    def __init__(self):
        self.kkma = Kkma()
        self.Prime_Word = pd.read_csv('1. Word Table.csv',encoding = 'CP949')
        self.Answer_DB =pd.read_csv('2. Info DB.csv',encoding = 'CP949')
        self.Sentence_DB = pd.read_csv('3. Info DB Sentence.csv',encoding = 'CP949')


    def Conversation(self,chat_text):
        Analized_Nouns = self.kkma.nouns(chat_text)
        return Analized_Nouns


    def Translating_Word(self, Words):
        for i in range(len(Words)):
            for j in range(len(self.Prime_Word)):
                if Words[i] == self.Prime_Word.loc[j, 'Word']:
                    Words[i] = self.Prime_Word.loc[j, 'Mapping']
        return Words

    def Answering(self, Words):
        for i in range(len(Words)):
            for j in range(len(self.Answer_DB)):
                if Words[i] == self.Answer_DB.loc[j, '항목']:
                    Answer_Sentence = self.Sentence_DB.loc[j, '문장1']
                    Answer_Sentence = Answer_Sentence.replace('[' + self.Answer_DB.loc[j, '항목'] + ']',
                                                              self.Answer_DB.loc[j, '#1'])
                    return Answer_Sentence
        return '없음'


#Start Main




#End Main







