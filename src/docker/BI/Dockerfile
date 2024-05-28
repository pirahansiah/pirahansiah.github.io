# docker build -t farshid_pirahansiah_bi .
# docker run -p 8050:8050 farshid_pirahansiah_bi
# docker run -p 8050:8050 -v /Users/farshid/farshid/pirahansiah.github.io/src/docker/BI/paths.txt:/data farshid_pirahansiah_bi
# docker run -p 8050:8050 -v /Users/farshid/farshid/pirahansiah.github.io/src/docker/BI/paths.txt:/config/folder_path.txt farshid_pirahansiah_bi
# docker run -p 8050:8050 -v /Users/farshid/Desktop:/data -v /Users/farshid/farshid/pirahansiah.github.io/src/docker/BI/paths.txt:folder_path.txt farshid_pirahansiah_bi


# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8050 available to the world outside this container
EXPOSE 8050

# Run app.py when the container launches
CMD ["python", "app.py"]
