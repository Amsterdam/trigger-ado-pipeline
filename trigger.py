import json
import requests
import sys
import base64
from json.decoder import JSONDecodeError

URL_TEMPLATE = "https://dev.azure.com/{organisation}/{project}/_apis/pipelines/{pipeline_id}/runs?api-version=7.1-preview.1"
uri_data = {"resources": {}, "templateParameters": {}, "variables": {}}


def _fetch_headers(pat_token):
    base64_token = str(base64.b64encode(bytes(":" + pat_token, "ascii")), "ascii")
    return {"Content-Type": "application/json", "Authorization": f"Basic {base64_token}"}


def trigger_pipeline(pipeline_id, organisation, project, pat_token, template_params=None):
    url = URL_TEMPLATE.format(organisation=organisation, project=project, pipeline_id=pipeline_id)
    if template_params.strip():
        try:
            uri_data["templateParameters"] = json.loads(template_params)
        except JSONDecodeError:
            pass
    try:
        response = requests.post(url, json=uri_data, headers=_fetch_headers(pat_token))
        if response.status_code == 203:
            print("Something is wrong with the pat token.")
            exit(1)
        if response.status_code == 400:
            print(f"Something wrong with the provide parameters '{template_params}'")
            exit(1)
        if response.status_code == 404:
            print(
                f"Something wrong with the url, check `pipeline_id`: {pipeline_id}, `organisation`: {organisation} and `project`: {project}"
            )
            exit(1)
        response.raise_for_status()
        if response.json()["name"]:
            print("Pipeline has been triggered, it's id is: " + response.json()["name"])
        else:
            print("Pipeline trigger has failed. here is the error: " + response.json())
    except ValueError as e:
        raise e


if __name__ == "__main__":
    cli_args = sys.argv
    if len(cli_args) < 5:
        print(
            "Arguments are: pipeline_id, organisation, project, pat_token, template_params(optional)"
        )
        exit(1)
    trigger_pipeline(*cli_args[1:])
