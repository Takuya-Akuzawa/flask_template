#! /usr/bin/env sh

# Let the DB start
sleep 1;

# Run migrations
flask db init
flask db migrate -m "Initial Migration"
flask db upgrade