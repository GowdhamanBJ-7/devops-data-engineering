resource "databricks_job" "medallion_pipeline" {
  name = "medallion-prod-pipeline"

  
  # SCHEDULE (Runs every 10 hours IST)
  schedule {
    quartz_cron_expression = "0 0 0/10 * * ?"
    timezone_id            = "Asia/Kolkata"
  }

  # BRONZE TASK
  task {
    task_key = "bronze_task"

    notebook_task {
      notebook_path = "/Shared/devops_demo/bronze_ingest"
    }

    # Serverless compute
    environment_key = "serverless"
  }

  
  # SILVER TASK
  task {
    task_key = "silver_task"

    depends_on {
      task_key = "bronze_task"
    }

    notebook_task {
      notebook_path = "/Shared/devops_demo/silver_transform"
    }

    # Serverless compute
    environment_key = "serverless"
  }

  # GOLD TASK
  task {
    task_key = "gold_task"

    depends_on {
      task_key = "silver_task"
    }

    notebook_task {
      notebook_path = "/Shared/devops_demo/gold_aggregate"
    }

    # Serverless compute
    environment_key = "serverless"
  }
}

