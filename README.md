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
   Cleaning csv files includes Games_cleaning.py  ->  remove unnecessary columns while adding new columns of home_winner (bool), Id of game winner and Id of loser for summary later. 

   Cleaning players.csv -> remove 

