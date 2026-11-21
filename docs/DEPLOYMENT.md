# Portfolio deployment

Live website: [katherine0292.github.io/portfolio](https://katherine0292.github.io/portfolio/).

GitHub Pages publishes the `github-pages` environment from the `main` branch using
`.github/workflows/deploy-pages.yml`.

The build selects the highest numbered `demo/vN/index.html`, publishes it at the
website root, and adjusts its preview-image path for that location. Assets and
the original demo URLs are included in the deployment.

To publish a later version, add its `demo/vN/index.html` and assets, then merge or
push the changes to `main`. The workflow can also be run manually from Actions.

Local build:

```sh
python3 scripts/build-pages.py
python3 -m http.server --directory _site 8000
```

The existing portfolio content, language switching, project destinations and
sound preferences are retained. The resume button remains a placeholder until
`RESUME_URL` in the selected source page is assigned a public resume URL.
