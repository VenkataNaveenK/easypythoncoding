import streamlit as st

def git_commands():
    st.header("Git Commands")
    st.subheader("1. Username and email configuration:")
    st.code("git config --global user.name 'yourName'")
    st.code("git config --global user.email 'youremail@email.com'")

    st.subheader("2. To verify the configuration:")
    st.code("git config user.name")
    st.code("git config user.email")

    st.subheader("3. To intialize a new repository")
    st.code("git init")

    st.subheader("4. To get the changes in repository")
    st.code("git status")

    st.subheader("5. To get differences")
    st.code("git diff")
    st.text("or")
    st.code("git diff <filename>")

    st.subheader("6. To add the file changes to working tree")
    st.code("git add .")
    st.text("or")
    st.code("git add <filename>")

    st.subheader("7. To commit the changes to working tree")
    st.code("git commit -m 'meaningful message'")

    st.subheader("8. To check the list of commits")
    st.code("git log")
    st.text("or")
    st.code("git log --oneline")

    st.subheader("9. To reset to a particular commit")
    st.code("git reset --hard <commit id>")

    st.subheader("10. To delete last commit")
    st.code("git reset --hard HEAD^0")

    st.subheader("11. Creation of a branch in local")
    st.code("git branch <branch name>")

    st.subheader("12. List of local branches")
    st.code("git branch")

    st.subheader("13. Checkout a branch")
    st.code("git checkout <branchname>")

    st.subheader("14. Merging master branch(old) to dev branch(new)")
    st.code("git checkout master")
    st.code("git merge dev")

    st.subheader("15. To delete a branch")
    st.code("git branch -d <branch name>")

    st.subheader("16. Configuring remote repository to local branch")
    st.code("git remote add origin <url for remote repo>")
    st.code("git remote -v")

    st.subheader("17. Pushing changes to remote repository")
    st.code("git push origin master")

    st.subheader("18. Cloning a remote repository")
    st.code("git clone <remote repo url>")

    st.subheader("19. Pulling changes from remote repository")
    st.code("git pull origin master")