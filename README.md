# WitchTowerBoardgameLibrary
Repo for gameboard shop, rental and workshop site


![Responsive preview image here]

## Table of Contents
- [1. Project Overview](#1-project-overview)
  - [1.1 Purpose](#11-purpose)
  - [1.2 User Goals](#12-user-goals)
  - [1.3 Site Owner Goals](#13-site-owner-goals)
  - [1.4 Target Audience](#14-target-audience)
- [2. UX / Design](#2-ux--design)
  - [2.1 Design Goals](#21-design-goals)
  - [2.2 Layout and Structure](#22-layout-and-structure)
  - [2.3 Colour and Visual Style](#23-colour-and-visual-style)
  - [2.4 Navigation](#24-navigation)
  - [2.5 Wireframes / Mockups / Planning Notes](#25-wireframes--mockups--planning-notes)
- [3. Agile Planning](#3-agile-planning)
  - [3.1 Project Board](#31-project-board)
  - [3.2 Epics](#32-epics)
  - [3.3 User Stories](#33-user-stories)
  - [3.4 Task Breakdown](#34-task-breakdown)
- [4. Data Model](#4-data-model)
  - [4.1 Game Model](#41-game-model)
  - [4.2 Category Model](#42-category-model)
  - [4.3 Review Model](#43-review-model)
  - [4.4 Relationships Between Models](#44-relationships-between-models)
- [5. Features](#5-features)
  - [5.1 Home Page](#51-home-page)
  - [5.2 Game List Page](#52-game-list-page)
  - [5.3 Filtering and Sorting](#53-filtering-and-sorting)
  - [5.4 Game Detail Page](#54-game-detail-page)
  - [5.5 Authentication](#55-authentication)
  - [5.6 Review CRUD](#56-review-crud)
  - [5.7 User Feedback Messages](#57-user-feedback-messages)
- [6. Technologies Used](#6-technologies-used)
  - [6.1 Languages](#61-languages)
  - [6.2 Frameworks and Libraries](#62-frameworks-and-libraries)
  - [6.3 Tools and Software](#63-tools-and-software)
- [7. Testing](#7-testing)
  - [7.1 Manual Testing](#71-manual-testing)
  - [7.2 Validation Testing](#72-validation-testing)
  - [7.3 Bugs Fixed](#73-bugs-fixed)
  - [7.4 Remaining Bugs / Known Issues](#74-remaining-bugs--known-issues)
- [8. Deployment](#8-deployment)
  - [8.1 Local Development](#81-local-development)
  - [8.2 Deployment Steps](#82-deployment-steps)
  - [8.3 Environment Variables](#83-environment-variables)
  - [8.4 Security Notes](#84-security-notes)
- [9. Future Improvements](#9-future-improvements)
- [10. Credits](#10-credits)
  - [10.1 Code / Learning References](#101-code--learning-references)
  - [10.2 Media / Content](#102-media--content)
  - [10.3 Acknowledgements](#103-acknowledgements)


## 1. Project Overview

  ### 1.1 Purpose

  Witch Tower Boardgame Library is a full-stack web aplication designed to display a personal library (of my friend Katarina) of board games in a clear and structrued way. The project was created to help users (her frends and family members) browse available games, learn more about them, and decide in advance what they would like to play before meeting in person (and sometimes spending time deciding on what game to play).

  Also it will help decide if game is even available and should friends bring their own copy, or addonns (DLC-s), if the number of people joining is supported for the game they want ot play.

  The long-term idea behind the project is closer to a library or lending system than an online shop. Although some shop-like featurs are currently used in the layout, the intended purpose is not selling games, but helping users track, reserve, and borrow them.

  The main purpose of the site is to make game selection easier and faster. Instead of spending time during a gathering deciding what to play, users can search, filter, and review the available games beforehand. The site also helps communicate whether a game is currently available, reserved, or unavailable.

  Witch Tower Boardgame Library is a full-stack web application designed to act as a shared board game database for a small group of users, such as family members or close friends. Its purpose is to let users see what board games are available, which games are currently lent out, and which games may be reserved for future play sessions.


  ### 1.2 User Goals

  The main goals for the user are:

  - to browse a library of available board games
  - to see which games are curently available and which are already lent out
  - to search and filter games by useful criteria such as player count, play time, age sutability, and category
  - to view detaield information about each game
  - to read and write revievs for games
  - to decide more easily which game to play before meeting up
  - to check weather they need to bring their own games or expansions


  ### 1.3 Site Ownr Goals

The main goals for the site owner are:

- to display a personal board game collection in an organised and user-friendly way
- to update collection when games are added, changed or removedž
-  -to let visitors quickly understand what games are available
- to reduce time spent deciding what to play during in-person gatherings
- to support a system where games may later be reserved, borrowed, or tracked more clearly
- to treck which games are available and which are currently borrowed
- to support planning and organising gaming nights more efficiently
- to provide usful information about each game, including stock/availability and user reviews


  ### 1.4 Target Audience

The target audience for this project is mainly a small, familiar group off users, such as family members and close friends who regularly meet to play board games.

- friends or grups planning to meet and play board games
- people who want to see what games are available before visiting
- users who want to compare games by number of players, play time, and other features- 
- returning usres who want to leave feedback or reviews on games they have played



## 4. Data Model
### 4.1 Game Model

Game model is the central model of the application. It prepresents one board game in the library and stores the main infromation users need in order to browse, compare, and choose games.

#### Key fields include:

- title
- slug
- tagline
- short description
- full description
 - price
-stock
-  minimum and maximum players
- minimum and maximum play time
- recommended age
- publisher
- designer
- category
- SKU
- created and updated timestamps

This model exists to give users structured way to explore the available board games and to support filtering, sorting, and detailwd game pages.

### 4.2 Category Model

The Category model is used to group games into organized categories such as strategy, family, or similar groupings.

Key fields include:

- name
- slug

This model impruves navigation and filtering by allowing users to browse games by category. It also supports cleaner URLs and more structured organization of the game library.

### 4.3 Review Model

The Review model allows authenticated users to leave feedback on a game.

#### Key fields include:

- linked game
- linked user
- rating
- comment
- created timestamp
- updated timestamp

This model was added to provide front-end CRUD functionallity. Logged-in users can create, read, update, and delete their own reviews directly from the site without using the Django admin panel.

The review model also includes a restriction that allows one user to leave one one review per game. This helps keep feedback clear and prevents duplicate reviews from the same user for the same game.

### 4.4 Relationshihps Between Models

The models in the project are conencted in the following way:

- one Category can contain many Games
- one Game can belong to one Category
- one Game can have many Reviews
- -one User can write many Reviews
 -one User can leave only one Review per Game

These relationships support the main business logic of the application by allowing games to be grouped, displayed in detail, and reviewed by autenticated users.


## 5. Features

### 5.1 Home Page

![Home Page image here]

Serves as a base where the the links are for Game lists, sign in/out/sign up.
Contact page, Event page. It is a hub from where we progress and navigate

### 5.2 Game List Page

![Game list image here]

List of all the games and filters. Applying filters and selecting "Apply FIlters" updates search results
Idea was that filters are applied only after "Apply Filters" button is applied to take to load of constant results update as user chanegs multiple searches.

It might be tediosu for user as well as memory cunsimuing 

### 5.3 Filtering and Sorting

![Filtering and sorting image here]

Filztering is the corner stone of games. TGhsi si where the magic happens and wherre users will spend most of the time

### 5.4 Game Detail Page

![Game Deetails image here]

This si where user will spend time browing through the games and finding out about the game itself that potential player will play

### 5.5 Authentication

![Authentication image here]

To filter just average users and members, auth method is provided. Everyone can sign up, and automatically write reviews and pick games. BUt this is possible onlly for sign up users

### 5.6 Review CRUD

![Review CRUD image here]

Abbility to add review and edit it (and even delete it). Only one review per user per game is possible tfor logivcal reasons and as well to reduce clutter

### 5.7 User Feedback Messages

![User feedback image here]

User woill be notified if their auth action was sucessfull as well as their comments and review status as Add, edited and deleted review.