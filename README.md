# Book Donation App
---

## Fundamental Project 

Contents
- Brief
  - Requirements 
  - My Approach
- Architecture
  - Database Structure
  - CI Pipeline
- Project Tracking
- Risk Assessment
- Testing
- Front-End Design
- Future Improvements

## Resources

Trello Board - add links
Risk Assessment - add links

## Brief
---
### Requirements

The minimum viable product was to create an application that utilises create, read, update, and delete (CRUD) functionalities using technologies, tools and methods covered so far during training. In addition, the secondary requirements for this piece of work must also pass the following criteria: 

- A Trello board
- A relational database, consisting of at least two tables that model a relationship
- Clear documentation of the design phase, app architecture and risk assessment
- A python-based functional application that follows best practices and design principles
- Test suites for the application, which will include automated tests for validation of the application
- A front-end website, created using Flask
- Code integrated into a Version Control System which will be built through a CI server and deployed to a cloud-based virtual machine

### My Approach

To satisfy the requirements above, I have decided to create a simple book donation app which allows the user to: 

- Create a shop (satisfies 'Create') with the following information:
  - *Shop name*
  - *Shop Location*

- Create a book listing with the following information:
  - *Book title*
  - *Date and Time* the book was added

- View the shop that has been created (satisfies 'Read')
- Update the shop details (satisfies 'Update')
- Delete the shop (satisfies 'Delete')

## Architecture 
---
### Database Structure
Below, entity relationship diagrams (ERD) help illustrate the architectural structure of the database and the types of relationships which occur between the tables. 

ERD Diagram 1 
Initially, a one-to-many relationship was created between Shops and Users. 
![erd3](https://user-images.githubusercontent.com/74771160/103586310-bb796980-4edc-11eb-9682-f4e06ca6d711.png)

ERD Diagram 2
The diagram below shows the final ERD diagram which builds on the previous relationship by associating both tables with another table.
![ERD](https://user-images.githubusercontent.com/74771160/103575321-70a22680-4ec9-11eb-8fbc-242090fe06b6.png)
As shown, the app models a many-to-many relationship between Users and Shops using an intermediate table for Books. This allows a user to create shop requests to donate a book to the shop in question. A user can donate books to many shops while a shop can have many users donating books. 

### CI Pipeline

![CI pipeline](https://user-images.githubusercontent.com/74771160/103585708-7ef93e00-4edb-11eb-8d70-518e833b6667.png)

Illustrated above is the continuous integration pipeline with the associated frameworks and services related to them. 
There are four key build stages:
- Source: Source Code Management (pull code from Git repository)
- Build: Jenkins & Python
- Test: Pytest and Selenium
- Run: Flask Framework on GCP comute VM

## Project Tracking 








