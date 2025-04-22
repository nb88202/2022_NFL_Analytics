# 2022_NFL_Analytics

## Business Goal
This project will analyze 2022 NFL Data in order to extract insights on player performance generally and among specific players.

## Data Source

Dimension tables include:
   Games.csv [gameId, season, week, gameDate, gameTime, visitorTeam, homeTeam, homeFinalScore, visitorFinalScore]
   Players.csv [nflId, height, weight, birthDate, collegeName, position, displayName]

Fact tables include:
   Plays.csv [playId,	ballCarrierId,	ballCarrierDisplayName,	playDescription,	quarter,	down	,yardsToGo	,possessionTeam,	defensiveTeam	yardlineSide,	yardlineNumber,	gameClock,	preSnapHomeScore,	preSnapVisitorScore,	passResult,	passLength,	penaltyYards	prePenaltyPlayResult,	playResult,	playNullifiedByPenalty	,absoluteYardlineNumber	,offenseFormation,	defendersInTheBox	,passProbability	,preSnapHomeTeamWinProbability,	preSnapVisitorTeamWinProbability,	homeTeamWinProbabilityAdded	,visitorTeamWinProbilityAdded	,expectedPoints,	expectedPointsAdded	,foulName1	,foulName2,	foulNFLId1	,foulNFLId2]

   Tackles.csv [gameId, playId,nflId, tackle, assist, forcedFumble,pff_missedTackle ]

## Tools Used
   All work will be imported and created in PowerBI

## Workflow and Logic
   
   1. Clean and create tables.
   Cleaning csv files includes Games_cleaning.py  ->  remove unnecessary columns while adding new columns of home_winner (bool), Id of game winner and Id of loser for summary later. 

      Cleaning players.csv -> remove unnecessary columns

      Create new tables in PowerBi using DAX 

   2. Set up a Data Model in PowerBi

![alt text](images/dm.png)

   3. Extract Teams data in PowerBI  with slicers for each team and each week (Overview)

![alt text](images/te.png)

Extract team data by yards gained per game against opponent for each team, slicer by team and by quarter of game(Offense Team Data) ---todo - add score and win or loss to each bar

![alt text](images/od.png)

![alt text](images/slice.png)
   
Extract Offensive Player data with slicers by team. 

![alt text](images/op.png)

![alt text](images/op1.png)
   

