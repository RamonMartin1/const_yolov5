build process is a little hacky (needs `node_modules`), run:
- `npm install` - only when first initializing the repo
- `docker build -t rlew631/frontend .`

to run:
- `docker run -p 3000:3000 rlew631/frontend`

push to dockerhub:
- `docker push rlew631/frontend`