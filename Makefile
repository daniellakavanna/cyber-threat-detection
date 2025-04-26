# Variables (retrieved from environment)
SRC_DIR = src

# Build the Docker image
build:
	docker build --platform linux/amd64 -t $(IMAGE_NAME) -f Dockerfile .

# Tag the Docker image for ECR
tag:
	docker tag $(IMAGE_NAME):latest $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPO_NAME):latest

# Push the image to ECR
push:
	aws ecr get-login-password --region $(AWS_REGION) | docker login --username AWS --password-stdin $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com
	docker push $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(ECR_REPO_NAME):latest

# Build the SAM application
sam-build:
	sam build --use-container

# Deploy the SAM application
sam-deploy:
	sam deploy --stack-name cyber-threat-detection-stack \
  	--region ${AWS_REGION} \
  	--image-repository ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO_NAME} \
  	--capabilities CAPABILITY_IAM 
	
# Clean up SAM build artifacts
sam-clean:
	rm -rf .aws-sam

# Full pipeline: build Docker image, tag, push to ECR, build SAM, and deploy SAM
all:
	build tag push sam-build sam-deploy
