1. STAGE-I :-

* deploy the cloudserver in the docker container:
PROCESS :
1. Install the cloudserver.py and the DOckerfile file from the repository.
2. Create a directory(say 'utkarsh2004') and copy both cloudserver and dockerfile into that directory.
    ***NOTE : make sure you create directory in the Linux folder, otherwise it will give error: file not found.
3. Make sure your Docker engine is running.
3. In the terminal, Change directory(I mean use cd command) to the folder which contains created directory(In my case created directory was 'utkarsh2004') and execute the following command:
    ```python
    docker build -t utkarsh2004 .
    ```
4. Next we have to run the docker container:
    ```python
    docker run -p 9998:9998 utkarsh2004
    ```
____________________________________________________________________________________________________________________

2. STAGE-II :-

* install the dataowner.py file from the repository.
* Run this program on another terminal.
_________________________________________________________________________________________________________________

3. STAGE-III :-

* Install the query_user.py file from the repository.
* Run this program on third terminal. In the dataowner terminal you will see the connection esttablished.
* It will ask for 'Enter integer:'. give the input number.
_________________________________________________________________________________________________________________

***YOU WILL SEE THE OUTPUT PRIME FACTORISATION OF NUMBER. ALSO THE CONNECTION WAS ESTABLISHED WITH THE SOCKET
PROGRAM MESSAGE IN THE DOCKER RUN TERMINAL.