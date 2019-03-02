[![Docker Build Status](https://img.shields.io/docker/build/mdstudio/cerise-mdstudio-mock.svg)](https://hub.docker.com/r/mdstudio/cerise-mdstudio-mock/)

# Mock Cerise specialisation for MDStudio

This repository contains a Cerise specialisation for MDStudio which returns the
same static answer to any workflow.

This is intended as a mock for testing components that use cerise-mdstudio to
run jobs on a cluster, so that the tests can run without needing an actual
cluster with credentials and other such complicating factors.

## Running

### Install the service via Docker

Get the specialised service from Docker:

```bash
docker pull mdstudio/cerise-mdstudio-mock
```

### Start it

```bash
docker run --name=cerise-mdstudio-mock -p 29593-29594:29593-29594 mdstudio/cerise-mdstudio-mock
```

### Run a job

Now we can submit an example Gromit/GROMACS job, using a virtual environment to
keep the dependencies away from the rest of the system:

```bash
cd examples/
virtualenv -p python3 venv
. venv/bin/activate
pip3 install bravado
python3 run_md.py
```

This will take about 2 minutes to complete.


## Legal Notes

This repository is covered by the following license grant:

   Copyright 2018 Netherlands eScience Center and VU University Amsterdam

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
