# autotoot
A script that will automatically toot some things on Mastodon.

### Workflow Activation

The `.github/workflows/toot-scheduler.yml` file in your repository defines the GitHub Action that schedules the toots.

- By default, the action is set to run every hour.
- If you wish to change the schedule, edit the cron syntax in the `.github/workflows/toot-scheduler.yml` file accordingly.

### Monitoring Your Action

- You can monitor the action's execution and view logs by going to the "Actions" tab of your GitHub repository.
- If the action fails, you can troubleshoot by examining the output and logs.

## Contributing

Please feel free to contribute to this project by submitting pull requests with improvements.
