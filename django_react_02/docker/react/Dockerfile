FROM node

WORKDIR /client 

COPY ./frontend/package*.json /client/ 

RUN npm install 

COPY ./frontend /client/ 

EXPOSE 3000

CMD ["npm", "start"]