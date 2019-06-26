from grakn.client import GraknClient

with GraknClient(uri="localhost:48555") as client:
    with client.session(keyspace="social_network") as session:
        with session.transaction().write() as write_transaction:
            insert_iterator = write_transaction.query('insert $x isa person, has email "x@email.com";')
            concepts = insert_iterator.collect_concepts()
            print("Inserted a person with ID: {0}".format(concepts[0].id))
            write_transaction.commit()

        with session.transaction().read() as read_transaction:
            answer_iterator = read_transaction.query("match $x isa person; get; limit 10;")

            for answer in answer_iterator:
                person = answer.map().get("x")
                print("Retrieved person with id " + person.id)

        with session.transaction().read() as read_transaction:
            answer_iterator = read_transaction.query("match $x isa person; get; limit 10;")
            persons = answer_iterator.collect_concepts()
            for person in persons:
                print("Retrieved person with id "+ person.id)
