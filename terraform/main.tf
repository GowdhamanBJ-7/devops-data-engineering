resource "databricks_job" "medallion_pipeline" {
  name = "medallion-prod-pipeline"

  # Schedule (Daily midnight IST)
  schedule {
    quartz_cron_expression = "0 0 0 * * ?"
    timezone_id            = "Asia/Kolkata"
  }

  # Bronze Task with Serverless
  task {
    task_key = "bronze_task"
    
    # Use serverless compute
    environment_key = "Default"  # This enables serverless compute
    
    notebook_task {
      notebook_path = "/Shared/devops_demo/bronze_ingest"
    }
  }

  # Silver Task with Serverless
  task {
    task_key = "silver_task"
    
    depends_on {
      task_key = "bronze_task"
    }
    
    # Use serverless compute
    environment_key = "Default"
    
    notebook_task {
      notebook_path = "/Shared/devops_demo/silver_transform"
    }
  }

  # Gold Task with Serverless
  task {
    task_key = "gold_task"
    
    depends_on {
      task_key = "silver_task"
    }
    
    # Use serverless compute
    environment_key = "Default"
    
    notebook_task {
      notebook_path = "/Shared/devops_demo/gold_aggregate"
    }
  }
}
