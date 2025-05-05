

# Pinterest Clone: Create and Organize Boards with Pins

This project is a Pinterest clone that allows users to create boards and save pins to those boards. Similar pins are displayed below each pin on the pin-detail page. The underlying algorithm is straightforward: when a user visits the pin-detail page, the system searches the database for all boards that may contain that particular pin and then displays all the pins within those boards.

## Features

- **Public profile**: Users can have a public profile that includes a bio, photo, website link, and more.
- **Pin creation**: Users can create pins with images or videos.
- **Board creation**: Users can create boards, both public and private (only visible to the user).
- **Board management**: Users can edit the board cover, name, and other details.
- **Pin management**: Users can edit a pin's board, title, description, or delete it.
- **Follow/unfollow**: Users can follow or unfollow other users.
- **Commenting**: Users can add comments to pins.
- **Pin saving**: Users can save pins to their own boards.
- And more...

## Technologies Used

- Python 3
- Django
- Bootstrap
- SQLite3 database
- Vanilla JavaScript

## How to Run the Application

1. Clone or download the project to your local machine.
2. Change directory to the "pinterest-clone-django" folder.
3. Ensure that you have Python 3, pip, and virtualenv installed on your machine.
4. Create a virtual environment using the following command:
   - For Mac and Linux: `python3 -m venv venv`
   - For Windows: `python -m venv venv`
5. Activate the virtual environment:
   - For Mac and Linux: `source venv/bin/activate`
   - For Windows: `venv\scripts\activate`
6. Install the application requirements by running: `pip install -r requirements.txt`
7. Migrate the database by executing: `python manage.py migrate`
8. Start the server: `python manage.py runserver`
9. You should now be able to access the application by visiting: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

