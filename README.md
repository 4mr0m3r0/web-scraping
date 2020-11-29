Description
-----------
Web Scraping Demo that use http://books.toscrape.com/ site as an example.

Running the project
-------------------
First of all, you need Docker installed, then go to the root of the project and run on the terminal:
```
docker build .
```
Next, run docker compose:
```
docker-compose build
```
Finally, you are ready for running the Spiders with docker compose: 
```
docker-compose run app sh -c "scrapy crawl books"

# if you want to see the output in .csv format run this command
docker-compose run app sh -c "scrapy crawl books -o books.csv"
```

License
-------
```
MIT License

Copyright (c) 2020 Angel Romero (4mr0m3r0)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
 
