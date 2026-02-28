resource "databricks_job" "medallion_pipeline" {
  name = "medallion-prod-pipeline"

  schedule {
    quartz_cron_expression = "0 0 * * * ?"
    timezone_id            = "Asia/Kolkata"
  }

  job_cluster {
    job_cluster_key = "medallion_cluster"

    new_cluster {
      num_workers   = 1
      spark_version = "13.3.x-scala2.12"
      node_type_id  = "Standard_DS3_v2"
    }
  }

  task {
    task_key = "bronze_task"
    job_cluster_key = "medallion_cluster"

    notebook_task {
      notebook_path = "/Shared/devops_demo/bronze_ingest"
    }
  }

  task {
    task_key = "silver_task"
    depends_on {
      task_key = "bronze_task"
    }

    job_cluster_key = "medallion_cluster"

    notebook_task {
      notebook_path = "/Shared/devops_demo/silver_transform"
    }
  }

  task {
    task_key = "gold_task"
    depends_on {
      task_key = "silver_task"
    }

    job_cluster_key = "medallion_cluster"

    notebook_task {
      notebook_path = "/Shared/devops_demo/gold_aggregate"
    }
  }
}