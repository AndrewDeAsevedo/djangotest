# djangotest

django!!!!!

## Setup Instructions

Run the following commands to get started:

1. Install `poetry`:

   ```sh
   # on macOS:
   brew install pipx && rehash

   # install poetry
   pipx install poetry
   ```

2. Clone the repository:
   ```sh
   git clone git@github.com:AndrewDeAsevedo/djangotest.git &&
       cd djangotest
   ```
3. Install dependencies and activate the virtual environment:
   ```sh
   poetry install &&
       poetry shell
   ```
4. Execute the following commands to initialize the Django project:

   ```sh
   # perform migrations on the database
   django-admin migrate

   # collect static files into the ./static directory (not needed for the local dev server)
   django-admin collectstatic

   django-admin createcachetable

   django-admin runserver 0.0.0.0:8000
   ```

5. Create a super user and log in to the admin UI:

   ```sh
   django-admin createsuperuser
   ```

   Visit http://localhost:8000/admin in your browser and log in with the super user credentials. 🚀


