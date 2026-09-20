FROM node:22-alpine AS build

WORKDIR /app

COPY angular-docker-app/package*.json ./
RUN npm ci

COPY angular-docker-app/ ./
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/dist/angular-docker-app/browser /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
