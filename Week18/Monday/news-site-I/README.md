# Overview
In this challenge, we will focus on creating three components that we will later use as we create a news site similar to [Reddit](https://www.reddit.com/).

## Initial Setup
To start, create a new create-react-app project from your terminal: `npx create-react-app news-site-i`
In your new project, copy over the `components` and `data` directories under `src/` and replace the boilerplate `App.js` with the one given here.

Each of the three components listed below has been stubbed out - your mission is to create the content that the component should `render`, and handle the `props` that are being passed in appropriately. For the first pass of this challenge, all components will be class-based.

Before diving in, it may be helpful to inspect the files in the `data` directory so you know the shape of the data your app will be handling.


## Component I: ArticleTeaser
The `ArticleTeaser` component should accept the following `props` from `App.js`:
1. `id` - a number
2. `title` - a string
3. `created_date` - a string
4. `handleTitleClick` - a event handling function

All of these `props` will always be passed in.

The `ArticleTeaser` component should:
1. Display the `title` inside of an `<a>` tag.
2. When the `title` `<a>` tag is clicked, it should call `this.props.handleTitleClick(this.props.id);`. Will arrow functions be useful here?
3. Display the `created_date` in a `<p>` tag.


## Component II: Article
In `App.js`, you'll notice that when the `Article` component is rendered, we pass `{...article}` to the component. This is known as the spread syntax. You can read more about it [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax). Rather than passing the entire `article` object, we are spreading its properties to be passed down via `props`.
Therefore, the `Article` component should accept the following `props`:
1. `title` - a string
2. `created_date` - a string
3. `abstract` - a string
4. `byline` - a string (optional)
5. `image` - a url string (optional)

The `title`, `abstract`, and `created_date` `props` will always contain values. `image` and `byline` may be set, but they may also be null. Be sure to account for this.

The `Article` component should:
1. Display the `title` inside of an `<h1>` tag.
2. Display the `created_date` in a `<p>` tag.
3. Display the `byline` (if it exists) in an `<h2>` tag.
4. Display the `image` (if it exists) in an `<img>` tag (the value of `image` should be set to the `src` attribute of the `<img>` tag).
5. Display the `abstract` inside of a `<p>` tag.

#### Sidenote: Conditional rendering in React
How do I only render something if the data exists? There are several ways we can handle this in React. Here we will explore three common options:

**Option 1: `&&`**

```javascript
// in the render
<ParentComponent>
  {dataExists && <ChildComponent>}
</ParentComponent>
```
Explanation: If there is just one piece of data we're checking for, we can do a quick existence check which will coerce the data to a boolean value `true` if the data does exist and then render the component/element that follows `&&`. If the data doesn't exist, it will be coerced to a boolean value `false` and will not render the child component/element.

**Option 2: Create a helper render function**

```javascript
renderIfDataExists = () => {
  if (dataExists) {
    return <ChildComponent />
  }
};

// in the render
<ParentComponent>
  {this.renderIfDataExists()}
</ParentComponent>
```
Explanation: This is a common pattern for rendering that involves more complex logic. For example, if our `dataExists` check was looking for multiple pieces of data, we might want to extract it out into this helper function.
(Also note that the above code snippet assumes a class-based React component. What would be different if it were written in a functional component?)

**Option 3: Use a ternary operator**
```javascript
<ParentComponent>
  { dataExists ? <ChildComponent /> : '' }
</ParentComponent>
```
Explanation: This is a good option to use if you are choosing between two different components/elements to render, but you can technically just render an empty string or `null` as seen above.

## Component III: AppNav
The `AppNav` component should accept the following `props`:
1. `navItems` - an array of navItem objects.
2. `handleNavClick` - a function.

The `AppNav` component should return a `<nav>` component that contains `<a>`'s as children - one for every item in the `this.props.navItems` array.

The AppNav component should:
1) Map through `this.props.navItems` to create an array of `<a>` elements. The objects within `this.props.navItems` look something like this:
```
{
  label: "NYREGION",
  value: "nyregion"
}
```
When transforming/mapping the `nav` item objects in `this.props.navItems` into an array of `<a>` tags, you'll want to use the `label` property (displayed in the example above) as the text that appears on screen. At the same time, you will want to attach an event handler to each `<a>`'s `onClick` event. `onClick` should call `this.props.handleNavClick`, and pass the 'value' property from the `nav` item object.

**You are done when all of your data is displayed and your `onClick` events are firing for your AppNav links and your ArticleTeaser links (i.e. you should see the `console.log`s)**

## Now make it Functional!
After you've committed your changes, open a new branch called `functional-version`. In this new branch, refactor your class-based components into functional ones. This may seem silly, but this is a large part of working in a real legacy React codebase, so understanding how to do these sorts of refactors is critical. Be sure to have BOTH versions of your work -- `master` as class-based and `functional-version` as functional. We will continue work on both in the future.
