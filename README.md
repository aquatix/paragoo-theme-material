# paragoo-theme-material

[MaterializeCSS](http://materializecss.com/) theme for [paragoo](https://github.com/aquatix/paragoo) site generator, using a [Material design](https://www.google.com/design/spec/material-design/introduction.html) look with pre-made responsive views.

## Usage

First generate the colour variants by running `python generate_variants.py`. This will create a directory called `build` with themes based on various colour sets, based on the 'parent' theme in `material-base`.

Now you can use these themes with [paragoo](https://github.com/aquatix/paragoo), like for example:

```
python paragoo.py generate_site --clean -s ../mydomain.net/site -t ../paragoo-theme-material/build/material-grey -o /srv/mydomain.net
```

For more information about paragoo, see [its project page](https://github.com/aquatix/paragoo).
