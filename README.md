# Masonic Periodicals Online

This is the repository for the Masonic Periodicals Online project at
[King's Digital Lab](https://kdl.kcl.ac.uk).

The project has been containerised using
[Docker Compose](https://docs.docker.com/compose/).
The containerised setup includes the following services:

1. [`kdl-apache-proxy`](https://gitlab.kdl.kcl.ac.uk:5050/docker-images/core/kdl-apache-proxy):
    This service provides a reverse proxy for the edition, routing requests to
    the appropriate backend service.
1. [`django`](https://hub.docker.com/_/python): This services runs the Django
    application, providing the core functionality/frontend of the edition.
1. [`postgres`](https://hub.docker.com/_/postgres): This service provides a
    Postgres database for the Django application.
1. [`solr`](https://hub.docker.com/_/solr): This service provides a Solr
    search index for the edition.

## Getting Started

Follow these steps to set up and run the project using Docker Compose.

**Note** that these instructions cover only the local setup; server deployment
is not covered here.

### Pre-requisites

Before you begin, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)

### Running the application

1. **Clone this repository**
1. **Set up the environment file**

Create a `.env` file inside the compose directory with the following content:

```sh
# Set to False in production
DEBUG=True

# Set to True in production
PRODUCTION=False

DJANGO_ALLOWED_HOSTS=masonicperiodicals.org,mpol-os.kdl.kcl.ac.uk,mpol.app.cch.kcl.ac.uk,django,localhost,127.0.0.1
DJANGO_SECRET_KEY=generate-a-secret-key

POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=generate-a-password
```