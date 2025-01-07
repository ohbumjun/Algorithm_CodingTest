// https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=cpp

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;
vector<string> totGenres;
vector<int> totPlays;

bool comparePlay(int aIdx, int bIdx)
{
    return totPlays[aIdx] > totPlays[bIdx];
}

struct Genre
{
    int totPlay = 0;        // 해당 값을 기준으로 sort
    vector<int> idxs;   // 여기도, sort 시키기.
    
    void sort()
    {
        std::sort(idxs.begin(), idxs.end(), comparePlay);
    }
};
bool compareGenre(Genre* aGenre, Genre* bGenre)
{
    // cout << aGenre->totPlay << endl;
    // cout << bGenre->totPlay << endl;
    return aGenre->totPlay > bGenre->totPlay;
}


vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    vector<Genre*> genresList;
    unordered_map<string, Genre*> genreMap;
    totGenres = genres; totPlays = plays;
    
    for (int i = 0; i < genres.size(); ++i)
    {
        if (genreMap.find(genres[i]) == genreMap.end())
            genreMap[genres[i]] = new Genre;
        Genre* curGenre = genreMap[genres[i]];
        curGenre->totPlay += plays[i];
        curGenre->idxs.push_back(i);
        
        // cout << "genre : "  << genres[i] << endl;
        // cout << "play  : "  << plays[i] << endl;
        // cout << "totPlay  : " << curGenre->totPlay << endl;
    }
    
    for (const auto& info : genreMap) 
    {
        info.second->sort();
        genresList.push_back(info.second);
    }
    
    sort(genresList.begin(), genresList.end(), compareGenre);
    
    for (const Genre* genre : genresList)
    {
        int size = genre->idxs.size() < 2 ? genre->idxs.size() : 2;
        for (int i = 0; i < size; ++i)
        {
            answer.push_back(genre->idxs[i]);
        }
    }
    
    return answer;
}