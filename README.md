# University api
### Description
The api service supports CRUD for all entities. 
The service sends emails with the schedule of classes for each student who have lessons on next day every day except Saturday. Implemented a endpoint to get the schedule for a selected date for a specific group.

### Quickstart
```console
git clone https://github.com/MrJustice/elinext-university-api.git
cd university
docker-compose up --build
```
After the container is up, the application will run on localhost:8000/api/ .