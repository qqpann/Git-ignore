Git-ignore
===

**Gitignore Template Generator.** | **[日本語記事](http://qiugits.hatenablog.com/entry/2018/09/20/024218)**  
Git-ignore helps you to generate `.gitignore` file based on templates.  
You can install it with ease, and customize with your own templates.

Try it now, and leave me a start if you like it. ☆ ヽ(^ω^ #)

## Install
```terminal
$ pip install git-ignore
```

## Usage
#### Example: Django project that uses Python and Sass.
```
$ git-ignore python sass
```
This will create a `.gitignore` file that comes from both Python and Sass gitignore templates.

Note that you can add multiple templates at once.
Also, it is _not_ case sensitive.


#### Example: When you want to just add a few lines.
```
$ git-ignore --add !.keep !.gitkeep
```
This will add two lines on the bottom of your `.gitignore` file.


#### Example: Use custom templates.
```
$ mkdir ~/.gitignore_templates
$ echo '.DS_Store' > ~/.gitignore_templates/macOS.gitignore
$ git-ignore macOS
```
Running this, the command will look up at `~/.gitignore_templates/`,
and try to use `~/.gitignore_templates/macOS.gitignore`.


#### And more...
Find the full list of options by running
```
$ git-ignore --help
```

## How it works
This tool uses templates from [GitHub's `.gitignore` Templates Collection](https://github.com/github/gitignore/).

Thus it supports:
> Perl6, Sass, Scala, Joomla, CakePHP, Go, Yeoman, ZendFramework, KiCad, Textpattern, ExpressionEngine, Typo3, Packer, Elisp, EPiServer, Gcov, Haskell, GWT, LabVIEW, C++, Objective-C, Composer, SketchUp, Eagle, Android, Symfony, ExtJs, Erlang, Finale, Sdcc, Scrivener, Qooxdoo, RhodesRhomobile, PlayFramework, Stella, SugarCRM, Delphi, TurboGears2, Waf, Leiningen, Dart, R, ChefCookbook, MetaProgrammingSystem, CFWheels, Lilypond, Processing, Kohana, Clojure, GitBook, Lithium, Magento, Node, Python, Nim, Terraform, Yii, Nanoc, Umbraco, DM, Java, Elixir, WordPress, Godot, Xojo, ArchLinuxPackages, Jekyll, Ada, D, Elm, Actionscript, Swift, Grails, Laravel, Perl, CMake, VVVV, VisualStudio, CraftCMS, Coq, Rust, Scheme, IGORPro, Drupal, Plone, AppEngine, Mercury, Jboss, Lua, PureScript, CUDA, AppceleratorTitanium, Concrete5, CodeIgniter, Fortran, Julia, ForceDotCom, OracleForms, Smalltalk, Rails, Phalcon, Prestashop, Agda, Unity, FuelPHP, LemonStand, SeamGen, SCons, SymphonyCMS, CommonLisp, Gradle, Maven, Ruby, OpenCart, Fancy, TeX, Zephir, OCaml, UnrealEngine, Autotools, C, Kotlin, Qt, ROS, Idris, Opa

## Features
- ✔︎ Add `.gitignore` from templates.
- ✔︎ Can add multiple templates at once.
- ✔︎ Based on GitHub's templates collection.
- ✔︎ Support "Global (operating system or editor specific) templates".
- ✔︎ Helpful `--help` option.
- ✔︎ User defined template.

## Contributing
Issues and PRs are welcome :)

## License
MIT
