FROM public.ecr.aws/glue/aws-glue-libs:5

USER root

# Optional: install extra libs
RUN pip install pytest pandas boto3

WORKDIR /home/hadoop/workspace
