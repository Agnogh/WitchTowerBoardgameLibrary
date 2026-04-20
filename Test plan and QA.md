## Testing

### Manual Testing

#### Authentication

| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Sign up | User opens sign up page, fills form, submits valid details | Account is created and user is logged in | Pass |
| Log in | Existing user enters correct username and password | User is logged in successfully | Pass |
| Log out | Logged-in user clicks log out | User is logged out and sees confirmation message | Pass |

#### Review CRUD

| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Create review | Logged-in user submits a valid review | Review is saved and shown on the game detail page | Pass |
| Read reviews | User opens a game detail page | Existing reviews are visible on the page | Pass |
| Update review | Review owner edits their review and saves changes | Updated review is shown on the page | Pass |
| Delete review | Review owner deletes their review | Review is removed from the page and database | Pass |

#### Review Permissions

| Feature | Action | Expected Result | Actual Result |
|---|---|---|---|
| Logged-out review access | Logged-out user opens game detail page | User can read reviews but cannot submit one | Pass |
| Logged-out create attempt | Logged-out user trie to submit a review | User is redirected to log in / prevented from submitting | Pass |
| Owner edit access | Review owner opens their review actions | Edit and Delete controls are visible | Pass |
| Non-owner edit access | Different logged-in user opens same game page | Edit and Delete kontrols are not visible for another user's review | Pass |
| Non-owner direct edit/delete attempt | Different logged-in user manually tries edit/delete URL | Access is denied / object is not accessible | Pass |

#### Game List Page

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
| Pagination | User moves beetwen pages | Correct page loads and active filters remain applied | Pass |

#### Responsivenes

| Screen Size | Areas Tested | Expected Result | Actual Result |
|---|---|---|---|
| Mobile | Sidebar, filters, chips, pagination | Layout stacks correctly and remains readable | Pass |
| Tablet | Sidebar and game list side by side | Text remains readable and layout stays usable | Pass |
| Desktop | Full list, sidebar, sort controls | Layout is spacious and readable | Not fully pass |

### Validation Testing

#### Python
Python code was checked during development for syntax errors and general code quality.

#### HTML
HTML was tested and corrected where needed.

#### CSS
CSS was tested and corrected where needed.

### Bugs Fixed

- Fixed filter auto-submit so filters now apply only when the user clicks **Apply filters**
- Fixed tablet sidebar readability with improved responsive layout and font sizing
- Fixed review duplication by allowing only one review per user per game
- Fixed review permissions so users can only edit or delete their own reviews
- Added feedback messages for sing up, log in, log out, create review, edit review, and delete review
- Limiting rating between 1 and 5
- Adding user text for Log in, log out, sign up, add, edit and delete review

### Remaining Bugs / Known Issues

- Review Edit and Delete controls are not yet equally styled
- Further UI polish may still be applied to some buttons and messages
- Improving resolution for 1200 (desktops)
- Additional UI styling (improvement)