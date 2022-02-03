FROM node:current-alpine

RUN mkdir -p /home/node/server/node_modules

WORKDIR /home/node/server

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]
