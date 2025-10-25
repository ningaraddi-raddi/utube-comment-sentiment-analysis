import mlflow

# ❌ Wrong: double http
# mlflow.set_tracking_uri("http://http://ec2-13-233-216-134.ap-south-1.compute.amazonaws.com:5000")

# ✅ Correct:
mlflow.set_tracking_uri("http://ec2-13-233-216-134.ap-south-1.compute.amazonaws.com:5000")

mlflow.set_experiment("my-experiment")

with mlflow.start_run():
    mlflow.log_param("param1", 5)
    mlflow.log_metric("metric1", 0.89)
