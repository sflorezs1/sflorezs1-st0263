FROM node:latest AS build
WORKDIR /build

COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm ci

COPY public/ public
COPY src/ src
RUN npm run build

FROM nginx:alpine
RUN apk update && apk add bash
COPY --from=build /build/build/ /usr/share/nginx/html
COPY ./src/env.sh /docker-entrypoint.d/
RUN chmod +x /docker-entrypoint.d/env.sh
