# Useful Links
https://gist.github.com/levibostian/71afa00ddc69688afebb215faab48fd7 
https://github.com/angular/angular/blob/22b96b96902e1a42ee8c5e807720424abad3082a/CONTRIBUTING.md?plain=1#type

## Commit Message Format
Each commit message consists of a **header**, a **body** and a **footer**.  The header has a special
format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The **header** is mandatory and the **scope** of the header is optional.

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier
to read on GitHub as well as in various git tools.

The footer should contain a [closing reference to an issue](https://help.github.com/articles/closing-issues-via-commit-messages/) if any.

Samples: (even more [samples](https://github.com/angular/angular/commits/master))

```
docs(changelog): update changelog to beta.5
```
```
fix(release): need to depend on latest rxjs and zone.js

The version in our package.json gets copied to the one we publish, and users need the latest of these.
```


## Type
Must be one of the following:

* **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
* **ci**: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
* **docs**: Documentation only changes
* **feat**: A new feature
* **fix**: A bug fix
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* **test**: Adding missing tests or correcting existing tests

# Examples:

Let's say that you...

* ...added a new feature to your app. 
```
feat: add ability for user to upload photo for profile
```
> Tip: Remember, you can include an optional body for your commit, but for feature additions it's not needed sometimes. The subject many times can explain the feature. 

* ...fixed a bug:
```
fix: crash when user uploads photo for profile

Crash was because uploaded files too large.

Closes: https://github.com/foo/repo/issues/2
```
> Tip: This commit message shows a body and a footer. You know that we have a body *and* a footer because there is a blank line separating the subject, body, and footer. 

* ...edited some of the documentation for the project
```
docs: add section about file upload limits

This update is for the internal team docs, only.
```
> Tip: This commit has a subject line and a body line, only. No footer. The body and the footer are both optional. There is no requirement to include either of them or both of them. 

* ...run lint tool to format source code files
```
style: format source files

Forgot to run lint tool for previous commits.
```

* ...changed a feature in your app but it adds a breaking change
```
feat: edit profile first and last name required

BREAKING CHANGE: First and last name are now required parameters when editing profile. Existing profiles are untouched but the client app needs to update to require this paramter. 
```
> Tip: See the subject explains that we made the first and last name required. Then, the `BREAKING CHANGE:` line explains this change in more detail. This sample commit message does not include a body for example purposes to show the body is optional when a footer exists, but for this commit a body would be good to have to explain *why* this change was put into place. 