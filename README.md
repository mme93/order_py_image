# order_py_image
docker run -p 4999:5000 -it --mount type=bind,src=/root/projekt/order_py_image/assets/download/example_one.jpg,target=/app/assets/download/example_one.jpg,dst=/app/assets/download/example_one.jpg image_py:latest
