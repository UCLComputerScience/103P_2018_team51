Development Methodology
=======================

Git Workflow
------------

Fetching the latest changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The latest changes can be fetched with: ``git fetch origin``.

Using ``git fetch`` is preferred over ``git pull`` as it means there's no risk of modifying the branch you're currently on - it gives you full control over what you want to do with the changes you've fetched.

Creating a feature branch
^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new branch to work on your feature with the latest commits from the master branch with: ``git branch -b feature-name origin/master``

Committing the feature
^^^^^^^^^^^^^^^^^^^^^^

Once you've finished working on your feature, you'll want to commit it to your branch. Do this by:

#. Checking the current status of your files with: ``git status``
#. Staging all the changes to files you want to commit with: ``git add file_one file_two``
#. Committing the staged changes with a descriptive commit message: ``git commit -m "commit message"``

If you've been working on a feature linked to an issue, which is usually the case, you'll want to end the commit message with the issue number. For example, if I'd been working on issue 7, my commit command might look something like: ``git commit -m "commit message #7"``.

Updating the branch with the latest changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

While you've been working on your feature, there may have been updates to the master branch which you'll want to include in your feature branch. Do this by:

#. Fetching the latest changes with: ``git fetch origin``
#. Rebasing your branch with the changes with: ``git rebase origin/master``

At this point the rebase may succeed, or it may fail. If it fails run ``git status`` and follow the instructions to resolve the merge conflicts.

Pushing the branch
^^^^^^^^^^^^^^^^^^

After committing your feature and rebasing with master, push the branch to the origin remote with: ``git push origin feature-name``.

Creating a pull request
^^^^^^^^^^^^^^^^^^^^^^^

Now that your feature branch is on the origin remote, go to https://github.com/UCLComputerScience/103P_2018_team51/compare/master...feature-name and click **Create pull request** to create a pull request.

Your commit will be reviewed, and if approved, rebased into the master branch.

If changes were requested, you can make them in your local branch, commit and push to the remote branch as before.
