FROM python

WORKDIR /usr/src/app/

COPY guessNumber.py $WORKDIR

CMD [ "python","./guessNumber.py"]