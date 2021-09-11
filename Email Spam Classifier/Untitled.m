vocabList = getVocabList();
vocabList;
s='hello';
%strcmp(s,vocabList)==1
for i=1:length(vocabList)
    if strcmp(s,vocabList(i))==1
  i
    end
end
