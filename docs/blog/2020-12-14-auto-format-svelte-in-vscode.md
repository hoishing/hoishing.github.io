---
title: Auto-format Svelte in VS Code
tags: 
  - svelte
  - vscode
---
###### date: 2020-12-14

[Svelte](https://svelte.dev/) is an amazing front-end framework, which gives much better developer experience over other frameworks like Vue or React. To enjoy the super handy auto-format on save feature in VS Code, a little setup is needed at time of writing, here is how:

1. install [Svelte extension](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode) in VS Code
1. in VS Code settings, add:

```js
"editor.formatOnSave": true,
"[svelte]": {"editor.defaultFormatter": "svelte.svelte-vscode"}
```

The first line let VS Code triggers auto-format on save, and the second line tells VS Code to use the Svelte extension as the default formatter for svelte files. Reload VS Code, you should be able to auto-format `.svelte` files on save from now on.

Note that Svelte extension internally uses [prettier-plugin-svelte](https://github.com/sveltejs/prettier-plugin-svelte) for auto formatting. It has no relationship with the [Prettier extension](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) in VS Code. That means, it dis-regards the Prettier extension settings in VS Code.

## Work with Prettier

So what if you want to tweak the Prettier settings, such as using single quote, removing semi colon at line end … etc? You have to add a `.prettierrc` file in your project root in order to configure the Prettier plugin behavior, a sample config file as follow:

```js
{
  "semi": false,
  "singleQuote": true,
  "arrowParens": "avoid",
  "printWidth": 120
}
```

Save the config and reload VS Code, custom auto-formatting on saving `.svelte` files is done 🎉

P.S. some old tutorials suggest installing [prettier-plugin-svelte](https://github.com/sveltejs/prettier-plugin-svelte) with npm in your project. You don’t have to do it now as its already included in the Svelte extension.
