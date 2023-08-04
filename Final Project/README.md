1. STAGE-0 :-

* install the data_gen.py from the repository.
* Run this program on the terminal.
 ```python
 python3 data_gen.py
 ```
*** NOTE : This program stores the database in a text file named database.txt (creates one if not present in folder).
______________________________________________________________________________________________________________________________________

3. STAGE-I :-

* deploy the cloudserver in the docker container:
PROCESS :
1. Install the cloud_server.py and the Dockerfile file from the repository.
2. Create a directory(say 'utkarsh2004') and copy both cloudserver and dockerfile into that directory.
    ***NOTE : make sure you create directory in the Linux folder, otherwise it will give error: file not found.
3. Make sure your Docker engine is running.
3. In the terminal, Change directory(I mean use cd command) to the folder which contains created directory(In my case created directory was 'utkarsh2004')
   and execute the following command:
    ```python
    docker build -t utkarsh2004 .
    ```
4. Next we have to run the docker container:
    ```python
    docker run -p 9998:9998 utkarsh2004
    ```
    This way you expose the port inside the container to the files outside container and -p command helps the inside
    program connnect to the program with the same port outside container.
5. It shows the message,'waiting for connection with DO....'.
____________________________________________________________________________________________________________________

2. STAGE-II :-

* install the data_owner.py file from the repository.
* Run this program on another terminal.
```python
python3 data_owner.py
```
_________________________________________________________________________________________________________________

3. STAGE-III :-

* Install the query_user.py file from the repository.
* Run this program on third terminal. 
```python
python3 query_user.py
```
In the dataowner terminal you will see the connection esttablished.
* In data_owner.py it will ask whether or not to allow query, respond 'y' for yes or 'n' for no.
* if you entered 'y' then program runs and give you the required output i.e. we obtain the index set in QU.
_________________________________________________________________________________________________________________

***NOTE: sometimes printing the result may take time as data is too large, so wait for sometime.

***ASSUMPTIONS MADE FOR IMPLEMENTATION:
1. data_gen.py generates a random database consisting of 10000 datapoints each of dimension 50. Each dimension of datapoint has integer values in range [-10,10].
2. The query user can only query 50-dimensional point (No partial dimension is allowed).
3. I have set the value of k=10. Which means we get 10 index numbers.
