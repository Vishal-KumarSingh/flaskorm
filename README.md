# Nobel Prize CRUD Project

## Introduction
This is a simple CRUD project built in Flask using ORM
## Features
- **Create**: Add new Nobel Prize winners to the database.
- **Read**: Retrieve information about Nobel Prize winners in paginated.
- **Update**: Updates the Nobel Prize winner data.
- **Delete**: Deletes the Nobel Prize winners from the database.
- **Search**: Search Nobel Prize winner from the database.

## Installation
```markdown
# Nobel Prize CRUD Project

## Introduction
This is a simple CRUD project built in Flask using ORM.

## Features
- **Create**: Add new Nobel Prize winners to the database.
- **Read**: Retrieve information about Nobel Prize winners in a paginated format.
- **Update**: Update the Nobel Prize winner data.
- **Delete**: Delete Nobel Prize winners from the database.
- **Search**: Search for Nobel Prize winners in the database.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Vishal-KumarSingh/flaskorm.git
    ```
    or extract the tar file:
    ```bash
    tar -xzvf 24M0742_hw11.tar.gz
    ```
2. Navigate to the project directory:
    ```bash
    cd webapi
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask server:
    ```bash
    python3 server.py
    ```

## Endpoints

- `GET /`: Retrieve the first page of Nobel Prize winners.
- `GET /?page=X`: Retrieve page number X of Nobel Prize winners.
- `GET /?search=X`: Search for X in Nobel Prize winners.
- `GET /add`: Add a new winner to the Nobel Prize winners.
- `POST /update/:X`: Update the winner with id X.

## API Endpoints

- `GET /api/`: Retrieve the first page of Nobel Prize winners.
- `GET /api/?page=X`: Retrieve page number X of Nobel Prize winners.
- `GET /api/?search=X`: Search for X in Nobel Prize winners. You can use both page and search at the same time.
Expects Empty Request
Response:
```json
[
    {
        "award_age": 57,
        "category": "Physiology or Medicine",
        "country": "Argentina",
        "date_of_birth": "1927-10-08",
        "date_of_death": "2002-03-24",
        "gender": "male",
        "id": 1,
        "link": "http://en.wikipedia.org/wiki/C%C3%A9sar_Milstein",
        "name": "César Milstein",
        "place_of_birth": "Bahía Blanca, Argentina",
        "place_of_death": "Cambridge, England",
        "text": "César Milstein, Physiology or Medicine, 1984",
        "year": 1985
    },
    {
        "award_age": 49,
        "category": "Literature",
        "country": "Belgium",
        "date_of_birth": "1862-08-29",
        "date_of_death": "1949-05-06",
        "gender": "male",
        "id": 3,
        "link": "http://en.wikipedia.org/wiki/Maurice_Maeterlinck",
        "name": "Maurice Maeterlinck",
        "place_of_birth": "Ghent, Belgium",
        "place_of_death": "Nice, France",
        "text": "Maurice Maeterlinck, Literature, 1911",
        "year": 1912
    }
]
```
- `POST /api/add`: Add a new winner to the Nobel Prize winners.

  Expects Request Body:
  ```json
  {
      "award_age": 57,
      "category": "Physiology or Medicine",
      "country": "Argentina",
      "date_of_birth": "1927-10-08",
      "date_of_death": "2002-03-24",
      "gender": "male",
      "id": 1,
      "link": "http://en.wikipedia.org/wiki/C%C3%A9sar_Milstein",
      "name": "César Milstein",
      "place_of_birth": "Bahía Blanca, Argentina",
      "place_of_death": "Cambridge, England",
      "text": "César Milstein, Physiology or Medicine, 1984",
      "year": 1985
  }
  ```
  Response Body:
  ```json
  {
      "message": "Winner added successfully!"
  }
  ```

- `POST /api/update/:X`: Update the winner with id X.

  Expects Request Body:
  ```json
  {
      "award_age": 57,
      "category": "Physiology or Medicine",
      "country": "Argentina",
      "date_of_birth": "1927-10-08",
      "date_of_death": "2002-03-24",
      "gender": "female",
      "link": "http://en.wikipedia.org/wiki/C%C3%A9sar_Milstein",
      "name": "César Milstein",
      "place_of_birth": "Bahía Blanca, Argentina",
      "place_of_death": "Cambridge, England",
      "text": "César Milstein, Physiology or Medicine, 1984",
      "year": 1985
  }
  ```
  Response Body:
  ```json
  {
      "message": "Winner updated successfully!"
  }
  ```

- `DELETE /api/delete/:X`: Delete the winner with id X.

  Expects an empty Request Body.
  Response Body:
  ```json
  {
      "message": "Winner deleted successfully!"
  }
  ```

   