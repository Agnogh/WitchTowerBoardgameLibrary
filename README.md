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

  The long-term idea behind the project is closer to a library or lending system than an online shop. Although some shop-like features are currently used in the layout, the intended purpose is not selling games, but helping users track, reserve, and borrow them.

  The main purpose of the site is to make game selection easier and faster. Instead of spending time during a gathering deciding what to play, users can search, filter, and review the available games beforehand. The site also helps communicate whether a game is currently available, reserved, or unavailable.

  Witch Tower Boardgame Library is a full-stack web application designed to act as a shared board game database for a small group of users, such as family members or close friends. Its purpose is to let users see what board games are available, which games are currently lent out, and which games may be reserved for future play sessions.


  ### 1.2 User Goals

  The main goals for the user are:

  - to browse a library of available board games
  - to see which games are currently available and which are already lent out
  - to search and filter games by useful criteria such as player count, play time, age suitability, and category
  - to view detailed information about each game
  - to read and write reviews for games
  - to decide more easily which game to play before meeting up
  - to check whether they need to bring their own games or expansions


  ### 1.3 Site Owner Goals

The main goals for the site owner are:

- to display a personal board game collection in an organised and user-friendly way
- to update the collection when games are added, changed, or removed
- to let visitors quickly understand what games are available
- to reduce time spent deciding what to play during in-person gatherings
- to support a system where games may later be reserved, borrowed, or tracked more clearly
- to track which games are available and which are currently borrowed
- to support planning and organising gaming nights more efficiently
- to provide useful information about each game, including stock/availability and user reviews


  ### 1.4 Target Audience

The target audience for this project is mainly a small, familiar group of users, such as family members and close friends who regularly meet to play board games.

- friends or groups planning to meet and play board games
- people who want to see what games are available before visiting
- users who want to compare games by number of players, play time, and other features 
- returning users who want to leave feedback or reviews on games they have played



## 3. Agile Planning

### 3.1 Project Board
The project was planned and tracked using a GitHub Project board. This board was used to organise development tasks, monitor progress, and keep the work structured throughout the build.

A simple workflow was used to move tasks through the project lifecycle:
- **Backlog / To Do**
- **In Progress**
- **Done**

![Responsive preview image of starting progress here]


![Responsive preview image of mid progess here]


![Responsive preview image of Completed tasks here]

This made it easier to separate planned work from active work and completed functionality.

### 3.2 Development Approach
The project was developed using an Agile approach, with the work being broken into smaller and more manageable steps rather than attempting to build everything at once.

The project originally began as an idea for a friend who wanted a webpage for managing and showing her board game library. As development progressed, the project was adjusted so that required portfolio project features could be built into that original idea. This meant balancing the real-life purpose of the website with the mandatory technical requirements of the assessment.

Core browsing and filtering features were prioritised first, followed by responsive layout improvements, authentication, front-end review CRUD, user permissions, and user feedback messages. Documentation, deployment preparation, and final testing were planned as later stages of the project.


### 3.3 Epics
The project board was organised into larger feature areas in the form of epics. These epics helped define the main structure of the project and separate core features from future ideas.

Examples of epics used during planning included:
- Navigation & Layout
- Game Library / Catalogue
- Game Details
- User Accounts & Authentication
- Reviews & User Feedback
- Deployment & Documentation
- Events
- Contact Page
- Rewards & Vouchers (Post-MVP)

This structure helped keep the project organised and allowed clear distinction between MVP features and future improvements.


### 3.4 User Stories
Each epic was supported by user stories written from the perspective of the user. This helped keep the project focused on practical user needs rather than only technical tasks.

Examples of user stories included:
- As a visitor, I want to browse a list of games so that I can see what is available.
- As a visitor, I want to view a game’s details so that I can decide whether it suits my group.
- As a logged-in user, I want to sign up, log in, and log out so that I can access member-only features.
- As a logged-in user, I want to leave, edit, and delete my own review so that I can manage my feedback on games.

Using user stories helped ensure that features were built with purpose and tied back to the intended audience.


### 3.5 Task Breakdown
The user stories were then broken down into smaller practical development tasks. This made the project easier to build step by step and made progress easier to track on the GitHub board.

Examples of tasks included:
- creating the game model
- creating the base layout template
- adding navigation links
- displaying login state in the header
- creating the review model
- creating the review form
- implementing review CRUD on the game detail page
- restricting review edit/delete actions to the review owner
- adding user feedback messages for authentication and review actions
- improving the responsive game list layout
- preparing settings for deployment with environment variables

This task-based approach helped turn larger features into smaller achievable pieces of work.


### 3.6 Prioritisation
The project was planned around a mixture of core functionality, user value, and assessment requirements.

Priority was given to:
- game browsing and filtering
- game detail pages
- responsive layout
- authentication
- review CRUD
- permissions and user feedback

Some features, such as Events, Contact, reward systems, and more advanced lending/reservation ideas, were kept as lower-priority or future work. This helped keep the MVP realistic and prevented the scope from growing too large too early.


### 3.7 MVP and Post-MVP Thinking
The project included both MVP and post-MVP planning.

The MVP focused on delivering the main features needed for the current application, including:
- browsing the game library
- filtering and sorting games
- viewing game details
- authentication
- review CRUD
- responsive layout improvements

Post-MVP ideas included:
- events page
- contact page
- reward/voucher functionality
- more advanced reservation or lending tracking
- improvements such as dynamic category counts and additional UI polish

This separation helped keep the project manageable while still allowing room for future expansion.


## 4. Data Model
### 4.1 Game Model

The Game model is the central model of the application. It represents one board game in the library and stores the main information users need in order to browse, compare, and choose games.

#### Key fields include:

- title
- slug
- tagline
- short description
- full description
- price
- stock
- minimum and maximum players
- minimum and maximum play time
- recommended age
- publisher
- designer
- category
- SKU
- created and updated timestamps

This model exists to give users a structured way to explore the available board games and to support filtering, sorting, and detailed game pages.

The game catalogue is managed through Django Admin, allowing the site owner to add, update, and maintain game records, including stock and descriptive information.

### 4.2 Category Model

The Category model is used to group games into organized categories such as strategy, family, or similar groupings.

Key fields include:

- name
- slug

This model improves navigation and filtering by allowing users to browse games by category. It also supports cleaner URLs and more structured organization of the game library.

### 4.3 Review Model

The Review model allows authenticated users to leave feedback on a game.

#### Key fields include:

- linked game
- linked user
- rating
- comment
- created timestamp
- updated timestamp

This model was added to provide front-end CRUD functionality. Logged-in users can create, read, update, and delete their own reviews directly from the site without using the Django admin panel.

The review model also includes a restriction that allows one user to leave only one review per game. This helps keep feedback clear and prevents duplicate reviews from the same user for the same game.

### 4.4 Relationships Between Models

The models in the project are connected in the following way:

- one Category can contain many Games
- one Game can belong to one Category
- one Game can have many Reviews
- one User can write many Reviews
- one User can leave only one Review per Game

These relationships support the main busines logic of the application by allowing games to be grouped, displayed in detail, and reviewed by authenticated users.


## 5. Features

### 5.1 Home Page

![Home Page image here]

The Home Page acts as the main entry point of the application. It provides users with a simple starting hub from which they can navigate to the main parts of the site, such as the game list, authentication pages, and other planned sections such as Events and Contact.

Its purpose is to give users a clear first step into the application and make navigation easier across 

### 5.2 Game List Page

![Game list image here]

The Game List Page displays the collection of board games available in the library. It is one of the main functional pages of the project and allows users to browse the current collection in an organised way.

This page includes filters, sorting options, active filter chips, and pagination. Users can narrow down the results based on their needs and then apply the selected filters using the **Apply Filters** button.

A deliberate design decision was made to apply filters only when the user clicks **Apply Filters**, rather than updating results instantly on every field change. This was done to keep the experience more predictable for the user and to avoid unnecessary repeated page reloads while multiple filters are being adjusted.

### 5.3 Filtering and Sorting

![Filtering and sorting image here]

Filtering and sorting form one of the most important features of the application. This is the area where users can narrow down the game collection and focus only on games that suit their current needs.

Users can filter games by:
- title search
- stock availability
- number of players
- exact player count
- play time
- age suitability
- category

Users can also sort the results by:
- title
- price
- newest entries

This feature is central to the purpose of the project, because it helps users decide in advance what to play based on group size, available time, and other practical criteria.

### 5.4 Game Detail Page

![Game Details image here]

The Game Detail Page gives the user more detailed information about a selected game. This is where users can spend time learning about a game before deciding whether it is suitable for their group or event.

The page includes information such as:
- title
- tagline
- price
- stock status
- player information
- play time
- age suitability
- description
- box contents
- game details such as publisher, designer, category, and SKU

This page supports the project goal of helping users make decisions before meeting in person, instead of spending time choosing a game during the event itself.


### 5.5 Authentication

![Authentication image here]

Authentication allows users to sign up, log in, and log out of the site. This creates a distinction between general visitors and authenticated users.

Any visitor can browse the available games, but only registered and logged-in users can interact with the review system. This helps create a more controlled and accountable environment for user-generated content.

Authentication is also important for ownership-based permissions, as it ensures that users can only edit or delete their own reviews.


### 5.6 Review CRUD

![Review CRUD image here]

The review system provides full front-end CRUD functionality for authenticated users.

Logged-in users can:
- create a review
- read reviews left by other users
- update their own review
- delete their own review

Each user is limited to one review per game. This was a deliberate design choice to keep feedback clear, reduce clutter, and prevent duplicate reviews for the same game by the same person.

This feature is one of the most important parts of the project because it satisfies the front-end CRUD requirement while also adding real value for users.


### 5.7 User Feedback Messages

![User feedback image here]

The application provides clear feedback messages to users after important actions.

Users receive confirmation messages for actions such as:
- signing up
- logging in
- logging out
- adding a review
- editing a review
- deleting a review

This improves usability by clearly informing users that their action was completed successfully. It also supports better overall UX by reducing uncertainty after important interactions.