AMQP
===================
Synchronous messaging is used when the message sender expects a response to the message within a specified time period and waiting for that response to carry out his next task. Basically he “blocks” until he receives the response.</br>

Asynchronous messaging means that sender does not expect an immediate response and does not “blocks” waiting for the response. There can be a response or not, but the sender will carry out his remaining tasks.<br>
>Usage:<br>
open two terminals: one for the consumer and another one for the publisher.</br> In the consumer terminal, type

    $ python consumer.py
Then 

    $ python publisher.py
in the publisher terminal.
Then the consumer terminal will display the message sent by the publisher the amount of times 

    $ python publisher.py
was executed.
