=====
Usage
=====

Getting started
###############

.. literalinclude:: examples/basic.py
  :language: python

How to use parametrized pipeline to keep the code DRY ?
#######################################################

It can happens that you end up with a lot of pipelines that looks nearly exactly the same.
To avoid this, the SDK offers the *ParametrizePipeline* and *ParametrizeEntity* class. With it, you can pass some parameters to your pipeline. The SDK would then generate automatically a new
pipeline for each possible combination of each parameters.

A set of parameters looks like this:

.. code-block:: python

    pipeline_parameters = {
        "language": ["nl", "fr"],
        "country": ["be", "en"],
    }

Such a parameters would generate 4 pipelines, one for each possible combination of parameter:

.. code-block:: python

    {"language": "nl", "country": "be"},
    {"language": "nl", "country": "en"},
    {"language": "fr", "country": "be"},
    {"language": "fr", "country": "en"},



Parameterized pipeline and entity also allow to introduce custom logic. Here is an example how to use it:

.. literalinclude:: examples/parametrize_pipeline.py
  :language: python


How to apply the same query on multiple tables ?
################################################

If you want to apply the same query on different tables and avoid copying the query files around to just change the table name in the query,
you can use the *tables* field on the *Transformation* class. By specifying a list of tables to the transformation, Flycs will automatically generate
a BigQueryOperator for this transformation for each table specified.


.. literalinclude:: examples/template_query.py
  :language: python
