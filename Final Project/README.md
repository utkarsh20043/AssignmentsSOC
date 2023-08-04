* STAGE-I :-

* deploy the cloudserver in the docker container:
PROCESS :
1. Install the cloud_server.py and the Dockerfile file from the repository.
2. ***NOTE : make sure you save the cloud_server.py and Dockerfile in the Linux folder, otherwise it will give error: file not found. In my case the linux folder name is 'utkarsh2004'.
3. Make sure your Docker engine is running.
4. In the terminal, Change directory(I mean use cd command) to the folder which contains created directory(In my case created directory was 'utkarsh2004') and execute the following command:
    ```python
    docker build -t utkarsh2004 .
    ```
5. Next we have to run the docker container:
    ```python
    docker run -p 9998:9998 utkarsh2004
    ```
____________________________________________________________________________________________________________________

* STAGE-II :-

* install the data_owner.py file from the repository.
* Run this program on another terminal.
_________________________________________________________________________________________________________________

* STAGE-III :-

* Install the query_user.py file from the repository.
* Run this program on third terminal. In the dataowner terminal you will see the connection esttablished.
* It will ask for 'Enter integer:'. give the input number.
_________________________________________________________________________________________________________________

***YOU WILL SEE THE OUTPUT PRIME FACTORISATION OF NUMBER. ALSO THE CONNECTION WAS ESTABLISHED WITH THE SOCKET
PROGRAM MESSAGE IN THE DOCKER RUN TERMINAL.