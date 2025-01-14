==============
CLI Reference
==============

Alice
-----

"Alice the Policy Authority" management commands.


.. code:: bash

    (nucypher)$ nucypher alice ACTION [OPTIONS]

**Alice Command Actions**

+--------------------------+-------------------------------------------------------------------------------+
| Action                   | Description                                                                   |
+==========================+===============================================================================+
| ``init``                 | Create a brand new persistent Alice.                                          |
+--------------------------+-------------------------------------------------------------------------------+
| ``config``               | View and optionally update an existing Alice's configuration.                 |
+--------------------------+-------------------------------------------------------------------------------+
| ``destroy``              | Delete existing Alice's configuration.                                        |
+--------------------------+-------------------------------------------------------------------------------+
| ``decrypt``              | Decrypt data encrypted using an Alice's policy encrypting key                 |
+--------------------------+-------------------------------------------------------------------------------+
| ``derive-policy-pubkey`` | Derive a policy public key from a policy label.                               |
+--------------------------+-------------------------------------------------------------------------------+
| ``grant``                | Create and enact an access policy for some Bob.                               |
+--------------------------+-------------------------------------------------------------------------------+
| ``make-card``            | Create a character card file for public key sharing.                          |
+--------------------------+-------------------------------------------------------------------------------+
| ``public-keys``          | Obtain Alice's public verification and encryption.                            |
+--------------------------+-------------------------------------------------------------------------------+
| ``revoke``               | Revoke a policy.                                                              |
+--------------------------+-------------------------------------------------------------------------------+
| ``run``                  | Start Alice's HTTP controller.                                                |
+--------------------------+-------------------------------------------------------------------------------+

Bob
---


"Bob the Data Recipient" management commands.


.. code:: bash

    (nucypher)$ nucypher bob ACTION [OPTIONS]

**Bob Command Actions**

+--------------------------+-------------------------------------------------------------------------------+
| Action                   | Description                                                                   |
+==========================+===============================================================================+
| ``init``                 | Create a brand new persistent Bob.                                            |
+--------------------------+-------------------------------------------------------------------------------+
| ``config``               | View and optionally update an existing Bob's configuration.                   |
+--------------------------+-------------------------------------------------------------------------------+
| ``destroy``              | Delete existing Bob's configuration.                                          |
+--------------------------+-------------------------------------------------------------------------------+
| ``retrieve``             | Obtain plaintext from encrypted data, if access was granted.                  |
+--------------------------+-------------------------------------------------------------------------------+
| ``make-card``            | Create a character card file for public key sharing.                          |
+--------------------------+-------------------------------------------------------------------------------+
| ``public-keys``          | Obtain Bob's public verification and encryption.                              |
+--------------------------+-------------------------------------------------------------------------------+
| ``run``                  | Start Bob's HTTP controller.                                                  |
+--------------------------+-------------------------------------------------------------------------------+


Enrico
-------

"Enrico the Encryptor" management commands.


.. code:: bash

    (nucypher)$ nucypher enrico ACTION [OPTIONS]

**Enrico Command Actions**


+--------------------------+-------------------------------------------------------------------------------+
| Action                   | Description                                                                   |
+==========================+===============================================================================+
| ``encrypt``              | Encrypt a message under a given policy public key.                            |
+--------------------------+-------------------------------------------------------------------------------+
| ``run``                  | Start Enrico's HTTP controller.                                               |
+--------------------------+-------------------------------------------------------------------------------+


Ursula
------

"Ursula the Untrusted" PRE Re-encryption node management commands.


.. code:: bash

    (nucypher)$ nucypher ursula ACTION [OPTIONS]


**Ursula Command Actions**


+--------------------------+---------------------------------------------------------------------+
| Action                   | Description                                                         |
+==========================+=====================================================================+
| ``init``                 | Create a brand new persistent Ursula.                               |
+--------------------------+---------------------------------------------------------------------+
| ``config``               | View and optionally update an existing Ursula's configuration.      |
+--------------------------+---------------------------------------------------------------------+
| ``destroy``              | Delete existing Ursula's configuration.                             |
+--------------------------+---------------------------------------------------------------------+
| ``forget``               | Delete all stored peer metadata.                                    |
+--------------------------+---------------------------------------------------------------------+
| ``save-metadata``        | Manually write node metadata to disk without running.               |
+--------------------------+---------------------------------------------------------------------+
| ``run``                  | Start Ursula.                                                       |
+--------------------------+---------------------------------------------------------------------+


Cloudworkers
------------

Manage PRE Node operations on cloud infrastructure.

.. code:: bash

    (nucypher)$ nucypher cloudworkers ACTION [OPTIONS]

**Cloudworkers Command Actions**

+----------------------+-------------------------------------------------------------------------------+
| Action               |  Description                                                                  |
+======================+===============================================================================+
|  ``up``              | Creates and deploys hosts for all active local stakers.                       |
+----------------------+-------------------------------------------------------------------------------+
|  ``create``          | Creates and deploys the given number of hosts independent of stakes           |
+----------------------+-------------------------------------------------------------------------------+
|  ``add``             | Add an existing host to be managed by cloudworkers CLI tools                  |
+----------------------+-------------------------------------------------------------------------------+
|  ``add_for_stake``   | Add an existing host to be managed for a specified local staker address       |
+----------------------+-------------------------------------------------------------------------------+
|  ``deploy``          | Install and run Ursula on existing managed hosts.                             |
+----------------------+-------------------------------------------------------------------------------+
|  ``update``          | Update or manage existing installed Ursula.                                   |
+----------------------+-------------------------------------------------------------------------------+
|  ``destroy``         | Shut down and cleanup resources deployed on AWS or Digital Ocean              |
+----------------------+-------------------------------------------------------------------------------+
|  ``stop``            | Stop the selected nodes.                                                      |
+----------------------+-------------------------------------------------------------------------------+
|  ``status``          | Prints a formatted status of selected managed hosts.                          |
+----------------------+-------------------------------------------------------------------------------+
|  ``logs``            | Download and display the accumulated stdout logs of selected hosts            |
+----------------------+-------------------------------------------------------------------------------+
|  ``backup``          | Download local copies of critical data from selected installed Ursulas        |
+----------------------+-------------------------------------------------------------------------------+
|  ``restore``         | Reconstitute and deploy an operating Ursula from backed up data               |
+----------------------+-------------------------------------------------------------------------------+
|  ``list_hosts``      | Print local nicknames of all managed hosts under a given namespace            |
+----------------------+-------------------------------------------------------------------------------+
|  ``list_namespaces`` | Print namespaces under a given network                                        |
+----------------------+-------------------------------------------------------------------------------+


Status
------

Echo a snapshot of live PRE Application metadata.

.. code:: bash

    (nucypher)$ nucypher status ACTION [OPTIONS]


**Status Command Actions**


+--------------------------+---------------------------------------------------------------------+
| Action                   | Description                                                         |
+==========================+=====================================================================+
| ``events``               | Show events associated to PRE Application contracts.                |
+--------------------------+---------------------------------------------------------------------+


Bond
----

Bond an Operator to a Staking Provider. The Staking Provider must be authorized to use the PREApplication.

.. code:: bash

    (nucypher)$ nucypher bond [OPTIONS]


Unbond
------

Unbonds an operator from an authorized Staking Provider.

.. code:: bash

    (nucypher)$ nucypher unbond [OPTIONS]
