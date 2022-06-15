FROM php:7.0.33-apache
COPY src/ /var/www/html
EXPOSE 80