Git-ignore
===

A cli helper that initiates `.gitignore` file from template.


## Install
```terminal
$ pip install git-ignore
```

## Usage
Example: Django project that uses Python and Sass.
```
$ git-ignore python sass
```
This will create a `.gitignore` file that comes from both Python and Sass gitignore templates.

Note that you can add multiple templates at once.
Also, it is _not_ case sensitive.

## How it works
This tool uses templates from [A collection of `.gitignore` templates | by GitHub](https://github.com/github/gitignore/).

Thus it supports:
> Perl6, Sass, Scala, Joomla, CakePHP, Go, Yeoman, ZendFramework, KiCad, Textpattern, ExpressionEngine, Typo3, Packer, Elisp, EPiServer, Gcov, Haskell, GWT, LabVIEW, C++, Objective-C, Composer, SketchUp, Eagle, Android, Symfony, ExtJs, Erlang, Finale, Sdcc, Scrivener, Qooxdoo, RhodesRhomobile, PlayFramework, Stella, SugarCRM, Delphi, TurboGears2, Waf, Leiningen, Dart, R, ChefCookbook, MetaProgrammingSystem, CFWheels, Lilypond, Processing, Kohana, Clojure, GitBook, Lithium, Magento, Node, Python, Nim, Terraform, Yii, Nanoc, Umbraco, DM, Java, Elixir, WordPress, Godot, Xojo, ArchLinuxPackages, Jekyll, Ada, D, Elm, Actionscript, Swift, Grails, Laravel, Perl, CMake, VVVV, VisualStudio, CraftCMS, Coq, Rust, Scheme, IGORPro, Drupal, Plone, AppEngine, Mercury, Jboss, Lua, PureScript, CUDA, AppceleratorTitanium, Concrete5, CodeIgniter, Fortran, Julia, ForceDotCom, OracleForms, Smalltalk, Rails, Phalcon, Prestashop, Agda, Unity, FuelPHP, LemonStand, SeamGen, SCons, SymphonyCMS, CommonLisp, Gradle, Maven, Ruby, OpenCart, Fancy, TeX, Zephir, OCaml, UnrealEngine, Autotools, C, Kotlin, Qt, ROS, Idris, Opa

## Features & TODOs
- [x] Add `.gitignore` from templates.
- [x] Can add multiple templates at once.
- [x] Based on GitHub's templates collection.
- [ ] Support "Global (operating system or editor specific) templates".
- [ ] Helpful `--help` option.
- [ ] Detect git base directry to place `.gitignore`.
- [ ] Autofill suggestion.

## Contributing
Please feel free to open an issue or PR.

A star will be appreciated. ☆ ヽ(^ω^ #)

## License
MIT
