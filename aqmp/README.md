AMQP
===================
TODO: difference bet blocking and non-blocking modes of operation.<br/>
Usage:<br>
open two terminals: one for the consumer and another one for the publisher.</br> In the consumer terminal, type

    $ python consumer.py
Then 

    $ python publisher.py
in the publisher terminal.
Then the consumer terminal will display the message sent by the publisher the amount of times 

    $ python publisher.py
was executed.
