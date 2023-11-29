# Trigger ADO pipeline action

This action triggers an ADO pipeline

## Inputs

## `pipeline-id`

**Required** The id of the pipeline. This can be found in the
browser url of the pipeline.


## `organisation`

**Required** The Organisation where the pipeline can be found in ADO.
This this the first part of the path in the pipeline url in the browser.
https://dev.azure.com/<Organisation>

## `project`

**Required** The Project where the pipeline can be found in ADO.
This this the second part of the path in the pipeline url in the browser.
https://dev.azure.com/<Organisation>/<Project>


## `pat-token`

**Required** The PAT token can be generated in ADO under User Settings.
Token needs to have "Build (read & execute)" scope.

## `template-params`

**Optional** When the pipeline yaml has parameters, those
can be provided as a json string.

## Example usage

    uses: jjmurre/trigger-ado-pipeline@v1
    with:
      pipeline-id: 1234
      organisation: CloudCompetenceCenter
      project: 'Data Diensten'
      pat-token: der2345tr
      template-params: '{"environment": "dev"}'
