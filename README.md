# WitchTowerBoardgameLibrary
Repo for a boardgame library, browsing, review, and event planning web application.


![Responsive preview image here]()

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
  - [3.2 Development Approach](#32-development-approach)
  - [3.3 Epics](#33-epics)
  - [3.4 User Stories](#34-user-stories)
  - [3.5 Task Breakdown](#35-task-breakdown)
  - [3.6 Prioritisation](#36-prioritisation)
  - [3.7 MVP and Post-MVP Thinking](#37-mvp-and-post-mvp-thinking)
- [4. Data Model](#4-data-model)
  - [4.1 Game Model](#41-game-model)
  - [4.2 Category Model](#42-category-model)
  - [4.3 Review Model](#43-review-model)
  - [4.4 Event Model](#44-event-model)
  - [4.5 ContactMessage Model](#45-contactmessage-model)
  - [4.6 Relationships Between Models](#46-relationships-between-models)
- [5. Features](#5-features)
  - [5.1 Home Page](#51-home-page)
  - [5.2 Game List Page](#52-game-list-page)
  - [5.3 Filtering and Sorting](#53-filtering-and-sorting)
  - [5.4 Game Detail Page](#54-game-detail-page)
  - [5.5 Authentication](#55-authentication)
  - [5.6 Review CRUD](#56-review-crud)
  - [5.7 User Feedback Messages](#57-user-feedback-messages)
  - [5.8 Contact Page](#58-contact-page)
  - [5.9 Events Page](#59-events-page)
  - [5.10 Placeholder Cart UX](#510-placeholder-cart-ux)
- [6. Technologies Used](#6-technologies-used)
  - [6.1 Languages](#61-languages)
  - [6.2 Frameworks and Libraries](#62-frameworks-and-libraries)
  - [6.3 Tools and Software](#63-tools-and-software)
- [7. Testing](#7-testing)
  - [7.1 Manual Testing](#71-manual-testing)
    - [7.1.1 Authentication](#711-authentication)
    - [7.1.2 Review CRUD](#712-Review-crud)
    - [7.1.3 Review Permissions](#713-review-permissions)
    - [7.1.4 Game List Page](#714-game-list-page)
    - [7.1.5 Responsiveness](#715-responsiveness)
  - [7.2 Validation Testing](#72-validation-testing)
    - [7.2.1 Python](#721-python)
    - [7.2.2 HTML](#722-html)
    - [7.2.3 CSS](#723-css)
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

Witch Tower Boardgame Library is a full-stack web application designed to display and manage a personal board game library in a clear and structured way. The project began as an idea for my friend Katarina, who wanted a webpage that would help friends and family browse the available games before meeting in person.

The main purpose of the site is to make game selection easier and faster. Instead of spending part of a gathering deciding what to play, users can browse the library in advance, check whether a game is available, read details, and leave feedback after playing.

Although some shop-like interface elements are currently used in the layout, the long-term purpose of the project is closer to a board game library and lending system than an online shop. The current version focuses on browsing, filtering, authentication, reviews, events, and contact messaging, while more advanced reservation and lending features are planned for future releases.


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


## 2. UX / Design

  ### 2.1 Design Goals

The main design goals for the project were:
- to create a clear and readable interface for browsing board games
- to keep the layout usable across phones, tablets, and desktop screens
- to make the game library easy to filter and explore
- to keep interactions simple and predictable
- to maintain a consistent visual theme across pages and forms

The overall design was influenced by the idea of a darker fantasy-inspired “Witch Tower” atmosphere, while still keeping the interface practical and readable.

  ### 2.2 Layout and Structure

The site uses a shared base layout with:
- a header containing login state and main navigation
- a central content area
- a footer used consistently across pages

![Layout and Structure](static/assets/readme/Navigation%20-%20README.jpg)

The structure was built around the main user flow:
1. arrive on the Home page
2. browse the game library
3. filter or sort games
4. open a game detail page
5. sign up or log in if the user wants to leave a review or send a contact message

The Contact, Events, Home, authentication, and review-related pages were gradually brought into a more consistent shared structure during development.

  ### 2.3 Colour and Visual Style

The visual style uses a dark background with purple, cyan, and gold accents. This was chosen to support the Witch Tower identity while keeping the project readable and distinct from a plain default Bootstrap or Django-admin look.

Design choices included:
- dark layered backgrounds
- glowing accent colours for buttons and selected states
- rounded controls and pills
- improved visibility for links and action buttons
- consistent styling for forms, review actions, and authentication pages

  ### 2.4 Navigation

The navigation was kept simple and placed in the shared header. The main navigation includes:
- Home
- Games
- Events
- Contact

**Home Page**
![Home page](static/assets/readme/Home%20Page%20-%20Smartphone%20-%20README.jpg)

**Game Page**
![Games page](static/assets/readme/Games%20-%20Smartphone%20-%20README.jpg)

**Event Page**
![Events page](static/assets/readme/Events%20-%20Smartphones%20-%20README.jpg)

**Contact Page**
![Contact page](static/assets/readme/Contact%20-%20Smartphones%20-%20README.jpg)


Authentication controls in the header also show whether the user is logged in.

The navigation structure was intentionally kept straightforward so that users could move between the main areas without confusion. Some earlier ideas, such as a separate collapsible menu, were later removed because the main navigation was already sufficient.

  ### 2.5 Wireframes / Mockups / Planning Notes

The project started from a practical idea rather than a polished design document. Planning was done incrementally through:
- GitHub Project board organisation
- epics, user stories, and tasks
- UI iteration directly inside the project
- responsive testing and repeated layout refinement

The design evolved during development, especially in areas such as:
- contact form layout
- event page styling
- review form styling
- authentication form consistency
- responsive breakpoints
- header and navigation polish


## 3. Agile Planning

  ### 3.1 Project Board
The project was planned and tracked using a GitHub Project board. This board was used to organise development tasks, monitor progress, and keep the work structured throughout the build.

A simple workflow was used to move tasks through the project lifecycle:
- **Backlog / To Do**
- **In Progress**
- **Done**


**Link to Agile board**
https://github.com/users/Agnogh/projects/9/views/1

**Link to Agile Board (General View)**
https://github.com/Agnogh/WitchTowerBoardgameLibrary/issues?q=is%3Aissue%20state%3Aclosed&page=1


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

These relationships support the main business logic of the application by allowing games to be grouped, displayed in detail, and reviewed by authenticated users.

  ### 4.4 Event Model

The Event model was added to support a simple MVP events page. It allows the site owner to add and manage upcoming board game events through Django Admin without editing the page manually every time.

The MVP version stores the game name as plain text rather than linking directly to the Game model. This was a deliberate decision to keep the first implementation simple and achievable. Linking events to the real Game model is planned as a future improvement.

The events feature exists to give users a quick overview of planned sessions, dates, and event details.

  ### 4.5 ContactMessage Model

The ContactMessage model allows logged-in users to send a message through the Contact page.

Key fields include:
- linked user
- topic
- message
- created timestamp
- resolved status

This feature was designed as a simple internal messaging/contact system. Messages are stored in the database and can be reviewed through Django Admin rather than being sent as email.

The topic selection was later refined from a dropdown into radio-button pills to improve usability on smaller screens.

  ### 4.6 Relationships Between Models

The models in the project are connected in the following way:

- one Category can contain many Games
- one Game can belong to one Category
- one Game can have many Reviews
- one User can write many Reviews
- one User can leave only one Review per Game
- one User can send many ContactMessages
- Event currently remains independent in MVP form and stores the game name as plain text

These relationships support the main business logic of the application by allowing games to be grouped, displayed in detail, reviewed by authenticated users, and supported by future event and communication features.

## 5. Features

  ### 5.1 Home Page

**HOME - Smartphones**
![Home Page Smartphone](static/assets/readme/Home%20Page%20-%20Smartphone%20-%20README.jpg)


**HOME - Tablets**
![Home Page Smartphone](static/assets/readme/Home%20Page%20-%20Tablet%20-%20README.jpg)


**HOME - Desktops**
![Home Page Smartphone](static/assets/readme/Home%20Page%20-%20Desktop%20-%20README.jpg)



The Home Page acts as the main entry point of the application. It provides users with a simple starting hub from which they can navigate to the main parts of the site, such as the game list, authentication pages, and other planned sections such as Events and Contact.

Its purpose is to give users a clear first step into the application and make navigation easier across the main areas of the site.

  ### 5.2 Game List Page

**Game List**
![Game list](static/assets/readme/Game%20list%20-%20README.jpg)

The Game List Page displays the collection of board games available in the library. It is one of the main functional pages of the project and allows users to browse the current collection in an organised way.

This page includes filters, sorting options, active filter chips, and pagination. Users can narrow down the results based on their needs and then apply the selected filters using the **Apply Filters** button.

A deliberate design decision was made to apply filters only when the user clicks **Apply Filters**, rather than updating results instantly on every field change. This was done to keep the experience more predictable for the user and to avoid unnecessary repeated page reloads while multiple filters are being adjusted.

  ### 5.3 Filtering and Sorting


**Game filtering and sorting**
![Filtering and sorting](static/assets/readme/Game%20Filtering%20-%20README.jpg)


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

**Game Details**
![Game Details](static/assets/readme/Game%20details%20-%20README.jpg)

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


**Sign Up pane**
![Sign up pane](static/assets/readme/Sign%20Up%20or%20Log%20In%20-%20README.jpg)


**Log in pane**
![Log in pane](static/assets/readme/Sign%20Up%20or%20Log%20In%202%20-%20README.jpg)



Authentication allows users to sign up, log in, and log out of the site. This creates a distinction between general visitors and authenticated users.

Any visitor can browse the available games, but only registered and logged-in users can interact with the review system. This helps create a more controlled and accountable environment for user-generated content.

Authentication is also important for ownership-based permissions, as it ensures that users can only edit or delete their own reviews.


  ### 5.6 Review CRUD


**Add Review**
![Review CRUD Add Review](static/assets/readme/Write%20review%20-%20README.jpg)


**Edit Review**
![Review CRUD Edit Review](static/assets/readme/Edit%20review%20-%20README.jpg)



The review system provides full front-end CRUD functionality for authenticated users.

Logged-in users can:
- create a review
- read reviews left by other users
- update their own review
- delete their own review

Each user is limited to one review per game. This was a deliberate design choice to keep feedback clear, reduce clutter, and prevent duplicate reviews for the same game by the same person.

This feature is one of the most important parts of the project because it satisfies the front-end CRUD requirement while also adding real value for users.


  ### 5.7 User Feedback Messages


**User feedback message - Log in**
![User feedback message - Log in](static/assets/readme/User%20Message%20Log%20in%20-%20README.jpg)


**User feedback message - Log out**
![User feedback message - Log out](static/assets/readme/User%20Message%20Log%20out%20-%20README.jpg)



**User feedback message - Add Review**
![User feedback message - Add Review](static/assets/readme/User%20Message%20Add%20Review%20-%20README.jpg)



**User feedback message - Edit Review**
![User feedback message - Edit Review](static/assets/readme/User%20Message%20Update%20Review%20-%20README.jpg)



**User feedback message - Delete Review**
![User feedback message - Delete Review](static/assets/readme/User%20Message%20Delete%20Review%20-%20README.jpg)



The application provides clear feedback messages to users after important actions.

Users receive confirmation messages for actions such as:
- signing up
- logging in
- logging out
- adding a review
- editing a review
- deleting a review

This improves usability by clearly informing users that their action was completed successfully. It also supports better overall UX by reducing uncertainty after important interactions.

  ### 5.8 Contact Page

**Contact page - Smartphone**
![Contact Page image - Smartphone](static/assets/readme/Contact%20-%20Smartphones%20-%20README.jpg)


**Contact page - Tablets**
![Contact Page image - Tablets](static/assets/readme/Contact%20-%20Tablets%20-%20README.jpg)


**Contact page - Desktop**
![Contact Page image - Desktop](static/assets/readme/Contact%20-%20Desktops-%20README.jpg)



The Contact page allows logged-in users to send a message to the site owner through the application. Instead of sending email, the submitted message is stored in the database and can be viewed later in Django Admin.

Users can choose a topic and write a message. During development, this topic selector was improved from a dropdown menu to radio-button pills to create a cleaner and more consistent mobile experience.

This page adds practical value to the project by giving users a direct way to ask questions about borrowing, events, or general library matters.

  ### 5.9 Events Page

**Events Page - Smartphone**
![Events Page - Smartphone](static/assets/readme/Events%20-%20Smartphones%20-%20README.jpg)


**Events Page - Tablet**
![Events Page - Tablet](static/assets/readme/Events%20-%20Tablets%20-%20README.jpg)


**Events Page - Desktop**
![Events Page - Desktop](static/assets/readme/Events%20-%20Desktops-%20README.jpg)



The Events page was added as an MVP feature so the site owner can display upcoming board game events without manually rewriting page content each time.

Event records are managed in Django Admin and then displayed on the site. In the current version, the event’s game is stored as plain text rather than being linked directly to a Game record. This was a conscious MVP decision to keep the feature simpler and easier to implement in the current release.

The page helps users see what sessions are planned and prepares the project for more advanced community/event planning later.

  ### 5.10 Placeholder Cart UX


**Placeholder cart message**
![Placeholder cart message](static/assets/readme/Cart%20system%20-%20README.jpg)


The current version includes a Cart link and Add to cart button as part of the interface layout, but the full cart / reserve system is not yet implemented.

To avoid a broken-feeling experience, these actions now show clear placeholder toast messages informing the user that the feature is planned for version 1.2. This was done as a usability improvement so users understand that the feature is intentionally postponed rather than broken.

## 6. Technologies Used

  ### 6.1 Languages

- Python
- HTML
- CSS
- JavaScript

  ### 6.2 Frameworks and Libraries

- Django
- Django authentication system
- Django messages framework

  ### 6.3 Tools and Software

- Git
- GitHub
- GitHub Projects
- VS Code
- SQLite (development database)
- PostgreSQL configuration prepared for production / deployment
- Chrome DevTools for responsive testing and debugging


## 7. Testing

  ### 7.1 Manual Testing

  #### 7.1.1. Authentication

| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Sign up | User opens sign up page, fills form, submits valid details | Account is created and user is logged in | Pass |
| Log in | Existing user enters correct username and password | User is logged in successfully | Pass |
| Log out | Logged-in user clicks log out | User is logged out and sees confirmation message | Pass |

  #### 7.1.2. Review CRUD

| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Create review | Logged-in user submits a valid review | Review is saved and shown on the game detail page | Pass |
| Read reviews | User opens a game detail page | Existing reviews are visible on the page | Pass |
| Update review | Review owner edits their review and saves changes | Updated review is shown on the page | Pass |
| Delete review | Review owner deletes their review | Review is removed from the page and database | Pass |

  #### 7.1.3. Review Permissions

| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Logged-out review access | Logged-out user opens game detail page | User can read reviews but cannot submit one | Pass |
| Logged-out create attempt | Logged-out user tries to submit a review | User is redirected to log in / prevented from submitting | Pass |
| Owner edit access | Review owner opens their review actions | Edit and Delete controls are visible | Pass |
| Non-owner edit access | Different logged-in user opens same game page | Edit and Delete controls are not visible for another user's review | Pass |
| Non-owner direct edit/delete attempt | Different logged-in user manually tries edit/delete URL | Access is denied / object is not accessible | Pass |

  #### 7.1.4. Game List Page

| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Search | User enters a title and clicks Apply filters | Matching games are shown | Pass |
| In stock filter | User ticks In stock only and clicks Apply filters | Only in-stock games are shown | Pass |
| Player range filter | User enters min/max players and clicks Apply filters | Games matching the player range are shown | Pass |
| Exact players filter | User enters exact player and clicks Apply filters | Games supporting that player count are shown | Pass |
| Time filter | User enters time values and clicks Apply filters | Games matching play-time filter are shown | Pass |
| Age filter | User enters age and clicks Apply filters | Games suitable for that age are shown | Pass |
| Remove single filter | User clicks x on one active filter chip | Only that filter is removed and results refresh correctly | Pass |
| Clear all | User clicks Clear all | All active filters are removed | Pass |
| Sorting | User clicks Title / Price / Newest | Results sort correctly | Pass |
| Pagination | User moves between pages | Correct page loads and active filters remain applied | Pass |

  #### 7.1.5. Responsiveness

| Screen Size | Areas Tested | Expected Result | Actual Result |
|---|---|---|---|
| Mobile | Sidebar, filters, chips, pagination | Layout stacks correctly and remains readable | Pass |
| Tablet | Sidebar and game list side by side | Text remains readable and layout stays usable | Pass |
| Desktop | Full list, sidebar, sort controls | Layout is spacious and readable | Partially pass – layout works, but spacing/readability around 1200px width still needs polish |

### 7.2 Validation Testing

  #### 7.2.1. Python
Python code was checked during development for syntax errors and general code quality.

  #### 7.2.2. HTML
HTML was tested and corrected where needed.

  #### 7.2.3. CSS
CSS was tested and corrected where needed.

  ### 7.3 Bugs Fixed

The following bugs and usability issues were identified and fixed during development:


- Fixed tablet sidebar readability with improved responsive layout and font sizing
- review duplication was prevented by allowing only one review per user per game
- review permissions were restricted so users can only edit or delete their own reviews
- feedback messages were added for sign up, log in, log out, create review, edit review, and delete review
- rating validation was added to keep review ratings between 1 and 5
- filters were changed to apply only when the user clicks **Apply filters**, rather than auto-submitting unexpectedly
- Contact and Events pages were styled for improved consistency and readability
- Contact topic selection was changed from a dropdown to radio-button pills for better mobile UX
- white browser-default form backgrounds were removed from review, contact, login, and sign-up areas to match the site theme
- the save button when editing a review was styled consistently with the rest of the UI
- link visibility was improved to make content links easier to see against the dark background
- the unused Menu button idea was removed because the fixed navigation was sufficient
- the duplicate Add to cart button issue was removed
- the General topic radio pill overlap issue was fixed by shortening topic labels and refining pill layout
- spacing and label alignment in the Contact form were improved
- missing placeholder image errors causing 404s were resolved by adding the expected image files
- Cart and Add to cart interactions were changed from dead-end placeholder actions into clear v1.2 toast notices

  ### 7.4 Remaining Bugs and Known Issues

- the favicon has not yet been added
- related/similar game suggestions are not implemented in the current release and are reserved for future development
- the full cart / reserve system is not implemented yet; placeholder messages are shown instead
- final deployment and production security verification remain to be completed


## 8. Deployment

  ### 8.1 Local Development


  ### 8.2 Deployment Steps


  ### 8.3 Environment Variables


  ### 8.4 Security Notes



## 9. Future Improvements

Planned future improvements include:

- implement a full cart / reserve system
- link Event entries to real Game records instead of using plain text
- build real related / similar game suggestions
- support more advanced lending or borrowing tracking
- allow a game to be assigned to a borrower
- improve category count behaviour and overall category UX
- expand account-management options for users
- add rewards / vouchers as a post-MVP feature
- add a favicon
- continue layout polish around larger breakpoint transitions

## 10. Credits

  ### 10.1 Code / Learning References

- Django documentation
- MDN Web Docs
- YouTube
- Stack Overflow
- GitHub documentation
- course materials and general learning resources used during project development

  ### 10.2 Media / Content

- board game descriptions, screenshots, and placeholder content were used for development and demonstration purposes
- placeholder images were added during development to support the game detail layout

  ### 10.3 Acknowledgements

- Katarina, whose original idea for a board game library page inspired the project
- Nurses Betty and Keila for their support and making me comfortable
- Doc Bashir for letting me use his office during his night shifts
- friends and family members who helped shape the real-life use case behind the project