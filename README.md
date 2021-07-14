[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/thananon/covidth">
    <img src="public/favicon.ico" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">COVID TH</h3>

  <p align="center">
    Project website display Covid data.
    <br />
    <a href="https://github.com/thananon/covidth"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://covidth.vercel.app/">View Demo</a>
    ·
    <a href="https://github.com/thananon/covidth/issues">Report Bug</a>
    ·
    <a href="https://github.com/thananon/covidth/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#Recommended IDE Setup">Recommended IDE Setup</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation & Run</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
# About The Project
[![Product Name Screen Shot][product-screenshot]](https://covidth.vercel.app/)


*** ฝากเติมหน่อยนะครับ ^ ^

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/thananon/covidth.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
3. Run Vite
   ```sh
   npm run dev
   ```

<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_ -->

## Built With
### Svelte + Vite
This template should help get you started developing with Svelte in Vite.

### Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Svelte](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)

## Need an official Svelte framework?

Check out [SvelteKit](https://github.com/sveltejs/kit#readme), which is also powered by Vite. Deploy anywhere with its serverless-first approach and adapt to various platforms, with out of the box support for TypeScript, SCSS, and Less, and easily-added support for mdsvex, GraphQL, PostCSS, Tailwind CSS, and more.

## Technical considerations

**Why use this over SvelteKit?**

- It brings its own routing solution which might not be preferable for some users.
- It is first and foremost a framework that just happens to use Vite under the hood, not a Vite app.
  `vite dev` and `vite build` wouldn't work in a SvelteKit environment, for example.

This template contains as little as possible to get started with Vite + Svelte, while taking into account the developer experience with regards to HMR and intellisense. It demonstrates capabilities on par with the other `create-vite` templates and is a good starting point for beginners dipping their toes into a Vite + Svelte project.

Should you later need the extended capabilities and extensibility provided by SvelteKit, the template has been structured similarly to SvelteKit so that it is easy to migrate.

**Why `global.d.ts` instead of `compilerOptions.types` inside `jsconfig.json` or `tsconfig.json`?**

Setting `compilerOptions.types` shuts out all other types not explicitly listed in the configuration. Using triple-slash references keeps the default TypeScript setting of accepting type information from the entire workspace, while also adding `svelte` and `vite/client` type information.

**Why include `.vscode/extensions.json`?**

Other templates indirectly recommend extensions via the README, but this file allows VS Code to prompt the user to install the recommended extension upon opening the project.

**Why enable `checkJs` in the JS template?**

It is likely that most cases of changing variable types in runtime are likely to be accidental, rather than deliberate. This provides advanced typechecking out of the box. Should you like to take advantage of the dynamically-typed nature of JavaScript, it is trivial to change the configuration.

**Why is HMR not preserving my local component state?**

HMR state preservation comes with a number of gotchas! It has been disabled by default in both `svelte-hmr` and `@sveltejs/vite-plugin-svelte` due to its often surprising behavior. You can read the details [here](https://github.com/rixo/svelte-hmr#svelte-hmr).

If you have state that's important to retain within a component, consider creating an external store which would not be replaced by HMR.

```js
// store.js
// An extremely simple external store
import { writable } from "svelte/store"
export default writable(0)
```

## Roadmap

See the [open issues](https://github.com/thananon/covidth/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the Website Covid data, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Foo`)
3. Commit your Changes (`git commit -m 'Add some FooFeature'`)
4. Push to the Branch (`git push origin feature/FooFeature`)
5. Open a Pull Request

<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE` for more information. -->
<!-- ROADMAP -->


<!-- CONTACT -->
## CONTACT

Your Name - [@9ARM](https://www.youtube.com/channel/UCoiEtD4v1qMAqHV5MDI5Qpg) - Youtube

Project Link: [https://github.com/thananon/covidth](https://github.com/thananon/covidth)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Svelte](https://svelte.dev/)
* [vite](https://vitejs.dev/)
* [chart.js](https://www.chartjs.org/)
* [Bootsrap for Svelt](https://sveltestrap.js.org/?path=/story/components--get-started)


[contributors-shield]: https://img.shields.io/github/contributors/thananon/covidth.svg?style=for-the-badge
[contributors-url]: https://github.com/thananon/covidth/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/thananon/covidth.svg?style=for-the-badge
[forks-url]: https://github.com/thananon/covidth/network/members
[stars-shield]: https://img.shields.io/github/stars/thananon/covidth.svg?style=for-the-badge
[stars-url]: https://github.com/thananon/covidth/stargazers
[issues-shield]: https://img.shields.io/github/issues/thananon/covidth.svg?style=for-the-badge
[issues-url]: https://github.com/thananon/covidth/issues
[product-screenshot]: public/rattaban_huakuy_v2.png

