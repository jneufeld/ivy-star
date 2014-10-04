# ivystar
Can machine learn who is sending a text message just based on the body of the
message? Let's start simple and see.

## What I set out to do
The goal was to use WhatsApp conversations between myself and a friend, teach
an ANN to identify the sender based on the content of the message, and see how
accurate I could make it.

I've learned a lot of machine learning and artificial neural networks in
particular. Initially inspired by an ANN used to identify the gender of
instagram users based solely on their public data, I thought this would be a
fantastic project.

## How to identify the sender
There were definitely differences in how my friend and I texted. Below are some
features I noted we differed in:

* Average message length
* Average sentence length
* Average word length
* Average sentences per message
* Average words per sentence
* Average words per message
* Average swear words per message

Some features held very little difference, like average word length. Others
seemed to vary enough I was hopeful it would be useful for learning, for
plopping texts into the right category.

## The neural network
I used PyBrain, fiddled around with the number of inputs, the type of and number
of hidden neurons, and the learning settings, but in the end had no success.

Some learning settings worked much better than others, and figuring out what
worked better drove me deeper in machine learning. In the end, though, I made no
discernable progress.

At best, the neural network was guessing. It could correctly identify the text's
sender about 50% of the time.
