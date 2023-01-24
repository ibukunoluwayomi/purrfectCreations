# PurrfectCreations

## Steps to run

Docker is required on the host machine

Execute commands below from within the root directory.

- Build the image.`docker build -t purrfectcreations .`
- Run the container. `docker run -t -i -p 8000:8000 --env AIRTABLE_API_KEY=<AIRTABLE_API_KEY> --env AIRTABLE_BASE_ID=<AIRTABLE_BASE_ID> --env AIRTABLE_ORDERS_TABLE_ID=<AIRTABLE_ORDERS_TABLE_ID> purrfectcreations`


## To run test
- Build the image.`docker build -t purrfectcreations .`
- Execute test in container `docker run -t -i purrfectcreations sh -c "python -m pytest dashboard/tests.py -vv"`